# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class TimestreamQueryError(Boto3Error):
    _SERVICE = "timestream-query"


class AccessDeniedException(TimestreamQueryError):
    """You do not have the necessary permissions to access the account settings."""
    _ERROR_CODE = "AccessDeniedException"


class ConflictException(TimestreamQueryError):
    """Unable to poll results for a cancelled query."""
    _ERROR_CODE = "ConflictException"


class InternalServerException(TimestreamQueryError):
    """An internal server error occurred while processing the request."""
    _ERROR_CODE = "InternalServerException"


class InvalidEndpointException(TimestreamQueryError):
    """The requested endpoint is invalid."""
    _ERROR_CODE = "InvalidEndpointException"


class QueryExecutionException(TimestreamQueryError):
    """Timestream was unable to run the query successfully."""
    _ERROR_CODE = "QueryExecutionException"


class ResourceNotFoundException(TimestreamQueryError):
    """The requested resource could not be found."""
    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def scheduled_query_arn(self) -> str | None:
        """The ARN of the scheduled query."""
        return self.response.get("ScheduledQueryArn")


class ServiceQuotaExceededException(TimestreamQueryError):
    """You have exceeded the service quota."""
    _ERROR_CODE = "ServiceQuotaExceededException"


class ThrottlingException(TimestreamQueryError):
    """The request was throttled due to excessive requests."""
    _ERROR_CODE = "ThrottlingException"


class ValidationException(TimestreamQueryError):
    """Invalid or malformed request."""
    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[TimestreamQueryError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "InvalidEndpointException": InvalidEndpointException,
    "QueryExecutionException": QueryExecutionException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
