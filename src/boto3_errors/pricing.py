# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class PricingError(Boto3Error):
    _SERVICE = "pricing"


class AccessDeniedException(PricingError):
    """General authentication failure. The request wasn't signed correctly."""
    _ERROR_CODE = "AccessDeniedException"


class ExpiredNextTokenException(PricingError):
    """The pagination token expired. Try again without a pagination token."""
    _ERROR_CODE = "ExpiredNextTokenException"


class InternalErrorException(PricingError):
    """An error on the server occurred during the processing of your request. Try again
    later.
    """

    _ERROR_CODE = "InternalErrorException"


class InvalidNextTokenException(PricingError):
    """The pagination token is invalid. Try again without a pagination token."""
    _ERROR_CODE = "InvalidNextTokenException"


class InvalidParameterException(PricingError):
    """One or more parameters had an invalid value."""
    _ERROR_CODE = "InvalidParameterException"


class NotFoundException(PricingError):
    """The requested resource can't be found."""
    _ERROR_CODE = "NotFoundException"


class ResourceNotFoundException(PricingError):
    """The requested resource can't be found."""
    _ERROR_CODE = "ResourceNotFoundException"


class ThrottlingException(PricingError):
    """You've made too many requests exceeding service quotas."""
    _ERROR_CODE = "ThrottlingException"


EXCEPTIONS: dict[str, type[PricingError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ExpiredNextTokenException": ExpiredNextTokenException,
    "InternalErrorException": InternalErrorException,
    "InvalidNextTokenException": InvalidNextTokenException,
    "InvalidParameterException": InvalidParameterException,
    "NotFoundException": NotFoundException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ThrottlingException": ThrottlingException,
}
