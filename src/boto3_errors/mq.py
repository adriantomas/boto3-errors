# Auto-generated. Do not edit manually.
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

    @property
    def resource_share_errors(self) -> list[Any] | None:
        """The list of resource share errors."""
        return self.response.get("ResourceShareErrors")


class ConflictException(mqError):
    """Returns information about an error."""
    _ERROR_CODE = "ConflictException"

    @property
    def error_attribute(self) -> str | None:
        """The attribute which caused the error."""
        return self.response.get("ErrorAttribute")

    @property
    def resource_share_errors(self) -> list[Any] | None:
        """The list of resource share errors."""
        return self.response.get("ResourceShareErrors")


class ForbiddenException(mqError):
    """Returns information about an error."""
    _ERROR_CODE = "ForbiddenException"

    @property
    def error_attribute(self) -> str | None:
        """The attribute which caused the error."""
        return self.response.get("ErrorAttribute")

    @property
    def resource_share_errors(self) -> list[Any] | None:
        """The list of resource share errors."""
        return self.response.get("ResourceShareErrors")


class InternalServerErrorException(mqError):
    """Returns information about an error."""
    _ERROR_CODE = "InternalServerErrorException"

    @property
    def error_attribute(self) -> str | None:
        """The attribute which caused the error."""
        return self.response.get("ErrorAttribute")

    @property
    def resource_share_errors(self) -> list[Any] | None:
        """The list of resource share errors."""
        return self.response.get("ResourceShareErrors")


class NotFoundException(mqError):
    """Returns information about an error."""
    _ERROR_CODE = "NotFoundException"

    @property
    def error_attribute(self) -> str | None:
        """The attribute which caused the error."""
        return self.response.get("ErrorAttribute")

    @property
    def resource_share_errors(self) -> list[Any] | None:
        """The list of resource share errors."""
        return self.response.get("ResourceShareErrors")


class UnauthorizedException(mqError):
    """Returns information about an error."""
    _ERROR_CODE = "UnauthorizedException"

    @property
    def error_attribute(self) -> str | None:
        """The attribute which caused the error."""
        return self.response.get("ErrorAttribute")

    @property
    def resource_share_errors(self) -> list[Any] | None:
        """The list of resource share errors."""
        return self.response.get("ResourceShareErrors")


EXCEPTIONS: dict[str, type[mqError]] = {
    "BadRequestException": BadRequestException,
    "ConflictException": ConflictException,
    "ForbiddenException": ForbiddenException,
    "InternalServerErrorException": InternalServerErrorException,
    "NotFoundException": NotFoundException,
    "UnauthorizedException": UnauthorizedException,
}
