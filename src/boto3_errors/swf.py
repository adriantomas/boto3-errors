# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class SWFError(Boto3Error):
    _SERVICE = "swf"


class DefaultUndefinedFault(SWFError):
    """The `StartWorkflowExecution` API action was called without the required parameters
    set.

    Some workflow execution parameters, such as the decision `taskList`, must be set to
    start the execution. However, these parameters might have been set as defaults when
    the workflow type was registered. In this case, you can omit these parameters from
    the `StartWorkflowExecution` call and Amazon SWF uses the values defined in the
    workflow type.

    Note:

    If these parameters aren't set and no default parameters were defined in the
    workflow type, this error is displayed.
    """

    _ERROR_CODE = "DefaultUndefinedFault"


class DomainAlreadyExistsFault(SWFError):
    """Returned if the domain already exists. You may get this fault if you are registering
    a domain that is either already registered or deprecated, or if you undeprecate a
    domain that is currently registered.
    """

    _ERROR_CODE = "DomainAlreadyExistsFault"


class DomainDeprecatedFault(SWFError):
    """Returned when the specified domain has been deprecated."""
    _ERROR_CODE = "DomainDeprecatedFault"


class LimitExceededFault(SWFError):
    """Returned by any operation if a system imposed limitation has been reached. To
    address this fault you should either clean up unused resources or increase the limit
    by contacting AWS.
    """

    _ERROR_CODE = "LimitExceededFault"


class OperationNotPermittedFault(SWFError):
    """Returned when the caller doesn't have sufficient permissions to invoke the action."""
    _ERROR_CODE = "OperationNotPermittedFault"


class TooManyTagsFault(SWFError):
    """You've exceeded the number of tags allowed for a domain."""
    _ERROR_CODE = "TooManyTagsFault"


class TypeAlreadyExistsFault(SWFError):
    """Returned if the type already exists in the specified domain. You may get this fault
    if you are registering a type that is either already registered or deprecated, or if
    you undeprecate a type that is currently registered.
    """

    _ERROR_CODE = "TypeAlreadyExistsFault"


class TypeDeprecatedFault(SWFError):
    """Returned when the specified activity or workflow type was already deprecated."""
    _ERROR_CODE = "TypeDeprecatedFault"


class UnknownResourceFault(SWFError):
    """Returned when the named resource cannot be found with in the scope of this operation
    (region or domain). This could happen if the named resource was never created or is
    no longer available for this operation.
    """

    _ERROR_CODE = "UnknownResourceFault"


class WorkflowExecutionAlreadyStartedFault(SWFError):
    """Returned by StartWorkflowExecution when an open execution with the same workflowId
    is already running in the specified domain.
    """

    _ERROR_CODE = "WorkflowExecutionAlreadyStartedFault"


EXCEPTIONS: dict[str, type[SWFError]] = {
    "DefaultUndefinedFault": DefaultUndefinedFault,
    "DomainAlreadyExistsFault": DomainAlreadyExistsFault,
    "DomainDeprecatedFault": DomainDeprecatedFault,
    "LimitExceededFault": LimitExceededFault,
    "OperationNotPermittedFault": OperationNotPermittedFault,
    "TooManyTagsFault": TooManyTagsFault,
    "TypeAlreadyExistsFault": TypeAlreadyExistsFault,
    "TypeDeprecatedFault": TypeDeprecatedFault,
    "UnknownResourceFault": UnknownResourceFault,
    "WorkflowExecutionAlreadyStartedFault": WorkflowExecutionAlreadyStartedFault,
}
