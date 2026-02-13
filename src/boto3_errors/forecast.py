# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class forecastError(Boto3Error):
    _SERVICE = "forecast"


class InvalidInputException(forecastError):
    """We can't process the request because it includes an invalid value or a value that
    exceeds the valid range.
    """

    _ERROR_CODE = "InvalidInputException"


class InvalidNextTokenException(forecastError):
    """The token is not valid. Tokens expire after 24 hours."""
    _ERROR_CODE = "InvalidNextTokenException"


class LimitExceededException(forecastError):
    """The limit on the number of resources per account has been exceeded."""
    _ERROR_CODE = "LimitExceededException"


class ResourceAlreadyExistsException(forecastError):
    """There is already a resource with this name. Try again with a different name."""
    _ERROR_CODE = "ResourceAlreadyExistsException"


class ResourceInUseException(forecastError):
    """The specified resource is in use."""
    _ERROR_CODE = "ResourceInUseException"


class ResourceNotFoundException(forecastError):
    """We can't find a resource with that Amazon Resource Name (ARN). Check the ARN and try
    again.
    """

    _ERROR_CODE = "ResourceNotFoundException"


EXCEPTIONS: dict[str, type[forecastError]] = {
    "InvalidInputException": InvalidInputException,
    "InvalidNextTokenException": InvalidNextTokenException,
    "LimitExceededException": LimitExceededException,
    "ResourceAlreadyExistsException": ResourceAlreadyExistsException,
    "ResourceInUseException": ResourceInUseException,
    "ResourceNotFoundException": ResourceNotFoundException,
}
