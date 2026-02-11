# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class SFNError(Boto3Error):
    _SERVICE = "stepfunctions"


class ActivityAlreadyExists(SFNError):
    """Activity already exists. `EncryptionConfiguration` may not be updated."""
    _ERROR_CODE = "ActivityAlreadyExists"


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


class InvalidEncryptionConfiguration(SFNError):
    """Received when `encryptionConfiguration` is specified but various conditions exist
    which make the configuration invalid. For example, if `type` is set to
    `CUSTOMER_MANAGED_KMS_KEY`, but `kmsKeyId` is null, or
    `kmsDataKeyReusePeriodSeconds` is not between 60 and 900, or the KMS key is not
    symmetric or inactive.
    """

    _ERROR_CODE = "InvalidEncryptionConfiguration"


class InvalidExecutionInput(SFNError):
    """The provided JSON input data is not valid."""
    _ERROR_CODE = "InvalidExecutionInput"


class InvalidLoggingConfiguration(SFNError):
    """Configuration is not valid."""
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


class KmsAccessDeniedException(SFNError):
    """Either your KMS key policy or API caller does not have the required permissions."""
    _ERROR_CODE = "KmsAccessDeniedException"


class KmsInvalidStateException(SFNError):
    """The KMS key is not in valid state, for example: Disabled or Deleted."""
    _ERROR_CODE = "KmsInvalidStateException"

    @property
    def kms_key_state(self) -> str | None:
        """Current status of the KMS; key. For example: `DISABLED`, `PENDING_DELETION`,
        `PENDING_IMPORT`, `UNAVAILABLE`, `CREATING`.
        """
        return self.response.get("kmsKeyState")


class KmsThrottlingException(SFNError):
    """Received when KMS returns `ThrottlingException` for a KMS call that Step Functions
    makes on behalf of the caller.
    """

    _ERROR_CODE = "KmsThrottlingException"


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
    """State machine type is not supported."""
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
    "ActivityAlreadyExists": ActivityAlreadyExists,
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
    "InvalidEncryptionConfiguration": InvalidEncryptionConfiguration,
    "InvalidExecutionInput": InvalidExecutionInput,
    "InvalidLoggingConfiguration": InvalidLoggingConfiguration,
    "InvalidName": InvalidName,
    "InvalidOutput": InvalidOutput,
    "InvalidToken": InvalidToken,
    "InvalidTracingConfiguration": InvalidTracingConfiguration,
    "KmsAccessDeniedException": KmsAccessDeniedException,
    "KmsInvalidStateException": KmsInvalidStateException,
    "KmsThrottlingException": KmsThrottlingException,
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
