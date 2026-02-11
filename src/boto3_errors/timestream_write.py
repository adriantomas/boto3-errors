# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class TimestreamWriteError(Boto3Error):
    _SERVICE = "timestream-write"


class AccessDeniedException(TimestreamWriteError):
    """You are not authorized to perform this action."""
    _ERROR_CODE = "AccessDeniedException"


class ConflictException(TimestreamWriteError):
    """Timestream was unable to process this request because it contains resource that
    already exists.
    """

    _ERROR_CODE = "ConflictException"


class InternalServerException(TimestreamWriteError):
    """Timestream was unable to fully process this request because of an internal server
    error.
    """

    _ERROR_CODE = "InternalServerException"


class InvalidEndpointException(TimestreamWriteError):
    """The requested endpoint was not valid."""
    _ERROR_CODE = "InvalidEndpointException"


class RejectedRecordsException(TimestreamWriteError):
    """WriteRecords would throw this exception in the following cases:

    - Records with duplicate data where there are multiple records with the same
      dimensions, timestamps, and measure names but:

      - Measure values are different
      - Version is not present in the request or the value of version in the new record
        is equal to or lower than the existing value
      In this case, if Timestream rejects data, the `ExistingVersion` field in the
    `RejectedRecords` response will indicate the current record’s version. To force an
    update, you can resend the request with a version for the record set to a value
    greater than the `ExistingVersion`.
    - Records with timestamps that lie outside the retention duration of the memory
      store.
    - Records with dimensions or measures that exceed the Timestream defined limits.

     For more information, see Quotas in the Amazon Timestream Developer Guide.
    """

    _ERROR_CODE = "RejectedRecordsException"

    @property
    def rejected_records(self) -> list[Any] | None:
        return self.response.get("RejectedRecords")


class ResourceNotFoundException(TimestreamWriteError):
    """The operation tried to access a nonexistent resource. The resource might not be
    specified correctly, or its status might not be ACTIVE.
    """

    _ERROR_CODE = "ResourceNotFoundException"


class ServiceQuotaExceededException(TimestreamWriteError):
    """The instance quota of resource exceeded for this account."""
    _ERROR_CODE = "ServiceQuotaExceededException"


class ThrottlingException(TimestreamWriteError):
    """Too many requests were made by a user and they exceeded the service quotas. The
    request was throttled.
    """

    _ERROR_CODE = "ThrottlingException"


class ValidationException(TimestreamWriteError):
    """An invalid or malformed request."""
    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[TimestreamWriteError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "InvalidEndpointException": InvalidEndpointException,
    "RejectedRecordsException": RejectedRecordsException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
