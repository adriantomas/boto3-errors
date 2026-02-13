# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class signerError(Boto3Error):
    _SERVICE = "signer"


class AccessDeniedException(signerError):
    """You do not have sufficient access to perform this action."""
    _ERROR_CODE = "AccessDeniedException"

    @property
    def code(self) -> str | None:
        return self.response.get("code")


class BadRequestException(signerError):
    """The request contains invalid parameters for the ARN or tags. This exception also
    occurs when you call a tagging API on a cancelled signing profile.
    """

    _ERROR_CODE = "BadRequestException"

    @property
    def code(self) -> str | None:
        return self.response.get("code")


class ConflictException(signerError):
    """The resource encountered a conflicting state."""
    _ERROR_CODE = "ConflictException"

    @property
    def code(self) -> str | None:
        return self.response.get("code")


class InternalServiceErrorException(signerError):
    """An internal error occurred."""
    _ERROR_CODE = "InternalServiceErrorException"

    @property
    def code(self) -> str | None:
        return self.response.get("code")


class NotFoundException(signerError):
    """The signing profile was not found."""
    _ERROR_CODE = "NotFoundException"

    @property
    def code(self) -> str | None:
        return self.response.get("code")


class ResourceNotFoundException(signerError):
    """A specified resource could not be found."""
    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def code(self) -> str | None:
        return self.response.get("code")


class ServiceLimitExceededException(signerError):
    """The client is making a request that exceeds service limits."""
    _ERROR_CODE = "ServiceLimitExceededException"

    @property
    def code(self) -> str | None:
        return self.response.get("code")


class ThrottlingException(signerError):
    """The request was denied due to request throttling.

    Instead of this error, `TooManyRequestsException` should be used.
    """

    _ERROR_CODE = "ThrottlingException"

    @property
    def code(self) -> str | None:
        return self.response.get("code")


class TooManyRequestsException(signerError):
    """The allowed number of job-signing requests has been exceeded.

    This error supersedes the error `ThrottlingException`.
    """

    _ERROR_CODE = "TooManyRequestsException"

    @property
    def code(self) -> str | None:
        return self.response.get("code")


class ValidationException(signerError):
    """You signing certificate could not be validated."""
    _ERROR_CODE = "ValidationException"

    @property
    def code(self) -> str | None:
        return self.response.get("code")


EXCEPTIONS: dict[str, type[signerError]] = {
    "AccessDeniedException": AccessDeniedException,
    "BadRequestException": BadRequestException,
    "ConflictException": ConflictException,
    "InternalServiceErrorException": InternalServiceErrorException,
    "NotFoundException": NotFoundException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceLimitExceededException": ServiceLimitExceededException,
    "ThrottlingException": ThrottlingException,
    "TooManyRequestsException": TooManyRequestsException,
    "ValidationException": ValidationException,
}
