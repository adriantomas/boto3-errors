# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class CodeStarconnectionsError(Boto3Error):
    _SERVICE = "codestar-connections"


class AccessDeniedException(CodeStarconnectionsError):
    """You do not have sufficient access to perform this action."""
    _ERROR_CODE = "AccessDeniedException"


class ConcurrentModificationException(CodeStarconnectionsError):
    """Exception thrown as a result of concurrent modification to an application. For
    example, two individuals attempting to edit the same application at the same time.
    """

    _ERROR_CODE = "ConcurrentModificationException"


class ConditionalCheckFailedException(CodeStarconnectionsError):
    """The conditional check failed. Try again later."""
    _ERROR_CODE = "ConditionalCheckFailedException"


class ConflictException(CodeStarconnectionsError):
    """Two conflicting operations have been made on the same resource."""
    _ERROR_CODE = "ConflictException"


class InternalServerException(CodeStarconnectionsError):
    """Received an internal server exception. Try again later."""
    _ERROR_CODE = "InternalServerException"


class InvalidInputException(CodeStarconnectionsError):
    """The input is not valid. Verify that the action is typed correctly."""
    _ERROR_CODE = "InvalidInputException"


class LimitExceededException(CodeStarconnectionsError):
    """Exceeded the maximum limit for connections."""
    _ERROR_CODE = "LimitExceededException"


class ResourceAlreadyExistsException(CodeStarconnectionsError):
    """Unable to create resource. Resource already exists."""
    _ERROR_CODE = "ResourceAlreadyExistsException"


class ResourceNotFoundException(CodeStarconnectionsError):
    """Resource not found. Verify the connection resource ARN and try again."""
    _ERROR_CODE = "ResourceNotFoundException"


class ResourceUnavailableException(CodeStarconnectionsError):
    """Resource not found. Verify the ARN for the host resource and try again."""
    _ERROR_CODE = "ResourceUnavailableException"


class RetryLatestCommitFailedException(CodeStarconnectionsError):
    """Retrying the latest commit failed. Try again later."""
    _ERROR_CODE = "RetryLatestCommitFailedException"


class SyncBlockerDoesNotExistException(CodeStarconnectionsError):
    """Unable to continue. The sync blocker does not exist."""
    _ERROR_CODE = "SyncBlockerDoesNotExistException"


class SyncConfigurationStillExistsException(CodeStarconnectionsError):
    """Unable to continue. The sync blocker still exists."""
    _ERROR_CODE = "SyncConfigurationStillExistsException"


class ThrottlingException(CodeStarconnectionsError):
    """The request was denied due to request throttling."""
    _ERROR_CODE = "ThrottlingException"


class UnsupportedOperationException(CodeStarconnectionsError):
    """The operation is not supported. Check the connection status and try again."""
    _ERROR_CODE = "UnsupportedOperationException"


class UnsupportedProviderTypeException(CodeStarconnectionsError):
    """The specified provider type is not supported for connections."""
    _ERROR_CODE = "UnsupportedProviderTypeException"


class UpdateOutOfSyncException(CodeStarconnectionsError):
    """The update is out of sync. Try syncing again."""
    _ERROR_CODE = "UpdateOutOfSyncException"


EXCEPTIONS: dict[str, type[CodeStarconnectionsError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConcurrentModificationException": ConcurrentModificationException,
    "ConditionalCheckFailedException": ConditionalCheckFailedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "InvalidInputException": InvalidInputException,
    "LimitExceededException": LimitExceededException,
    "ResourceAlreadyExistsException": ResourceAlreadyExistsException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ResourceUnavailableException": ResourceUnavailableException,
    "RetryLatestCommitFailedException": RetryLatestCommitFailedException,
    "SyncBlockerDoesNotExistException": SyncBlockerDoesNotExistException,
    "SyncConfigurationStillExistsException": SyncConfigurationStillExistsException,
    "ThrottlingException": ThrottlingException,
    "UnsupportedOperationException": UnsupportedOperationException,
    "UnsupportedProviderTypeException": UnsupportedProviderTypeException,
    "UpdateOutOfSyncException": UpdateOutOfSyncException,
}
