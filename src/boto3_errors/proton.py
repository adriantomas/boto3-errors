# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class ProtonError(Boto3Error):
    _SERVICE = "proton"


class AccessDeniedException(ProtonError):
    """There isn't sufficient access for performing this action."""
    _ERROR_CODE = "AccessDeniedException"


class ConflictException(ProtonError):
    """The request couldn't be made due to a conflicting operation or resource."""
    _ERROR_CODE = "ConflictException"


class InternalServerException(ProtonError):
    """The request failed to register with the service."""
    _ERROR_CODE = "InternalServerException"


class ResourceNotFoundException(ProtonError):
    """The requested resource wasn't found."""
    _ERROR_CODE = "ResourceNotFoundException"


class ServiceQuotaExceededException(ProtonError):
    """A quota was exceeded. For more information, see Proton Quotas in the Proton User
    Guide.
    """

    _ERROR_CODE = "ServiceQuotaExceededException"


class ThrottlingException(ProtonError):
    """The request was denied due to request throttling."""
    _ERROR_CODE = "ThrottlingException"


class ValidationException(ProtonError):
    """The input is invalid or an out-of-range value was supplied for the input parameter."""
    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[ProtonError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
