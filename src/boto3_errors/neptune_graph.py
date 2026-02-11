# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class NeptuneGraphError(Boto3Error):
    _SERVICE = "neptune-graph"


class AccessDeniedException(NeptuneGraphError):
    """Raised in case of an authentication or authorization failure."""
    _ERROR_CODE = "AccessDeniedException"


class ConflictException(NeptuneGraphError):
    """Raised when a conflict is encountered."""
    _ERROR_CODE = "ConflictException"

    @property
    def reason(self) -> str | None:
        """The reason for the conflict exception."""
        return self.response.get("reason")


class InternalServerException(NeptuneGraphError):
    """A failure occurred on the server."""
    _ERROR_CODE = "InternalServerException"


class ResourceNotFoundException(NeptuneGraphError):
    """A specified resource could not be located."""
    _ERROR_CODE = "ResourceNotFoundException"


class ServiceQuotaExceededException(NeptuneGraphError):
    """A service quota was exceeded."""
    _ERROR_CODE = "ServiceQuotaExceededException"

    @property
    def resource_id(self) -> str | None:
        """The identifier of the resource that exceeded quota."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of the resource that exceeded quota. Ex: Graph, Snapshot"""
        return self.response.get("resourceType")

    @property
    def service_code(self) -> str | None:
        """The service code that exceeded quota."""
        return self.response.get("serviceCode")

    @property
    def quota_code(self) -> str | None:
        """Service quota code of the resource for which quota was exceeded."""
        return self.response.get("quotaCode")


class ThrottlingException(NeptuneGraphError):
    """The exception was interrupted by throttling."""
    _ERROR_CODE = "ThrottlingException"


class UnprocessableException(NeptuneGraphError):
    """Request cannot be processed due to known reasons. Eg. partition full."""
    _ERROR_CODE = "UnprocessableException"

    @property
    def reason(self) -> str | None:
        """The reason for the unprocessable exception."""
        return self.response.get("reason")


class ValidationException(NeptuneGraphError):
    """A resource could not be validated."""
    _ERROR_CODE = "ValidationException"

    @property
    def reason(self) -> str | None:
        """The reason that the resource could not be validated."""
        return self.response.get("reason")


EXCEPTIONS: dict[str, type[NeptuneGraphError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "UnprocessableException": UnprocessableException,
    "ValidationException": ValidationException,
}
