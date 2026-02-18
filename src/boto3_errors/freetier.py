# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class FreeTierError(Boto3Error):
    _SERVICE = "freetier"


class InternalServerException(FreeTierError):
    """An unexpected error occurred during the processing of your request."""
    _ERROR_CODE = "InternalServerException"


class ThrottlingException(FreeTierError):
    """The request was denied due to request throttling."""
    _ERROR_CODE = "ThrottlingException"


class ValidationException(FreeTierError):
    """The input fails to satisfy the constraints specified by an Amazon Web Service."""
    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[FreeTierError]] = {
    "InternalServerException": InternalServerException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
