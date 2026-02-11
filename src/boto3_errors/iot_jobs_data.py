# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class IoTJobsDataPlaneError(Boto3Error):
    _SERVICE = "iot-jobs-data"


class CertificateValidationException(IoTJobsDataPlaneError):
    """The certificate is invalid."""
    _ERROR_CODE = "CertificateValidationException"


class ConflictException(IoTJobsDataPlaneError):
    """A conflict has occurred when performing the API request."""
    _ERROR_CODE = "ConflictException"

    @property
    def resource_id(self) -> str | None:
        """A conflict occurred while performing the API request on the resource ID."""
        return self.response.get("resourceId")


class InternalServerException(IoTJobsDataPlaneError):
    """An internal server error occurred when performing the API request."""
    _ERROR_CODE = "InternalServerException"


class InvalidRequestException(IoTJobsDataPlaneError):
    """The contents of the request were invalid."""
    _ERROR_CODE = "InvalidRequestException"


class InvalidStateTransitionException(IoTJobsDataPlaneError):
    """An update attempted to change the job execution to a state that is invalid because
    of the job execution's current state (for example, an attempt to change a request in
    state SUCCESS to state IN_PROGRESS). In this case, the body of the error message
    also contains the executionState field.
    """

    _ERROR_CODE = "InvalidStateTransitionException"


class ResourceNotFoundException(IoTJobsDataPlaneError):
    """The specified resource does not exist."""
    _ERROR_CODE = "ResourceNotFoundException"


class ServiceQuotaExceededException(IoTJobsDataPlaneError):
    """The service quota has been exceeded for this request."""
    _ERROR_CODE = "ServiceQuotaExceededException"


class ServiceUnavailableException(IoTJobsDataPlaneError):
    """The service is temporarily unavailable."""
    _ERROR_CODE = "ServiceUnavailableException"


class TerminalStateException(IoTJobsDataPlaneError):
    """The job is in a terminal state."""
    _ERROR_CODE = "TerminalStateException"


class ThrottlingException(IoTJobsDataPlaneError):
    """The rate exceeds the limit."""
    _ERROR_CODE = "ThrottlingException"

    @property
    def payload(self) -> bytes | None:
        """The payload associated with the exception."""
        return self.response.get("payload")


class ValidationException(IoTJobsDataPlaneError):
    """A validation error occurred when performing the API request."""
    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[IoTJobsDataPlaneError]] = {
    "CertificateValidationException": CertificateValidationException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "InvalidRequestException": InvalidRequestException,
    "InvalidStateTransitionException": InvalidStateTransitionException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ServiceUnavailableException": ServiceUnavailableException,
    "TerminalStateException": TerminalStateException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
