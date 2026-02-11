# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class codeartifactError(Boto3Error):
    _SERVICE = "codeartifact"


class AccessDeniedException(codeartifactError):
    """The operation did not succeed because of an unauthorized access attempt."""
    _ERROR_CODE = "AccessDeniedException"


class ConflictException(codeartifactError):
    """The operation did not succeed because prerequisites are not met."""
    _ERROR_CODE = "ConflictException"

    @property
    def resource_id(self) -> str | None:
        """The ID of the resource."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of Amazon Web Services resource."""
        return self.response.get("resourceType")


class InternalServerException(codeartifactError):
    """The operation did not succeed because of an error that occurred inside CodeArtifact."""
    _ERROR_CODE = "InternalServerException"


class ResourceNotFoundException(codeartifactError):
    """The operation did not succeed because the resource requested is not found in the
    service.
    """

    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def resource_id(self) -> str | None:
        """The ID of the resource."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of Amazon Web Services resource."""
        return self.response.get("resourceType")


class ServiceQuotaExceededException(codeartifactError):
    """The operation did not succeed because it would have exceeded a service limit for
    your account.
    """

    _ERROR_CODE = "ServiceQuotaExceededException"

    @property
    def resource_id(self) -> str | None:
        """The ID of the resource."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of Amazon Web Services resource."""
        return self.response.get("resourceType")


class ThrottlingException(codeartifactError):
    """The operation did not succeed because too many requests are sent to the service."""
    _ERROR_CODE = "ThrottlingException"

    @property
    def retry_after_seconds(self) -> int | None:
        """The time period, in seconds, to wait before retrying the request."""
        return self.response.get("retryAfterSeconds")


class ValidationException(codeartifactError):
    """The operation did not succeed because a parameter in the request was sent with an
    invalid value.
    """

    _ERROR_CODE = "ValidationException"

    @property
    def reason(self) -> str | None:
        return self.response.get("reason")


EXCEPTIONS: dict[str, type[codeartifactError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
