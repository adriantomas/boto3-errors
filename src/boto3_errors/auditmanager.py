# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class AuditManagerError(Boto3Error):
    _SERVICE = "auditmanager"


class AccessDeniedException(AuditManagerError):
    """Your account isn't registered with Audit Manager. Check the delegated administrator
    setup on the Audit Manager settings page, and try again.
    """

    _ERROR_CODE = "AccessDeniedException"


class InternalServerException(AuditManagerError):
    """An internal service error occurred during the processing of your request. Try again
    later.
    """

    _ERROR_CODE = "InternalServerException"


class ResourceNotFoundException(AuditManagerError):
    """The resource that's specified in the request can't be found."""
    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def resource_id(self) -> str | None:
        """The unique identifier for the resource."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of resource that's affected by the error."""
        return self.response.get("resourceType")


class ServiceQuotaExceededException(AuditManagerError):
    """You've reached your account quota for this resource type. To perform the requested
    action, delete some existing resources or request a quota increase from the Service
    Quotas console. For a list of Audit Manager service quotas, see Quotas and
    restrictions for Audit Manager.
    """

    _ERROR_CODE = "ServiceQuotaExceededException"


class ThrottlingException(AuditManagerError):
    """The request was denied due to request throttling."""
    _ERROR_CODE = "ThrottlingException"


class ValidationException(AuditManagerError):
    """The request has invalid or missing parameters."""
    _ERROR_CODE = "ValidationException"

    @property
    def fields(self) -> list[Any] | None:
        """The fields that caused the error, if applicable."""
        return self.response.get("fields")

    @property
    def reason(self) -> str | None:
        """The reason the request failed validation."""
        return self.response.get("reason")


EXCEPTIONS: dict[str, type[AuditManagerError]] = {
    "AccessDeniedException": AccessDeniedException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
