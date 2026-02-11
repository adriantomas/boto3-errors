# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class AIOpsError(Boto3Error):
    _SERVICE = "aiops"


class AccessDeniedException(AIOpsError):
    """You don't have sufficient permissions to perform this action."""
    _ERROR_CODE = "AccessDeniedException"


class ConflictException(AIOpsError):
    """This operation couldn't be completed because of a conflict in resource states."""
    _ERROR_CODE = "ConflictException"


class ForbiddenException(AIOpsError):
    """Access id denied for this operation, or this operation is not valid for the
    specified resource.
    """

    _ERROR_CODE = "ForbiddenException"


class InternalServerException(AIOpsError):
    """An internal server error occurred. You can try again later."""
    _ERROR_CODE = "InternalServerException"


class ResourceNotFoundException(AIOpsError):
    """The specified resource doesn't exist."""
    _ERROR_CODE = "ResourceNotFoundException"


class ServiceQuotaExceededException(AIOpsError):
    """This request exceeds a service quota."""
    _ERROR_CODE = "ServiceQuotaExceededException"

    @property
    def resource_id(self) -> str | None:
        """The resource that caused the quota exception."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of resource that caused the quota exception."""
        return self.response.get("resourceType")

    @property
    def service_code(self) -> str | None:
        """This name of the service associated with the error."""
        return self.response.get("serviceCode")

    @property
    def quota_code(self) -> str | None:
        """This quota that was exceeded."""
        return self.response.get("quotaCode")


class ThrottlingException(AIOpsError):
    """The request was throttled because of quota limits. You can try again later."""
    _ERROR_CODE = "ThrottlingException"


class ValidationException(AIOpsError):
    """This operation or its parameters aren't formatted correctly."""
    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[AIOpsError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "ForbiddenException": ForbiddenException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
