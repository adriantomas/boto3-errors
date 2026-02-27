# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class SignerDataError(Boto3Error):
    _SERVICE = "signer-data"


class AccessDeniedException(SignerDataError):
    """You do not have sufficient permissions to perform this action."""
    _ERROR_CODE = "AccessDeniedException"

    @property
    def code(self) -> str | None:
        return self.response.get("code")


class InternalServiceErrorException(SignerDataError):
    """An internal service error occurred."""
    _ERROR_CODE = "InternalServiceErrorException"

    @property
    def code(self) -> str | None:
        return self.response.get("code")


class TooManyRequestsException(SignerDataError):
    """The request was denied due to request throttling."""
    _ERROR_CODE = "TooManyRequestsException"

    @property
    def code(self) -> str | None:
        return self.response.get("code")


class ValidationException(SignerDataError):
    """The request contains invalid parameters or is malformed."""
    _ERROR_CODE = "ValidationException"

    @property
    def code(self) -> str | None:
        return self.response.get("code")


EXCEPTIONS: dict[str, type[SignerDataError]] = {
    "AccessDeniedException": AccessDeniedException,
    "InternalServiceErrorException": InternalServiceErrorException,
    "TooManyRequestsException": TooManyRequestsException,
    "ValidationException": ValidationException,
}
