# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class ConnectCasesError(Boto3Error):
    _SERVICE = "connectcases"


class AccessDeniedException(ConnectCasesError):
    """You do not have sufficient access to perform this action."""
    _ERROR_CODE = "AccessDeniedException"


class ConflictException(ConnectCasesError):
    """The requested operation would cause a conflict with the current state of a service
    resource associated with the request. Resolve the conflict before retrying this
    request. See the accompanying error message for details.
    """

    _ERROR_CODE = "ConflictException"


class InternalServerException(ConnectCasesError):
    """We couldn't process your request because of an issue with the server. Try again
    later.
    """

    _ERROR_CODE = "InternalServerException"

    @property
    def retry_after_seconds(self) -> int | None:
        """Advice to clients on when the call can be safely retried."""
        return self.response.get("retryAfterSeconds")


class ResourceNotFoundException(ConnectCasesError):
    """We couldn't find the requested resource. Check that your resources exists and were
    created in the same Amazon Web Services Region as your request, and try your request
    again.
    """

    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def resource_id(self) -> str | None:
        """Unique identifier of the resource affected."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """Type of the resource affected."""
        return self.response.get("resourceType")


class ServiceQuotaExceededException(ConnectCasesError):
    """The service quota has been exceeded. For a list of service quotas, see Amazon
    Connect Service Quotas in the Amazon Connect Administrator Guide.
    """

    _ERROR_CODE = "ServiceQuotaExceededException"


class ThrottlingException(ConnectCasesError):
    """The rate has been exceeded for this API. Please try again after a few minutes."""
    _ERROR_CODE = "ThrottlingException"


class ValidationException(ConnectCasesError):
    """The request isn't valid. Check the syntax and try again."""
    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[ConnectCasesError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
