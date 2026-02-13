# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class MigrationHubRefactorSpacesError(Boto3Error):
    _SERVICE = "migration-hub-refactor-spaces"


class AccessDeniedException(MigrationHubRefactorSpacesError):
    """The user does not have sufficient access to perform this action."""
    _ERROR_CODE = "AccessDeniedException"


class ConflictException(MigrationHubRefactorSpacesError):
    """Updating or deleting a resource can cause an inconsistent state."""
    _ERROR_CODE = "ConflictException"

    @property
    def resource_id(self) -> str | None:
        """The ID of the resource."""
        return self.response.get("ResourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of resource."""
        return self.response.get("ResourceType")


class InternalServerException(MigrationHubRefactorSpacesError):
    """An unexpected error occurred while processing the request."""
    _ERROR_CODE = "InternalServerException"


class InvalidResourcePolicyException(MigrationHubRefactorSpacesError):
    """The resource policy is not valid."""
    _ERROR_CODE = "InvalidResourcePolicyException"


class ResourceNotFoundException(MigrationHubRefactorSpacesError):
    """The request references a resource that does not exist."""
    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def resource_id(self) -> str | None:
        """The ID of the resource."""
        return self.response.get("ResourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of resource."""
        return self.response.get("ResourceType")


class ServiceQuotaExceededException(MigrationHubRefactorSpacesError):
    """The request would cause a service quota to be exceeded."""
    _ERROR_CODE = "ServiceQuotaExceededException"

    @property
    def quota_code(self) -> str | None:
        """Service quota requirement to identify originating quota. Reached throttling
        quota exception.
        """
        return self.response.get("QuotaCode")

    @property
    def resource_id(self) -> str | None:
        """The ID of the resource."""
        return self.response.get("ResourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of resource."""
        return self.response.get("ResourceType")

    @property
    def service_code(self) -> str | None:
        """Service quota requirement to identify originating service. Reached throttling
        quota exception service code.
        """
        return self.response.get("ServiceCode")


class ThrottlingException(MigrationHubRefactorSpacesError):
    """Request was denied because the request was throttled."""
    _ERROR_CODE = "ThrottlingException"

    @property
    def quota_code(self) -> str | None:
        """Service quota requirement to identify originating quota. Reached throttling
        quota exception.
        """
        return self.response.get("QuotaCode")

    @property
    def retry_after_seconds(self) -> int | None:
        """The number of seconds to wait before retrying."""
        return self.response.get("RetryAfterSeconds")

    @property
    def service_code(self) -> str | None:
        """Service quota requirement to identify originating service. Reached throttling
        quota exception service code.
        """
        return self.response.get("ServiceCode")


class ValidationException(MigrationHubRefactorSpacesError):
    """The input does not satisfy the constraints specified by an Amazon Web Service."""
    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[MigrationHubRefactorSpacesError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "InvalidResourcePolicyException": InvalidResourcePolicyException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
