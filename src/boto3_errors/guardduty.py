# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class GuardDutyError(Boto3Error):
    _SERVICE = "guardduty"


class AccessDeniedException(GuardDutyError):
    """An access denied exception object."""
    _ERROR_CODE = "AccessDeniedException"

    @property
    def type(self) -> str | None:
        """The error type."""
        return self.response.get("Type")


class BadRequestException(GuardDutyError):
    """A bad request exception object."""
    _ERROR_CODE = "BadRequestException"

    @property
    def type(self) -> str | None:
        """The error type."""
        return self.response.get("Type")


class ConflictException(GuardDutyError):
    """A request conflict exception object."""
    _ERROR_CODE = "ConflictException"

    @property
    def type(self) -> str | None:
        """The error type."""
        return self.response.get("Type")


class InternalServerErrorException(GuardDutyError):
    """An internal server error exception object."""
    _ERROR_CODE = "InternalServerErrorException"

    @property
    def type(self) -> str | None:
        """The error type."""
        return self.response.get("Type")


class ResourceNotFoundException(GuardDutyError):
    """The requested resource can't be found."""
    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def type(self) -> str | None:
        """The error type."""
        return self.response.get("Type")


EXCEPTIONS: dict[str, type[GuardDutyError]] = {
    "AccessDeniedException": AccessDeniedException,
    "BadRequestException": BadRequestException,
    "ConflictException": ConflictException,
    "InternalServerErrorException": InternalServerErrorException,
    "ResourceNotFoundException": ResourceNotFoundException,
}
