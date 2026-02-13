# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class LookoutEquipmentError(Boto3Error):
    _SERVICE = "lookoutequipment"


class AccessDeniedException(LookoutEquipmentError):
    """The request could not be completed because you do not have access to the resource."""
    _ERROR_CODE = "AccessDeniedException"


class ConflictException(LookoutEquipmentError):
    """The request could not be completed due to a conflict with the current state of the
    target resource.
    """

    _ERROR_CODE = "ConflictException"


class InternalServerException(LookoutEquipmentError):
    """Processing of the request has failed because of an unknown error, exception or
    failure.
    """

    _ERROR_CODE = "InternalServerException"


class ResourceNotFoundException(LookoutEquipmentError):
    """The resource requested could not be found. Verify the resource ID and retry your
    request.
    """

    _ERROR_CODE = "ResourceNotFoundException"


class ServiceQuotaExceededException(LookoutEquipmentError):
    """Resource limitations have been exceeded."""
    _ERROR_CODE = "ServiceQuotaExceededException"


class ThrottlingException(LookoutEquipmentError):
    """The request was denied due to request throttling."""
    _ERROR_CODE = "ThrottlingException"


class ValidationException(LookoutEquipmentError):
    """The input fails to satisfy constraints specified by Amazon Lookout for Equipment or
    a related Amazon Web Services service that's being utilized.
    """

    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[LookoutEquipmentError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
