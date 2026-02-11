# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class forecastqueryError(Boto3Error):
    _SERVICE = "forecastquery"


class InvalidInputException(forecastqueryError):
    """The value is invalid or is too long."""
    _ERROR_CODE = "InvalidInputException"


class InvalidNextTokenException(forecastqueryError):
    """The token is not valid. Tokens expire after 24 hours."""
    _ERROR_CODE = "InvalidNextTokenException"


class LimitExceededException(forecastqueryError):
    """The limit on the number of requests per second has been exceeded."""
    _ERROR_CODE = "LimitExceededException"


class ResourceInUseException(forecastqueryError):
    """The specified resource is in use."""
    _ERROR_CODE = "ResourceInUseException"


class ResourceNotFoundException(forecastqueryError):
    """We can't find that resource. Check the information that you've provided and try
    again.
    """

    _ERROR_CODE = "ResourceNotFoundException"


EXCEPTIONS: dict[str, type[forecastqueryError]] = {
    "InvalidInputException": InvalidInputException,
    "InvalidNextTokenException": InvalidNextTokenException,
    "LimitExceededException": LimitExceededException,
    "ResourceInUseException": ResourceInUseException,
    "ResourceNotFoundException": ResourceNotFoundException,
}
