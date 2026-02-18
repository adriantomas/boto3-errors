# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class billingconductorError(Boto3Error):
    _SERVICE = "billingconductor"


class AccessDeniedException(billingconductorError):
    """You do not have sufficient access to perform this action."""
    _ERROR_CODE = "AccessDeniedException"


class ConflictException(billingconductorError):
    """You can cause an inconsistent state by updating or deleting a resource."""
    _ERROR_CODE = "ConflictException"

    @property
    def reason(self) -> str | None:
        """Reason for the inconsistent state."""
        return self.response.get("Reason")

    @property
    def resource_id(self) -> str | None:
        """Identifier of the resource in use."""
        return self.response.get("ResourceId")

    @property
    def resource_type(self) -> str | None:
        """Type of the resource in use."""
        return self.response.get("ResourceType")


class InternalServerException(billingconductorError):
    """An unexpected error occurred while processing a request."""
    _ERROR_CODE = "InternalServerException"

    @property
    def retry_after_seconds(self) -> int | None:
        """Number of seconds you can retry after the call."""
        return self.response.get("RetryAfterSeconds")


class ResourceNotFoundException(billingconductorError):
    """The request references a resource that doesn't exist."""
    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def resource_id(self) -> str | None:
        """Resource identifier that was not found."""
        return self.response.get("ResourceId")

    @property
    def resource_type(self) -> str | None:
        """Resource type that was not found."""
        return self.response.get("ResourceType")


class ServiceLimitExceededException(billingconductorError):
    """The request would cause a service limit to exceed."""
    _ERROR_CODE = "ServiceLimitExceededException"

    @property
    def limit_code(self) -> str | None:
        """The unique code identifier of the service limit that is being exceeded."""
        return self.response.get("LimitCode")

    @property
    def resource_id(self) -> str | None:
        """Identifier of the resource affected."""
        return self.response.get("ResourceId")

    @property
    def resource_type(self) -> str | None:
        """Type of the resource affected."""
        return self.response.get("ResourceType")

    @property
    def service_code(self) -> str | None:
        """The unique code for the service of the limit that is being exceeded."""
        return self.response.get("ServiceCode")


class ThrottlingException(billingconductorError):
    """The request was denied due to request throttling."""
    _ERROR_CODE = "ThrottlingException"

    @property
    def retry_after_seconds(self) -> int | None:
        """Number of seconds you can safely retry after the call."""
        return self.response.get("RetryAfterSeconds")


class ValidationException(billingconductorError):
    """The input doesn't match with the constraints specified by Amazon Web Services
    services.
    """

    _ERROR_CODE = "ValidationException"

    @property
    def fields(self) -> list[Any] | None:
        """The fields that caused the error, if applicable."""
        return self.response.get("Fields")

    @property
    def reason(self) -> str | None:
        """The reason the request's validation failed."""
        return self.response.get("Reason")


EXCEPTIONS: dict[str, type[billingconductorError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceLimitExceededException": ServiceLimitExceededException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
