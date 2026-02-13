# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class WorkDocsError(Boto3Error):
    _SERVICE = "workdocs"


class ConcurrentModificationException(WorkDocsError):
    """The resource hierarchy is changing."""
    _ERROR_CODE = "ConcurrentModificationException"


class ConflictingOperationException(WorkDocsError):
    """Another operation is in progress on the resource that conflicts with the current
    operation.
    """

    _ERROR_CODE = "ConflictingOperationException"


class CustomMetadataLimitExceededException(WorkDocsError):
    """The limit has been reached on the number of custom properties for the specified
    resource.
    """

    _ERROR_CODE = "CustomMetadataLimitExceededException"


class DeactivatingLastSystemUserException(WorkDocsError):
    """The last user in the organization is being deactivated."""
    _ERROR_CODE = "DeactivatingLastSystemUserException"


class DocumentLockedForCommentsException(WorkDocsError):
    """This exception is thrown when the document is locked for comments and user tries to
    create or delete a comment on that document.
    """

    _ERROR_CODE = "DocumentLockedForCommentsException"


class DraftUploadOutOfSyncException(WorkDocsError):
    """This exception is thrown when a valid checkout ID is not presented on document
    version upload calls for a document that has been checked out from Web client.
    """

    _ERROR_CODE = "DraftUploadOutOfSyncException"


class EntityAlreadyExistsException(WorkDocsError):
    """The resource already exists."""
    _ERROR_CODE = "EntityAlreadyExistsException"


class EntityNotExistsException(WorkDocsError):
    """The resource does not exist."""
    _ERROR_CODE = "EntityNotExistsException"

    @property
    def entity_ids(self) -> list[Any] | None:
        """The IDs of the non-existent resources."""
        return self.response.get("EntityIds")


class FailedDependencyException(WorkDocsError):
    """The Directory Service cannot reach an on-premises instance. Or a dependency under
    the control of the organization is failing, such as a connected Active Directory.
    """

    _ERROR_CODE = "FailedDependencyException"


class IllegalUserStateException(WorkDocsError):
    """The user is undergoing transfer of ownership."""
    _ERROR_CODE = "IllegalUserStateException"


class InvalidArgumentException(WorkDocsError):
    """The pagination marker or limit fields are not valid."""
    _ERROR_CODE = "InvalidArgumentException"


class InvalidCommentOperationException(WorkDocsError):
    """The requested operation is not allowed on the specified comment object."""
    _ERROR_CODE = "InvalidCommentOperationException"


class InvalidOperationException(WorkDocsError):
    """The operation is invalid."""
    _ERROR_CODE = "InvalidOperationException"


class InvalidPasswordException(WorkDocsError):
    """The password is invalid."""
    _ERROR_CODE = "InvalidPasswordException"


class LimitExceededException(WorkDocsError):
    """The maximum of 100,000 files and folders under the parent folder has been exceeded."""
    _ERROR_CODE = "LimitExceededException"


class ProhibitedStateException(WorkDocsError):
    """The specified document version is not in the INITIALIZED state."""
    _ERROR_CODE = "ProhibitedStateException"


class RequestedEntityTooLargeException(WorkDocsError):
    """The response is too large to return. The request must include a filter to reduce the
    size of the response.
    """

    _ERROR_CODE = "RequestedEntityTooLargeException"


class ResourceAlreadyCheckedOutException(WorkDocsError):
    """The resource is already checked out."""
    _ERROR_CODE = "ResourceAlreadyCheckedOutException"


class ServiceUnavailableException(WorkDocsError):
    """One or more of the dependencies is unavailable."""
    _ERROR_CODE = "ServiceUnavailableException"


class StorageLimitExceededException(WorkDocsError):
    """The storage limit has been exceeded."""
    _ERROR_CODE = "StorageLimitExceededException"


class StorageLimitWillExceedException(WorkDocsError):
    """The storage limit will be exceeded."""
    _ERROR_CODE = "StorageLimitWillExceedException"


class TooManyLabelsException(WorkDocsError):
    """The limit has been reached on the number of labels for the specified resource."""
    _ERROR_CODE = "TooManyLabelsException"


class TooManySubscriptionsException(WorkDocsError):
    """You've reached the limit on the number of subscriptions for the WorkDocs instance."""
    _ERROR_CODE = "TooManySubscriptionsException"


class UnauthorizedOperationException(WorkDocsError):
    """The operation is not permitted."""
    _ERROR_CODE = "UnauthorizedOperationException"


class UnauthorizedResourceAccessException(WorkDocsError):
    """The caller does not have access to perform the action on the resource."""
    _ERROR_CODE = "UnauthorizedResourceAccessException"


EXCEPTIONS: dict[str, type[WorkDocsError]] = {
    "ConcurrentModificationException": ConcurrentModificationException,
    "ConflictingOperationException": ConflictingOperationException,
    "CustomMetadataLimitExceededException": CustomMetadataLimitExceededException,
    "DeactivatingLastSystemUserException": DeactivatingLastSystemUserException,
    "DocumentLockedForCommentsException": DocumentLockedForCommentsException,
    "DraftUploadOutOfSyncException": DraftUploadOutOfSyncException,
    "EntityAlreadyExistsException": EntityAlreadyExistsException,
    "EntityNotExistsException": EntityNotExistsException,
    "FailedDependencyException": FailedDependencyException,
    "IllegalUserStateException": IllegalUserStateException,
    "InvalidArgumentException": InvalidArgumentException,
    "InvalidCommentOperationException": InvalidCommentOperationException,
    "InvalidOperationException": InvalidOperationException,
    "InvalidPasswordException": InvalidPasswordException,
    "LimitExceededException": LimitExceededException,
    "ProhibitedStateException": ProhibitedStateException,
    "RequestedEntityTooLargeException": RequestedEntityTooLargeException,
    "ResourceAlreadyCheckedOutException": ResourceAlreadyCheckedOutException,
    "ServiceUnavailableException": ServiceUnavailableException,
    "StorageLimitExceededException": StorageLimitExceededException,
    "StorageLimitWillExceedException": StorageLimitWillExceedException,
    "TooManyLabelsException": TooManyLabelsException,
    "TooManySubscriptionsException": TooManySubscriptionsException,
    "UnauthorizedOperationException": UnauthorizedOperationException,
    "UnauthorizedResourceAccessException": UnauthorizedResourceAccessException,
}
