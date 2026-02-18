# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class SFNError(Boto3Error):
    _SERVICE = "stepfunctions"


class ActivityDoesNotExist(SFNError):
    """The specified activity does not exist."""
    _ERROR_CODE = "ActivityDoesNotExist"


class ActivityLimitExceeded(SFNError):
    """The maximum number of activities has been reached. Existing activities must be
    deleted before a new activity can be created.
    """

    _ERROR_CODE = "ActivityLimitExceeded"


class ActivityWorkerLimitExceeded(SFNError):
    """The maximum number of workers concurrently polling for activity tasks has been
    reached.
    """

    _ERROR_CODE = "ActivityWorkerLimitExceeded"


class ConflictException(SFNError):
    """Updating or deleting a resource can cause an inconsistent state. This error occurs
    when there're concurrent requests for DeleteStateMachineVersion,
    PublishStateMachineVersion, or UpdateStateMachine with the `publish` parameter set
    to `true`.

    HTTP Status Code: 409
    """

    _ERROR_CODE = "ConflictException"


class ExecutionAlreadyExists(SFNError):
    """The execution has the same `name` as another execution (but a different `input`).

    Note:

    Executions with the same `name` and `input` are considered idempotent.
    """

    _ERROR_CODE = "ExecutionAlreadyExists"


class ExecutionDoesNotExist(SFNError):
    """The specified execution does not exist."""
    _ERROR_CODE = "ExecutionDoesNotExist"


class ExecutionLimitExceeded(SFNError):
    """The maximum number of running executions has been reached. Running executions must
    end or be stopped before a new execution can be started.
    """

    _ERROR_CODE = "ExecutionLimitExceeded"


class ExecutionNotRedrivable(SFNError):
    """The execution Amazon Resource Name (ARN) that you specified for `executionArn`
    cannot be redriven.
    """

    _ERROR_CODE = "ExecutionNotRedrivable"


class InvalidArn(SFNError):
    """The provided Amazon Resource Name (ARN) is not valid."""
    _ERROR_CODE = "InvalidArn"


class InvalidDefinition(SFNError):
    """The provided Amazon States Language definition is not valid."""
    _ERROR_CODE = "InvalidDefinition"


class InvalidExecutionInput(SFNError):
    """The provided JSON input data is not valid."""
    _ERROR_CODE = "InvalidExecutionInput"


class InvalidLoggingConfiguration(SFNError):
    _ERROR_CODE = "InvalidLoggingConfiguration"


class InvalidName(SFNError):
    """The provided name is not valid."""
    _ERROR_CODE = "InvalidName"


class InvalidOutput(SFNError):
    """The provided JSON output data is not valid."""
    _ERROR_CODE = "InvalidOutput"


class InvalidToken(SFNError):
    """The provided token is not valid."""
    _ERROR_CODE = "InvalidToken"


class InvalidTracingConfiguration(SFNError):
    """Your `tracingConfiguration` key does not match, or `enabled` has not been set to
    `true` or `false`.
    """

    _ERROR_CODE = "InvalidTracingConfiguration"


class MissingRequiredParameter(SFNError):
    """Request is missing a required parameter. This error occurs if both `definition` and
    `roleArn` are not specified.
    """

    _ERROR_CODE = "MissingRequiredParameter"


class ResourceNotFound(SFNError):
    """Could not find the referenced resource."""
    _ERROR_CODE = "ResourceNotFound"

    @property
    def resource_name(self) -> str | None:
        return self.response.get("resourceName")


class ServiceQuotaExceededException(SFNError):
    """The request would cause a service quota to be exceeded.

    HTTP Status Code: 402
    """

    _ERROR_CODE = "ServiceQuotaExceededException"


class StateMachineAlreadyExists(SFNError):
    """A state machine with the same name but a different definition or role ARN already
    exists.
    """

    _ERROR_CODE = "StateMachineAlreadyExists"


class StateMachineDeleting(SFNError):
    """The specified state machine is being deleted."""
    _ERROR_CODE = "StateMachineDeleting"


class StateMachineDoesNotExist(SFNError):
    """The specified state machine does not exist."""
    _ERROR_CODE = "StateMachineDoesNotExist"


class StateMachineLimitExceeded(SFNError):
    """The maximum number of state machines has been reached. Existing state machines must
    be deleted before a new state machine can be created.
    """

    _ERROR_CODE = "StateMachineLimitExceeded"


class StateMachineTypeNotSupported(SFNError):
    _ERROR_CODE = "StateMachineTypeNotSupported"


class TaskDoesNotExist(SFNError):
    """The activity does not exist."""
    _ERROR_CODE = "TaskDoesNotExist"


class TaskTimedOut(SFNError):
    """The task token has either expired or the task associated with the token has already
    been closed.
    """

    _ERROR_CODE = "TaskTimedOut"


class TooManyTags(SFNError):
    """You've exceeded the number of tags allowed for a resource. See the Limits Topic in
    the Step Functions Developer Guide.
    """

    _ERROR_CODE = "TooManyTags"

    @property
    def resource_name(self) -> str | None:
        return self.response.get("resourceName")


class ValidationException(SFNError):
    """The input does not satisfy the constraints specified by an Amazon Web Services
    service.
    """

    _ERROR_CODE = "ValidationException"

    @property
    def reason(self) -> str | None:
        """The input does not satisfy the constraints specified by an Amazon Web Services
        service.
        """
        return self.response.get("reason")


EXCEPTIONS: dict[str, type[SFNError]] = {
    "ActivityDoesNotExist": ActivityDoesNotExist,
    "ActivityLimitExceeded": ActivityLimitExceeded,
    "ActivityWorkerLimitExceeded": ActivityWorkerLimitExceeded,
    "ConflictException": ConflictException,
    "ExecutionAlreadyExists": ExecutionAlreadyExists,
    "ExecutionDoesNotExist": ExecutionDoesNotExist,
    "ExecutionLimitExceeded": ExecutionLimitExceeded,
    "ExecutionNotRedrivable": ExecutionNotRedrivable,
    "InvalidArn": InvalidArn,
    "InvalidDefinition": InvalidDefinition,
    "InvalidExecutionInput": InvalidExecutionInput,
    "InvalidLoggingConfiguration": InvalidLoggingConfiguration,
    "InvalidName": InvalidName,
    "InvalidOutput": InvalidOutput,
    "InvalidToken": InvalidToken,
    "InvalidTracingConfiguration": InvalidTracingConfiguration,
    "MissingRequiredParameter": MissingRequiredParameter,
    "ResourceNotFound": ResourceNotFound,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "StateMachineAlreadyExists": StateMachineAlreadyExists,
    "StateMachineDeleting": StateMachineDeleting,
    "StateMachineDoesNotExist": StateMachineDoesNotExist,
    "StateMachineLimitExceeded": StateMachineLimitExceeded,
    "StateMachineTypeNotSupported": StateMachineTypeNotSupported,
    "TaskDoesNotExist": TaskDoesNotExist,
    "TaskTimedOut": TaskTimedOut,
    "TooManyTags": TooManyTags,
    "ValidationException": ValidationException,
}
