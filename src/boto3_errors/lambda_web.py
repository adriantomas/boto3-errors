# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class LambdaWebError(Boto3Error):
    _SERVICE = "lambda-web"


class AccessDeniedException(LambdaWebError):
    """You do not have sufficient permissions to perform this operation."""
    _ERROR_CODE = "AccessDeniedException"


class ConflictException(LambdaWebError):
    """The request conflicts with the current state of the resource. Resolve the conflict
    and try again.
    """

    _ERROR_CODE = "ConflictException"

    @property
    def resource_id(self) -> str | None:
        """The identifier of the resource in conflict."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of the resource in conflict."""
        return self.response.get("resourceType")


class InternalServerException(LambdaWebError):
    """An internal server error occurred. Try again later."""
    _ERROR_CODE = "InternalServerException"


class ResourceNotFoundException(LambdaWebError):
    """The specified resource was not found. Verify the resource identifier and try again."""
    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def resource_id(self) -> str | None:
        """The identifier of the resource that was not found."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of the resource that was not found."""
        return self.response.get("resourceType")


class ServiceQuotaExceededException(LambdaWebError):
    """A service quota was exceeded. Request a quota increase or reduce usage and try
    again.
    """

    _ERROR_CODE = "ServiceQuotaExceededException"

    @property
    def quota_code(self) -> str | None:
        """The quota code of the exceeded quota."""
        return self.response.get("quotaCode")

    @property
    def resource_id(self) -> str | None:
        """The identifier of the resource that exceeded the quota."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of resource that exceeded the quota."""
        return self.response.get("resourceType")

    @property
    def service_code(self) -> str | None:
        """The service code of the service that owns the quota."""
        return self.response.get("serviceCode")


class ThrottlingException(LambdaWebError):
    """The request was throttled. Reduce the frequency of requests and try again."""
    _ERROR_CODE = "ThrottlingException"

    @property
    def quota_code(self) -> str | None:
        """The quota code that was exceeded, if applicable."""
        return self.response.get("quotaCode")

    @property
    def retry_after_seconds(self) -> int | None:
        """The number of seconds to wait before retrying the request."""
        return self.response.get("retryAfterSeconds")

    @property
    def service_code(self) -> str | None:
        """The service code of the throttled service."""
        return self.response.get("serviceCode")


class ValidationException(LambdaWebError):
    """The request failed validation. Check the request parameters and try again."""
    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[LambdaWebError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
