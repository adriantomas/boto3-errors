# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class OutpostsError(Boto3Error):
    _SERVICE = "outposts"


class AccessDeniedException(OutpostsError):
    """You do not have permission to perform this operation."""
    _ERROR_CODE = "AccessDeniedException"


class ConflictException(OutpostsError):
    """Updating or deleting this resource can cause an inconsistent state."""
    _ERROR_CODE = "ConflictException"

    @property
    def resource_id(self) -> str | None:
        """The ID of the resource causing the conflict."""
        return self.response.get("ResourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of the resource causing the conflict."""
        return self.response.get("ResourceType")


class InternalServerException(OutpostsError):
    """An internal error has occurred."""
    _ERROR_CODE = "InternalServerException"


class NotFoundException(OutpostsError):
    """The specified request is not valid."""
    _ERROR_CODE = "NotFoundException"


class ServiceQuotaExceededException(OutpostsError):
    """You have exceeded a service quota."""
    _ERROR_CODE = "ServiceQuotaExceededException"


class ValidationException(OutpostsError):
    """A parameter is not valid."""
    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[OutpostsError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "NotFoundException": NotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ValidationException": ValidationException,
}
