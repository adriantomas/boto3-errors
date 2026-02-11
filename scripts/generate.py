#!/usr/bin/env python3
"""Generate per-service exception modules from botocore service models.

Usage:
    python scripts/generate.py
"""

from __future__ import annotations

import gzip
import html.parser
import json
import keyword
import re
import textwrap
from pathlib import Path

import botocore

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
BOTOCORE_DATA = Path(botocore.__file__).parent / "data"
OUTPUT_DIR = Path(__file__).resolve().parent.parent / "src" / "boto3_errors"

# ---------------------------------------------------------------------------
# Type mapping from botocore shape types to Python type annotations
# ---------------------------------------------------------------------------
TYPE_MAP: dict[str, str] = {
    "string": "str",
    "integer": "int",
    "long": "int",
    "boolean": "bool",
    "float": "float",
    "double": "float",
    "map": "dict[str, Any]",
    "list": "list[Any]",
    "structure": "dict[str, Any]",
    "blob": "bytes",
    "timestamp": "str",
}


def _python_type(shape_name: str, shapes: dict) -> str:
    """Resolve a shape reference to a Python type string."""
    shape = shapes.get(shape_name, {})
    return TYPE_MAP.get(shape.get("type", "string"), "Any")


def _module_name(service: str) -> str:
    name = service.replace("-", "_")
    if keyword.iskeyword(name):
        name += "_"
    return name


def _class_name(service_id: str) -> str:
    """Turn a serviceId like 'ACM PCA' into 'ACMPCAError'.

    Strips spaces and non-alphanumeric chars to produce a valid Python identifier.
    """
    return re.sub(r"[^A-Za-z0-9]", "", service_id) + "Error"


def _snake_case(name: str) -> str:
    """Convert CamelCase member name to snake_case property name."""
    s = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1_\2", name)
    s = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", s)
    return s.lower()


class _DocConverter(html.parser.HTMLParser):
    """Convert botocore HTML docs to structured plaintext with nested list support."""

    def __init__(self) -> None:
        super().__init__()
        self._parts: list[str] = []
        self._list_depth = 0
        # Count of nested <li> tags — suppress <p> paragraph breaks inside items
        self._li_depth = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:  # noqa: ARG002
        if tag == "p":
            if self._li_depth == 0:
                self._parts.append("\n\n")
        elif tag == "note":
            self._parts.append("\n\nNote: ")
        elif tag == "br":
            self._parts.append("\n")
        elif tag == "ul":
            self._list_depth += 1
            self._parts.append("\n")
        elif tag == "li":
            self._li_depth += 1
            prefix = "  " * (self._list_depth - 1) + "- "
            self._parts.append("\n" + prefix)
        elif tag == "code":
            self._parts.append("`")

    def handle_endtag(self, tag: str) -> None:
        if tag == "note":
            self._parts.append("\n\n")
        elif tag == "ul":
            self._list_depth = max(0, self._list_depth - 1)
            self._parts.append("\n")
        elif tag == "li":
            self._li_depth = max(0, self._li_depth - 1)
        elif tag == "code":
            self._parts.append("`")

    def handle_data(self, data: str) -> None:
        self._parts.append(data)

    def get_text(self) -> str:
        text = "".join(self._parts)
        # Clean up whitespace within each line, preserving leading indent
        lines = text.split("\n")
        cleaned: list[str] = []
        for line in lines:
            stripped = line.lstrip()
            if not stripped:
                cleaned.append("")
                continue
            indent_chars = len(line) - len(stripped)
            normalized = re.sub(r"[ \t]+", " ", stripped).strip()
            cleaned.append(" " * indent_chars + normalized)
        text = "\n".join(cleaned)
        # Collapse 3+ newlines to 2 (paragraph break)
        return re.sub(r"\n{3,}", "\n\n", text).strip()


def _clean_doc(raw_html: str | None) -> str:
    """Convert HTML documentation to structured plaintext for docstrings."""
    if not raw_html:
        return ""
    converter = _DocConverter()
    converter.feed(raw_html)
    text = converter.get_text()
    # Escape for docstrings
    return text.replace("\\", "\\\\").replace('"""', r"\"\"\"")


def _format_docstring(doc: str, indent: int) -> list[str]:
    """Wrap *doc* to fit within 88 columns and return indented docstring lines."""
    prefix = " " * indent
    width = 88 - indent
    result_lines: list[str] = []
    for paragraph in doc.split("\n\n"):
        if result_lines:
            result_lines.append("")  # blank line between paragraphs
        for line in paragraph.split("\n"):
            bullet_match = re.match(r"^(\s*- )", line)
            if bullet_match:
                indent_str = bullet_match.group(1)
                subsequent = " " * len(indent_str)
                wrapped = textwrap.fill(
                    line,
                    width=width,
                    initial_indent="",
                    subsequent_indent=subsequent,
                )
                result_lines.extend(wrapped.split("\n"))
            else:
                wrapped = textwrap.fill(line, width=width)
                result_lines.extend(wrapped.split("\n"))
    # Format as docstring
    if len(result_lines) == 1:
        return [f'{prefix}"""{result_lines[0]}"""']
    out = [f'{prefix}"""{result_lines[0]}']
    out.extend(f"{prefix}{line}" if line else "" for line in result_lines[1:])
    out.append(f'{prefix}"""')
    return out


def _load_model(service_dir: Path) -> dict | None:
    versions = sorted(p.name for p in service_dir.iterdir())
    if not versions:
        return None
    latest = versions[-1]
    gz_path = service_dir / latest / "service-2.json.gz"
    json_path = service_dir / latest / "service-2.json"
    if gz_path.exists():
        with gzip.open(gz_path, "rt") as f:
            return json.load(f)
    elif json_path.exists():
        with json_path.open() as f:
            return json.load(f)
    return None


def _generate_service(service: str) -> str | None:  # noqa: C901, PLR0915
    """Generate the module source for a single service.

    Returns ``None`` if no exceptions are defined.
    """
    model = _load_model(BOTOCORE_DATA / service)
    if model is None:
        return None

    shapes = model.get("shapes", {})
    metadata = model.get("metadata", {})
    service_id = metadata.get("serviceId", service)

    # Collect exception shapes
    exceptions: list[tuple[str, str, dict]] = []  # (shape_name, error_code, shape)
    for name, shape in shapes.items():
        if shape.get("type") == "structure" and shape.get("exception"):
            error_code = shape.get("error", {}).get("code", name)
            exceptions.append((name, error_code, shape))

    if not exceptions:
        return None

    exceptions.sort(key=lambda x: x[0])

    base_class = _class_name(service_id)

    lines: list[str] = []
    lines.append("# Auto-generated. Do not edit manually.")
    lines.append("from __future__ import annotations")
    lines.append("")
    lines.append("from typing import Any")
    lines.append("")
    lines.append("from boto3_errors._base import Boto3Error")
    lines.append("")
    lines.append("")
    lines.append(f"class {base_class}(Boto3Error):")
    lines.append(f'    _SERVICE = "{service}"')
    lines.append("")
    lines.append("")

    for shape_name, error_code, shape in exceptions:
        doc = _clean_doc(shape.get("documentation"))
        members = shape.get("members", {})

        lines.append(f"class {shape_name}({base_class}):")
        if doc:
            doc_lines = _format_docstring(doc, indent=4)
            lines.extend(doc_lines)
            if len(doc_lines) > 1:
                lines.append("")  # PEP 257 blank line after multi-line docstring
        lines.append(f'    _ERROR_CODE = "{error_code}"')

        # Generate properties for non-message members
        extra_members = {k: v for k, v in members.items() if k.lower() != "message"}
        if extra_members:
            lines.append("")
        for member_name, member_info in extra_members.items():
            prop_name = _snake_case(member_name)
            member_shape_name = member_info.get("shape", "")
            py_type = _python_type(member_shape_name, shapes)
            member_doc = _clean_doc(member_info.get("documentation"))

            lines.append("    @property")
            lines.append(f"    def {prop_name}(self) -> {py_type} | None:")
            if member_doc:
                lines.extend(_format_docstring(member_doc, indent=8))
            lines.append(f'        return self.response.get("{member_name}")')
            lines.append("")

        # Ensure exactly 2 blank lines between top-level classes
        while lines and lines[-1] == "":
            lines.pop()
        lines.append("")
        lines.append("")

    # EXCEPTIONS dict
    lines.append(f"EXCEPTIONS: dict[str, type[{base_class}]] = {{")
    for shape_name, error_code, _ in exceptions:
        lines.append(f'    "{error_code}": {shape_name},')
    lines.append("}")
    lines.append("")

    return "\n".join(lines)


def main() -> None:
    """Generate all per-service exception modules."""
    services = sorted(
        p.name
        for p in BOTOCORE_DATA.iterdir()
        if p.is_dir() and not p.name.startswith("_")
    )

    generated = 0
    for service in services:
        source = _generate_service(service)
        if source is None:
            continue
        mod_name = _module_name(service)
        out_path = OUTPUT_DIR / f"{mod_name}.py"
        out_path.write_text(source)
        generated += 1

    print(f"Generated {generated} service modules in {OUTPUT_DIR}")  # noqa: T201


if __name__ == "__main__":
    main()
