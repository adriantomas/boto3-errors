# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class MPAError(Boto3Error):
    _SERVICE = "mpa"


class AccessDeniedException(MPAError):
    """You do not have sufficient access to perform this action. Check your permissions,
    and try again.
    """

    _ERROR_CODE = "AccessDeniedException"


class ConflictException(MPAError):
    """The request cannot be completed because it conflicts with the current state of a
    resource.
    """

    _ERROR_CODE = "ConflictException"


class InternalServerException(MPAError):
    """The service encountered an internal error. Try your request again. If the problem
    persists, contact Amazon Web Services Support.
    """

    _ERROR_CODE = "InternalServerException"


class InvalidParameterException(MPAError):
    """The request contains an invalid parameter value."""
    _ERROR_CODE = "InvalidParameterException"


class ResourceNotFoundException(MPAError):
    """The specified resource doesn't exist. Check the resource ID, and try again."""
    _ERROR_CODE = "ResourceNotFoundException"


class ServiceQuotaExceededException(MPAError):
    """The request exceeds the service quota for your account. Request a quota increase or
    reduce your request size.
    """

    _ERROR_CODE = "ServiceQuotaExceededException"


class ThrottlingException(MPAError):
    """The request was denied due to request throttling."""
    _ERROR_CODE = "ThrottlingException"


class TooManyTagsException(MPAError):
    """The request exceeds the maximum number of tags allowed for this resource. Remove
    some tags, and try again.
    """

    _ERROR_CODE = "TooManyTagsException"

    @property
    def resource_name(self) -> str | None:
        """Name of the resource for the `TooManyTagsException` error."""
        return self.response.get("ResourceName")


class ValidationException(MPAError):
    """The input fails to satisfy the constraints specified by an Amazon Web Services
    service.
    """

    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[MPAError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "InvalidParameterException": InvalidParameterException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "TooManyTagsException": TooManyTagsException,
    "ValidationException": ValidationException,
}
