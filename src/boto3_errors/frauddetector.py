# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class FraudDetectorError(Boto3Error):
    _SERVICE = "frauddetector"


class AccessDeniedException(FraudDetectorError):
    """An exception indicating Amazon Fraud Detector does not have the needed permissions.
    This can occur if you submit a request, such as `PutExternalModel`, that specifies a
    role that is not in your account.
    """

    _ERROR_CODE = "AccessDeniedException"


class ConflictException(FraudDetectorError):
    """An exception indicating there was a conflict during a delete operation."""
    _ERROR_CODE = "ConflictException"


class InternalServerException(FraudDetectorError):
    """An exception indicating an internal server error."""
    _ERROR_CODE = "InternalServerException"


class ResourceNotFoundException(FraudDetectorError):
    """An exception indicating the specified resource was not found."""
    _ERROR_CODE = "ResourceNotFoundException"


class ResourceUnavailableException(FraudDetectorError):
    """An exception indicating that the attached customer-owned (external) model threw an
    exception when Amazon Fraud Detector invoked the model.
    """

    _ERROR_CODE = "ResourceUnavailableException"


class ThrottlingException(FraudDetectorError):
    """An exception indicating a throttling error."""
    _ERROR_CODE = "ThrottlingException"


class ValidationException(FraudDetectorError):
    """An exception indicating a specified value is not allowed."""
    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[FraudDetectorError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ResourceUnavailableException": ResourceUnavailableException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
