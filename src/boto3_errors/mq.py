# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class mqError(Boto3Error):
    _SERVICE = "mq"


class BadRequestException(mqError):
    """Returns information about an error."""
    _ERROR_CODE = "BadRequestException"

    @property
    def error_attribute(self) -> str | None:
        """The attribute which caused the error."""
        return self.response.get("ErrorAttribute")


class ConflictException(mqError):
    """Returns information about an error."""
    _ERROR_CODE = "ConflictException"

    @property
    def error_attribute(self) -> str | None:
        """The attribute which caused the error."""
        return self.response.get("ErrorAttribute")


class ForbiddenException(mqError):
    """Returns information about an error."""
    _ERROR_CODE = "ForbiddenException"

    @property
    def error_attribute(self) -> str | None:
        """The attribute which caused the error."""
        return self.response.get("ErrorAttribute")


class InternalServerErrorException(mqError):
    """Returns information about an error."""
    _ERROR_CODE = "InternalServerErrorException"

    @property
    def error_attribute(self) -> str | None:
        """The attribute which caused the error."""
        return self.response.get("ErrorAttribute")


class NotFoundException(mqError):
    """Returns information about an error."""
    _ERROR_CODE = "NotFoundException"

    @property
    def error_attribute(self) -> str | None:
        """The attribute which caused the error."""
        return self.response.get("ErrorAttribute")


class UnauthorizedException(mqError):
    """Returns information about an error."""
    _ERROR_CODE = "UnauthorizedException"

    @property
    def error_attribute(self) -> str | None:
        """The attribute which caused the error."""
        return self.response.get("ErrorAttribute")


EXCEPTIONS: dict[str, type[mqError]] = {
    "BadRequestException": BadRequestException,
    "ConflictException": ConflictException,
    "ForbiddenException": ForbiddenException,
    "InternalServerErrorException": InternalServerErrorException,
    "NotFoundException": NotFoundException,
    "UnauthorizedException": UnauthorizedException,
}
