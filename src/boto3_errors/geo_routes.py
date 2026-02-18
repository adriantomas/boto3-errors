# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class GeoRoutesError(Boto3Error):
    _SERVICE = "geo-routes"


class AccessDeniedException(GeoRoutesError):
    """You don't have sufficient access to perform this action."""
    _ERROR_CODE = "AccessDeniedException"


class InternalServerException(GeoRoutesError):
    """The request processing has failed because of an unknown error, exception or failure."""
    _ERROR_CODE = "InternalServerException"


class ThrottlingException(GeoRoutesError):
    """The request was denied due to request throttling."""
    _ERROR_CODE = "ThrottlingException"


class ValidationException(GeoRoutesError):
    """The input fails to satisfy the constraints specified by an AWS service."""
    _ERROR_CODE = "ValidationException"

    @property
    def field_list(self) -> list[Any] | None:
        """The field where the invalid entry was detected."""
        return self.response.get("FieldList")

    @property
    def reason(self) -> str | None:
        """A message with the reason for the validation exception error."""
        return self.response.get("Reason")


EXCEPTIONS: dict[str, type[GeoRoutesError]] = {
    "AccessDeniedException": AccessDeniedException,
    "InternalServerException": InternalServerException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
