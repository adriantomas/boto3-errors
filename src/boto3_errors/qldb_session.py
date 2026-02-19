# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class QLDBSessionError(Boto3Error):
    _SERVICE = "qldb-session"


class BadRequestException(QLDBSessionError):
    """Returned if the request is malformed or contains an error such as an invalid
    parameter value or a missing required parameter.
    """

    _ERROR_CODE = "BadRequestException"

    @property
    def code(self) -> str | None:
        return self.response.get("Code")


class CapacityExceededException(QLDBSessionError):
    """Returned when the request exceeds the processing capacity of the ledger."""
    _ERROR_CODE = "CapacityExceededException"


class InvalidSessionException(QLDBSessionError):
    """Returned if the session doesn't exist anymore because it timed out or expired."""
    _ERROR_CODE = "InvalidSessionException"

    @property
    def code(self) -> str | None:
        return self.response.get("Code")


class LimitExceededException(QLDBSessionError):
    """Returned if a resource limit such as number of active sessions is exceeded."""
    _ERROR_CODE = "LimitExceededException"


class OccConflictException(QLDBSessionError):
    """Returned when a transaction cannot be written to the journal due to a failure in the
    verification phase of optimistic concurrency control (OCC).
    """

    _ERROR_CODE = "OccConflictException"


class RateExceededException(QLDBSessionError):
    """Returned when the rate of requests exceeds the allowed throughput."""
    _ERROR_CODE = "RateExceededException"


EXCEPTIONS: dict[str, type[QLDBSessionError]] = {
    "BadRequestException": BadRequestException,
    "CapacityExceededException": CapacityExceededException,
    "InvalidSessionException": InvalidSessionException,
    "LimitExceededException": LimitExceededException,
    "OccConflictException": OccConflictException,
    "RateExceededException": RateExceededException,
}
