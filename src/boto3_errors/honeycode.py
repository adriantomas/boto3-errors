# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class HoneycodeError(Boto3Error):
    _SERVICE = "honeycode"


class AccessDeniedException(HoneycodeError):
    """You do not have sufficient access to perform this action. Check that the workbook is
    owned by you and your IAM policy allows access to the resource in the request.
    """

    _ERROR_CODE = "AccessDeniedException"


class AutomationExecutionException(HoneycodeError):
    """The automation execution did not end successfully."""
    _ERROR_CODE = "AutomationExecutionException"


class AutomationExecutionTimeoutException(HoneycodeError):
    """The automation execution timed out."""
    _ERROR_CODE = "AutomationExecutionTimeoutException"


class InternalServerException(HoneycodeError):
    """There were unexpected errors from the server."""
    _ERROR_CODE = "InternalServerException"


class RequestTimeoutException(HoneycodeError):
    """The request timed out."""
    _ERROR_CODE = "RequestTimeoutException"


class ResourceNotFoundException(HoneycodeError):
    """A Workbook, Table, App, Screen or Screen Automation was not found with the given ID."""
    _ERROR_CODE = "ResourceNotFoundException"


class ServiceQuotaExceededException(HoneycodeError):
    """The request caused service quota to be breached."""
    _ERROR_CODE = "ServiceQuotaExceededException"


class ServiceUnavailableException(HoneycodeError):
    """Remote service is unreachable."""
    _ERROR_CODE = "ServiceUnavailableException"


class ThrottlingException(HoneycodeError):
    """Tps(transactions per second) rate reached."""
    _ERROR_CODE = "ThrottlingException"


class ValidationException(HoneycodeError):
    """Request is invalid. The message in the response contains details on why the request
    is invalid.
    """

    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[HoneycodeError]] = {
    "AccessDeniedException": AccessDeniedException,
    "AutomationExecutionException": AutomationExecutionException,
    "AutomationExecutionTimeoutException": AutomationExecutionTimeoutException,
    "InternalServerException": InternalServerException,
    "RequestTimeoutException": RequestTimeoutException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ServiceUnavailableException": ServiceUnavailableException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
