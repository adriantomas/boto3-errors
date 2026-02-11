# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class CodeCatalystError(Boto3Error):
    _SERVICE = "codecatalyst"


class AccessDeniedException(CodeCatalystError):
    """The request was denied because you don't have sufficient access to perform this
    action. Verify that you are a member of a role that allows this action.
    """

    _ERROR_CODE = "AccessDeniedException"


class ConflictException(CodeCatalystError):
    """The request was denied because the requested operation would cause a conflict with
    the current state of a service resource associated with the request. Another user
    might have updated the resource. Reload, make sure you have the latest data, and
    then try again.
    """

    _ERROR_CODE = "ConflictException"


class ResourceNotFoundException(CodeCatalystError):
    """The request was denied because the specified resource was not found. Verify that the
    spelling is correct and that you have access to the resource.
    """

    _ERROR_CODE = "ResourceNotFoundException"


class ServiceQuotaExceededException(CodeCatalystError):
    """The request was denied because one or more resources has reached its limits for the
    tier the space belongs to. Either reduce the number of resources, or change the tier
    if applicable.
    """

    _ERROR_CODE = "ServiceQuotaExceededException"


class ThrottlingException(CodeCatalystError):
    """The request was denied due to request throttling."""
    _ERROR_CODE = "ThrottlingException"


class ValidationException(CodeCatalystError):
    """The request was denied because an input failed to satisfy the constraints specified
    by the service. Check the spelling and input requirements, and then try again.
    """

    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[CodeCatalystError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
