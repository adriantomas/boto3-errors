# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class BedrockAgentCoreError(Boto3Error):
    _SERVICE = "bedrock-agentcore"


class AccessDeniedException(BedrockAgentCoreError):
    """The exception that occurs when you do not have sufficient permissions to perform an
    action. Verify that your IAM policy includes the necessary permissions for the
    operation you are trying to perform.
    """

    _ERROR_CODE = "AccessDeniedException"


class ConflictException(BedrockAgentCoreError):
    """The exception that occurs when the request conflicts with the current state of the
    resource. This can happen when trying to modify a resource that is currently being
    modified by another request, or when trying to create a resource that already
    exists.
    """

    _ERROR_CODE = "ConflictException"


class DuplicateIdException(BedrockAgentCoreError):
    """An exception thrown when attempting to create a resource with an identifier that
    already exists.
    """

    _ERROR_CODE = "DuplicateIdException"


class InternalServerException(BedrockAgentCoreError):
    """The exception that occurs when the service encounters an unexpected internal error.
    This is a temporary condition that will resolve itself with retries. We recommend
    implementing exponential backoff retry logic in your application.
    """

    _ERROR_CODE = "InternalServerException"


class InvalidInputException(BedrockAgentCoreError):
    """The input fails to satisfy the constraints specified by AgentCore. Check your input
    values and try again.
    """

    _ERROR_CODE = "InvalidInputException"


class ResourceNotFoundException(BedrockAgentCoreError):
    """The exception that occurs when the specified resource does not exist. This can
    happen when using an invalid identifier or when trying to access a resource that has
    been deleted.
    """

    _ERROR_CODE = "ResourceNotFoundException"


class RetryableConflictException(BedrockAgentCoreError):
    """The exception that occurs when there is a retryable conflict performing an
    operation. This is a temporary condition that may resolve itself with retries. We
    recommend implementing exponential backoff retry logic in your application.
    """

    _ERROR_CODE = "RetryableConflictException"


class RuntimeClientError(BedrockAgentCoreError):
    """The exception that occurs when there is an error in the runtime client. This can
    happen due to network issues, invalid configuration, or other client-side problems.
    Check the error message for specific details about the error.
    """

    _ERROR_CODE = "RuntimeClientError"


class ServiceException(BedrockAgentCoreError):
    """The service encountered an internal error. Try your request again later."""
    _ERROR_CODE = "ServiceException"


class ServiceQuotaExceededException(BedrockAgentCoreError):
    """The exception that occurs when the request would cause a service quota to be
    exceeded. Review your service quotas and either reduce your request rate or request
    a quota increase.
    """

    _ERROR_CODE = "ServiceQuotaExceededException"


class ThrottledException(BedrockAgentCoreError):
    """The request was denied due to request throttling. Reduce the frequency of requests
    and try again.
    """

    _ERROR_CODE = "ThrottledException"


class ThrottlingException(BedrockAgentCoreError):
    """The exception that occurs when the request was denied due to request throttling.
    This happens when you exceed the allowed request rate for an operation. Reduce the
    frequency of requests or implement exponential backoff retry logic in your
    application.
    """

    _ERROR_CODE = "ThrottlingException"


class UnauthorizedException(BedrockAgentCoreError):
    """This exception is thrown when the JWT bearer token is invalid or not found for OAuth
    bearer token based access
    """

    _ERROR_CODE = "UnauthorizedException"


class ValidationException(BedrockAgentCoreError):
    """The exception that occurs when the input fails to satisfy the constraints specified
    by the service. Check the error message for details about which input parameter is
    invalid and correct your request.
    """

    _ERROR_CODE = "ValidationException"

    @property
    def reason(self) -> str | None:
        return self.response.get("reason")

    @property
    def field_list(self) -> list[Any] | None:
        return self.response.get("fieldList")


EXCEPTIONS: dict[str, type[BedrockAgentCoreError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "DuplicateIdException": DuplicateIdException,
    "InternalServerException": InternalServerException,
    "InvalidInputException": InvalidInputException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "RetryableConflictException": RetryableConflictException,
    "RuntimeClientError": RuntimeClientError,
    "ServiceException": ServiceException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottledException": ThrottledException,
    "ThrottlingException": ThrottlingException,
    "UnauthorizedException": UnauthorizedException,
    "ValidationException": ValidationException,
}
