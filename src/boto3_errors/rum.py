# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class RUMError(Boto3Error):
    _SERVICE = "rum"


class AccessDeniedException(RUMError):
    """You don't have sufficient permissions to perform this action."""
    _ERROR_CODE = "AccessDeniedException"


class ConflictException(RUMError):
    """This operation attempted to create a resource that already exists."""
    _ERROR_CODE = "ConflictException"

    @property
    def resource_name(self) -> str | None:
        """The name of the resource that is associated with the error."""
        return self.response.get("resourceName")

    @property
    def resource_type(self) -> str | None:
        """The type of the resource that is associated with the error."""
        return self.response.get("resourceType")


class InternalServerException(RUMError):
    """Internal service exception."""
    _ERROR_CODE = "InternalServerException"

    @property
    def retry_after_seconds(self) -> int | None:
        """The value of a parameter in the request caused an error."""
        return self.response.get("retryAfterSeconds")


class InvalidPolicyRevisionIdException(RUMError):
    """The policy revision ID that you provided doeesn't match the latest policy revision
    ID.
    """

    _ERROR_CODE = "InvalidPolicyRevisionIdException"


class MalformedPolicyDocumentException(RUMError):
    """The policy document that you specified is not formatted correctly."""
    _ERROR_CODE = "MalformedPolicyDocumentException"


class PolicyNotFoundException(RUMError):
    """The resource-based policy doesn't exist on this app monitor."""
    _ERROR_CODE = "PolicyNotFoundException"


class PolicySizeLimitExceededException(RUMError):
    """The policy document is too large. The limit is 4 KB."""
    _ERROR_CODE = "PolicySizeLimitExceededException"


class ResourceNotFoundException(RUMError):
    """Resource not found."""
    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def resource_name(self) -> str | None:
        """The name of the resource that is associated with the error."""
        return self.response.get("resourceName")

    @property
    def resource_type(self) -> str | None:
        """The type of the resource that is associated with the error."""
        return self.response.get("resourceType")


class ServiceQuotaExceededException(RUMError):
    """This request exceeds a service quota."""
    _ERROR_CODE = "ServiceQuotaExceededException"


class ThrottlingException(RUMError):
    """The request was throttled because of quota limits."""
    _ERROR_CODE = "ThrottlingException"

    @property
    def quota_code(self) -> str | None:
        """The ID of the service quota that was exceeded."""
        return self.response.get("quotaCode")

    @property
    def retry_after_seconds(self) -> int | None:
        """The value of a parameter in the request caused an error."""
        return self.response.get("retryAfterSeconds")

    @property
    def service_code(self) -> str | None:
        """The ID of the service that is associated with the error."""
        return self.response.get("serviceCode")


class ValidationException(RUMError):
    """One of the arguments for the request is not valid."""
    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[RUMError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "InvalidPolicyRevisionIdException": InvalidPolicyRevisionIdException,
    "MalformedPolicyDocumentException": MalformedPolicyDocumentException,
    "PolicyNotFoundException": PolicyNotFoundException,
    "PolicySizeLimitExceededException": PolicySizeLimitExceededException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
