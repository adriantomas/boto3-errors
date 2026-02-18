# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class IoTJobsDataPlaneError(Boto3Error):
    _SERVICE = "iot-jobs-data"


class CertificateValidationException(IoTJobsDataPlaneError):
    """The certificate is invalid."""
    _ERROR_CODE = "CertificateValidationException"


class InvalidRequestException(IoTJobsDataPlaneError):
    """The contents of the request were invalid. For example, this code is returned when an
    UpdateJobExecution request contains invalid status details. The message contains
    details about the error.
    """

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


EXCEPTIONS: dict[str, type[IoTJobsDataPlaneError]] = {
    "CertificateValidationException": CertificateValidationException,
    "InvalidRequestException": InvalidRequestException,
    "InvalidStateTransitionException": InvalidStateTransitionException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceUnavailableException": ServiceUnavailableException,
    "TerminalStateException": TerminalStateException,
    "ThrottlingException": ThrottlingException,
}
