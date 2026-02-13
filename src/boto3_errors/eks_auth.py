# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class EKSAuthError(Boto3Error):
    _SERVICE = "eks-auth"


class AccessDeniedException(EKSAuthError):
    """You don't have permissions to perform the requested operation. The IAM principal
    making the request must have at least one IAM permissions policy attached that
    grants the required permissions. For more information, see Access management in the
    IAM User Guide.
    """

    _ERROR_CODE = "AccessDeniedException"


class ExpiredTokenException(EKSAuthError):
    """The specified Kubernetes service account token is expired."""
    _ERROR_CODE = "ExpiredTokenException"


class InternalServerException(EKSAuthError):
    """These errors are usually caused by a server-side issue."""
    _ERROR_CODE = "InternalServerException"


class InvalidParameterException(EKSAuthError):
    """The specified parameter is invalid. Review the available parameters for the API
    request.
    """

    _ERROR_CODE = "InvalidParameterException"


class InvalidRequestException(EKSAuthError):
    """This exception is thrown if the request contains a semantic error. The precise
    meaning will depend on the API, and will be documented in the error message.
    """

    _ERROR_CODE = "InvalidRequestException"


class InvalidTokenException(EKSAuthError):
    """The specified Kubernetes service account token is invalid."""
    _ERROR_CODE = "InvalidTokenException"


class ResourceNotFoundException(EKSAuthError):
    """The specified resource could not be found."""
    _ERROR_CODE = "ResourceNotFoundException"


class ServiceUnavailableException(EKSAuthError):
    """The service is unavailable. Back off and retry the operation."""
    _ERROR_CODE = "ServiceUnavailableException"


class ThrottlingException(EKSAuthError):
    """The request was denied because your request rate is too high. Reduce the frequency
    of requests.
    """

    _ERROR_CODE = "ThrottlingException"


EXCEPTIONS: dict[str, type[EKSAuthError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ExpiredTokenException": ExpiredTokenException,
    "InternalServerException": InternalServerException,
    "InvalidParameterException": InvalidParameterException,
    "InvalidRequestException": InvalidRequestException,
    "InvalidTokenException": InvalidTokenException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceUnavailableException": ServiceUnavailableException,
    "ThrottlingException": ThrottlingException,
}
