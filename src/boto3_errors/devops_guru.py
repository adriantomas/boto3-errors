# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class DevOpsGuruError(Boto3Error):
    _SERVICE = "devops-guru"


class AccessDeniedException(DevOpsGuruError):
    """You don't have permissions to perform the requested operation. The user or role that
    is making the request must have at least one IAM permissions policy attached that
    grants the required permissions. For more information, see Access Management in the
    IAM User Guide.
    """

    _ERROR_CODE = "AccessDeniedException"


class ConflictException(DevOpsGuruError):
    """An exception that is thrown when a conflict occurs."""
    _ERROR_CODE = "ConflictException"

    @property
    def resource_id(self) -> str | None:
        """The ID of the Amazon Web Services resource in which a conflict occurred."""
        return self.response.get("ResourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of the Amazon Web Services resource in which a conflict occurred."""
        return self.response.get("ResourceType")


class InternalServerException(DevOpsGuruError):
    """An internal failure in an Amazon service occurred."""
    _ERROR_CODE = "InternalServerException"

    @property
    def retry_after_seconds(self) -> int | None:
        """The number of seconds after which the action that caused the internal server
        exception can be retried.
        """
        return self.response.get("RetryAfterSeconds")


class ResourceNotFoundException(DevOpsGuruError):
    """A requested resource could not be found"""
    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def resource_id(self) -> str | None:
        """The ID of the Amazon Web Services resource that could not be found."""
        return self.response.get("ResourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of the Amazon Web Services resource that could not be found."""
        return self.response.get("ResourceType")


class ServiceQuotaExceededException(DevOpsGuruError):
    """The request contains a value that exceeds a maximum quota."""
    _ERROR_CODE = "ServiceQuotaExceededException"


class ThrottlingException(DevOpsGuruError):
    """The request was denied due to a request throttling."""
    _ERROR_CODE = "ThrottlingException"

    @property
    def quota_code(self) -> str | None:
        """The code of the quota that was exceeded, causing the throttling exception."""
        return self.response.get("QuotaCode")

    @property
    def retry_after_seconds(self) -> int | None:
        """The number of seconds after which the action that caused the throttling
        exception can be retried.
        """
        return self.response.get("RetryAfterSeconds")

    @property
    def service_code(self) -> str | None:
        """The code of the service that caused the throttling exception."""
        return self.response.get("ServiceCode")


class ValidationException(DevOpsGuruError):
    """Contains information about data passed in to a field during a request that is not
    valid.
    """

    _ERROR_CODE = "ValidationException"

    @property
    def fields(self) -> list[Any] | None:
        return self.response.get("Fields")

    @property
    def reason(self) -> str | None:
        """The reason the validation exception was thrown."""
        return self.response.get("Reason")


EXCEPTIONS: dict[str, type[DevOpsGuruError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
