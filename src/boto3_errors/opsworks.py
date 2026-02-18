# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class OpsWorksError(Boto3Error):
    _SERVICE = "opsworks"


class ResourceNotFoundException(OpsWorksError):
    """Indicates that a resource was not found."""
    _ERROR_CODE = "ResourceNotFoundException"


class ValidationException(OpsWorksError):
    """Indicates that a request was not valid."""
    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[OpsWorksError]] = {
    "ResourceNotFoundException": ResourceNotFoundException,
    "ValidationException": ValidationException,
}
