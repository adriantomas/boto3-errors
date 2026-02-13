# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class Route53RecoveryControlConfigError(Boto3Error):
    _SERVICE = "route53-recovery-control-config"


class AccessDeniedException(Route53RecoveryControlConfigError):
    """403 response - You do not have sufficient access to perform this action."""
    _ERROR_CODE = "AccessDeniedException"


class ConflictException(Route53RecoveryControlConfigError):
    """409 response - ConflictException. You might be using a predefined variable."""
    _ERROR_CODE = "ConflictException"


class InternalServerException(Route53RecoveryControlConfigError):
    """500 response - InternalServiceError. Temporary service error. Retry the request."""
    _ERROR_CODE = "InternalServerException"


class ResourceNotFoundException(Route53RecoveryControlConfigError):
    """404 response - MalformedQueryString. The query string contains a syntax error or
    resource not found.
    """

    _ERROR_CODE = "ResourceNotFoundException"


class ServiceQuotaExceededException(Route53RecoveryControlConfigError):
    """402 response - You attempted to create more resources than the service allows based
    on service quotas.
    """

    _ERROR_CODE = "ServiceQuotaExceededException"


class ThrottlingException(Route53RecoveryControlConfigError):
    """429 response - LimitExceededException or TooManyRequestsException."""
    _ERROR_CODE = "ThrottlingException"


class ValidationException(Route53RecoveryControlConfigError):
    """400 response - Multiple causes. For example, you might have a malformed query string
    and input parameter might be out of range, or you might have used parameters
    together incorrectly.
    """

    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[Route53RecoveryControlConfigError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
