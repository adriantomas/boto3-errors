# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class ElementalInferenceError(Boto3Error):
    _SERVICE = "elementalinference"


class AccessDeniedException(ElementalInferenceError):
    """You do not have sufficient access to perform this action."""
    _ERROR_CODE = "AccessDeniedException"


class ConflictException(ElementalInferenceError):
    """The request could not be completed due to a conflict."""
    _ERROR_CODE = "ConflictException"


class InternalServerErrorException(ElementalInferenceError):
    """An internal server error occurred. This is a temporary condition and the request can
    be retried. If the problem persists, contact AWS Support.
    """

    _ERROR_CODE = "InternalServerErrorException"


class ResourceNotFoundException(ElementalInferenceError):
    """The resource specified in the action doesn't exist."""
    _ERROR_CODE = "ResourceNotFoundException"


class ServiceQuotaExceededException(ElementalInferenceError):
    """The request was rejected because it would exceed one or more service quotas for your
    account. Review your service quotas and either delete unused resources or request a
    quota increase.
    """

    _ERROR_CODE = "ServiceQuotaExceededException"


class TooManyRequestException(ElementalInferenceError):
    """The request was denied due to request throttling. Too many requests have been made
    within a given time period. Reduce the frequency of requests and use exponential
    backoff when retrying.
    """

    _ERROR_CODE = "TooManyRequestException"


class ValidationException(ElementalInferenceError):
    """The input fails to satisfy the constraints specified by the service. Check the error
    message for details about which parameter or field is invalid and correct the
    request before retrying.
    """

    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[ElementalInferenceError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerErrorException": InternalServerErrorException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "TooManyRequestException": TooManyRequestException,
    "ValidationException": ValidationException,
}
