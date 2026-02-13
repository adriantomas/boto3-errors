# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class odbError(Boto3Error):
    _SERVICE = "odb"


class AccessDeniedException(odbError):
    """You don't have sufficient access to perform this action. Make sure you have the
    required permissions and try again.
    """

    _ERROR_CODE = "AccessDeniedException"


class ConflictException(odbError):
    """Occurs when a conflict with the current status of your resource. Fix any
    inconsistencies with your resource and try again.
    """

    _ERROR_CODE = "ConflictException"

    @property
    def resource_id(self) -> str | None:
        """The identifier of the resource that caused the conflict."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of resource that caused the conflict."""
        return self.response.get("resourceType")


class InternalServerException(odbError):
    """Occurs when there is an internal failure in the Oracle Database@Amazon Web Services
    service. Wait and try again.
    """

    _ERROR_CODE = "InternalServerException"

    @property
    def retry_after_seconds(self) -> int | None:
        """The number of seconds to wait before retrying the request after an internal
        server error.
        """
        return self.response.get("retryAfterSeconds")


class ResourceNotFoundException(odbError):
    """The operation tried to access a resource that doesn't exist. Make sure you provided
    the correct resource and try again.
    """

    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def resource_id(self) -> str | None:
        """The identifier of the resource that was not found."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of resource that was not found."""
        return self.response.get("resourceType")


class ServiceQuotaExceededException(odbError):
    """You have exceeded the service quota."""
    _ERROR_CODE = "ServiceQuotaExceededException"

    @property
    def resource_id(self) -> str | None:
        """The identifier of the resource that exceeded the service quota."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of resource that exceeded the service quota."""
        return self.response.get("resourceType")

    @property
    def quota_code(self) -> str | None:
        """The unqiue identifier of the service quota that was exceeded."""
        return self.response.get("quotaCode")


class ThrottlingException(odbError):
    """The request was denied due to request throttling."""
    _ERROR_CODE = "ThrottlingException"

    @property
    def retry_after_seconds(self) -> int | None:
        """The number of seconds to wait before retrying the request after being throttled."""
        return self.response.get("retryAfterSeconds")


class ValidationException(odbError):
    """The request has failed validation because it is missing required fields or has
    invalid inputs.
    """

    _ERROR_CODE = "ValidationException"

    @property
    def reason(self) -> str | None:
        """The reason why the validation failed."""
        return self.response.get("reason")

    @property
    def field_list(self) -> list[Any] | None:
        """A list of fields that failed validation."""
        return self.response.get("fieldList")


EXCEPTIONS: dict[str, type[odbError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
