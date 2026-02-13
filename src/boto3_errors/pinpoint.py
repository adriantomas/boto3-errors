# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class PinpointError(Boto3Error):
    _SERVICE = "pinpoint"


class BadRequestException(PinpointError):
    """Provides information about an API request or response."""
    _ERROR_CODE = "BadRequestException"

    @property
    def request_id(self) -> str | None:
        """The unique identifier for the request or response."""
        return self.response.get("RequestID")


class ConflictException(PinpointError):
    """Provides information about an API request or response."""
    _ERROR_CODE = "ConflictException"

    @property
    def request_id(self) -> str | None:
        """The unique identifier for the request or response."""
        return self.response.get("RequestID")


class ForbiddenException(PinpointError):
    """Provides information about an API request or response."""
    _ERROR_CODE = "ForbiddenException"

    @property
    def request_id(self) -> str | None:
        """The unique identifier for the request or response."""
        return self.response.get("RequestID")


class InternalServerErrorException(PinpointError):
    """Provides information about an API request or response."""
    _ERROR_CODE = "InternalServerErrorException"

    @property
    def request_id(self) -> str | None:
        """The unique identifier for the request or response."""
        return self.response.get("RequestID")


class MethodNotAllowedException(PinpointError):
    """Provides information about an API request or response."""
    _ERROR_CODE = "MethodNotAllowedException"

    @property
    def request_id(self) -> str | None:
        """The unique identifier for the request or response."""
        return self.response.get("RequestID")


class NotFoundException(PinpointError):
    """Provides information about an API request or response."""
    _ERROR_CODE = "NotFoundException"

    @property
    def request_id(self) -> str | None:
        """The unique identifier for the request or response."""
        return self.response.get("RequestID")


class PayloadTooLargeException(PinpointError):
    """Provides information about an API request or response."""
    _ERROR_CODE = "PayloadTooLargeException"

    @property
    def request_id(self) -> str | None:
        """The unique identifier for the request or response."""
        return self.response.get("RequestID")


class TooManyRequestsException(PinpointError):
    """Provides information about an API request or response."""
    _ERROR_CODE = "TooManyRequestsException"

    @property
    def request_id(self) -> str | None:
        """The unique identifier for the request or response."""
        return self.response.get("RequestID")


EXCEPTIONS: dict[str, type[PinpointError]] = {
    "BadRequestException": BadRequestException,
    "ConflictException": ConflictException,
    "ForbiddenException": ForbiddenException,
    "InternalServerErrorException": InternalServerErrorException,
    "MethodNotAllowedException": MethodNotAllowedException,
    "NotFoundException": NotFoundException,
    "PayloadTooLargeException": PayloadTooLargeException,
    "TooManyRequestsException": TooManyRequestsException,
}
