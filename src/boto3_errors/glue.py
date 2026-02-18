# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class GlueError(Boto3Error):
    _SERVICE = "glue"


class AccessDeniedException(GlueError):
    """Access to a resource was denied."""
    _ERROR_CODE = "AccessDeniedException"


class AlreadyExistsException(GlueError):
    """A resource to be created or added already exists."""
    _ERROR_CODE = "AlreadyExistsException"


class ColumnStatisticsTaskNotRunningException(GlueError):
    """An exception thrown when you try to stop a task run when there is no task running."""
    _ERROR_CODE = "ColumnStatisticsTaskNotRunningException"


class ColumnStatisticsTaskRunningException(GlueError):
    """An exception thrown when you try to start another job while running a column stats
    generation job.
    """

    _ERROR_CODE = "ColumnStatisticsTaskRunningException"


class ColumnStatisticsTaskStoppingException(GlueError):
    """An exception thrown when you try to stop a task run."""
    _ERROR_CODE = "ColumnStatisticsTaskStoppingException"


class ConcurrentModificationException(GlueError):
    """Two processes are trying to modify a resource simultaneously."""
    _ERROR_CODE = "ConcurrentModificationException"


class ConcurrentRunsExceededException(GlueError):
    """Too many jobs are being run concurrently."""
    _ERROR_CODE = "ConcurrentRunsExceededException"


class ConditionCheckFailureException(GlueError):
    """A specified condition was not satisfied."""
    _ERROR_CODE = "ConditionCheckFailureException"


class ConflictException(GlueError):
    """The `CreatePartitions` API was called on a table that has indexes enabled."""
    _ERROR_CODE = "ConflictException"


class CrawlerNotRunningException(GlueError):
    """The specified crawler is not running."""
    _ERROR_CODE = "CrawlerNotRunningException"


class CrawlerRunningException(GlueError):
    """The operation cannot be performed because the crawler is already running."""
    _ERROR_CODE = "CrawlerRunningException"


class CrawlerStoppingException(GlueError):
    """The specified crawler is stopping."""
    _ERROR_CODE = "CrawlerStoppingException"


class EntityNotFoundException(GlueError):
    """A specified entity does not exist"""
    _ERROR_CODE = "EntityNotFoundException"

    @property
    def from_federation_source(self) -> bool | None:
        """Indicates whether or not the exception relates to a federated source."""
        return self.response.get("FromFederationSource")


class FederatedResourceAlreadyExistsException(GlueError):
    """A federated resource already exists."""
    _ERROR_CODE = "FederatedResourceAlreadyExistsException"

    @property
    def associated_glue_resource(self) -> str | None:
        """The associated Glue resource already exists."""
        return self.response.get("AssociatedGlueResource")


class FederationSourceException(GlueError):
    """A federation source failed."""
    _ERROR_CODE = "FederationSourceException"

    @property
    def federation_source_error_code(self) -> str | None:
        """The error code of the problem."""
        return self.response.get("FederationSourceErrorCode")


class FederationSourceRetryableException(GlueError):
    """A federation source failed, but the operation may be retried."""
    _ERROR_CODE = "FederationSourceRetryableException"


class GlueEncryptionException(GlueError):
    """An encryption operation failed."""
    _ERROR_CODE = "GlueEncryptionException"


class IdempotentParameterMismatchException(GlueError):
    """The same unique identifier was associated with two different records."""
    _ERROR_CODE = "IdempotentParameterMismatchException"


class IllegalBlueprintStateException(GlueError):
    """The blueprint is in an invalid state to perform a requested operation."""
    _ERROR_CODE = "IllegalBlueprintStateException"


class IllegalSessionStateException(GlueError):
    """The session is in an invalid state to perform a requested operation."""
    _ERROR_CODE = "IllegalSessionStateException"


class IllegalWorkflowStateException(GlueError):
    """The workflow is in an invalid state to perform a requested operation."""
    _ERROR_CODE = "IllegalWorkflowStateException"


class InternalServiceException(GlueError):
    """An internal service error occurred."""
    _ERROR_CODE = "InternalServiceException"


class InvalidInputException(GlueError):
    """The input provided was not valid."""
    _ERROR_CODE = "InvalidInputException"

    @property
    def from_federation_source(self) -> bool | None:
        """Indicates whether or not the exception relates to a federated source."""
        return self.response.get("FromFederationSource")


class InvalidStateException(GlueError):
    """An error that indicates your data is in an invalid state."""
    _ERROR_CODE = "InvalidStateException"


class MLTransformNotReadyException(GlueError):
    """The machine learning transform is not ready to run."""
    _ERROR_CODE = "MLTransformNotReadyException"


class NoScheduleException(GlueError):
    """There is no applicable schedule."""
    _ERROR_CODE = "NoScheduleException"


class OperationTimeoutException(GlueError):
    """The operation timed out."""
    _ERROR_CODE = "OperationTimeoutException"


class PermissionTypeMismatchException(GlueError):
    """The operation timed out."""
    _ERROR_CODE = "PermissionTypeMismatchException"


class ResourceNotReadyException(GlueError):
    """A resource was not ready for a transaction."""
    _ERROR_CODE = "ResourceNotReadyException"


class ResourceNumberLimitExceededException(GlueError):
    """A resource numerical limit was exceeded."""
    _ERROR_CODE = "ResourceNumberLimitExceededException"


class SchedulerNotRunningException(GlueError):
    """The specified scheduler is not running."""
    _ERROR_CODE = "SchedulerNotRunningException"


class SchedulerRunningException(GlueError):
    """The specified scheduler is already running."""
    _ERROR_CODE = "SchedulerRunningException"


class SchedulerTransitioningException(GlueError):
    """The specified scheduler is transitioning."""
    _ERROR_CODE = "SchedulerTransitioningException"


class ValidationException(GlueError):
    """A value could not be validated."""
    _ERROR_CODE = "ValidationException"


class VersionMismatchException(GlueError):
    """There was a version conflict."""
    _ERROR_CODE = "VersionMismatchException"


EXCEPTIONS: dict[str, type[GlueError]] = {
    "AccessDeniedException": AccessDeniedException,
    "AlreadyExistsException": AlreadyExistsException,
    "ColumnStatisticsTaskNotRunningException": ColumnStatisticsTaskNotRunningException,
    "ColumnStatisticsTaskRunningException": ColumnStatisticsTaskRunningException,
    "ColumnStatisticsTaskStoppingException": ColumnStatisticsTaskStoppingException,
    "ConcurrentModificationException": ConcurrentModificationException,
    "ConcurrentRunsExceededException": ConcurrentRunsExceededException,
    "ConditionCheckFailureException": ConditionCheckFailureException,
    "ConflictException": ConflictException,
    "CrawlerNotRunningException": CrawlerNotRunningException,
    "CrawlerRunningException": CrawlerRunningException,
    "CrawlerStoppingException": CrawlerStoppingException,
    "EntityNotFoundException": EntityNotFoundException,
    "FederatedResourceAlreadyExistsException": FederatedResourceAlreadyExistsException,
    "FederationSourceException": FederationSourceException,
    "FederationSourceRetryableException": FederationSourceRetryableException,
    "GlueEncryptionException": GlueEncryptionException,
    "IdempotentParameterMismatchException": IdempotentParameterMismatchException,
    "IllegalBlueprintStateException": IllegalBlueprintStateException,
    "IllegalSessionStateException": IllegalSessionStateException,
    "IllegalWorkflowStateException": IllegalWorkflowStateException,
    "InternalServiceException": InternalServiceException,
    "InvalidInputException": InvalidInputException,
    "InvalidStateException": InvalidStateException,
    "MLTransformNotReadyException": MLTransformNotReadyException,
    "NoScheduleException": NoScheduleException,
    "OperationTimeoutException": OperationTimeoutException,
    "PermissionTypeMismatchException": PermissionTypeMismatchException,
    "ResourceNotReadyException": ResourceNotReadyException,
    "ResourceNumberLimitExceededException": ResourceNumberLimitExceededException,
    "SchedulerNotRunningException": SchedulerNotRunningException,
    "SchedulerRunningException": SchedulerRunningException,
    "SchedulerTransitioningException": SchedulerTransitioningException,
    "ValidationException": ValidationException,
    "VersionMismatchException": VersionMismatchException,
}
