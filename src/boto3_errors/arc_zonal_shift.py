# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class ARCZonalShiftError(Boto3Error):
    _SERVICE = "arc-zonal-shift"


class AccessDeniedException(ARCZonalShiftError):
    """You do not have sufficient access to perform this action."""
    _ERROR_CODE = "AccessDeniedException"


class ConflictException(ARCZonalShiftError):
    """The request could not be processed because of conflict in the current state of the
    resource.
    """

    _ERROR_CODE = "ConflictException"

    @property
    def reason(self) -> str | None:
        """The reason for the conflict exception."""
        return self.response.get("reason")

    @property
    def zonal_shift_id(self) -> str | None:
        """The zonal shift ID associated with the conflict exception."""
        return self.response.get("zonalShiftId")


class InternalServerException(ARCZonalShiftError):
    """There was an internal server error."""
    _ERROR_CODE = "InternalServerException"


class ResourceNotFoundException(ARCZonalShiftError):
    """The input requested a resource that was not found."""
    _ERROR_CODE = "ResourceNotFoundException"


class ThrottlingException(ARCZonalShiftError):
    """The request was denied due to request throttling."""
    _ERROR_CODE = "ThrottlingException"


class ValidationException(ARCZonalShiftError):
    """The input fails to satisfy the constraints specified by an Amazon Web Services
    service.
    """

    _ERROR_CODE = "ValidationException"

    @property
    def reason(self) -> str | None:
        """The reason for the validation exception."""
        return self.response.get("reason")


EXCEPTIONS: dict[str, type[ARCZonalShiftError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
