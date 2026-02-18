# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class ControlTowerError(Boto3Error):
    _SERVICE = "controltower"


class AccessDeniedException(ControlTowerError):
    """You do not have sufficient access to perform this action."""
    _ERROR_CODE = "AccessDeniedException"


class ConflictException(ControlTowerError):
    """Updating or deleting the resource can cause an inconsistent state."""
    _ERROR_CODE = "ConflictException"


class InternalServerException(ControlTowerError):
    """An unexpected error occurred during processing of a request."""
    _ERROR_CODE = "InternalServerException"


class ResourceNotFoundException(ControlTowerError):
    """The request references a resource that does not exist."""
    _ERROR_CODE = "ResourceNotFoundException"


class ServiceQuotaExceededException(ControlTowerError):
    """The request would cause a service quota to be exceeded. The limit is 10 concurrent
    operations.
    """

    _ERROR_CODE = "ServiceQuotaExceededException"


class ThrottlingException(ControlTowerError):
    """The request was denied due to request throttling."""
    _ERROR_CODE = "ThrottlingException"

    @property
    def quota_code(self) -> str | None:
        """The ID of the service quota that was exceeded."""
        return self.response.get("quotaCode")

    @property
    def retry_after_seconds(self) -> int | None:
        """The number of seconds the caller should wait before retrying."""
        return self.response.get("retryAfterSeconds")

    @property
    def service_code(self) -> str | None:
        """The ID of the service that is associated with the error."""
        return self.response.get("serviceCode")


class ValidationException(ControlTowerError):
    """The input does not satisfy the constraints specified by an Amazon Web Services
    service.
    """

    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[ControlTowerError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
