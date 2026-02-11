# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class CloudDirectoryError(Boto3Error):
    _SERVICE = "clouddirectory"


class AccessDeniedException(CloudDirectoryError):
    """Access denied or directory not found. Either you don't have permissions for this
    directory or the directory does not exist. Try calling ListDirectories and check
    your permissions.
    """

    _ERROR_CODE = "AccessDeniedException"


class BatchWriteException(CloudDirectoryError):
    """A `BatchWrite` exception has occurred."""
    _ERROR_CODE = "BatchWriteException"

    @property
    def index(self) -> int | None:
        return self.response.get("Index")

    @property
    def type(self) -> str | None:
        return self.response.get("Type")


class CannotListParentOfRootException(CloudDirectoryError):
    """Cannot list the parents of a Directory root."""
    _ERROR_CODE = "CannotListParentOfRootException"


class DirectoryAlreadyExistsException(CloudDirectoryError):
    """Indicates that a Directory could not be created due to a naming conflict. Choose a
    different name and try again.
    """

    _ERROR_CODE = "DirectoryAlreadyExistsException"


class DirectoryDeletedException(CloudDirectoryError):
    """A directory that has been deleted and to which access has been attempted. Note: The
    requested resource will eventually cease to exist.
    """

    _ERROR_CODE = "DirectoryDeletedException"


class DirectoryNotDisabledException(CloudDirectoryError):
    """An operation can only operate on a disabled directory."""
    _ERROR_CODE = "DirectoryNotDisabledException"


class DirectoryNotEnabledException(CloudDirectoryError):
    """Operations are only permitted on enabled directories."""
    _ERROR_CODE = "DirectoryNotEnabledException"


class FacetAlreadyExistsException(CloudDirectoryError):
    """A facet with the same name already exists."""
    _ERROR_CODE = "FacetAlreadyExistsException"


class FacetInUseException(CloudDirectoryError):
    """Occurs when deleting a facet that contains an attribute that is a target to an
    attribute reference in a different facet.
    """

    _ERROR_CODE = "FacetInUseException"


class FacetNotFoundException(CloudDirectoryError):
    """The specified Facet could not be found."""
    _ERROR_CODE = "FacetNotFoundException"


class FacetValidationException(CloudDirectoryError):
    """The Facet that you provided was not well formed or could not be validated with the
    schema.
    """

    _ERROR_CODE = "FacetValidationException"


class IncompatibleSchemaException(CloudDirectoryError):
    """Indicates a failure occurred while performing a check for backward compatibility
    between the specified schema and the schema that is currently applied to the
    directory.
    """

    _ERROR_CODE = "IncompatibleSchemaException"


class IndexedAttributeMissingException(CloudDirectoryError):
    """An object has been attempted to be attached to an object that does not have the
    appropriate attribute value.
    """

    _ERROR_CODE = "IndexedAttributeMissingException"


class InternalServiceException(CloudDirectoryError):
    """Indicates a problem that must be resolved by Amazon Web Services. This might be a
    transient error in which case you can retry your request until it succeeds.
    Otherwise, go to the AWS Service Health Dashboard site to see if there are any
    operational issues with the service.
    """

    _ERROR_CODE = "InternalServiceException"


class InvalidArnException(CloudDirectoryError):
    """Indicates that the provided ARN value is not valid."""
    _ERROR_CODE = "InvalidArnException"


class InvalidAttachmentException(CloudDirectoryError):
    """Indicates that an attempt to make an attachment was invalid. For example, attaching
    two nodes with a link type that is not applicable to the nodes or attempting to
    apply a schema to a directory a second time.
    """

    _ERROR_CODE = "InvalidAttachmentException"


class InvalidFacetUpdateException(CloudDirectoryError):
    """An attempt to modify a Facet resulted in an invalid schema exception."""
    _ERROR_CODE = "InvalidFacetUpdateException"


class InvalidNextTokenException(CloudDirectoryError):
    """Indicates that the `NextToken` value is not valid."""
    _ERROR_CODE = "InvalidNextTokenException"


class InvalidRuleException(CloudDirectoryError):
    """Occurs when any of the rule parameter keys or values are invalid."""
    _ERROR_CODE = "InvalidRuleException"


class InvalidSchemaDocException(CloudDirectoryError):
    """Indicates that the provided `SchemaDoc` value is not valid."""
    _ERROR_CODE = "InvalidSchemaDocException"


class InvalidTaggingRequestException(CloudDirectoryError):
    """Can occur for multiple reasons such as when you tag a resource that doesn’t exist or
    if you specify a higher number of tags for a resource than the allowed limit.
    Allowed limit is 50 tags per resource.
    """

    _ERROR_CODE = "InvalidTaggingRequestException"


class LimitExceededException(CloudDirectoryError):
    """Indicates that limits are exceeded. See Limits for more information."""
    _ERROR_CODE = "LimitExceededException"


class LinkNameAlreadyInUseException(CloudDirectoryError):
    """Indicates that a link could not be created due to a naming conflict. Choose a
    different name and then try again.
    """

    _ERROR_CODE = "LinkNameAlreadyInUseException"


class NotIndexException(CloudDirectoryError):
    """Indicates that the requested operation can only operate on index objects."""
    _ERROR_CODE = "NotIndexException"


class NotNodeException(CloudDirectoryError):
    """Occurs when any invalid operations are performed on an object that is not a node,
    such as calling `ListObjectChildren` for a leaf node object.
    """

    _ERROR_CODE = "NotNodeException"


class NotPolicyException(CloudDirectoryError):
    """Indicates that the requested operation can only operate on policy objects."""
    _ERROR_CODE = "NotPolicyException"


class ObjectAlreadyDetachedException(CloudDirectoryError):
    """Indicates that the object is not attached to the index."""
    _ERROR_CODE = "ObjectAlreadyDetachedException"


class ObjectNotDetachedException(CloudDirectoryError):
    """Indicates that the requested operation cannot be completed because the object has
    not been detached from the tree.
    """

    _ERROR_CODE = "ObjectNotDetachedException"


class ResourceNotFoundException(CloudDirectoryError):
    """The specified resource could not be found."""
    _ERROR_CODE = "ResourceNotFoundException"


class RetryableConflictException(CloudDirectoryError):
    """Occurs when a conflict with a previous successful write is detected. For example, if
    a write operation occurs on an object and then an attempt is made to read the object
    using “SERIALIZABLE” consistency, this exception may result. This generally occurs
    when the previous write did not have time to propagate to the host serving the
    current request. A retry (with appropriate backoff logic) is the recommended
    response to this exception.
    """

    _ERROR_CODE = "RetryableConflictException"


class SchemaAlreadyExistsException(CloudDirectoryError):
    """Indicates that a schema could not be created due to a naming conflict. Please select
    a different name and then try again.
    """

    _ERROR_CODE = "SchemaAlreadyExistsException"


class SchemaAlreadyPublishedException(CloudDirectoryError):
    """Indicates that a schema is already published."""
    _ERROR_CODE = "SchemaAlreadyPublishedException"


class StillContainsLinksException(CloudDirectoryError):
    """The object could not be deleted because links still exist. Remove the links and then
    try the operation again.
    """

    _ERROR_CODE = "StillContainsLinksException"


class UnsupportedIndexTypeException(CloudDirectoryError):
    """Indicates that the requested index type is not supported."""
    _ERROR_CODE = "UnsupportedIndexTypeException"


class ValidationException(CloudDirectoryError):
    """Indicates that your request is malformed in some manner. See the exception message."""
    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[CloudDirectoryError]] = {
    "AccessDeniedException": AccessDeniedException,
    "BatchWriteException": BatchWriteException,
    "CannotListParentOfRootException": CannotListParentOfRootException,
    "DirectoryAlreadyExistsException": DirectoryAlreadyExistsException,
    "DirectoryDeletedException": DirectoryDeletedException,
    "DirectoryNotDisabledException": DirectoryNotDisabledException,
    "DirectoryNotEnabledException": DirectoryNotEnabledException,
    "FacetAlreadyExistsException": FacetAlreadyExistsException,
    "FacetInUseException": FacetInUseException,
    "FacetNotFoundException": FacetNotFoundException,
    "FacetValidationException": FacetValidationException,
    "IncompatibleSchemaException": IncompatibleSchemaException,
    "IndexedAttributeMissingException": IndexedAttributeMissingException,
    "InternalServiceException": InternalServiceException,
    "InvalidArnException": InvalidArnException,
    "InvalidAttachmentException": InvalidAttachmentException,
    "InvalidFacetUpdateException": InvalidFacetUpdateException,
    "InvalidNextTokenException": InvalidNextTokenException,
    "InvalidRuleException": InvalidRuleException,
    "InvalidSchemaDocException": InvalidSchemaDocException,
    "InvalidTaggingRequestException": InvalidTaggingRequestException,
    "LimitExceededException": LimitExceededException,
    "LinkNameAlreadyInUseException": LinkNameAlreadyInUseException,
    "NotIndexException": NotIndexException,
    "NotNodeException": NotNodeException,
    "NotPolicyException": NotPolicyException,
    "ObjectAlreadyDetachedException": ObjectAlreadyDetachedException,
    "ObjectNotDetachedException": ObjectNotDetachedException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "RetryableConflictException": RetryableConflictException,
    "SchemaAlreadyExistsException": SchemaAlreadyExistsException,
    "SchemaAlreadyPublishedException": SchemaAlreadyPublishedException,
    "StillContainsLinksException": StillContainsLinksException,
    "UnsupportedIndexTypeException": UnsupportedIndexTypeException,
    "ValidationException": ValidationException,
}
