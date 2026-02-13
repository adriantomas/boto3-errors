# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class AppConfigDataError(Boto3Error):
    _SERVICE = "appconfigdata"


class BadRequestException(AppConfigDataError):
    """The input fails to satisfy the constraints specified by the service."""
    _ERROR_CODE = "BadRequestException"

    @property
    def reason(self) -> str | None:
        """Code indicating the reason the request was invalid."""
        return self.response.get("Reason")

    @property
    def details(self) -> dict[str, Any] | None:
        """Details describing why the request was invalid."""
        return self.response.get("Details")


class InternalServerException(AppConfigDataError):
    """There was an internal failure in the service."""
    _ERROR_CODE = "InternalServerException"


class ResourceNotFoundException(AppConfigDataError):
    """The requested resource could not be found."""
    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def resource_type(self) -> str | None:
        """The type of resource that was not found."""
        return self.response.get("ResourceType")

    @property
    def referenced_by(self) -> dict[str, Any] | None:
        """A map indicating which parameters in the request reference the resource that was
        not found.
        """
        return self.response.get("ReferencedBy")


class ThrottlingException(AppConfigDataError):
    """The request was denied due to request throttling."""
    _ERROR_CODE = "ThrottlingException"


EXCEPTIONS: dict[str, type[AppConfigDataError]] = {
    "BadRequestException": BadRequestException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ThrottlingException": ThrottlingException,
}
