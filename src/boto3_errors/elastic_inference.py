# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class ElasticInferenceError(Boto3Error):
    _SERVICE = "elastic-inference"


class BadRequestException(ElasticInferenceError):
    """Raised when a malformed input has been provided to the API."""
    _ERROR_CODE = "BadRequestException"


class InternalServerException(ElasticInferenceError):
    """Raised when an unexpected error occurred during request processing."""
    _ERROR_CODE = "InternalServerException"


class ResourceNotFoundException(ElasticInferenceError):
    """Raised when the requested resource cannot be found."""
    _ERROR_CODE = "ResourceNotFoundException"


EXCEPTIONS: dict[str, type[ElasticInferenceError]] = {
    "BadRequestException": BadRequestException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
}
