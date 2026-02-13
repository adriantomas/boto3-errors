# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class m2Error(Boto3Error):
    _SERVICE = "m2"


class AccessDeniedException(m2Error):
    """The account or role doesn't have the right permissions to make the request."""
    _ERROR_CODE = "AccessDeniedException"


class ConflictException(m2Error):
    """The parameters provided in the request conflict with existing resources."""
    _ERROR_CODE = "ConflictException"

    @property
    def resource_id(self) -> str | None:
        """The ID of the conflicting resource."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of the conflicting resource."""
        return self.response.get("resourceType")


class ExecutionTimeoutException(m2Error):
    """Failed to connect to server, or didn’t receive response within expected time period."""
    _ERROR_CODE = "ExecutionTimeoutException"


class InternalServerException(m2Error):
    """An unexpected error occurred during the processing of the request."""
    _ERROR_CODE = "InternalServerException"

    @property
    def retry_after_seconds(self) -> int | None:
        """The number of seconds to wait before retrying the request."""
        return self.response.get("retryAfterSeconds")


class ResourceNotFoundException(m2Error):
    """The specified resource was not found."""
    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def resource_id(self) -> str | None:
        """The ID of the missing resource."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of the missing resource."""
        return self.response.get("resourceType")


class ServiceQuotaExceededException(m2Error):
    """One or more quotas for Amazon Web Services Mainframe Modernization exceeds the
    limit.
    """

    _ERROR_CODE = "ServiceQuotaExceededException"

    @property
    def quota_code(self) -> str | None:
        """The identifier of the exceeded quota."""
        return self.response.get("quotaCode")

    @property
    def resource_id(self) -> str | None:
        """The ID of the resource that is exceeding the quota limit."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of resource that is exceeding the quota limit for Amazon Web Services
        Mainframe Modernization.
        """
        return self.response.get("resourceType")

    @property
    def service_code(self) -> str | None:
        """A code that identifies the service that the exceeded quota belongs to."""
        return self.response.get("serviceCode")


class ServiceUnavailableException(m2Error):
    """Server cannot process the request at the moment."""
    _ERROR_CODE = "ServiceUnavailableException"


class ThrottlingException(m2Error):
    """The number of requests made exceeds the limit."""
    _ERROR_CODE = "ThrottlingException"

    @property
    def quota_code(self) -> str | None:
        """The identifier of the throttled request."""
        return self.response.get("quotaCode")

    @property
    def retry_after_seconds(self) -> int | None:
        """The number of seconds to wait before retrying the request."""
        return self.response.get("retryAfterSeconds")

    @property
    def service_code(self) -> str | None:
        """The identifier of the service that the throttled request was made to."""
        return self.response.get("serviceCode")


class ValidationException(m2Error):
    """One or more parameters provided in the request is not valid."""
    _ERROR_CODE = "ValidationException"

    @property
    def field_list(self) -> list[Any] | None:
        """The list of fields that failed service validation."""
        return self.response.get("fieldList")

    @property
    def reason(self) -> str | None:
        """The reason why it failed service validation."""
        return self.response.get("reason")


EXCEPTIONS: dict[str, type[m2Error]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "ExecutionTimeoutException": ExecutionTimeoutException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ServiceUnavailableException": ServiceUnavailableException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
