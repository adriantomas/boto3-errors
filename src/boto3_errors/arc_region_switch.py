# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class ARCRegionswitchError(Boto3Error):
    _SERVICE = "arc-region-switch"


class AccessDeniedException(ARCRegionswitchError):
    """You do not have sufficient access to perform this action.

    HTTP Status Code: 403
    """

    _ERROR_CODE = "AccessDeniedException"


class IllegalArgumentException(ARCRegionswitchError):
    """The request processing has an invalid argument."""
    _ERROR_CODE = "IllegalArgumentException"


class IllegalStateException(ARCRegionswitchError):
    """The operation failed because the current state of the resource doesn't allow the
    operation to proceed.

    HTTP Status Code: 400
    """

    _ERROR_CODE = "IllegalStateException"


class InternalServerException(ARCRegionswitchError):
    """The request processing has failed because of an unknown error, exception, or
    failure.

    HTTP Status Code: 500
    """

    _ERROR_CODE = "InternalServerException"


class ResourceNotFoundException(ARCRegionswitchError):
    """The specified resource was not found.

    HTTP Status Code: 404
    """

    _ERROR_CODE = "ResourceNotFoundException"


EXCEPTIONS: dict[str, type[ARCRegionswitchError]] = {
    "AccessDeniedException": AccessDeniedException,
    "IllegalArgumentException": IllegalArgumentException,
    "IllegalStateException": IllegalStateException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
}
