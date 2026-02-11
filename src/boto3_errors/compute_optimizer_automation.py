# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class ComputeOptimizerAutomationError(Boto3Error):
    _SERVICE = "compute-optimizer-automation"


class AccessDeniedException(ComputeOptimizerAutomationError):
    """You do not have sufficient permissions to perform this action."""
    _ERROR_CODE = "AccessDeniedException"


class ForbiddenException(ComputeOptimizerAutomationError):
    """You are not authorized to perform this action."""
    _ERROR_CODE = "ForbiddenException"


class IdempotencyTokenInUseException(ComputeOptimizerAutomationError):
    """The specified client token is already in use."""
    _ERROR_CODE = "IdempotencyTokenInUseException"


class IdempotentParameterMismatchException(ComputeOptimizerAutomationError):
    """Exception thrown when the same client token is used with different parameters,
    indicating a mismatch in idempotent request parameters.
    """

    _ERROR_CODE = "IdempotentParameterMismatchException"


class InternalServerException(ComputeOptimizerAutomationError):
    """An internal error occurred while processing the request."""
    _ERROR_CODE = "InternalServerException"


class InvalidParameterValueException(ComputeOptimizerAutomationError):
    """One or more parameter values are not valid."""
    _ERROR_CODE = "InvalidParameterValueException"


class NotManagementAccountException(ComputeOptimizerAutomationError):
    """The operation can only be performed by a management account."""
    _ERROR_CODE = "NotManagementAccountException"


class OptInRequiredException(ComputeOptimizerAutomationError):
    """The account must be opted in to Compute Optimizer Automation before performing this
    action.
    """

    _ERROR_CODE = "OptInRequiredException"


class ResourceNotFoundException(ComputeOptimizerAutomationError):
    """The specified resource was not found."""
    _ERROR_CODE = "ResourceNotFoundException"


class ServiceQuotaExceededException(ComputeOptimizerAutomationError):
    """The request would exceed service quotas."""
    _ERROR_CODE = "ServiceQuotaExceededException"


class ServiceUnavailableException(ComputeOptimizerAutomationError):
    """The service is temporarily unavailable."""
    _ERROR_CODE = "ServiceUnavailableException"


class ThrottlingException(ComputeOptimizerAutomationError):
    """The request was denied due to request throttling."""
    _ERROR_CODE = "ThrottlingException"


EXCEPTIONS: dict[str, type[ComputeOptimizerAutomationError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ForbiddenException": ForbiddenException,
    "IdempotencyTokenInUseException": IdempotencyTokenInUseException,
    "IdempotentParameterMismatchException": IdempotentParameterMismatchException,
    "InternalServerException": InternalServerException,
    "InvalidParameterValueException": InvalidParameterValueException,
    "NotManagementAccountException": NotManagementAccountException,
    "OptInRequiredException": OptInRequiredException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ServiceUnavailableException": ServiceUnavailableException,
    "ThrottlingException": ThrottlingException,
}
