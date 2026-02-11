# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class OAMError(Boto3Error):
    _SERVICE = "oam"


class ConflictException(OAMError):
    """A resource was in an inconsistent state during an update or a deletion."""
    _ERROR_CODE = "ConflictException"

    @property
    def amzn_error_type(self) -> str | None:
        """The name of the exception."""
        return self.response.get("amznErrorType")


class InternalServiceFault(OAMError):
    """Unexpected error while processing the request. Retry the request."""
    _ERROR_CODE = "InternalServiceFault"

    @property
    def amzn_error_type(self) -> str | None:
        """The name of the exception."""
        return self.response.get("amznErrorType")


class InvalidParameterException(OAMError):
    """A parameter is specified incorrectly."""
    _ERROR_CODE = "InvalidParameterException"

    @property
    def amzn_error_type(self) -> str | None:
        """The name of the exception."""
        return self.response.get("amznErrorType")


class MissingRequiredParameterException(OAMError):
    """A required parameter is missing from the request."""
    _ERROR_CODE = "MissingRequiredParameterException"

    @property
    def amzn_error_type(self) -> str | None:
        """The name of the exception."""
        return self.response.get("amznErrorType")


class ResourceNotFoundException(OAMError):
    """The request references a resource that does not exist."""
    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def amzn_error_type(self) -> str | None:
        """The name of the exception."""
        return self.response.get("amznErrorType")


class ServiceQuotaExceededException(OAMError):
    """The request would cause a service quota to be exceeded."""
    _ERROR_CODE = "ServiceQuotaExceededException"

    @property
    def amzn_error_type(self) -> str | None:
        """The name of the exception."""
        return self.response.get("amznErrorType")


class TooManyTagsException(OAMError):
    """A resource can have no more than 50 tags."""
    _ERROR_CODE = "TooManyTagsException"


class ValidationException(OAMError):
    """The value of a parameter in the request caused an error."""
    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[OAMError]] = {
    "ConflictException": ConflictException,
    "InternalServiceFault": InternalServiceFault,
    "InvalidParameterException": InvalidParameterException,
    "MissingRequiredParameterException": MissingRequiredParameterException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "TooManyTagsException": TooManyTagsException,
    "ValidationException": ValidationException,
}
