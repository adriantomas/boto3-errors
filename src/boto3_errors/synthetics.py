# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class syntheticsError(Boto3Error):
    _SERVICE = "synthetics"


class BadRequestException(syntheticsError):
    """The request was not valid."""
    _ERROR_CODE = "BadRequestException"


class ConflictException(syntheticsError):
    """A conflicting operation is already in progress."""
    _ERROR_CODE = "ConflictException"


class InternalFailureException(syntheticsError):
    """An internal failure occurred. Try the operation again."""
    _ERROR_CODE = "InternalFailureException"


class InternalServerException(syntheticsError):
    """An unknown internal error occurred."""
    _ERROR_CODE = "InternalServerException"


class NotFoundException(syntheticsError):
    """The specified resource was not found."""
    _ERROR_CODE = "NotFoundException"


class RequestEntityTooLargeException(syntheticsError):
    """One of the input resources is larger than is allowed."""
    _ERROR_CODE = "RequestEntityTooLargeException"


class ResourceNotFoundException(syntheticsError):
    """One of the specified resources was not found."""
    _ERROR_CODE = "ResourceNotFoundException"


class ServiceQuotaExceededException(syntheticsError):
    """The request exceeded a service quota value."""
    _ERROR_CODE = "ServiceQuotaExceededException"


class TooManyRequestsException(syntheticsError):
    """There were too many simultaneous requests. Try the operation again."""
    _ERROR_CODE = "TooManyRequestsException"


class ValidationException(syntheticsError):
    """A parameter could not be validated."""
    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[syntheticsError]] = {
    "BadRequestException": BadRequestException,
    "ConflictException": ConflictException,
    "InternalFailureException": InternalFailureException,
    "InternalServerException": InternalServerException,
    "NotFoundException": NotFoundException,
    "RequestEntityTooLargeException": RequestEntityTooLargeException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "TooManyRequestsException": TooManyRequestsException,
    "ValidationException": ValidationException,
}
