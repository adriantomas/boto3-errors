# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class TimestreamInfluxDBError(Boto3Error):
    _SERVICE = "timestream-influxdb"


class AccessDeniedException(TimestreamInfluxDBError):
    """You do not have sufficient access to perform this action."""
    _ERROR_CODE = "AccessDeniedException"


class ConflictException(TimestreamInfluxDBError):
    """The request conflicts with an existing resource in Timestream for InfluxDB."""
    _ERROR_CODE = "ConflictException"

    @property
    def resource_id(self) -> str | None:
        """The identifier for the Timestream for InfluxDB resource associated with the
        request.
        """
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of Timestream for InfluxDB resource associated with the request."""
        return self.response.get("resourceType")


class InternalServerException(TimestreamInfluxDBError):
    """The request processing has failed because of an unknown error, exception or failure."""
    _ERROR_CODE = "InternalServerException"


class ResourceNotFoundException(TimestreamInfluxDBError):
    """The requested resource was not found or does not exist."""
    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def resource_id(self) -> str | None:
        """The identifier for the Timestream for InfluxDB resource associated with the
        request.
        """
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of Timestream for InfluxDB resource associated with the request."""
        return self.response.get("resourceType")


class ServiceQuotaExceededException(TimestreamInfluxDBError):
    """The request exceeds the service quota."""
    _ERROR_CODE = "ServiceQuotaExceededException"


class ThrottlingException(TimestreamInfluxDBError):
    """The request was denied due to request throttling."""
    _ERROR_CODE = "ThrottlingException"

    @property
    def retry_after_seconds(self) -> int | None:
        """The number of seconds the caller should wait before retrying."""
        return self.response.get("retryAfterSeconds")


class ValidationException(TimestreamInfluxDBError):
    """The input fails to satisfy the constraints specified by Timestream for InfluxDB."""
    _ERROR_CODE = "ValidationException"

    @property
    def reason(self) -> str | None:
        """The reason that validation failed."""
        return self.response.get("reason")


EXCEPTIONS: dict[str, type[TimestreamInfluxDBError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
