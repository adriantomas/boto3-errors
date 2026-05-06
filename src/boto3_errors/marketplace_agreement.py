# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class MarketplaceAgreementError(Boto3Error):
    _SERVICE = "marketplace-agreement"


class AccessDeniedException(MarketplaceAgreementError):
    """User does not have sufficient access to perform this action."""
    _ERROR_CODE = "AccessDeniedException"

    @property
    def reason(self) -> str | None:
        """The reason for the access denied exception."""
        return self.response.get("reason")

    @property
    def request_id(self) -> str | None:
        """The unique identifier for the error."""
        return self.response.get("requestId")


class ConflictException(MarketplaceAgreementError):
    """Request was denied due to a resource conflict."""
    _ERROR_CODE = "ConflictException"

    @property
    def request_id(self) -> str | None:
        """The unique identifier for the error."""
        return self.response.get("requestId")

    @property
    def resource_id(self) -> str | None:
        """The unique identifier of the resource involved in the conflict."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of the resource involved in the conflict."""
        return self.response.get("resourceType")


class InternalServerException(MarketplaceAgreementError):
    """Unexpected error during processing of request."""
    _ERROR_CODE = "InternalServerException"

    @property
    def request_id(self) -> str | None:
        """The unique identifier for the error."""
        return self.response.get("requestId")


class ResourceNotFoundException(MarketplaceAgreementError):
    """Request references a resource which does not exist."""
    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def request_id(self) -> str | None:
        """The unique identifier for the error."""
        return self.response.get("requestId")

    @property
    def resource_id(self) -> str | None:
        """The unique identifier for the resource."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of resource."""
        return self.response.get("resourceType")


class ServiceQuotaExceededException(MarketplaceAgreementError):
    """Request exceeded the maximum allowed limit (quota) for a specific resource or API
    operation.
    """

    _ERROR_CODE = "ServiceQuotaExceededException"

    @property
    def quota_code(self) -> str | None:
        """The code of the quota that was exceeded."""
        return self.response.get("quotaCode")

    @property
    def request_id(self) -> str | None:
        """The unique identifier for the error."""
        return self.response.get("requestId")

    @property
    def resource_id(self) -> str | None:
        """The unique identifier of the resource that exceeded the quota."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of the resource that exceeded the quota."""
        return self.response.get("resourceType")

    @property
    def service_code(self) -> str | None:
        """The code of the service whose quota was exceeded."""
        return self.response.get("serviceCode")


class ThrottlingException(MarketplaceAgreementError):
    """Request was denied due to request throttling."""
    _ERROR_CODE = "ThrottlingException"

    @property
    def request_id(self) -> str | None:
        """The unique identifier for the error."""
        return self.response.get("requestId")


class ValidationException(MarketplaceAgreementError):
    """The input fails to satisfy the constraints specified by the service."""
    _ERROR_CODE = "ValidationException"

    @property
    def fields(self) -> list[Any] | None:
        """The fields associated with the error."""
        return self.response.get("fields")

    @property
    def reason(self) -> str | None:
        """The reason associated with the error."""
        return self.response.get("reason")

    @property
    def request_id(self) -> str | None:
        """The unique identifier associated with the error."""
        return self.response.get("requestId")


EXCEPTIONS: dict[str, type[MarketplaceAgreementError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
