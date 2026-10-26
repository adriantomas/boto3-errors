# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class ContinuumError(Boto3Error):
    _SERVICE = "continuum"


class AccessDeniedException(ContinuumError):
    """The request is not authorized. Verify that your credentials and request signature
    are valid and that you have permission to perform this action.
    """

    _ERROR_CODE = "AccessDeniedException"


class ConflictException(ContinuumError):
    """The request could not be completed due to a conflict with the current state of the
    resource.
    """

    _ERROR_CODE = "ConflictException"


class InternalServerException(ContinuumError):
    """The request couldn't be processed because of an internal server issue. Try again
    later. If the problem persists, contact AWS Support.
    """

    _ERROR_CODE = "InternalServerException"


class ResourceNotFoundException(ContinuumError):
    """The specified resource was not found. Verify that the resource identifier is correct
    and that the resource exists.
    """

    _ERROR_CODE = "ResourceNotFoundException"


class ServiceQuotaExceededException(ContinuumError):
    """The request would exceed a service quota. Review your quota and request an increase
    if needed.
    """

    _ERROR_CODE = "ServiceQuotaExceededException"

    @property
    def quota_code(self) -> str | None:
        """The quota code for the exceeded limit."""
        return self.response.get("quotaCode")

    @property
    def service_code(self) -> str | None:
        """The service code for the exceeded limit."""
        return self.response.get("serviceCode")


class ThrottlingException(ContinuumError):
    """The request was denied due to request throttling."""
    _ERROR_CODE = "ThrottlingException"


class ValidationException(ContinuumError):
    _ERROR_CODE = "ValidationException"

    @property
    def field_list(self) -> list[Any] | None:
        return self.response.get("fieldList")


EXCEPTIONS: dict[str, type[ContinuumError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
