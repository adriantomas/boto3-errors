# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class CloudFormationError(Boto3Error):
    _SERVICE = "cloudformation"


class AlreadyExistsException(CloudFormationError):
    """The resource with the name requested already exists."""
    _ERROR_CODE = "AlreadyExistsException"


class CFNRegistryException(CloudFormationError):
    """An error occurred during a CloudFormation registry operation."""
    _ERROR_CODE = "CFNRegistryException"


class ChangeSetNotFoundException(CloudFormationError):
    """The specified change set name or ID doesn't exit. To view valid change sets for a
    stack, use the `ListChangeSets` operation.
    """

    _ERROR_CODE = "ChangeSetNotFound"


class ConcurrentResourcesLimitExceededException(CloudFormationError):
    """No more than 5 generated templates can be in an `InProgress` or `Pending` status at
    one time. This error is also returned if a generated template that is in an
    `InProgress` or `Pending` status is attempted to be updated or deleted.
    """

    _ERROR_CODE = "ConcurrentResourcesLimitExceeded"


class CreatedButModifiedException(CloudFormationError):
    """The specified resource exists, but has been changed."""
    _ERROR_CODE = "CreatedButModifiedException"


class GeneratedTemplateNotFoundException(CloudFormationError):
    """The generated template was not found."""
    _ERROR_CODE = "GeneratedTemplateNotFound"


class InsufficientCapabilitiesException(CloudFormationError):
    """The template contains resources with capabilities that weren't specified in the
    Capabilities parameter.
    """

    _ERROR_CODE = "InsufficientCapabilitiesException"


class InvalidChangeSetStatusException(CloudFormationError):
    """The specified change set can't be used to update the stack. For example, the change
    set status might be `CREATE_IN_PROGRESS`, or the stack status might be
    `UPDATE_IN_PROGRESS`.
    """

    _ERROR_CODE = "InvalidChangeSetStatus"


class InvalidOperationException(CloudFormationError):
    """The specified operation isn't valid."""
    _ERROR_CODE = "InvalidOperationException"


class InvalidStateTransitionException(CloudFormationError):
    """Error reserved for use by the CloudFormation CLI. CloudFormation doesn't return this
    error to users.
    """

    _ERROR_CODE = "InvalidStateTransition"


class LimitExceededException(CloudFormationError):
    """The quota for the resource has already been reached.

    For information about resource and stack limitations, see CloudFormation quotas in
    the CloudFormation User Guide.
    """

    _ERROR_CODE = "LimitExceededException"


class NameAlreadyExistsException(CloudFormationError):
    """The specified name is already in use."""
    _ERROR_CODE = "NameAlreadyExistsException"


class OperationIdAlreadyExistsException(CloudFormationError):
    """The specified operation ID already exists."""
    _ERROR_CODE = "OperationIdAlreadyExistsException"


class OperationInProgressException(CloudFormationError):
    """Another operation is currently in progress for this stack set. Only one operation
    can be performed for a stack set at a given time.
    """

    _ERROR_CODE = "OperationInProgressException"


class OperationNotFoundException(CloudFormationError):
    """The specified ID refers to an operation that doesn't exist."""
    _ERROR_CODE = "OperationNotFoundException"


class OperationStatusCheckFailedException(CloudFormationError):
    """Error reserved for use by the CloudFormation CLI. CloudFormation doesn't return this
    error to users.
    """

    _ERROR_CODE = "ConditionalCheckFailed"


class ResourceScanInProgressException(CloudFormationError):
    """A resource scan is currently in progress. Only one can be run at a time for an
    account in a Region.
    """

    _ERROR_CODE = "ResourceScanInProgress"


class ResourceScanLimitExceededException(CloudFormationError):
    """The limit on resource scans has been exceeded. Reasons include:

    - Exceeded the daily quota for resource scans.
    - A resource scan recently failed. You must wait 10 minutes before starting a new
      resource scan.
    - The last resource scan failed after exceeding 100,000 resources. When this
      happens, you must wait 24 hours before starting a new resource scan.
    """

    _ERROR_CODE = "ResourceScanLimitExceeded"


class ResourceScanNotFoundException(CloudFormationError):
    """The resource scan was not found."""
    _ERROR_CODE = "ResourceScanNotFound"


class StackInstanceNotFoundException(CloudFormationError):
    """The specified stack instance doesn't exist."""
    _ERROR_CODE = "StackInstanceNotFoundException"


class StackNotFoundException(CloudFormationError):
    """The specified stack ARN doesn't exist or stack doesn't exist corresponding to the
    ARN in input.
    """

    _ERROR_CODE = "StackNotFoundException"


class StackSetNotEmptyException(CloudFormationError):
    """You can't yet delete this stack set, because it still contains one or more stack
    instances. Delete all stack instances from the stack set before deleting the stack
    set.
    """

    _ERROR_CODE = "StackSetNotEmptyException"


class StackSetNotFoundException(CloudFormationError):
    """The specified stack set doesn't exist."""
    _ERROR_CODE = "StackSetNotFoundException"


class StaleRequestException(CloudFormationError):
    """Another operation has been performed on this stack set since the specified operation
    was performed.
    """

    _ERROR_CODE = "StaleRequestException"


class TokenAlreadyExistsException(CloudFormationError):
    """A client request token already exists."""
    _ERROR_CODE = "TokenAlreadyExistsException"


class TypeConfigurationNotFoundException(CloudFormationError):
    """The specified extension configuration can't be found."""
    _ERROR_CODE = "TypeConfigurationNotFoundException"


class TypeNotFoundException(CloudFormationError):
    """The specified extension doesn't exist in the CloudFormation registry."""
    _ERROR_CODE = "TypeNotFoundException"


EXCEPTIONS: dict[str, type[CloudFormationError]] = {
    "AlreadyExistsException": AlreadyExistsException,
    "CFNRegistryException": CFNRegistryException,
    "ChangeSetNotFound": ChangeSetNotFoundException,
    "ConcurrentResourcesLimitExceeded": ConcurrentResourcesLimitExceededException,
    "CreatedButModifiedException": CreatedButModifiedException,
    "GeneratedTemplateNotFound": GeneratedTemplateNotFoundException,
    "InsufficientCapabilitiesException": InsufficientCapabilitiesException,
    "InvalidChangeSetStatus": InvalidChangeSetStatusException,
    "InvalidOperationException": InvalidOperationException,
    "InvalidStateTransition": InvalidStateTransitionException,
    "LimitExceededException": LimitExceededException,
    "NameAlreadyExistsException": NameAlreadyExistsException,
    "OperationIdAlreadyExistsException": OperationIdAlreadyExistsException,
    "OperationInProgressException": OperationInProgressException,
    "OperationNotFoundException": OperationNotFoundException,
    "ConditionalCheckFailed": OperationStatusCheckFailedException,
    "ResourceScanInProgress": ResourceScanInProgressException,
    "ResourceScanLimitExceeded": ResourceScanLimitExceededException,
    "ResourceScanNotFound": ResourceScanNotFoundException,
    "StackInstanceNotFoundException": StackInstanceNotFoundException,
    "StackNotFoundException": StackNotFoundException,
    "StackSetNotEmptyException": StackSetNotEmptyException,
    "StackSetNotFoundException": StackSetNotFoundException,
    "StaleRequestException": StaleRequestException,
    "TokenAlreadyExistsException": TokenAlreadyExistsException,
    "TypeConfigurationNotFoundException": TypeConfigurationNotFoundException,
    "TypeNotFoundException": TypeNotFoundException,
}
