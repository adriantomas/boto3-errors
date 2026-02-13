# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class CleanRoomsMLError(Boto3Error):
    _SERVICE = "cleanroomsml"


class AccessDeniedException(CleanRoomsMLError):
    """You do not have sufficient access to perform this action."""
    _ERROR_CODE = "AccessDeniedException"


class ConflictException(CleanRoomsMLError):
    """You can't complete this action because another resource depends on this resource."""
    _ERROR_CODE = "ConflictException"


class InternalServiceException(CleanRoomsMLError):
    """An internal service error occurred. Retry your request. If the problem persists,
    contact AWS Support.
    """

    _ERROR_CODE = "InternalServiceException"


class ResourceNotFoundException(CleanRoomsMLError):
    """The resource you are requesting does not exist."""
    _ERROR_CODE = "ResourceNotFoundException"


class ServiceQuotaExceededException(CleanRoomsMLError):
    """You have exceeded your service quota."""
    _ERROR_CODE = "ServiceQuotaExceededException"

    @property
    def quota_name(self) -> str | None:
        """The name of the service quota limit that was exceeded"""
        return self.response.get("quotaName")

    @property
    def quota_value(self) -> float | None:
        """The current limit on the service quota that was exceeded"""
        return self.response.get("quotaValue")


class ThrottlingException(CleanRoomsMLError):
    """The request was denied due to request throttling."""
    _ERROR_CODE = "ThrottlingException"


class ValidationException(CleanRoomsMLError):
    """The request parameters for this request are incorrect."""
    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[CleanRoomsMLError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServiceException": InternalServiceException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
