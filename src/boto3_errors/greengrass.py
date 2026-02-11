# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class GreengrassError(Boto3Error):
    _SERVICE = "greengrass"


class BadRequestException(GreengrassError):
    """General error information."""
    _ERROR_CODE = "BadRequestException"

    @property
    def error_details(self) -> list[Any] | None:
        """Details about the error."""
        return self.response.get("ErrorDetails")


class InternalServerErrorException(GreengrassError):
    """General error information."""
    _ERROR_CODE = "InternalServerErrorException"

    @property
    def error_details(self) -> list[Any] | None:
        """Details about the error."""
        return self.response.get("ErrorDetails")


EXCEPTIONS: dict[str, type[GreengrassError]] = {
    "BadRequestException": BadRequestException,
    "InternalServerErrorException": InternalServerErrorException,
}
