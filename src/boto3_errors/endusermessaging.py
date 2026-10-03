# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class EndUserMessagingError(Boto3Error):
    _SERVICE = "endusermessaging"


class AccessDeniedException(EndUserMessagingError):
    """You do not have sufficient access to perform this action."""
    _ERROR_CODE = "AccessDeniedException"


class ConflictException(EndUserMessagingError):
    """The request conflicts with the current state of the resource."""
    _ERROR_CODE = "ConflictException"

    @property
    def resource_id(self) -> str | None:
        """The identifier of the resource that the request conflicts with."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of the resource that the request conflicts with."""
        return self.response.get("resourceType")


class InternalServerException(EndUserMessagingError):
    """An unexpected error occurred during the processing of the request."""
    _ERROR_CODE = "InternalServerException"


class ResourceNotFoundException(EndUserMessagingError):
    """The request references a resource that does not exist. Verify that the resource
    identifier is correct and try your request again.
    """

    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def resource_id(self) -> str | None:
        """The identifier of the resource that could not be found."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of the resource that could not be found."""
        return self.response.get("resourceType")


class ServiceQuotaExceededException(EndUserMessagingError):
    """The request would exceed a service quota for your account."""
    _ERROR_CODE = "ServiceQuotaExceededException"


class ThrottlingException(EndUserMessagingError):
    """The request was denied because it exceeded the allowed request rate."""
    _ERROR_CODE = "ThrottlingException"


class ValidationException(EndUserMessagingError):
    """A standard error for input validation failures. This should be thrown by services
    when a member of the input structure falls outside of the modeled or documented
    constraints.
    """

    _ERROR_CODE = "ValidationException"

    @property
    def field_list(self) -> list[Any] | None:
        """A list of specific failures encountered while validating the input. A member can
        appear in this list more than once if it failed to satisfy multiple constraints.
        """
        return self.response.get("fieldList")


EXCEPTIONS: dict[str, type[EndUserMessagingError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
