# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class LookoutMetricsError(Boto3Error):
    _SERVICE = "lookoutmetrics"


class AccessDeniedException(LookoutMetricsError):
    """You do not have sufficient permissions to perform this action."""
    _ERROR_CODE = "AccessDeniedException"


class ConflictException(LookoutMetricsError):
    """There was a conflict processing the request. Try your request again."""
    _ERROR_CODE = "ConflictException"

    @property
    def resource_id(self) -> str | None:
        """The ID of the resource."""
        return self.response.get("ResourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of the resource."""
        return self.response.get("ResourceType")


class InternalServerException(LookoutMetricsError):
    """The request processing has failed because of an unknown error, exception, or
    failure.
    """

    _ERROR_CODE = "InternalServerException"


class ResourceNotFoundException(LookoutMetricsError):
    """The specified resource cannot be found. Check the ARN of the resource and try again."""
    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def resource_id(self) -> str | None:
        """The ID of the resource."""
        return self.response.get("ResourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of the resource."""
        return self.response.get("ResourceType")


class ServiceQuotaExceededException(LookoutMetricsError):
    """The request exceeded the service's quotas. Check the service quotas and try again."""
    _ERROR_CODE = "ServiceQuotaExceededException"

    @property
    def quota_code(self) -> str | None:
        """The quota code."""
        return self.response.get("QuotaCode")

    @property
    def resource_id(self) -> str | None:
        """The ID of the resource."""
        return self.response.get("ResourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of the resource."""
        return self.response.get("ResourceType")

    @property
    def service_code(self) -> str | None:
        """The service code."""
        return self.response.get("ServiceCode")


class TooManyRequestsException(LookoutMetricsError):
    """The request was denied due to too many requests being submitted at the same time."""
    _ERROR_CODE = "TooManyRequestsException"


class ValidationException(LookoutMetricsError):
    """The input fails to satisfy the constraints specified by the AWS service. Check your
    input values and try again.
    """

    _ERROR_CODE = "ValidationException"

    @property
    def fields(self) -> list[Any] | None:
        """Fields that failed validation."""
        return self.response.get("Fields")

    @property
    def reason(self) -> str | None:
        """The reason that validation failed."""
        return self.response.get("Reason")


EXCEPTIONS: dict[str, type[LookoutMetricsError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "TooManyRequestsException": TooManyRequestsException,
    "ValidationException": ValidationException,
}
