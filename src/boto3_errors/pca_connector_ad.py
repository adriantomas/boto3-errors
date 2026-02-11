# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class PcaConnectorAdError(Boto3Error):
    _SERVICE = "pca-connector-ad"


class AccessDeniedException(PcaConnectorAdError):
    """You can receive this error if you attempt to create a resource share when you don't
    have the required permissions. This can be caused by insufficient permissions in
    policies attached to your Amazon Web Services Identity and Access Management (IAM)
    principal. It can also happen because of restrictions in place from an Amazon Web
    Services Organizations service control policy (SCP) that affects your Amazon Web
    Services account.
    """

    _ERROR_CODE = "AccessDeniedException"


class ConflictException(PcaConnectorAdError):
    """This request cannot be completed for one of the following reasons because the
    requested resource was being concurrently modified by another request.
    """

    _ERROR_CODE = "ConflictException"

    @property
    def resource_id(self) -> str | None:
        """The identifier of the Amazon Web Services resource."""
        return self.response.get("ResourceId")

    @property
    def resource_type(self) -> str | None:
        """The resource type, which can be one of `Connector`, `Template`,
        `TemplateGroupAccessControlEntry`, `ServicePrincipalName`, or
        `DirectoryRegistration`.
        """
        return self.response.get("ResourceType")


class InternalServerException(PcaConnectorAdError):
    """The request processing has failed because of an unknown error, exception or failure
    with an internal server.
    """

    _ERROR_CODE = "InternalServerException"


class ResourceNotFoundException(PcaConnectorAdError):
    """The operation tried to access a nonexistent resource. The resource might not be
    specified correctly, or its status might not be ACTIVE.
    """

    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def resource_id(self) -> str | None:
        """The identifier of the Amazon Web Services resource."""
        return self.response.get("ResourceId")

    @property
    def resource_type(self) -> str | None:
        """The resource type, which can be one of `Connector`, `Template`,
        `TemplateGroupAccessControlEntry`, `ServicePrincipalName`, or
        `DirectoryRegistration`.
        """
        return self.response.get("ResourceType")


class ServiceQuotaExceededException(PcaConnectorAdError):
    """Request would cause a service quota to be exceeded."""
    _ERROR_CODE = "ServiceQuotaExceededException"

    @property
    def quota_code(self) -> str | None:
        """The code associated with the service quota."""
        return self.response.get("QuotaCode")

    @property
    def resource_id(self) -> str | None:
        """The identifier of the Amazon Web Services resource."""
        return self.response.get("ResourceId")

    @property
    def resource_type(self) -> str | None:
        """The resource type, which can be one of `Connector`, `Template`,
        `TemplateGroupAccessControlEntry`, `ServicePrincipalName`, or
        `DirectoryRegistration`.
        """
        return self.response.get("ResourceType")

    @property
    def service_code(self) -> str | None:
        """Identifies the originating service."""
        return self.response.get("ServiceCode")


class ThrottlingException(PcaConnectorAdError):
    """The limit on the number of requests per second was exceeded."""
    _ERROR_CODE = "ThrottlingException"

    @property
    def quota_code(self) -> str | None:
        """The code associated with the quota."""
        return self.response.get("QuotaCode")

    @property
    def service_code(self) -> str | None:
        """Identifies the originating service."""
        return self.response.get("ServiceCode")


class ValidationException(PcaConnectorAdError):
    """An input validation error occurred. For example, invalid characters in a template
    name, or if a pagination token is invalid.
    """

    _ERROR_CODE = "ValidationException"

    @property
    def reason(self) -> str | None:
        """The reason for the validation error. This won't be return for every validation
        exception.
        """
        return self.response.get("Reason")


EXCEPTIONS: dict[str, type[PcaConnectorAdError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
