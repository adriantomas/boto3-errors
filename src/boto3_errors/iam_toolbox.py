# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class IAMToolboxError(Boto3Error):
    _SERVICE = "iam-toolbox"


class AccessDeniedException(IAMToolboxError):
    """The caller does not have sufficient access to perform this action."""
    _ERROR_CODE = "AccessDeniedException"


class InternalServerException(IAMToolboxError):
    """An unexpected error occurred while processing the request. Try again."""
    _ERROR_CODE = "InternalServerException"


class ResourceNotFoundException(IAMToolboxError):
    """The requested authorization details do not exist in this region or have expired.
    Verify that the authorization ID from the access denied error message is correct and
    the call is made in the region where the denial occurred. Ensure that the calling
    principal belongs to the same account or organization as the original denied
    request.
    """

    _ERROR_CODE = "ResourceNotFoundException"


class ValidationException(IAMToolboxError):
    """The request is malformed or is missing one or more required parameters. Check the
    request parameters and try again.
    """

    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[IAMToolboxError]] = {
    "AccessDeniedException": AccessDeniedException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ValidationException": ValidationException,
}
