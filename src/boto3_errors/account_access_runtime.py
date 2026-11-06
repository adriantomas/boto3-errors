# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class AccountAccessRuntimeError(Boto3Error):
    _SERVICE = "account-access-runtime"


class AccessDeniedException(AccountAccessRuntimeError):
    """You are authenticated but not authorized to perform the requested action, such as
    assuming a role that you aren't entitled to. This error returns an HTTP 403 status
    code.
    """

    _ERROR_CODE = "AccessDeniedException"


class InternalServerException(AccountAccessRuntimeError):
    """An internal server error occurred. Retry the request. If the problem persists,
    contact Amazon Web Services Support. This error returns an HTTP 500 status code.
    """

    _ERROR_CODE = "InternalServerException"


class ThrottlingException(AccountAccessRuntimeError):
    """The request rate exceeded the allowed limit. Reduce your request rate, and then
    retry the request. This error returns an HTTP 429 status code.
    """

    _ERROR_CODE = "ThrottlingException"


class UnauthorizedException(AccountAccessRuntimeError):
    """The bearer token is missing, invalid, or expired. Obtain a new token, and then retry
    the request. This error returns an HTTP 401 status code.
    """

    _ERROR_CODE = "UnauthorizedException"


class ValidationException(AccountAccessRuntimeError):
    """The request is missing a required parameter, or a parameter value doesn't satisfy
    its constraints, such as its length or pattern. Correct the input, and then retry
    the request. This error returns an HTTP 400 status code.
    """

    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[AccountAccessRuntimeError]] = {
    "AccessDeniedException": AccessDeniedException,
    "InternalServerException": InternalServerException,
    "ThrottlingException": ThrottlingException,
    "UnauthorizedException": UnauthorizedException,
    "ValidationException": ValidationException,
}
