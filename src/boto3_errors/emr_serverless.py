# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class EMRServerlessError(Boto3Error):
    _SERVICE = "emr-serverless"


class ConflictException(EMRServerlessError):
    """The request could not be processed because of conflict in the current state of the
    resource.
    """

    _ERROR_CODE = "ConflictException"


class InternalServerException(EMRServerlessError):
    """Request processing failed because of an error or failure with the service."""
    _ERROR_CODE = "InternalServerException"


class ResourceNotFoundException(EMRServerlessError):
    """The specified resource was not found."""
    _ERROR_CODE = "ResourceNotFoundException"


class ServiceQuotaExceededException(EMRServerlessError):
    """The maximum number of resources per account has been reached."""
    _ERROR_CODE = "ServiceQuotaExceededException"


class ValidationException(EMRServerlessError):
    """The input fails to satisfy the constraints specified by an Amazon Web Services
    service.
    """

    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[EMRServerlessError]] = {
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ValidationException": ValidationException,
}
