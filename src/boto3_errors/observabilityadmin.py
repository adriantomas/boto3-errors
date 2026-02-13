# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class ObservabilityAdminError(Boto3Error):
    _SERVICE = "observabilityadmin"


class AccessDeniedException(ObservabilityAdminError):
    """Indicates you don't have permissions to perform the requested operation. The user or
    role that is making the request must have at least one IAM permissions policy
    attached that grants the required permissions. For more information, see Access
    management for Amazon Web Services resources in the IAM user guide.
    """

    _ERROR_CODE = "AccessDeniedException"

    @property
    def amzn_error_type(self) -> str | None:
        """The name of the exception."""
        return self.response.get("amznErrorType")


class ConflictException(ObservabilityAdminError):
    """The requested operation conflicts with the current state of the specified resource
    or with another request.
    """

    _ERROR_CODE = "ConflictException"

    @property
    def resource_id(self) -> str | None:
        """The identifier of the resource which is in conflict with the requested
        operation.
        """
        return self.response.get("ResourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of the resource which is in conflict with the requested operation."""
        return self.response.get("ResourceType")


class InternalServerException(ObservabilityAdminError):
    """Indicates the request has failed to process because of an unknown server error,
    exception, or failure.
    """

    _ERROR_CODE = "InternalServerException"

    @property
    def amzn_error_type(self) -> str | None:
        """The name of the exception."""
        return self.response.get("amznErrorType")

    @property
    def retry_after_seconds(self) -> int | None:
        """The number of seconds to wait before retrying the request."""
        return self.response.get("retryAfterSeconds")


class InvalidStateException(ObservabilityAdminError):
    """The requested operation cannot be completed on the specified resource in the current
    state.
    """

    _ERROR_CODE = "InvalidStateException"


class ResourceNotFoundException(ObservabilityAdminError):
    """The specified resource (such as a telemetry rule) could not be found."""
    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def resource_id(self) -> str | None:
        """The identifier of the resource which could not be found."""
        return self.response.get("ResourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of the resource which could not be found."""
        return self.response.get("ResourceType")


class ServiceQuotaExceededException(ObservabilityAdminError):
    """The requested operation would exceed the allowed quota for the specified resource
    type.
    """

    _ERROR_CODE = "ServiceQuotaExceededException"

    @property
    def resource_id(self) -> str | None:
        """The identifier of the resource which exceeds the service quota."""
        return self.response.get("ResourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of the resource which exceeds the service quota."""
        return self.response.get("ResourceType")

    @property
    def service_code(self) -> str | None:
        """The code for the service of the exceeded quota."""
        return self.response.get("ServiceCode")

    @property
    def quota_code(self) -> str | None:
        """The code for the exceeded service quota."""
        return self.response.get("QuotaCode")

    @property
    def amzn_error_type(self) -> str | None:
        """The name of the exception."""
        return self.response.get("amznErrorType")


class TooManyRequestsException(ObservabilityAdminError):
    """The request throughput limit was exceeded."""
    _ERROR_CODE = "TooManyRequestsException"


class ValidationException(ObservabilityAdminError):
    """Indicates input validation failed. Check your request parameters and retry the
    request.
    """

    _ERROR_CODE = "ValidationException"

    @property
    def errors(self) -> list[Any] | None:
        """The errors in the input which caused the exception."""
        return self.response.get("Errors")


EXCEPTIONS: dict[str, type[ObservabilityAdminError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "InvalidStateException": InvalidStateException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "TooManyRequestsException": TooManyRequestsException,
    "ValidationException": ValidationException,
}
