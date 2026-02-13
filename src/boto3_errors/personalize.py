# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class PersonalizeError(Boto3Error):
    _SERVICE = "personalize"


class InvalidInputException(PersonalizeError):
    """Provide a valid value for the field or parameter."""
    _ERROR_CODE = "InvalidInputException"


class InvalidNextTokenException(PersonalizeError):
    """The token is not valid."""
    _ERROR_CODE = "InvalidNextTokenException"


class LimitExceededException(PersonalizeError):
    """The limit on the number of requests per second has been exceeded."""
    _ERROR_CODE = "LimitExceededException"


class ResourceAlreadyExistsException(PersonalizeError):
    """The specified resource already exists."""
    _ERROR_CODE = "ResourceAlreadyExistsException"


class ResourceInUseException(PersonalizeError):
    """The specified resource is in use."""
    _ERROR_CODE = "ResourceInUseException"


class ResourceNotFoundException(PersonalizeError):
    """Could not find the specified resource."""
    _ERROR_CODE = "ResourceNotFoundException"


class TooManyTagKeysException(PersonalizeError):
    """The request contains more tag keys than can be associated with a resource (50 tag
    keys per resource).
    """

    _ERROR_CODE = "TooManyTagKeysException"


class TooManyTagsException(PersonalizeError):
    """You have exceeded the maximum number of tags you can apply to this resource."""
    _ERROR_CODE = "TooManyTagsException"


EXCEPTIONS: dict[str, type[PersonalizeError]] = {
    "InvalidInputException": InvalidInputException,
    "InvalidNextTokenException": InvalidNextTokenException,
    "LimitExceededException": LimitExceededException,
    "ResourceAlreadyExistsException": ResourceAlreadyExistsException,
    "ResourceInUseException": ResourceInUseException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "TooManyTagKeysException": TooManyTagKeysException,
    "TooManyTagsException": TooManyTagsException,
}
