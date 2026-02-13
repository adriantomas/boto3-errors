# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class LexRuntimeServiceError(Boto3Error):
    _SERVICE = "lex-runtime"


class BadGatewayException(LexRuntimeServiceError):
    """Either the Amazon Lex bot is still building, or one of the dependent services
    (Amazon Polly, AWS Lambda) failed with an internal service error.
    """

    _ERROR_CODE = "BadGatewayException"


class BadRequestException(LexRuntimeServiceError):
    """Request validation failed, there is no usable message in the context, or the bot
    build failed, is still in progress, or contains unbuilt changes.
    """

    _ERROR_CODE = "BadRequestException"


class ConflictException(LexRuntimeServiceError):
    """Two clients are using the same AWS account, Amazon Lex bot, and user ID."""
    _ERROR_CODE = "ConflictException"


class DependencyFailedException(LexRuntimeServiceError):
    """One of the dependencies, such as AWS Lambda or Amazon Polly, threw an exception. For
    example,

    - If Amazon Lex does not have sufficient permissions to call a Lambda function.
    - If a Lambda function takes longer than 30 seconds to execute.
    - If a fulfillment Lambda function returns a `Delegate` dialog action without
      removing any slot values.
    """

    _ERROR_CODE = "DependencyFailedException"


class InternalFailureException(LexRuntimeServiceError):
    """Internal service error. Retry the call."""
    _ERROR_CODE = "InternalFailureException"


class LimitExceededException(LexRuntimeServiceError):
    """Exceeded a limit."""
    _ERROR_CODE = "LimitExceededException"

    @property
    def retry_after_seconds(self) -> str | None:
        return self.response.get("retryAfterSeconds")


class LoopDetectedException(LexRuntimeServiceError):
    """This exception is not used."""
    _ERROR_CODE = "LoopDetectedException"


class NotAcceptableException(LexRuntimeServiceError):
    """The accept header in the request does not have a valid value."""
    _ERROR_CODE = "NotAcceptableException"


class NotFoundException(LexRuntimeServiceError):
    """The resource (such as the Amazon Lex bot or an alias) that is referred to is not
    found.
    """

    _ERROR_CODE = "NotFoundException"


class RequestTimeoutException(LexRuntimeServiceError):
    """The input speech is too long."""
    _ERROR_CODE = "RequestTimeoutException"


class UnsupportedMediaTypeException(LexRuntimeServiceError):
    """The Content-Type header (`PostContent` API) has an invalid value."""
    _ERROR_CODE = "UnsupportedMediaTypeException"


EXCEPTIONS: dict[str, type[LexRuntimeServiceError]] = {
    "BadGatewayException": BadGatewayException,
    "BadRequestException": BadRequestException,
    "ConflictException": ConflictException,
    "DependencyFailedException": DependencyFailedException,
    "InternalFailureException": InternalFailureException,
    "LimitExceededException": LimitExceededException,
    "LoopDetectedException": LoopDetectedException,
    "NotAcceptableException": NotAcceptableException,
    "NotFoundException": NotFoundException,
    "RequestTimeoutException": RequestTimeoutException,
    "UnsupportedMediaTypeException": UnsupportedMediaTypeException,
}
