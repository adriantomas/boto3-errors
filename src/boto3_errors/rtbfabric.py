# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class RTBFabricError(Boto3Error):
    _SERVICE = "rtbfabric"


class AccessDeniedException(RTBFabricError):
    """The request could not be completed because you do not have sufficient access to
    perform this action.
    """

    _ERROR_CODE = "AccessDeniedException"


class ConflictException(RTBFabricError):
    """The request could not be completed because of a conflict in the current state of the
    resource.
    """

    _ERROR_CODE = "ConflictException"


class InternalServerException(RTBFabricError):
    """The request could not be completed because of an internal server error. Try your
    call again.
    """

    _ERROR_CODE = "InternalServerException"


class ResourceNotFoundException(RTBFabricError):
    """The request could not be completed because the resource does not exist."""
    _ERROR_CODE = "ResourceNotFoundException"


class ServiceQuotaExceededException(RTBFabricError):
    """The request could not be completed because you exceeded a service quota."""
    _ERROR_CODE = "ServiceQuotaExceededException"


class ThrottlingException(RTBFabricError):
    """The request was denied due to request throttling."""
    _ERROR_CODE = "ThrottlingException"


class ValidationException(RTBFabricError):
    """The request could not be completed because it fails satisfy the constraints
    specified by the service.
    """

    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[RTBFabricError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
