# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class PaymentCryptographyError(Boto3Error):
    _SERVICE = "payment-cryptography"


class AccessDeniedException(PaymentCryptographyError):
    """You do not have sufficient access to perform this action.

    This exception is thrown when the caller lacks the necessary IAM permissions to
    perform the requested operation. Verify that your IAM policy includes the required
    permissions for the specific Amazon Web Services Payment Cryptography action you're
    attempting.
    """

    _ERROR_CODE = "AccessDeniedException"


class ConflictException(PaymentCryptographyError):
    """This request can cause an inconsistent state for the resource.

    The requested operation conflicts with the current state of the resource. For
    example, attempting to delete a key that is currently being used, or trying to
    create a resource that already exists.
    """

    _ERROR_CODE = "ConflictException"


class InternalServerException(PaymentCryptographyError):
    """The request processing has failed because of an unknown error, exception, or
    failure.

    This indicates a server-side error within the Amazon Web Services Payment
    Cryptography service. If this error persists, contact support for assistance.
    """

    _ERROR_CODE = "InternalServerException"


class ResourceNotFoundException(PaymentCryptographyError):
    """The request was denied due to resource not found.

    The specified key, alias, or other resource does not exist in your account or
    region. Verify that the resource identifier is correct and that the resource exists
    in the expected region.
    """

    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def resource_id(self) -> str | None:
        """The identifier of the resource that was not found.

        This field contains the specific resource identifier (such as a key ARN or alias
        name) that could not be located.
        """
        return self.response.get("ResourceId")


class ServiceQuotaExceededException(PaymentCryptographyError):
    """This request would cause a service quota to be exceeded.

    You have reached the maximum number of keys, aliases, or other resources allowed in
    your account. Review your current usage and consider deleting unused resources or
    requesting a quota increase.
    """

    _ERROR_CODE = "ServiceQuotaExceededException"


class ServiceUnavailableException(PaymentCryptographyError):
    """The service cannot complete the request.

    The Amazon Web Services Payment Cryptography service is temporarily unavailable.
    This is typically a temporary condition - retry your request after a brief delay.
    """

    _ERROR_CODE = "ServiceUnavailableException"


class ThrottlingException(PaymentCryptographyError):
    """The request was denied due to request throttling.

    You have exceeded the rate limits for Amazon Web Services Payment Cryptography API
    calls. Implement exponential backoff and retry logic in your application to handle
    throttling gracefully.
    """

    _ERROR_CODE = "ThrottlingException"


class ValidationException(PaymentCryptographyError):
    """The request was denied due to an invalid request error.

    One or more parameters in your request are invalid. Check the parameter values,
    formats, and constraints specified in the API documentation.
    """

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
