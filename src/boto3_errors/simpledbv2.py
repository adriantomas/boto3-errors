# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class SimpleDBv2Error(Boto3Error):
    _SERVICE = "simpledbv2"


class ConflictException(SimpleDBv2Error):
    """Indicates a conflict with one or more parameters of the request."""
    _ERROR_CODE = "ConflictException"


class InvalidNextTokenException(SimpleDBv2Error):
    """The specified next token is not valid."""
    _ERROR_CODE = "InvalidNextTokenException"


class InvalidParameterCombinationException(SimpleDBv2Error):
    """Parameters that must not be used together were used together in the request."""
    _ERROR_CODE = "InvalidParameterCombinationException"


class InvalidParameterValueException(SimpleDBv2Error):
    """The specified parameter value is not valid."""
    _ERROR_CODE = "InvalidParameterValueException"


class NoSuchDomainException(SimpleDBv2Error):
    """The specified domain does not exist."""
    _ERROR_CODE = "NoSuchDomainException"


class NoSuchExportException(SimpleDBv2Error):
    """Export with specified ARN does not exist."""
    _ERROR_CODE = "NoSuchExportException"


class NumberExportsLimitExceeded(SimpleDBv2Error):
    """Cannot start export as export quota limit was exceeded"""
    _ERROR_CODE = "NumberExportsLimitExceeded"


EXCEPTIONS: dict[str, type[SimpleDBv2Error]] = {
    "ConflictException": ConflictException,
    "InvalidNextTokenException": InvalidNextTokenException,
    "InvalidParameterCombinationException": InvalidParameterCombinationException,
    "InvalidParameterValueException": InvalidParameterValueException,
    "NoSuchDomainException": NoSuchDomainException,
    "NoSuchExportException": NoSuchExportException,
    "NumberExportsLimitExceeded": NumberExportsLimitExceeded,
}
