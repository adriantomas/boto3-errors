# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class BudgetsError(Boto3Error):
    _SERVICE = "budgets"


class AccessDeniedException(BudgetsError):
    """You are not authorized to use this operation with the given parameters."""
    _ERROR_CODE = "AccessDeniedException"


class BillingViewHealthStatusException(BudgetsError):
    """The billing view status must be HEALTHY to perform this action. Try again when the
    status is HEALTHY.
    """

    _ERROR_CODE = "BillingViewHealthStatusException"


class CreationLimitExceededException(BudgetsError):
    """You've exceeded the notification or subscriber limit."""
    _ERROR_CODE = "CreationLimitExceededException"


class DuplicateRecordException(BudgetsError):
    """The budget name already exists. Budget names must be unique within an account."""
    _ERROR_CODE = "DuplicateRecordException"


class ExpiredNextTokenException(BudgetsError):
    """The pagination token expired."""
    _ERROR_CODE = "ExpiredNextTokenException"


class InternalErrorException(BudgetsError):
    """An error on the server occurred during the processing of your request. Try again
    later.
    """

    _ERROR_CODE = "InternalErrorException"


class InvalidNextTokenException(BudgetsError):
    """The pagination token is invalid."""
    _ERROR_CODE = "InvalidNextTokenException"


class InvalidParameterException(BudgetsError):
    """An error on the client occurred. Typically, the cause is an invalid input value."""
    _ERROR_CODE = "InvalidParameterException"


class NotFoundException(BudgetsError):
    """We can’t locate the resource that you specified."""
    _ERROR_CODE = "NotFoundException"


class ResourceLockedException(BudgetsError):
    """The request was received and recognized by the server, but the server rejected that
    particular method for the requested resource.
    """

    _ERROR_CODE = "ResourceLockedException"


class ServiceQuotaExceededException(BudgetsError):
    """You've reached a Service Quota limit on this resource."""
    _ERROR_CODE = "ServiceQuotaExceededException"


class ThrottlingException(BudgetsError):
    """The number of API requests has exceeded the maximum allowed API request throttling
    limit for the account.
    """

    _ERROR_CODE = "ThrottlingException"


EXCEPTIONS: dict[str, type[BudgetsError]] = {
    "AccessDeniedException": AccessDeniedException,
    "BillingViewHealthStatusException": BillingViewHealthStatusException,
    "CreationLimitExceededException": CreationLimitExceededException,
    "DuplicateRecordException": DuplicateRecordException,
    "ExpiredNextTokenException": ExpiredNextTokenException,
    "InternalErrorException": InternalErrorException,
    "InvalidNextTokenException": InvalidNextTokenException,
    "InvalidParameterException": InvalidParameterException,
    "NotFoundException": NotFoundException,
    "ResourceLockedException": ResourceLockedException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
}
