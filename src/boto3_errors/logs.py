# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class CloudWatchLogsError(Boto3Error):
    _SERVICE = "logs"


class AccessDeniedException(CloudWatchLogsError):
    """You don't have sufficient permissions to perform this action."""
    _ERROR_CODE = "AccessDeniedException"


class ConflictException(CloudWatchLogsError):
    """This operation attempted to create a resource that already exists."""
    _ERROR_CODE = "ConflictException"


class DataAlreadyAcceptedException(CloudWatchLogsError):
    """The event was already logged.

     `PutLogEvents` actions are now always accepted and never return
    `DataAlreadyAcceptedException` regardless of whether a given batch of log events has
    already been accepted.
    """

    _ERROR_CODE = "DataAlreadyAcceptedException"

    @property
    def expected_sequence_token(self) -> str | None:
        return self.response.get("expectedSequenceToken")


class InternalServerException(CloudWatchLogsError):
    """An internal server error occurred while processing the request. This exception is
    returned when the service encounters an unexpected condition that prevents it from
    fulfilling the request.
    """

    _ERROR_CODE = "InternalServerException"


class InternalStreamingException(CloudWatchLogsError):
    """An internal error occurred during the streaming of log data. This exception is
    thrown when there's an issue with the internal streaming mechanism used by the
    GetLogObject operation.
    """

    _ERROR_CODE = "InternalStreamingException"


class InvalidOperationException(CloudWatchLogsError):
    """The operation is not valid on the specified resource."""
    _ERROR_CODE = "InvalidOperationException"


class InvalidParameterException(CloudWatchLogsError):
    """A parameter is specified incorrectly."""
    _ERROR_CODE = "InvalidParameterException"


class InvalidSequenceTokenException(CloudWatchLogsError):
    """The sequence token is not valid. You can get the correct sequence token in the
    `expectedSequenceToken` field in the `InvalidSequenceTokenException` message.

     `PutLogEvents` actions are now always accepted and never return
    `InvalidSequenceTokenException` regardless of receiving an invalid sequence token.
    """

    _ERROR_CODE = "InvalidSequenceTokenException"

    @property
    def expected_sequence_token(self) -> str | None:
        return self.response.get("expectedSequenceToken")


class LimitExceededException(CloudWatchLogsError):
    """You have reached the maximum number of resources that can be created."""
    _ERROR_CODE = "LimitExceededException"


class MalformedQueryException(CloudWatchLogsError):
    """The query string is not valid. Details about this error are displayed in a
    `QueryCompileError` object. For more information, see QueryCompileError.

    For more information about valid query syntax, see CloudWatch Logs Insights Query
    Syntax.
    """

    _ERROR_CODE = "MalformedQueryException"

    @property
    def query_compile_error(self) -> dict[str, Any] | None:
        return self.response.get("queryCompileError")


class OperationAbortedException(CloudWatchLogsError):
    """Multiple concurrent requests to update the same resource were in conflict."""
    _ERROR_CODE = "OperationAbortedException"


class ResourceAlreadyExistsException(CloudWatchLogsError):
    """The specified resource already exists."""
    _ERROR_CODE = "ResourceAlreadyExistsException"


class ResourceNotFoundException(CloudWatchLogsError):
    """The specified resource does not exist."""
    _ERROR_CODE = "ResourceNotFoundException"


class ServiceQuotaExceededException(CloudWatchLogsError):
    """This request exceeds a service quota."""
    _ERROR_CODE = "ServiceQuotaExceededException"


class ServiceUnavailableException(CloudWatchLogsError):
    """The service cannot complete the request."""
    _ERROR_CODE = "ServiceUnavailableException"


class SessionStreamingException(CloudWatchLogsError):
    """This exception is returned if an unknown error occurs during a Live Tail session."""
    _ERROR_CODE = "SessionStreamingException"


class SessionTimeoutException(CloudWatchLogsError):
    """This exception is returned in a Live Tail stream when the Live Tail session times
    out. Live Tail sessions time out after three hours.
    """

    _ERROR_CODE = "SessionTimeoutException"


class ThrottlingException(CloudWatchLogsError):
    """The request was throttled because of quota limits."""
    _ERROR_CODE = "ThrottlingException"


class TooManyTagsException(CloudWatchLogsError):
    """A resource can have no more than 50 tags."""
    _ERROR_CODE = "TooManyTagsException"

    @property
    def resource_name(self) -> str | None:
        """The name of the resource."""
        return self.response.get("resourceName")


class UnrecognizedClientException(CloudWatchLogsError):
    """The most likely cause is an Amazon Web Services access key ID or secret key that's
    not valid.
    """

    _ERROR_CODE = "UnrecognizedClientException"


class ValidationException(CloudWatchLogsError):
    """One of the parameters for the request is not valid."""
    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[CloudWatchLogsError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "DataAlreadyAcceptedException": DataAlreadyAcceptedException,
    "InternalServerException": InternalServerException,
    "InternalStreamingException": InternalStreamingException,
    "InvalidOperationException": InvalidOperationException,
    "InvalidParameterException": InvalidParameterException,
    "InvalidSequenceTokenException": InvalidSequenceTokenException,
    "LimitExceededException": LimitExceededException,
    "MalformedQueryException": MalformedQueryException,
    "OperationAbortedException": OperationAbortedException,
    "ResourceAlreadyExistsException": ResourceAlreadyExistsException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ServiceUnavailableException": ServiceUnavailableException,
    "SessionStreamingException": SessionStreamingException,
    "SessionTimeoutException": SessionTimeoutException,
    "ThrottlingException": ThrottlingException,
    "TooManyTagsException": TooManyTagsException,
    "UnrecognizedClientException": UnrecognizedClientException,
    "ValidationException": ValidationException,
}
