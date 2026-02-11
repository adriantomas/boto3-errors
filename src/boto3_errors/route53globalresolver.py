# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class Route53GlobalResolverError(Boto3Error):
    _SERVICE = "route53globalresolver"


class AccessDeniedException(Route53GlobalResolverError):
    """You don't have permission to perform this operation. Check your IAM permissions and
    try again.
    """

    _ERROR_CODE = "AccessDeniedException"


class ConflictException(Route53GlobalResolverError):
    """The request conflicts with the current state of the resource. This can occur when
    trying to modify a resource that is not in a valid state for the requested
    operation.
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


class InternalServerException(Route53GlobalResolverError):
    """An internal server error occurred. Try again later."""
    _ERROR_CODE = "InternalServerException"

    @property
    def retry_after_seconds(self) -> int | None:
        """Number of seconds in which the caller can retry the request."""
        return self.response.get("retryAfterSeconds")


class ResourceNotFoundException(Route53GlobalResolverError):
    """The specified resource was not found. Verify the resource ID and try again."""
    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def resource_id(self) -> str | None:
        """The unique ID of the resource referenced in the failed request."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """The resource type of the resource referenced in the failed request."""
        return self.response.get("resourceType")


class ServiceQuotaExceededException(Route53GlobalResolverError):
    """The request would exceed one or more service quotas. Check your current usage and
    quotas, then try again.
    """

    _ERROR_CODE = "ServiceQuotaExceededException"

    @property
    def resource_id(self) -> str | None:
        """The unique ID of the resource referenced in the failed request."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """The resource type of the resource referenced in the failed request."""
        return self.response.get("resourceType")

    @property
    def service_code(self) -> str | None:
        """The code for the AWS service that owns the quota."""
        return self.response.get("serviceCode")

    @property
    def quota_code(self) -> str | None:
        """The quota code recognized by the AWS Service Quotas service."""
        return self.response.get("quotaCode")


class ThrottlingException(Route53GlobalResolverError):
    """The request was throttled due to too many requests. Wait a moment and try again."""
    _ERROR_CODE = "ThrottlingException"

    @property
    def service_code(self) -> str | None:
        """The code for the AWS service that owns the quota."""
        return self.response.get("serviceCode")

    @property
    def quota_code(self) -> str | None:
        """The quota code recognized by the AWS Service Quotas service."""
        return self.response.get("quotaCode")

    @property
    def retry_after_seconds(self) -> int | None:
        """Number of seconds in which the caller can retry the request."""
        return self.response.get("retryAfterSeconds")


class ValidationException(Route53GlobalResolverError):
    """The input parameters are invalid. Check the parameter values and try again."""
    _ERROR_CODE = "ValidationException"

    @property
    def reason(self) -> str | None:
        """Reason the request failed validation."""
        return self.response.get("reason")

    @property
    def field_list(self) -> list[Any] | None:
        """The list of fields that aren't valid."""
        return self.response.get("fieldList")


EXCEPTIONS: dict[str, type[Route53GlobalResolverError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
