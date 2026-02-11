# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class MediaTailorError(Boto3Error):
    _SERVICE = "mediatailor"


class BadRequestException(MediaTailorError):
    """A request contains unexpected data."""
    _ERROR_CODE = "BadRequestException"


EXCEPTIONS: dict[str, type[MediaTailorError]] = {
    "BadRequestException": BadRequestException,
}
