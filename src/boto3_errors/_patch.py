import functools
import importlib
from typing import Any

from botocore.client import BaseClient
from botocore.exceptions import ClientError


def patch_client(client: BaseClient) -> None:
    """Wrap *client*'s ``_make_api_call``.

    Re-raises ``ClientError`` as a typed :class:`~boto3_errors._base.Boto3Error`
    subclass when a matching exception class exists.

    Safe to call more than once on the same client (subsequent calls are
    no-ops).
    """
    if getattr(client, "_boto3_errors_patched", False):
        return

    service: str = client._service_model.service_name  # type: ignore[attr-defined]
    module_name = _service_to_module(service)

    try:
        mod = importlib.import_module(f"boto3_errors.{module_name}")
    except ModuleNotFoundError:
        # No generated module for this service — nothing to patch.
        return

    exceptions: dict[str, type] = getattr(mod, "EXCEPTIONS", {})
    original = client._make_api_call  # type: ignore[attr-defined]

    @functools.wraps(original)
    def _patched_make_api_call(
        operation_name: str, api_params: dict[str, Any]
    ) -> dict[str, Any]:
        try:
            return original(operation_name, api_params)  # type: ignore[no-any-return]
        except ClientError as e:
            code = e.response.get("Error", {}).get("Code", "")
            exc_cls = exceptions.get(code)
            if exc_cls is not None:
                raise exc_cls(e.response, e.operation_name) from e
            raise

    client._make_api_call = _patched_make_api_call  # type: ignore[attr-defined]
    client._boto3_errors_patched = True  # type: ignore[attr-defined]


def _service_to_module(service: str) -> str:
    name = service.replace("-", "_")
    if name == "lambda":
        name = "lambda_"
    return name
