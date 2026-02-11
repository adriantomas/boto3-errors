# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class AppRunnerError(Boto3Error):
    _SERVICE = "apprunner"


class InternalServiceErrorException(AppRunnerError):
    """An unexpected service exception occurred."""
    _ERROR_CODE = "InternalServiceErrorException"


class InvalidRequestException(AppRunnerError):
    """One or more input parameters aren't valid. Refer to the API action's document page,
    correct the input parameters, and try the action again.
    """

    _ERROR_CODE = "InvalidRequestException"


class InvalidStateException(AppRunnerError):
    """You can't perform this action when the resource is in its current state."""
    _ERROR_CODE = "InvalidStateException"


class ResourceNotFoundException(AppRunnerError):
    """A resource doesn't exist for the specified Amazon Resource Name (ARN) in your Amazon
    Web Services account.
    """

    _ERROR_CODE = "ResourceNotFoundException"


class ServiceQuotaExceededException(AppRunnerError):
    """App Runner can't create this resource. You've reached your account quota for this
    resource type.

    For App Runner per-resource quotas, see App Runner endpoints and quotas in the
    Amazon Web Services General Reference.
    """

    _ERROR_CODE = "ServiceQuotaExceededException"


EXCEPTIONS: dict[str, type[AppRunnerError]] = {
    "InternalServiceErrorException": InternalServiceErrorException,
    "InvalidRequestException": InvalidRequestException,
    "InvalidStateException": InvalidStateException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
}
