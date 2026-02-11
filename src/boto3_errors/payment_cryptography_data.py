# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class PaymentCryptographyDataError(Boto3Error):
    _SERVICE = "payment-cryptography-data"


class AccessDeniedException(PaymentCryptographyDataError):
    """You do not have sufficient access to perform this action."""
    _ERROR_CODE = "AccessDeniedException"


class InternalServerException(PaymentCryptographyDataError):
    """The request processing has failed because of an unknown error, exception, or
    failure.
    """

    _ERROR_CODE = "InternalServerException"


class ResourceNotFoundException(PaymentCryptographyDataError):
    """The request was denied due to an invalid resource error."""
    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def resource_id(self) -> str | None:
        """The resource that is missing."""
        return self.response.get("ResourceId")


class ThrottlingException(PaymentCryptographyDataError):
    """The request was denied due to request throttling."""
    _ERROR_CODE = "ThrottlingException"


class ValidationException(PaymentCryptographyDataError):
    """The request was denied due to an invalid request error."""
    _ERROR_CODE = "ValidationException"

    @property
    def field_list(self) -> list[Any] | None:
        """The request was denied due to an invalid request error."""
        return self.response.get("fieldList")


class VerificationFailedException(PaymentCryptographyDataError):
    """This request failed verification."""
    _ERROR_CODE = "VerificationFailedException"

    @property
    def reason(self) -> str | None:
        """The reason for the exception."""
        return self.response.get("Reason")


EXCEPTIONS: dict[str, type[PaymentCryptographyDataError]] = {
    "AccessDeniedException": AccessDeniedException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
    "VerificationFailedException": VerificationFailedException,
}
