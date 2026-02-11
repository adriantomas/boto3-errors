# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class LaunchWizardError(Boto3Error):
    _SERVICE = "launch-wizard"


class InternalServerException(LaunchWizardError):
    """An internal error has occurred. Retry your request, but if the problem persists,
    contact us with details by posting a question on re:Post.
    """

    _ERROR_CODE = "InternalServerException"


class ResourceLimitException(LaunchWizardError):
    """You have exceeded an Launch Wizard resource limit. For example, you might have too
    many deployments in progress.
    """

    _ERROR_CODE = "ResourceLimitException"


class ResourceNotFoundException(LaunchWizardError):
    """The specified workload or deployment resource can't be found."""
    _ERROR_CODE = "ResourceNotFoundException"


class ValidationException(LaunchWizardError):
    """The input fails to satisfy the constraints specified by an Amazon Web Services
    service.
    """

    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[LaunchWizardError]] = {
    "InternalServerException": InternalServerException,
    "ResourceLimitException": ResourceLimitException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ValidationException": ValidationException,
}
