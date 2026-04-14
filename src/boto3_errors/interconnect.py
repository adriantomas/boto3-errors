# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class InterconnectError(Boto3Error):
    _SERVICE = "interconnect"


class AccessDeniedException(InterconnectError):
    """The calling principal is not allowed to access the specified resource, or the
    resource does not exist.
    """

    _ERROR_CODE = "AccessDeniedException"


class InterconnectClientException(InterconnectError):
    """The request was denied due to incorrect client supplied parameters."""
    _ERROR_CODE = "InterconnectClientException"


class InterconnectServerException(InterconnectError):
    """The request resulted in an exception internal to the service."""
    _ERROR_CODE = "InterconnectServerException"


class InterconnectValidationException(InterconnectError):
    """The input fails to satisfy the constraints specified."""
    _ERROR_CODE = "InterconnectValidationException"


class ResourceNotFoundException(InterconnectError):
    """The request specifies a resource that does not exist on the server."""
    _ERROR_CODE = "ResourceNotFoundException"


class ServiceQuotaExceededException(InterconnectError):
    """The requested operation would result in the calling principal exceeding their
    allotted quota.
    """

    _ERROR_CODE = "ServiceQuotaExceededException"


class ThrottlingException(InterconnectError):
    """The request was denied due to request throttling."""
    _ERROR_CODE = "ThrottlingException"


EXCEPTIONS: dict[str, type[InterconnectError]] = {
    "AccessDeniedException": AccessDeniedException,
    "InterconnectClientException": InterconnectClientException,
    "InterconnectServerException": InterconnectServerException,
    "InterconnectValidationException": InterconnectValidationException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
}
