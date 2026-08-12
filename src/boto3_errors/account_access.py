# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class AccountAccessError(Boto3Error):
    _SERVICE = "account-access"


class AccessDeniedException(AccountAccessError):
    """You do not have sufficient access to perform this operation."""
    _ERROR_CODE = "AccessDeniedException"


class AlreadyCreatedException(AccountAccessError):
    """The resource you are trying to create already exists. To retrieve the existing
    resource, use the corresponding Get operation.
    """

    _ERROR_CODE = "AlreadyCreatedException"


class ConflictException(AccountAccessError):
    """The request conflicts with the current state of the resource."""
    _ERROR_CODE = "ConflictException"


class InternalServerException(AccountAccessError):
    """An internal service error occurred. Try your request again later."""
    _ERROR_CODE = "InternalServerException"


class ResourceNotFoundException(AccountAccessError):
    """The specified resource does not exist. Verify that the resource identifier is
    correct and that the resource exists in the current Region.
    """

    _ERROR_CODE = "ResourceNotFoundException"


class ServiceQuotaExceededException(AccountAccessError):
    """The request exceeds a service quota for your account."""
    _ERROR_CODE = "ServiceQuotaExceededException"


class ThrottlingException(AccountAccessError):
    """The request was denied due to request throttling. Try your request again later."""
    _ERROR_CODE = "ThrottlingException"


class ValidationException(AccountAccessError):
    """The input does not satisfy the constraints specified by the service. Check your
    request parameters and retry the request.
    """

    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[AccountAccessError]] = {
    "AccessDeniedException": AccessDeniedException,
    "AlreadyCreatedException": AlreadyCreatedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
