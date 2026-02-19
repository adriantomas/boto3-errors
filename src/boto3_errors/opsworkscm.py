# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class OpsWorksCMError(Boto3Error):
    _SERVICE = "opsworkscm"


class InvalidNextTokenException(OpsWorksCMError):
    """This occurs when the provided nextToken is not valid."""
    _ERROR_CODE = "InvalidNextTokenException"


class InvalidStateException(OpsWorksCMError):
    """The resource is in a state that does not allow you to perform a specified action."""
    _ERROR_CODE = "InvalidStateException"


class LimitExceededException(OpsWorksCMError):
    """The limit of servers or backups has been reached."""
    _ERROR_CODE = "LimitExceededException"


class ResourceAlreadyExistsException(OpsWorksCMError):
    """The requested resource cannot be created because it already exists."""
    _ERROR_CODE = "ResourceAlreadyExistsException"


class ResourceNotFoundException(OpsWorksCMError):
    """The requested resource does not exist, or access was denied."""
    _ERROR_CODE = "ResourceNotFoundException"


class ValidationException(OpsWorksCMError):
    """One or more of the provided request parameters are not valid."""
    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[OpsWorksCMError]] = {
    "InvalidNextTokenException": InvalidNextTokenException,
    "InvalidStateException": InvalidStateException,
    "LimitExceededException": LimitExceededException,
    "ResourceAlreadyExistsException": ResourceAlreadyExistsException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ValidationException": ValidationException,
}
