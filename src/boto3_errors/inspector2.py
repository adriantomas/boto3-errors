# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class Inspector2Error(Boto3Error):
    _SERVICE = "inspector2"


class AccessDeniedException(Inspector2Error):
    """You do not have sufficient access to perform this action.

     For `Enable`, you receive this error if you attempt to use a feature in an
    unsupported Amazon Web Services Region.
    """

    _ERROR_CODE = "AccessDeniedException"


class BadRequestException(Inspector2Error):
    """One or more tags submitted as part of the request is not valid."""
    _ERROR_CODE = "BadRequestException"


class ConflictException(Inspector2Error):
    """A conflict occurred. This exception occurs when the same resource is being modified
    by concurrent requests.
    """

    _ERROR_CODE = "ConflictException"

    @property
    def resource_id(self) -> str | None:
        """The ID of the conflicting resource."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of the conflicting resource."""
        return self.response.get("resourceType")


class InternalServerException(Inspector2Error):
    """The request has failed due to an internal failure of the Amazon Inspector service."""
    _ERROR_CODE = "InternalServerException"

    @property
    def retry_after_seconds(self) -> int | None:
        """The number of seconds to wait before retrying the request."""
        return self.response.get("retryAfterSeconds")


class ResourceNotFoundException(Inspector2Error):
    """The operation tried to access an invalid resource. Make sure the resource is
    specified correctly.
    """

    _ERROR_CODE = "ResourceNotFoundException"


class ServiceQuotaExceededException(Inspector2Error):
    """You have exceeded your service quota. To perform the requested action, remove some
    of the relevant resources, or use Service Quotas to request a service quota
    increase.
    """

    _ERROR_CODE = "ServiceQuotaExceededException"

    @property
    def resource_id(self) -> str | None:
        """The ID of the resource that exceeds a service quota."""
        return self.response.get("resourceId")


class ThrottlingException(Inspector2Error):
    """The limit on the number of requests per second was exceeded."""
    _ERROR_CODE = "ThrottlingException"

    @property
    def retry_after_seconds(self) -> int | None:
        """The number of seconds to wait before retrying the request."""
        return self.response.get("retryAfterSeconds")


class ValidationException(Inspector2Error):
    """The request has failed validation due to missing required fields or having invalid
    inputs.
    """

    _ERROR_CODE = "ValidationException"

    @property
    def reason(self) -> str | None:
        """The reason for the validation failure."""
        return self.response.get("reason")

    @property
    def fields(self) -> list[Any] | None:
        """The fields that failed validation."""
        return self.response.get("fields")


EXCEPTIONS: dict[str, type[Inspector2Error]] = {
    "AccessDeniedException": AccessDeniedException,
    "BadRequestException": BadRequestException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
