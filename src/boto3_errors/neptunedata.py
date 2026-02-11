# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class neptunedataError(Boto3Error):
    _SERVICE = "neptunedata"


class AccessDeniedException(neptunedataError):
    """Raised in case of an authentication or authorization failure."""
    _ERROR_CODE = "AccessDeniedException"

    @property
    def detailed_message(self) -> str | None:
        """A detailed message describing the problem."""
        return self.response.get("detailedMessage")

    @property
    def request_id(self) -> str | None:
        """The ID of the request in question."""
        return self.response.get("requestId")

    @property
    def code(self) -> str | None:
        """The HTTP status code returned with the exception."""
        return self.response.get("code")


class BadRequestException(neptunedataError):
    """Raised when a request is submitted that cannot be processed."""
    _ERROR_CODE = "BadRequestException"

    @property
    def detailed_message(self) -> str | None:
        """A detailed message describing the problem."""
        return self.response.get("detailedMessage")

    @property
    def request_id(self) -> str | None:
        """The ID of the bad request."""
        return self.response.get("requestId")

    @property
    def code(self) -> str | None:
        """The HTTP status code returned with the exception."""
        return self.response.get("code")


class BulkLoadIdNotFoundException(neptunedataError):
    """Raised when a specified bulk-load job ID cannot be found."""
    _ERROR_CODE = "BulkLoadIdNotFoundException"

    @property
    def detailed_message(self) -> str | None:
        """A detailed message describing the problem."""
        return self.response.get("detailedMessage")

    @property
    def request_id(self) -> str | None:
        """The bulk-load job ID that could not be found."""
        return self.response.get("requestId")

    @property
    def code(self) -> str | None:
        """The HTTP status code returned with the exception."""
        return self.response.get("code")


class CancelledByUserException(neptunedataError):
    """Raised when a user cancelled a request."""
    _ERROR_CODE = "CancelledByUserException"

    @property
    def detailed_message(self) -> str | None:
        """A detailed message describing the problem."""
        return self.response.get("detailedMessage")

    @property
    def request_id(self) -> str | None:
        """The ID of the request in question."""
        return self.response.get("requestId")

    @property
    def code(self) -> str | None:
        """The HTTP status code returned with the exception."""
        return self.response.get("code")


class ClientTimeoutException(neptunedataError):
    """Raised when a request timed out in the client."""
    _ERROR_CODE = "ClientTimeoutException"

    @property
    def detailed_message(self) -> str | None:
        """A detailed message describing the problem."""
        return self.response.get("detailedMessage")

    @property
    def request_id(self) -> str | None:
        """The ID of the request in question."""
        return self.response.get("requestId")

    @property
    def code(self) -> str | None:
        """The HTTP status code returned with the exception."""
        return self.response.get("code")


class ConcurrentModificationException(neptunedataError):
    """Raised when a request attempts to modify data that is concurrently being modified by
    another process.
    """

    _ERROR_CODE = "ConcurrentModificationException"

    @property
    def detailed_message(self) -> str | None:
        """A detailed message describing the problem."""
        return self.response.get("detailedMessage")

    @property
    def request_id(self) -> str | None:
        """The ID of the request in question."""
        return self.response.get("requestId")

    @property
    def code(self) -> str | None:
        """The HTTP status code returned with the exception."""
        return self.response.get("code")


class ConstraintViolationException(neptunedataError):
    """Raised when a value in a request field did not satisfy required constraints."""
    _ERROR_CODE = "ConstraintViolationException"

    @property
    def detailed_message(self) -> str | None:
        """A detailed message describing the problem."""
        return self.response.get("detailedMessage")

    @property
    def request_id(self) -> str | None:
        """The ID of the request in question."""
        return self.response.get("requestId")

    @property
    def code(self) -> str | None:
        """The HTTP status code returned with the exception."""
        return self.response.get("code")


class ExpiredStreamException(neptunedataError):
    """Raised when a request attempts to access an stream that has expired."""
    _ERROR_CODE = "ExpiredStreamException"

    @property
    def detailed_message(self) -> str | None:
        """A detailed message describing the problem."""
        return self.response.get("detailedMessage")

    @property
    def request_id(self) -> str | None:
        """The ID of the request in question."""
        return self.response.get("requestId")

    @property
    def code(self) -> str | None:
        """The HTTP status code returned with the exception."""
        return self.response.get("code")


class FailureByQueryException(neptunedataError):
    """Raised when a request fails."""
    _ERROR_CODE = "FailureByQueryException"

    @property
    def detailed_message(self) -> str | None:
        """A detailed message describing the problem."""
        return self.response.get("detailedMessage")

    @property
    def request_id(self) -> str | None:
        """The ID of the request in question."""
        return self.response.get("requestId")

    @property
    def code(self) -> str | None:
        """The HTTP status code returned with the exception."""
        return self.response.get("code")


class IllegalArgumentException(neptunedataError):
    """Raised when an argument in a request is not supported."""
    _ERROR_CODE = "IllegalArgumentException"

    @property
    def detailed_message(self) -> str | None:
        """A detailed message describing the problem."""
        return self.response.get("detailedMessage")

    @property
    def request_id(self) -> str | None:
        """The ID of the request in question."""
        return self.response.get("requestId")

    @property
    def code(self) -> str | None:
        """The HTTP status code returned with the exception."""
        return self.response.get("code")


class InternalFailureException(neptunedataError):
    """Raised when the processing of the request failed unexpectedly."""
    _ERROR_CODE = "InternalFailureException"

    @property
    def detailed_message(self) -> str | None:
        """A detailed message describing the problem."""
        return self.response.get("detailedMessage")

    @property
    def request_id(self) -> str | None:
        """The ID of the request in question."""
        return self.response.get("requestId")

    @property
    def code(self) -> str | None:
        """The HTTP status code returned with the exception."""
        return self.response.get("code")


class InvalidArgumentException(neptunedataError):
    """Raised when an argument in a request has an invalid value."""
    _ERROR_CODE = "InvalidArgumentException"

    @property
    def detailed_message(self) -> str | None:
        """A detailed message describing the problem."""
        return self.response.get("detailedMessage")

    @property
    def request_id(self) -> str | None:
        """The ID of the request in question."""
        return self.response.get("requestId")

    @property
    def code(self) -> str | None:
        """The HTTP status code returned with the exception."""
        return self.response.get("code")


class InvalidNumericDataException(neptunedataError):
    """Raised when invalid numerical data is encountered when servicing a request."""
    _ERROR_CODE = "InvalidNumericDataException"

    @property
    def detailed_message(self) -> str | None:
        """A detailed message describing the problem."""
        return self.response.get("detailedMessage")

    @property
    def request_id(self) -> str | None:
        """The ID of the request in question."""
        return self.response.get("requestId")

    @property
    def code(self) -> str | None:
        """The HTTP status code returned with the exception."""
        return self.response.get("code")


class InvalidParameterException(neptunedataError):
    """Raised when a parameter value is not valid."""
    _ERROR_CODE = "InvalidParameterException"

    @property
    def detailed_message(self) -> str | None:
        """A detailed message describing the problem."""
        return self.response.get("detailedMessage")

    @property
    def request_id(self) -> str | None:
        """The ID of the request that includes an invalid parameter."""
        return self.response.get("requestId")

    @property
    def code(self) -> str | None:
        """The HTTP status code returned with the exception."""
        return self.response.get("code")


class LoadUrlAccessDeniedException(neptunedataError):
    """Raised when access is denied to a specified load URL."""
    _ERROR_CODE = "LoadUrlAccessDeniedException"

    @property
    def detailed_message(self) -> str | None:
        """A detailed message describing the problem."""
        return self.response.get("detailedMessage")

    @property
    def request_id(self) -> str | None:
        """The ID of the request in question."""
        return self.response.get("requestId")

    @property
    def code(self) -> str | None:
        """The HTTP status code returned with the exception."""
        return self.response.get("code")


class MLResourceNotFoundException(neptunedataError):
    """Raised when a specified machine-learning resource could not be found."""
    _ERROR_CODE = "MLResourceNotFoundException"

    @property
    def detailed_message(self) -> str | None:
        """A detailed message describing the problem."""
        return self.response.get("detailedMessage")

    @property
    def request_id(self) -> str | None:
        """The ID of the request in question."""
        return self.response.get("requestId")

    @property
    def code(self) -> str | None:
        """The HTTP status code returned with the exception."""
        return self.response.get("code")


class MalformedQueryException(neptunedataError):
    """Raised when a query is submitted that is syntactically incorrect or does not pass
    additional validation.
    """

    _ERROR_CODE = "MalformedQueryException"

    @property
    def detailed_message(self) -> str | None:
        """A detailed message describing the problem."""
        return self.response.get("detailedMessage")

    @property
    def request_id(self) -> str | None:
        """The ID of the malformed query request."""
        return self.response.get("requestId")

    @property
    def code(self) -> str | None:
        """The HTTP status code returned with the exception."""
        return self.response.get("code")


class MemoryLimitExceededException(neptunedataError):
    """Raised when a request fails because of insufficient memory resources. The request
    can be retried.
    """

    _ERROR_CODE = "MemoryLimitExceededException"

    @property
    def detailed_message(self) -> str | None:
        """A detailed message describing the problem."""
        return self.response.get("detailedMessage")

    @property
    def request_id(self) -> str | None:
        """The ID of the request that failed."""
        return self.response.get("requestId")

    @property
    def code(self) -> str | None:
        """The HTTP status code returned with the exception."""
        return self.response.get("code")


class MethodNotAllowedException(neptunedataError):
    """Raised when the HTTP method used by a request is not supported by the endpoint being
    used.
    """

    _ERROR_CODE = "MethodNotAllowedException"

    @property
    def detailed_message(self) -> str | None:
        """A detailed message describing the problem."""
        return self.response.get("detailedMessage")

    @property
    def request_id(self) -> str | None:
        """The ID of the request in question."""
        return self.response.get("requestId")

    @property
    def code(self) -> str | None:
        """The HTTP status code returned with the exception."""
        return self.response.get("code")


class MissingParameterException(neptunedataError):
    """Raised when a required parameter is missing."""
    _ERROR_CODE = "MissingParameterException"

    @property
    def detailed_message(self) -> str | None:
        """A detailed message describing the problem."""
        return self.response.get("detailedMessage")

    @property
    def request_id(self) -> str | None:
        """The ID of the request in which the parameter is missing."""
        return self.response.get("requestId")

    @property
    def code(self) -> str | None:
        """The HTTP status code returned with the exception."""
        return self.response.get("code")


class ParsingException(neptunedataError):
    """Raised when a parsing issue is encountered."""
    _ERROR_CODE = "ParsingException"

    @property
    def detailed_message(self) -> str | None:
        """A detailed message describing the problem."""
        return self.response.get("detailedMessage")

    @property
    def request_id(self) -> str | None:
        """The ID of the request in question."""
        return self.response.get("requestId")

    @property
    def code(self) -> str | None:
        """The HTTP status code returned with the exception."""
        return self.response.get("code")


class PreconditionsFailedException(neptunedataError):
    """Raised when a precondition for processing a request is not satisfied."""
    _ERROR_CODE = "PreconditionsFailedException"

    @property
    def detailed_message(self) -> str | None:
        """A detailed message describing the problem."""
        return self.response.get("detailedMessage")

    @property
    def request_id(self) -> str | None:
        """The ID of the request in question."""
        return self.response.get("requestId")

    @property
    def code(self) -> str | None:
        """The HTTP status code returned with the exception."""
        return self.response.get("code")


class QueryLimitExceededException(neptunedataError):
    """Raised when the number of active queries exceeds what the server can process. The
    query in question can be retried when the system is less busy.
    """

    _ERROR_CODE = "QueryLimitExceededException"

    @property
    def detailed_message(self) -> str | None:
        """A detailed message describing the problem."""
        return self.response.get("detailedMessage")

    @property
    def request_id(self) -> str | None:
        """The ID of the request which exceeded the limit."""
        return self.response.get("requestId")

    @property
    def code(self) -> str | None:
        """The HTTP status code returned with the exception."""
        return self.response.get("code")


class QueryLimitException(neptunedataError):
    """Raised when the size of a query exceeds the system limit."""
    _ERROR_CODE = "QueryLimitException"

    @property
    def detailed_message(self) -> str | None:
        """A detailed message describing the problem."""
        return self.response.get("detailedMessage")

    @property
    def request_id(self) -> str | None:
        """The ID of the request that exceeded the limit."""
        return self.response.get("requestId")

    @property
    def code(self) -> str | None:
        """The HTTP status code returned with the exception."""
        return self.response.get("code")


class QueryTooLargeException(neptunedataError):
    """Raised when the body of a query is too large."""
    _ERROR_CODE = "QueryTooLargeException"

    @property
    def detailed_message(self) -> str | None:
        """A detailed message describing the problem."""
        return self.response.get("detailedMessage")

    @property
    def request_id(self) -> str | None:
        """The ID of the request that is too large."""
        return self.response.get("requestId")

    @property
    def code(self) -> str | None:
        """The HTTP status code returned with the exception."""
        return self.response.get("code")


class ReadOnlyViolationException(neptunedataError):
    """Raised when a request attempts to write to a read-only resource."""
    _ERROR_CODE = "ReadOnlyViolationException"

    @property
    def detailed_message(self) -> str | None:
        """A detailed message describing the problem."""
        return self.response.get("detailedMessage")

    @property
    def request_id(self) -> str | None:
        """The ID of the request in which the parameter is missing."""
        return self.response.get("requestId")

    @property
    def code(self) -> str | None:
        """The HTTP status code returned with the exception."""
        return self.response.get("code")


class S3Exception(neptunedataError):
    """Raised when there is a problem accessing Amazon S3."""
    _ERROR_CODE = "S3Exception"

    @property
    def detailed_message(self) -> str | None:
        """A detailed message describing the problem."""
        return self.response.get("detailedMessage")

    @property
    def request_id(self) -> str | None:
        """The ID of the request in question."""
        return self.response.get("requestId")

    @property
    def code(self) -> str | None:
        """The HTTP status code returned with the exception."""
        return self.response.get("code")


class ServerShutdownException(neptunedataError):
    """Raised when the server shuts down while processing a request."""
    _ERROR_CODE = "ServerShutdownException"

    @property
    def detailed_message(self) -> str | None:
        """A detailed message describing the problem."""
        return self.response.get("detailedMessage")

    @property
    def request_id(self) -> str | None:
        """The ID of the request in question."""
        return self.response.get("requestId")

    @property
    def code(self) -> str | None:
        """The HTTP status code returned with the exception."""
        return self.response.get("code")


class StatisticsNotAvailableException(neptunedataError):
    """Raised when statistics needed to satisfy a request are not available."""
    _ERROR_CODE = "StatisticsNotAvailableException"

    @property
    def detailed_message(self) -> str | None:
        """A detailed message describing the problem."""
        return self.response.get("detailedMessage")

    @property
    def request_id(self) -> str | None:
        """The ID of the request in question."""
        return self.response.get("requestId")

    @property
    def code(self) -> str | None:
        """The HTTP status code returned with the exception."""
        return self.response.get("code")


class StreamRecordsNotFoundException(neptunedataError):
    """Raised when stream records requested by a query cannot be found."""
    _ERROR_CODE = "StreamRecordsNotFoundException"

    @property
    def detailed_message(self) -> str | None:
        """A detailed message describing the problem."""
        return self.response.get("detailedMessage")

    @property
    def request_id(self) -> str | None:
        """The ID of the request in question."""
        return self.response.get("requestId")

    @property
    def code(self) -> str | None:
        """The HTTP status code returned with the exception."""
        return self.response.get("code")


class ThrottlingException(neptunedataError):
    """Raised when the rate of requests exceeds the maximum throughput. Requests can be
    retried after encountering this exception.
    """

    _ERROR_CODE = "ThrottlingException"

    @property
    def detailed_message(self) -> str | None:
        """A detailed message describing the problem."""
        return self.response.get("detailedMessage")

    @property
    def request_id(self) -> str | None:
        """The ID of the request that could not be processed for this reason."""
        return self.response.get("requestId")

    @property
    def code(self) -> str | None:
        """The HTTP status code returned with the exception."""
        return self.response.get("code")


class TimeLimitExceededException(neptunedataError):
    """Raised when the an operation exceeds the time limit allowed for it."""
    _ERROR_CODE = "TimeLimitExceededException"

    @property
    def detailed_message(self) -> str | None:
        """A detailed message describing the problem."""
        return self.response.get("detailedMessage")

    @property
    def request_id(self) -> str | None:
        """The ID of the request that could not be processed for this reason."""
        return self.response.get("requestId")

    @property
    def code(self) -> str | None:
        """The HTTP status code returned with the exception."""
        return self.response.get("code")


class TooManyRequestsException(neptunedataError):
    """Raised when the number of requests being processed exceeds the limit."""
    _ERROR_CODE = "TooManyRequestsException"

    @property
    def detailed_message(self) -> str | None:
        """A detailed message describing the problem."""
        return self.response.get("detailedMessage")

    @property
    def request_id(self) -> str | None:
        """The ID of the request that could not be processed for this reason."""
        return self.response.get("requestId")

    @property
    def code(self) -> str | None:
        """The HTTP status code returned with the exception."""
        return self.response.get("code")


class UnsupportedOperationException(neptunedataError):
    """Raised when a request attempts to initiate an operation that is not supported."""
    _ERROR_CODE = "UnsupportedOperationException"

    @property
    def detailed_message(self) -> str | None:
        """A detailed message describing the problem."""
        return self.response.get("detailedMessage")

    @property
    def request_id(self) -> str | None:
        """The ID of the request in question."""
        return self.response.get("requestId")

    @property
    def code(self) -> str | None:
        """The HTTP status code returned with the exception."""
        return self.response.get("code")


EXCEPTIONS: dict[str, type[neptunedataError]] = {
    "AccessDeniedException": AccessDeniedException,
    "BadRequestException": BadRequestException,
    "BulkLoadIdNotFoundException": BulkLoadIdNotFoundException,
    "CancelledByUserException": CancelledByUserException,
    "ClientTimeoutException": ClientTimeoutException,
    "ConcurrentModificationException": ConcurrentModificationException,
    "ConstraintViolationException": ConstraintViolationException,
    "ExpiredStreamException": ExpiredStreamException,
    "FailureByQueryException": FailureByQueryException,
    "IllegalArgumentException": IllegalArgumentException,
    "InternalFailureException": InternalFailureException,
    "InvalidArgumentException": InvalidArgumentException,
    "InvalidNumericDataException": InvalidNumericDataException,
    "InvalidParameterException": InvalidParameterException,
    "LoadUrlAccessDeniedException": LoadUrlAccessDeniedException,
    "MLResourceNotFoundException": MLResourceNotFoundException,
    "MalformedQueryException": MalformedQueryException,
    "MemoryLimitExceededException": MemoryLimitExceededException,
    "MethodNotAllowedException": MethodNotAllowedException,
    "MissingParameterException": MissingParameterException,
    "ParsingException": ParsingException,
    "PreconditionsFailedException": PreconditionsFailedException,
    "QueryLimitExceededException": QueryLimitExceededException,
    "QueryLimitException": QueryLimitException,
    "QueryTooLargeException": QueryTooLargeException,
    "ReadOnlyViolationException": ReadOnlyViolationException,
    "S3Exception": S3Exception,
    "ServerShutdownException": ServerShutdownException,
    "StatisticsNotAvailableException": StatisticsNotAvailableException,
    "StreamRecordsNotFoundException": StreamRecordsNotFoundException,
    "ThrottlingException": ThrottlingException,
    "TimeLimitExceededException": TimeLimitExceededException,
    "TooManyRequestsException": TooManyRequestsException,
    "UnsupportedOperationException": UnsupportedOperationException,
}
