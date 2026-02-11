# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class TrustedAdvisorError(Boto3Error):
    _SERVICE = "trustedadvisor"


class AccessDeniedException(TrustedAdvisorError):
    """Exception that access has been denied due to insufficient access"""
    _ERROR_CODE = "AccessDeniedException"


class ConflictException(TrustedAdvisorError):
    """Exception that the request was denied due to conflictions in state"""
    _ERROR_CODE = "ConflictException"


class InternalServerException(TrustedAdvisorError):
    """Exception to notify that an unexpected internal error occurred during processing of
    the request
    """

    _ERROR_CODE = "InternalServerException"


class ResourceNotFoundException(TrustedAdvisorError):
    """Exception that the requested resource has not been found"""
    _ERROR_CODE = "ResourceNotFoundException"


class ThrottlingException(TrustedAdvisorError):
    """Exception to notify that requests are being throttled"""
    _ERROR_CODE = "ThrottlingException"


class ValidationException(TrustedAdvisorError):
    """Exception that the request failed to satisfy service constraints"""
    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[TrustedAdvisorError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
