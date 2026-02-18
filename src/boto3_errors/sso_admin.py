# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class SSOAdminError(Boto3Error):
    _SERVICE = "sso-admin"


class AccessDeniedException(SSOAdminError):
    """You do not have sufficient access to perform this action."""
    _ERROR_CODE = "AccessDeniedException"


class ConflictException(SSOAdminError):
    """Occurs when a conflict with a previous successful write is detected. This generally
    occurs when the previous write did not have time to propagate to the host serving
    the current request. A retry (with appropriate backoff logic) is the recommended
    response to this exception.
    """

    _ERROR_CODE = "ConflictException"


class InternalServerException(SSOAdminError):
    """The request processing has failed because of an unknown error, exception, or failure
    with an internal server.
    """

    _ERROR_CODE = "InternalServerException"


class ResourceNotFoundException(SSOAdminError):
    """Indicates that a requested resource is not found."""
    _ERROR_CODE = "ResourceNotFoundException"


class ServiceQuotaExceededException(SSOAdminError):
    """Indicates that the principal has crossed the permitted number of resources that can
    be created.
    """

    _ERROR_CODE = "ServiceQuotaExceededException"


class ThrottlingException(SSOAdminError):
    """Indicates that the principal has crossed the throttling limits of the API
    operations.
    """

    _ERROR_CODE = "ThrottlingException"


class ValidationException(SSOAdminError):
    """The request failed because it contains a syntax error."""
    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[SSOAdminError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
