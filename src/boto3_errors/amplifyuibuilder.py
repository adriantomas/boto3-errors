# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class AmplifyUIBuilderError(Boto3Error):
    _SERVICE = "amplifyuibuilder"


class InternalServerException(AmplifyUIBuilderError):
    """An internal error has occurred. Please retry your request."""
    _ERROR_CODE = "InternalServerException"


class InvalidParameterException(AmplifyUIBuilderError):
    """An invalid or out-of-range value was supplied for the input parameter."""
    _ERROR_CODE = "InvalidParameterException"


class ResourceConflictException(AmplifyUIBuilderError):
    """The resource specified in the request conflicts with an existing resource."""
    _ERROR_CODE = "ResourceConflictException"


class ResourceNotFoundException(AmplifyUIBuilderError):
    """The requested resource does not exist, or access was denied."""
    _ERROR_CODE = "ResourceNotFoundException"


class ServiceQuotaExceededException(AmplifyUIBuilderError):
    """You exceeded your service quota. Service quotas, also referred to as limits, are the
    maximum number of service resources or operations for your Amazon Web Services
    account.
    """

    _ERROR_CODE = "ServiceQuotaExceededException"


class ThrottlingException(AmplifyUIBuilderError):
    """The request was denied due to request throttling."""
    _ERROR_CODE = "ThrottlingException"


class UnauthorizedException(AmplifyUIBuilderError):
    """You don't have permission to perform this operation."""
    _ERROR_CODE = "UnauthorizedException"


EXCEPTIONS: dict[str, type[AmplifyUIBuilderError]] = {
    "InternalServerException": InternalServerException,
    "InvalidParameterException": InvalidParameterException,
    "ResourceConflictException": ResourceConflictException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "UnauthorizedException": UnauthorizedException,
}
