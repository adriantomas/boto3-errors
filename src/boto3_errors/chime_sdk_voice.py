# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class ChimeSDKVoiceError(Boto3Error):
    _SERVICE = "chime-sdk-voice"


class AccessDeniedException(ChimeSDKVoiceError):
    """You don't have the permissions needed to run this action."""
    _ERROR_CODE = "AccessDeniedException"


class BadRequestException(ChimeSDKVoiceError):
    """The input parameters don't match the service's restrictions."""
    _ERROR_CODE = "BadRequestException"


class ConflictException(ChimeSDKVoiceError):
    """Multiple instances of the same request were made simultaneously."""
    _ERROR_CODE = "ConflictException"


class ForbiddenException(ChimeSDKVoiceError):
    """The client is permanently forbidden from making the request."""
    _ERROR_CODE = "ForbiddenException"


class GoneException(ChimeSDKVoiceError):
    """Access to the target resource is no longer available at the origin server. This
    condition is likely to be permanent.
    """

    _ERROR_CODE = "GoneException"


class NotFoundException(ChimeSDKVoiceError):
    """The requested resource couldn't be found."""
    _ERROR_CODE = "NotFoundException"


class ResourceLimitExceededException(ChimeSDKVoiceError):
    """The request exceeds the resource limit."""
    _ERROR_CODE = "ResourceLimitExceededException"


class ServiceFailureException(ChimeSDKVoiceError):
    """The service encountered an unexpected error."""
    _ERROR_CODE = "ServiceFailureException"


class ServiceUnavailableException(ChimeSDKVoiceError):
    """The service is currently unavailable."""
    _ERROR_CODE = "ServiceUnavailableException"


class ThrottledClientException(ChimeSDKVoiceError):
    """The number of customer requests exceeds the request rate limit."""
    _ERROR_CODE = "ThrottledClientException"


class UnauthorizedClientException(ChimeSDKVoiceError):
    """The client isn't authorized to request a resource."""
    _ERROR_CODE = "UnauthorizedClientException"


class UnprocessableEntityException(ChimeSDKVoiceError):
    """A well-formed request couldn't be followed due to semantic errors."""
    _ERROR_CODE = "UnprocessableEntityException"


EXCEPTIONS: dict[str, type[ChimeSDKVoiceError]] = {
    "AccessDeniedException": AccessDeniedException,
    "BadRequestException": BadRequestException,
    "ConflictException": ConflictException,
    "ForbiddenException": ForbiddenException,
    "GoneException": GoneException,
    "NotFoundException": NotFoundException,
    "ResourceLimitExceededException": ResourceLimitExceededException,
    "ServiceFailureException": ServiceFailureException,
    "ServiceUnavailableException": ServiceUnavailableException,
    "ThrottledClientException": ThrottledClientException,
    "UnauthorizedClientException": UnauthorizedClientException,
    "UnprocessableEntityException": UnprocessableEntityException,
}
