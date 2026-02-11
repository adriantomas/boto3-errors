# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class b2biError(Boto3Error):
    _SERVICE = "b2bi"


class AccessDeniedException(b2biError):
    """You do not have sufficient access to perform this action."""
    _ERROR_CODE = "AccessDeniedException"


class ConflictException(b2biError):
    """A conflict exception is thrown when you attempt to delete a resource (such as a
    profile or a capability) that is being used by other resources.
    """

    _ERROR_CODE = "ConflictException"


class InternalServerException(b2biError):
    """This exception is thrown when an error occurs in the Amazon Web Services B2B Data
    Interchange service.
    """

    _ERROR_CODE = "InternalServerException"

    @property
    def retry_after_seconds(self) -> int | None:
        """The server attempts to retry a failed command."""
        return self.response.get("retryAfterSeconds")


class ResourceNotFoundException(b2biError):
    """Occurs when the requested resource does not exist, or cannot be found. In some
    cases, the resource exists in a region other than the region specified in the API
    call.
    """

    _ERROR_CODE = "ResourceNotFoundException"


class ServiceQuotaExceededException(b2biError):
    """Occurs when the calling command attempts to exceed one of the service quotas, for
    example trying to create a capability when you already have the maximum number of
    capabilities allowed.
    """

    _ERROR_CODE = "ServiceQuotaExceededException"

    @property
    def resource_id(self) -> str | None:
        """The ID for the resource that exceeded the quota, which caused the exception."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """The resource type (profile, partnership, transformer, or capability) that
        exceeded the quota, which caused the exception.
        """
        return self.response.get("resourceType")

    @property
    def service_code(self) -> str | None:
        """The code responsible for exceeding the quota, which caused the exception."""
        return self.response.get("serviceCode")

    @property
    def quota_code(self) -> str | None:
        """The quota that was exceeded, which caused the exception."""
        return self.response.get("quotaCode")


class ThrottlingException(b2biError):
    """The request was denied due to throttling: the data speed and rendering may be
    limited depending on various parameters and conditions.
    """

    _ERROR_CODE = "ThrottlingException"

    @property
    def retry_after_seconds(self) -> int | None:
        """The server attempts to retry a command that was throttled."""
        return self.response.get("retryAfterSeconds")


class ValidationException(b2biError):
    """Occurs when a B2BI object cannot be validated against a request from another object.
    This exception can be thrown during standard EDI validation or when custom
    validation rules fail, such as when element length constraints are violated, invalid
    codes are used in code list validations, or required elements are missing based on
    configured element requirement rules.
    """

    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[b2biError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
