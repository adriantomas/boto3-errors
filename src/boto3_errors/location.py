# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class LocationError(Boto3Error):
    _SERVICE = "location"


class AccessDeniedException(LocationError):
    """The request was denied because of insufficient access or permissions. Check with an
    administrator to verify your permissions.
    """

    _ERROR_CODE = "AccessDeniedException"


class ConflictException(LocationError):
    """The request was unsuccessful because of a conflict."""
    _ERROR_CODE = "ConflictException"


class InternalServerException(LocationError):
    """The request has failed to process because of an unknown server error, exception, or
    failure.
    """

    _ERROR_CODE = "InternalServerException"


class ResourceNotFoundException(LocationError):
    """The resource that you've entered was not found in your AWS account."""
    _ERROR_CODE = "ResourceNotFoundException"


class ServiceQuotaExceededException(LocationError):
    """The operation was denied because the request would exceed the maximum quota set for
    Amazon Location Service.
    """

    _ERROR_CODE = "ServiceQuotaExceededException"


class ThrottlingException(LocationError):
    """The request was denied because of request throttling."""
    _ERROR_CODE = "ThrottlingException"


class ValidationException(LocationError):
    """The input failed to meet the constraints specified by the AWS service."""
    _ERROR_CODE = "ValidationException"

    @property
    def reason(self) -> str | None:
        """A message with the reason for the validation exception error."""
        return self.response.get("Reason")

    @property
    def field_list(self) -> list[Any] | None:
        """The field where the invalid entry was detected."""
        return self.response.get("FieldList")


EXCEPTIONS: dict[str, type[LocationError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
