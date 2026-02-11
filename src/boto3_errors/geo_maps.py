# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class GeoMapsError(Boto3Error):
    _SERVICE = "geo-maps"


class AccessDeniedException(GeoMapsError):
    """The request was denied because of insufficient access or permissions. Check with an
    administrator to verify your permissions.
    """

    _ERROR_CODE = "AccessDeniedException"


class InternalServerException(GeoMapsError):
    """The request processing has failed because of an unknown error, exception or failure."""
    _ERROR_CODE = "InternalServerException"


class ResourceNotFoundException(GeoMapsError):
    """Exception thrown when the associated resource could not be found."""
    _ERROR_CODE = "ResourceNotFoundException"


class ThrottlingException(GeoMapsError):
    """The request was denied due to request throttling."""
    _ERROR_CODE = "ThrottlingException"


class ValidationException(GeoMapsError):
    """The input fails to satisfy the constraints specified by an AWS service."""
    _ERROR_CODE = "ValidationException"

    @property
    def reason(self) -> str | None:
        """The field where the invalid entry was detected."""
        return self.response.get("Reason")

    @property
    def field_list(self) -> list[Any] | None:
        """A message with the reason for the validation exception error."""
        return self.response.get("FieldList")


EXCEPTIONS: dict[str, type[GeoMapsError]] = {
    "AccessDeniedException": AccessDeniedException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
