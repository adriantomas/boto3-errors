# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class PersonalizeEventsError(Boto3Error):
    _SERVICE = "personalize-events"


class InvalidInputException(PersonalizeEventsError):
    """Provide a valid value for the field or parameter."""
    _ERROR_CODE = "InvalidInputException"


class ResourceInUseException(PersonalizeEventsError):
    """The specified resource is in use."""
    _ERROR_CODE = "ResourceInUseException"


class ResourceNotFoundException(PersonalizeEventsError):
    """Could not find the specified resource."""
    _ERROR_CODE = "ResourceNotFoundException"


EXCEPTIONS: dict[str, type[PersonalizeEventsError]] = {
    "InvalidInputException": InvalidInputException,
    "ResourceInUseException": ResourceInUseException,
    "ResourceNotFoundException": ResourceNotFoundException,
}
