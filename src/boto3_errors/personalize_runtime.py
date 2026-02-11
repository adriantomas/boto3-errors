# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class PersonalizeRuntimeError(Boto3Error):
    _SERVICE = "personalize-runtime"


class InvalidInputException(PersonalizeRuntimeError):
    """Provide a valid value for the field or parameter."""
    _ERROR_CODE = "InvalidInputException"


class ResourceNotFoundException(PersonalizeRuntimeError):
    """The specified resource does not exist."""
    _ERROR_CODE = "ResourceNotFoundException"


EXCEPTIONS: dict[str, type[PersonalizeRuntimeError]] = {
    "InvalidInputException": InvalidInputException,
    "ResourceNotFoundException": ResourceNotFoundException,
}
