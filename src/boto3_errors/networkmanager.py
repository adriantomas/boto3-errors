# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class NetworkManagerError(Boto3Error):
    _SERVICE = "networkmanager"


class AccessDeniedException(NetworkManagerError):
    """You do not have sufficient access to perform this action."""
    _ERROR_CODE = "AccessDeniedException"


class ConflictException(NetworkManagerError):
    """There was a conflict processing the request. Updating or deleting the resource can
    cause an inconsistent state.
    """

    _ERROR_CODE = "ConflictException"

    @property
    def resource_id(self) -> str | None:
        """The ID of the resource."""
        return self.response.get("ResourceId")

    @property
    def resource_type(self) -> str | None:
        """The resource type."""
        return self.response.get("ResourceType")


class CoreNetworkPolicyException(NetworkManagerError):
    """Describes a core network policy exception."""
    _ERROR_CODE = "CoreNetworkPolicyException"

    @property
    def errors(self) -> list[Any] | None:
        """Describes a core network policy exception."""
        return self.response.get("Errors")


class InternalServerException(NetworkManagerError):
    """The request has failed due to an internal error."""
    _ERROR_CODE = "InternalServerException"

    @property
    def retry_after_seconds(self) -> int | None:
        """Indicates when to retry the request."""
        return self.response.get("RetryAfterSeconds")


class ResourceNotFoundException(NetworkManagerError):
    """The specified resource could not be found."""
    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def resource_id(self) -> str | None:
        """The ID of the resource."""
        return self.response.get("ResourceId")

    @property
    def resource_type(self) -> str | None:
        """The resource type."""
        return self.response.get("ResourceType")

    @property
    def context(self) -> dict[str, Any] | None:
        """The specified resource could not be found."""
        return self.response.get("Context")


class ServiceQuotaExceededException(NetworkManagerError):
    """A service limit was exceeded."""
    _ERROR_CODE = "ServiceQuotaExceededException"

    @property
    def resource_id(self) -> str | None:
        """The ID of the resource."""
        return self.response.get("ResourceId")

    @property
    def resource_type(self) -> str | None:
        """The resource type."""
        return self.response.get("ResourceType")

    @property
    def limit_code(self) -> str | None:
        """The limit code."""
        return self.response.get("LimitCode")

    @property
    def service_code(self) -> str | None:
        """The service code."""
        return self.response.get("ServiceCode")


class ThrottlingException(NetworkManagerError):
    """The request was denied due to request throttling."""
    _ERROR_CODE = "ThrottlingException"

    @property
    def retry_after_seconds(self) -> int | None:
        """Indicates when to retry the request."""
        return self.response.get("RetryAfterSeconds")


class ValidationException(NetworkManagerError):
    """The input fails to satisfy the constraints."""
    _ERROR_CODE = "ValidationException"

    @property
    def reason(self) -> str | None:
        """The reason for the error."""
        return self.response.get("Reason")

    @property
    def fields(self) -> list[Any] | None:
        """The fields that caused the error, if applicable."""
        return self.response.get("Fields")


EXCEPTIONS: dict[str, type[NetworkManagerError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "CoreNetworkPolicyException": CoreNetworkPolicyException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
