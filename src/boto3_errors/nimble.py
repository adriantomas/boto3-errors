# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class nimbleError(Boto3Error):
    _SERVICE = "nimble"


class AccessDeniedException(nimbleError):
    """You are not authorized to perform this operation. Check your IAM policies, and
    ensure that you are using the correct access keys.
    """

    _ERROR_CODE = "AccessDeniedException"

    @property
    def code(self) -> str | None:
        """A more specific error code."""
        return self.response.get("code")

    @property
    def context(self) -> dict[str, Any] | None:
        """The exception context."""
        return self.response.get("context")


class ConflictException(nimbleError):
    """Another operation is in progress."""
    _ERROR_CODE = "ConflictException"

    @property
    def code(self) -> str | None:
        """A more specific error code."""
        return self.response.get("code")

    @property
    def context(self) -> dict[str, Any] | None:
        """The exception context."""
        return self.response.get("context")


class InternalServerErrorException(nimbleError):
    """An internal error has occurred. Please retry your request."""
    _ERROR_CODE = "InternalServerErrorException"

    @property
    def code(self) -> str | None:
        """A more specific error code."""
        return self.response.get("code")

    @property
    def context(self) -> dict[str, Any] | None:
        """The exception context."""
        return self.response.get("context")


class ResourceNotFoundException(nimbleError):
    """The specified resource could not be found."""
    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def code(self) -> str | None:
        """A more specific error code."""
        return self.response.get("code")

    @property
    def context(self) -> dict[str, Any] | None:
        """The exception context."""
        return self.response.get("context")


class ServiceQuotaExceededException(nimbleError):
    """Your current quota does not allow you to perform the request action. You can request
    increases for some quotas, and other quotas cannot be increased.

    Please use Amazon Web Services Service Quotas to request an increase.
    """

    _ERROR_CODE = "ServiceQuotaExceededException"

    @property
    def code(self) -> str | None:
        """A more specific error code."""
        return self.response.get("code")

    @property
    def context(self) -> dict[str, Any] | None:
        """The exception context."""
        return self.response.get("context")


class ThrottlingException(nimbleError):
    """The request throughput limit was exceeded."""
    _ERROR_CODE = "ThrottlingException"

    @property
    def code(self) -> str | None:
        """A more specific error code."""
        return self.response.get("code")

    @property
    def context(self) -> dict[str, Any] | None:
        """The exception context."""
        return self.response.get("context")


class ValidationException(nimbleError):
    """One of the parameters in the request is invalid."""
    _ERROR_CODE = "ValidationException"

    @property
    def code(self) -> str | None:
        """A more specific error code."""
        return self.response.get("code")

    @property
    def context(self) -> dict[str, Any] | None:
        """The exception context."""
        return self.response.get("context")


EXCEPTIONS: dict[str, type[nimbleError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerErrorException": InternalServerErrorException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
