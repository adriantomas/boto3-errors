# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class EMRcontainersError(Boto3Error):
    _SERVICE = "emr-containers"


class EKSRequestThrottledException(EMRcontainersError):
    """The request exceeded the Amazon EKS API operation limits."""
    _ERROR_CODE = "EKSRequestThrottledException"


class InternalServerException(EMRcontainersError):
    """This is an internal server exception."""
    _ERROR_CODE = "InternalServerException"


class RequestThrottledException(EMRcontainersError):
    """The request throttled."""
    _ERROR_CODE = "RequestThrottledException"


class ResourceNotFoundException(EMRcontainersError):
    """The specified resource was not found."""
    _ERROR_CODE = "ResourceNotFoundException"


class ValidationException(EMRcontainersError):
    """There are invalid parameters in the client request."""
    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[EMRcontainersError]] = {
    "EKSRequestThrottledException": EKSRequestThrottledException,
    "InternalServerException": InternalServerException,
    "RequestThrottledException": RequestThrottledException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ValidationException": ValidationException,
}
