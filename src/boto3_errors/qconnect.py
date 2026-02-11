# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class QConnectError(Boto3Error):
    _SERVICE = "qconnect"


class AccessDeniedException(QConnectError):
    """You do not have sufficient access to perform this action."""
    _ERROR_CODE = "AccessDeniedException"


class ConflictException(QConnectError):
    """The request could not be processed because of conflict in the current state of the
    resource. For example, if you're using a `Create` API (such as `CreateAssistant`)
    that accepts name, a conflicting resource (usually with the same name) is being
    created or mutated.
    """

    _ERROR_CODE = "ConflictException"


class DependencyFailedException(QConnectError):
    """The request failed because it depends on another request that failed."""
    _ERROR_CODE = "DependencyFailedException"


class PreconditionFailedException(QConnectError):
    """The provided `revisionId` does not match, indicating the content has been modified
    since it was last read.
    """

    _ERROR_CODE = "PreconditionFailedException"


class RequestTimeoutException(QConnectError):
    """The request reached the service more than 15 minutes after the date stamp on the
    request or more than 15 minutes after the request expiration date (such as for pre-
    signed URLs), or the date stamp on the request is more than 15 minutes in the
    future.
    """

    _ERROR_CODE = "RequestTimeoutException"


class ResourceNotFoundException(QConnectError):
    """The specified resource does not exist."""
    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def resource_name(self) -> str | None:
        """The specified resource name."""
        return self.response.get("resourceName")


class ServiceQuotaExceededException(QConnectError):
    """You've exceeded your service quota. To perform the requested action, remove some of
    the relevant resources, or use service quotas to request a service quota increase.
    """

    _ERROR_CODE = "ServiceQuotaExceededException"


class ThrottlingException(QConnectError):
    """The throttling limit has been exceeded."""
    _ERROR_CODE = "ThrottlingException"


class TooManyTagsException(QConnectError):
    """Amazon Q in Connect throws this exception if you have too many tags in your tag set."""
    _ERROR_CODE = "TooManyTagsException"

    @property
    def resource_name(self) -> str | None:
        """The specified resource name."""
        return self.response.get("resourceName")


class UnauthorizedException(QConnectError):
    """You do not have permission to perform this action."""
    _ERROR_CODE = "UnauthorizedException"


class UnprocessableContentException(QConnectError):
    """The server has a failure of processing the message"""
    _ERROR_CODE = "UnprocessableContentException"


class ValidationException(QConnectError):
    """The input fails to satisfy the constraints specified by a service."""
    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[QConnectError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "DependencyFailedException": DependencyFailedException,
    "PreconditionFailedException": PreconditionFailedException,
    "RequestTimeoutException": RequestTimeoutException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "TooManyTagsException": TooManyTagsException,
    "UnauthorizedException": UnauthorizedException,
    "UnprocessableContentException": UnprocessableContentException,
    "ValidationException": ValidationException,
}
