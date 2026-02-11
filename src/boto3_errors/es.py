# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class ElasticsearchServiceError(Boto3Error):
    _SERVICE = "es"


class AccessDeniedException(ElasticsearchServiceError):
    """An error occurred because user does not have permissions to access the resource.
    Returns HTTP status code 403.
    """

    _ERROR_CODE = "AccessDeniedException"


class BaseException(ElasticsearchServiceError):
    """An error occurred while processing the request."""
    _ERROR_CODE = "BaseException"


class ConflictException(ElasticsearchServiceError):
    """An error occurred because the client attempts to remove a resource that is currently
    in use. Returns HTTP status code 409.
    """

    _ERROR_CODE = "ConflictException"


class DisabledOperationException(ElasticsearchServiceError):
    """An error occured because the client wanted to access a not supported operation.
    Gives http status code of 409.
    """

    _ERROR_CODE = "DisabledOperationException"


class InternalException(ElasticsearchServiceError):
    """The request processing has failed because of an unknown error, exception or failure
    (the failure is internal to the service) . Gives http status code of 500.
    """

    _ERROR_CODE = "InternalException"


class InvalidPaginationTokenException(ElasticsearchServiceError):
    """The request processing has failed because of invalid pagination token provided by
    customer. Returns an HTTP status code of 400.
    """

    _ERROR_CODE = "InvalidPaginationTokenException"


class InvalidTypeException(ElasticsearchServiceError):
    """An exception for trying to create or access sub-resource that is either invalid or
    not supported. Gives http status code of 409.
    """

    _ERROR_CODE = "InvalidTypeException"


class LimitExceededException(ElasticsearchServiceError):
    """An exception for trying to create more than allowed resources or sub-resources.
    Gives http status code of 409.
    """

    _ERROR_CODE = "LimitExceededException"


class ResourceAlreadyExistsException(ElasticsearchServiceError):
    """An exception for creating a resource that already exists. Gives http status code of
    400.
    """

    _ERROR_CODE = "ResourceAlreadyExistsException"


class ResourceNotFoundException(ElasticsearchServiceError):
    """An exception for accessing or deleting a resource that does not exist. Gives http
    status code of 400.
    """

    _ERROR_CODE = "ResourceNotFoundException"


class ValidationException(ElasticsearchServiceError):
    """An exception for missing / invalid input fields. Gives http status code of 400."""
    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[ElasticsearchServiceError]] = {
    "AccessDeniedException": AccessDeniedException,
    "BaseException": BaseException,
    "ConflictException": ConflictException,
    "DisabledOperationException": DisabledOperationException,
    "InternalException": InternalException,
    "InvalidPaginationTokenException": InvalidPaginationTokenException,
    "InvalidTypeException": InvalidTypeException,
    "LimitExceededException": LimitExceededException,
    "ResourceAlreadyExistsException": ResourceAlreadyExistsException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ValidationException": ValidationException,
}
