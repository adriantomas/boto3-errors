# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class HealthLakeError(Boto3Error):
    _SERVICE = "healthlake"


class AccessDeniedException(HealthLakeError):
    """Access is denied. Your account is not authorized to perform this operation."""
    _ERROR_CODE = "AccessDeniedException"


class AgentMessageOutOfContextException(HealthLakeError):
    """The agent message does not fit within the current conversation context. Start a new
    conversation or provide a message that relates to the current profile customization
    session.
    """

    _ERROR_CODE = "AgentMessageOutOfContextException"


class ConflictException(HealthLakeError):
    """The data store is in a transition state and the user requested action cannot be
    performed.
    """

    _ERROR_CODE = "ConflictException"


class ConversationNotFoundException(HealthLakeError):
    """The specified conversation identifier does not exist. Verify the conversation ID or
    omit it to start a new conversation.
    """

    _ERROR_CODE = "ConversationNotFoundException"


class FailedDependencyException(HealthLakeError):
    """A dependent service failed to fulfill the request."""
    _ERROR_CODE = "FailedDependencyException"


class InternalServerException(HealthLakeError):
    """An unknown internal error occurred in the service."""
    _ERROR_CODE = "InternalServerException"


class NotImplementedOperationException(HealthLakeError):
    """The requested operation is not yet available. Check the service documentation for a
    list of supported operations.
    """

    _ERROR_CODE = "NotImplementedOperationException"


class ResourceNotFoundException(HealthLakeError):
    """The requested data store was not found."""
    _ERROR_CODE = "ResourceNotFoundException"


class ServiceQuotaExceededException(HealthLakeError):
    """The request exceeds the service quota."""
    _ERROR_CODE = "ServiceQuotaExceededException"


class ThrottlingException(HealthLakeError):
    """The user has exceeded their maximum number of allowed calls to the given API."""
    _ERROR_CODE = "ThrottlingException"


class UnauthorizedException(HealthLakeError):
    """You are not authorized to make this request. Verify that your AWS credentials are
    valid and that you have the required permissions.
    """

    _ERROR_CODE = "UnauthorizedException"


class UnsupportedMIMETypeException(HealthLakeError):
    """The content type in your request is not supported. Use a supported content type for
    this operation.
    """

    _ERROR_CODE = "UnsupportedMIMETypeException"


class ValidationException(HealthLakeError):
    """The user input parameter was invalid."""
    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[HealthLakeError]] = {
    "AccessDeniedException": AccessDeniedException,
    "AgentMessageOutOfContextException": AgentMessageOutOfContextException,
    "ConflictException": ConflictException,
    "ConversationNotFoundException": ConversationNotFoundException,
    "FailedDependencyException": FailedDependencyException,
    "InternalServerException": InternalServerException,
    "NotImplementedOperationException": NotImplementedOperationException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "UnauthorizedException": UnauthorizedException,
    "UnsupportedMIMETypeException": UnsupportedMIMETypeException,
    "ValidationException": ValidationException,
}
