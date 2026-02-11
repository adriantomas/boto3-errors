# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class rbinError(Boto3Error):
    _SERVICE = "rbin"


class ConflictException(rbinError):
    """The specified retention rule lock request can't be completed."""
    _ERROR_CODE = "ConflictException"

    @property
    def reason(self) -> str | None:
        """The reason for the exception."""
        return self.response.get("Reason")


class InternalServerException(rbinError):
    """The service could not respond to the request due to an internal problem."""
    _ERROR_CODE = "InternalServerException"


class ResourceNotFoundException(rbinError):
    """The specified resource was not found."""
    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def reason(self) -> str | None:
        """The reason for the exception."""
        return self.response.get("Reason")


class ServiceQuotaExceededException(rbinError):
    """The request would cause a service quota for the number of tags per resource to be
    exceeded.
    """

    _ERROR_CODE = "ServiceQuotaExceededException"

    @property
    def reason(self) -> str | None:
        """The reason for the exception."""
        return self.response.get("Reason")


class ValidationException(rbinError):
    """One or more of the parameters in the request is not valid."""
    _ERROR_CODE = "ValidationException"

    @property
    def reason(self) -> str | None:
        """The reason for the exception."""
        return self.response.get("Reason")


EXCEPTIONS: dict[str, type[rbinError]] = {
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ValidationException": ValidationException,
}
