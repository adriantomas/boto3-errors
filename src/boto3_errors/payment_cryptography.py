# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class PaymentCryptographyError(Boto3Error):
    _SERVICE = "payment-cryptography"


class AccessDeniedException(PaymentCryptographyError):
    """You do not have sufficient access to perform this action."""
    _ERROR_CODE = "AccessDeniedException"


class ConflictException(PaymentCryptographyError):
    """This request can cause an inconsistent state for the resource."""
    _ERROR_CODE = "ConflictException"


class InternalServerException(PaymentCryptographyError):
    """The request processing has failed because of an unknown error, exception, or
    failure.
    """

    _ERROR_CODE = "InternalServerException"


class ResourceNotFoundException(PaymentCryptographyError):
    """The request was denied due to an invalid resource error."""
    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def resource_id(self) -> str | None:
        """The string for the exception."""
        return self.response.get("ResourceId")


class ServiceQuotaExceededException(PaymentCryptographyError):
    """This request would cause a service quota to be exceeded."""
    _ERROR_CODE = "ServiceQuotaExceededException"


class ServiceUnavailableException(PaymentCryptographyError):
    """The service cannot complete the request."""
    _ERROR_CODE = "ServiceUnavailableException"


class ThrottlingException(PaymentCryptographyError):
    """The request was denied due to request throttling."""
    _ERROR_CODE = "ThrottlingException"


class ValidationException(PaymentCryptographyError):
    """The request was denied due to an invalid request error."""
    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[PaymentCryptographyError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ServiceUnavailableException": ServiceUnavailableException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
