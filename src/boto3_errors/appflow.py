# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class AppflowError(Boto3Error):
    _SERVICE = "appflow"


class AccessDeniedException(AppflowError):
    """AppFlow/Requester has invalid or missing permissions."""
    _ERROR_CODE = "AccessDeniedException"


class ConflictException(AppflowError):
    """There was a conflict when processing the request (for example, a flow with the given
    name already exists within the account. Check for conflicting resource names and try
    again.
    """

    _ERROR_CODE = "ConflictException"


class ConnectorAuthenticationException(AppflowError):
    """An error occurred when authenticating with the connector endpoint."""
    _ERROR_CODE = "ConnectorAuthenticationException"


class ConnectorServerException(AppflowError):
    """An error occurred when retrieving data from the connector endpoint."""
    _ERROR_CODE = "ConnectorServerException"


class InternalServerException(AppflowError):
    """An internal service error occurred during the processing of your request. Try again
    later.
    """

    _ERROR_CODE = "InternalServerException"


class ResourceNotFoundException(AppflowError):
    """The resource specified in the request (such as the source or destination connector
    profile) is not found.
    """

    _ERROR_CODE = "ResourceNotFoundException"


class ServiceQuotaExceededException(AppflowError):
    """The request would cause a service quota (such as the number of flows) to be
    exceeded.
    """

    _ERROR_CODE = "ServiceQuotaExceededException"


class ThrottlingException(AppflowError):
    """API calls have exceeded the maximum allowed API request rate per account and per
    Region.
    """

    _ERROR_CODE = "ThrottlingException"


class UnsupportedOperationException(AppflowError):
    """The requested operation is not supported for the current flow."""
    _ERROR_CODE = "UnsupportedOperationException"


class ValidationException(AppflowError):
    """The request has invalid or missing parameters."""
    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[AppflowError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "ConnectorAuthenticationException": ConnectorAuthenticationException,
    "ConnectorServerException": ConnectorServerException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "UnsupportedOperationException": UnsupportedOperationException,
    "ValidationException": ValidationException,
}
