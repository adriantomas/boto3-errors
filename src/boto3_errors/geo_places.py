# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class GeoPlacesError(Boto3Error):
    _SERVICE = "geo-places"


class AccessDeniedException(GeoPlacesError):
    """You don't have sufficient access to perform this action."""
    _ERROR_CODE = "AccessDeniedException"


class InternalServerException(GeoPlacesError):
    """The request processing has failed because of an unknown error, exception or failure."""
    _ERROR_CODE = "InternalServerException"


class ThrottlingException(GeoPlacesError):
    """The request was denied due to request throttling."""
    _ERROR_CODE = "ThrottlingException"


class ValidationException(GeoPlacesError):
    """The input fails to satisfy the constraints specified by an AWS service."""
    _ERROR_CODE = "ValidationException"

    @property
    def reason(self) -> str | None:
        """Test stub for reason"""
        return self.response.get("Reason")

    @property
    def field_list(self) -> list[Any] | None:
        """Test stub for FieldList."""
        return self.response.get("FieldList")


EXCEPTIONS: dict[str, type[GeoPlacesError]] = {
    "AccessDeniedException": AccessDeniedException,
    "InternalServerException": InternalServerException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
