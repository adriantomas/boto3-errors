# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class ManagedBlockchainQueryError(Boto3Error):
    _SERVICE = "managedblockchain-query"


class AccessDeniedException(ManagedBlockchainQueryError):
    """The Amazon Web Services account doesn’t have access to this resource."""
    _ERROR_CODE = "AccessDeniedException"


class InternalServerException(ManagedBlockchainQueryError):
    """The request processing has failed because of an internal error in the service."""
    _ERROR_CODE = "InternalServerException"

    @property
    def retry_after_seconds(self) -> int | None:
        """Specifies the `retryAfterSeconds` value."""
        return self.response.get("retryAfterSeconds")


class ResourceNotFoundException(ManagedBlockchainQueryError):
    """The resource was not found."""
    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def resource_id(self) -> str | None:
        """The `resourceId` of the resource that caused the exception."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """The `resourceType` of the resource that caused the exception."""
        return self.response.get("resourceType")


class ServiceQuotaExceededException(ManagedBlockchainQueryError):
    """The service quota has been exceeded for this resource."""
    _ERROR_CODE = "ServiceQuotaExceededException"

    @property
    def resource_id(self) -> str | None:
        """The `resourceId` of the resource that caused the exception."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """The `resourceType` of the resource that caused the exception."""
        return self.response.get("resourceType")

    @property
    def service_code(self) -> str | None:
        """The container for the `serviceCode`."""
        return self.response.get("serviceCode")

    @property
    def quota_code(self) -> str | None:
        """The container for the `quotaCode`."""
        return self.response.get("quotaCode")


class ThrottlingException(ManagedBlockchainQueryError):
    """The request or operation couldn't be performed because a service is throttling
    requests. The most common source of throttling errors is when you create resources
    that exceed your service limit for this resource type. Request a limit increase or
    delete unused resources, if possible.
    """

    _ERROR_CODE = "ThrottlingException"

    @property
    def service_code(self) -> str | None:
        """The container for the `serviceCode`."""
        return self.response.get("serviceCode")

    @property
    def quota_code(self) -> str | None:
        """The container for the `quotaCode`."""
        return self.response.get("quotaCode")

    @property
    def retry_after_seconds(self) -> int | None:
        """The container of the `retryAfterSeconds` value."""
        return self.response.get("retryAfterSeconds")


class ValidationException(ManagedBlockchainQueryError):
    """The resource passed is invalid."""
    _ERROR_CODE = "ValidationException"

    @property
    def reason(self) -> str | None:
        """The container for the reason for the exception"""
        return self.response.get("reason")

    @property
    def field_list(self) -> list[Any] | None:
        """The container for the `fieldList` of the exception."""
        return self.response.get("fieldList")


EXCEPTIONS: dict[str, type[ManagedBlockchainQueryError]] = {
    "AccessDeniedException": AccessDeniedException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
