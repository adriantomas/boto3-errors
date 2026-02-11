# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class Route53RecoveryReadinessError(Boto3Error):
    _SERVICE = "route53-recovery-readiness"


class AccessDeniedException(Route53RecoveryReadinessError):
    """User does not have sufficient access to perform this action."""
    _ERROR_CODE = "AccessDeniedException"


class ConflictException(Route53RecoveryReadinessError):
    """Updating or deleting a resource can cause an inconsistent state."""
    _ERROR_CODE = "ConflictException"


class InternalServerException(Route53RecoveryReadinessError):
    """An unexpected error occurred."""
    _ERROR_CODE = "InternalServerException"


class ResourceNotFoundException(Route53RecoveryReadinessError):
    """The requested resource does not exist."""
    _ERROR_CODE = "ResourceNotFoundException"


class ThrottlingException(Route53RecoveryReadinessError):
    """Request was denied due to request throttling."""
    _ERROR_CODE = "ThrottlingException"


class ValidationException(Route53RecoveryReadinessError):
    """The input fails to satisfy the constraints specified by an AWS service."""
    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[Route53RecoveryReadinessError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
