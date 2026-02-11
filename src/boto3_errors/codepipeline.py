# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class CodePipelineError(Boto3Error):
    _SERVICE = "codepipeline"


class ActionExecutionNotFoundException(CodePipelineError):
    """The action execution was not found."""
    _ERROR_CODE = "ActionExecutionNotFoundException"


class ActionNotFoundException(CodePipelineError):
    """The specified action cannot be found."""
    _ERROR_CODE = "ActionNotFoundException"


class ActionTypeAlreadyExistsException(CodePipelineError):
    """The specified action type already exists with a different definition."""
    _ERROR_CODE = "ActionTypeAlreadyExistsException"


class ActionTypeNotFoundException(CodePipelineError):
    """The specified action type cannot be found."""
    _ERROR_CODE = "ActionTypeNotFoundException"


class ApprovalAlreadyCompletedException(CodePipelineError):
    """The approval action has already been approved or rejected."""
    _ERROR_CODE = "ApprovalAlreadyCompletedException"


class ConcurrentModificationException(CodePipelineError):
    """Unable to modify the tag due to a simultaneous update request."""
    _ERROR_CODE = "ConcurrentModificationException"


class ConcurrentPipelineExecutionsLimitExceededException(CodePipelineError):
    """The pipeline has reached the limit for concurrent pipeline executions."""
    _ERROR_CODE = "ConcurrentPipelineExecutionsLimitExceededException"


class ConditionNotOverridableException(CodePipelineError):
    """Unable to override because the condition does not allow overrides."""
    _ERROR_CODE = "ConditionNotOverridableException"


class ConflictException(CodePipelineError):
    """Your request cannot be handled because the pipeline is busy handling ongoing
    activities. Try again later.
    """

    _ERROR_CODE = "ConflictException"


class DuplicatedStopRequestException(CodePipelineError):
    """The pipeline execution is already in a `Stopping` state. If you already chose to
    stop and wait, you cannot make that request again. You can choose to stop and
    abandon now, but be aware that this option can lead to failed tasks or out of
    sequence tasks. If you already chose to stop and abandon, you cannot make that
    request again.
    """

    _ERROR_CODE = "DuplicatedStopRequestException"


class InvalidActionDeclarationException(CodePipelineError):
    """The action declaration was specified in an invalid format."""
    _ERROR_CODE = "InvalidActionDeclarationException"


class InvalidApprovalTokenException(CodePipelineError):
    """The approval request already received a response or has expired."""
    _ERROR_CODE = "InvalidApprovalTokenException"


class InvalidArnException(CodePipelineError):
    """The specified resource ARN is invalid."""
    _ERROR_CODE = "InvalidArnException"


class InvalidBlockerDeclarationException(CodePipelineError):
    """Reserved for future use."""
    _ERROR_CODE = "InvalidBlockerDeclarationException"


class InvalidClientTokenException(CodePipelineError):
    """The client token was specified in an invalid format"""
    _ERROR_CODE = "InvalidClientTokenException"


class InvalidJobException(CodePipelineError):
    """The job was specified in an invalid format or cannot be found."""
    _ERROR_CODE = "InvalidJobException"


class InvalidJobStateException(CodePipelineError):
    """The job state was specified in an invalid format."""
    _ERROR_CODE = "InvalidJobStateException"


class InvalidNextTokenException(CodePipelineError):
    """The next token was specified in an invalid format. Make sure that the next token you
    provide is the token returned by a previous call.
    """

    _ERROR_CODE = "InvalidNextTokenException"


class InvalidNonceException(CodePipelineError):
    """The nonce was specified in an invalid format."""
    _ERROR_CODE = "InvalidNonceException"


class InvalidStageDeclarationException(CodePipelineError):
    """The stage declaration was specified in an invalid format."""
    _ERROR_CODE = "InvalidStageDeclarationException"


class InvalidStructureException(CodePipelineError):
    """The structure was specified in an invalid format."""
    _ERROR_CODE = "InvalidStructureException"


class InvalidTagsException(CodePipelineError):
    """The specified resource tags are invalid."""
    _ERROR_CODE = "InvalidTagsException"


class InvalidWebhookAuthenticationParametersException(CodePipelineError):
    """The specified authentication type is in an invalid format."""
    _ERROR_CODE = "InvalidWebhookAuthenticationParametersException"


class InvalidWebhookFilterPatternException(CodePipelineError):
    """The specified event filter rule is in an invalid format."""
    _ERROR_CODE = "InvalidWebhookFilterPatternException"


class JobNotFoundException(CodePipelineError):
    """The job was specified in an invalid format or cannot be found."""
    _ERROR_CODE = "JobNotFoundException"


class LimitExceededException(CodePipelineError):
    """The number of pipelines associated with the Amazon Web Services account has exceeded
    the limit allowed for the account.
    """

    _ERROR_CODE = "LimitExceededException"


class NotLatestPipelineExecutionException(CodePipelineError):
    """The stage has failed in a later run of the pipeline and the `pipelineExecutionId`
    associated with the request is out of date.
    """

    _ERROR_CODE = "NotLatestPipelineExecutionException"


class OutputVariablesSizeExceededException(CodePipelineError):
    """Exceeded the total size limit for all variables in the pipeline."""
    _ERROR_CODE = "OutputVariablesSizeExceededException"


class PipelineExecutionNotFoundException(CodePipelineError):
    """The pipeline execution was specified in an invalid format or cannot be found, or an
    execution ID does not belong to the specified pipeline.
    """

    _ERROR_CODE = "PipelineExecutionNotFoundException"


class PipelineExecutionNotStoppableException(CodePipelineError):
    """Unable to stop the pipeline execution. The execution might already be in a `Stopped`
    state, or it might no longer be in progress.
    """

    _ERROR_CODE = "PipelineExecutionNotStoppableException"


class PipelineExecutionOutdatedException(CodePipelineError):
    """The specified pipeline execution is outdated and cannot be used as a target pipeline
    execution for rollback.
    """

    _ERROR_CODE = "PipelineExecutionOutdatedException"


class PipelineNameInUseException(CodePipelineError):
    """The specified pipeline name is already in use."""
    _ERROR_CODE = "PipelineNameInUseException"


class PipelineNotFoundException(CodePipelineError):
    """The pipeline was specified in an invalid format or cannot be found."""
    _ERROR_CODE = "PipelineNotFoundException"


class PipelineVersionNotFoundException(CodePipelineError):
    """The pipeline version was specified in an invalid format or cannot be found."""
    _ERROR_CODE = "PipelineVersionNotFoundException"


class RequestFailedException(CodePipelineError):
    """The request failed because of an unknown error, exception, or failure."""
    _ERROR_CODE = "RequestFailedException"


class ResourceNotFoundException(CodePipelineError):
    """The resource was specified in an invalid format."""
    _ERROR_CODE = "ResourceNotFoundException"


class StageNotFoundException(CodePipelineError):
    """The stage was specified in an invalid format or cannot be found."""
    _ERROR_CODE = "StageNotFoundException"


class StageNotRetryableException(CodePipelineError):
    """Unable to retry. The pipeline structure or stage state might have changed while
    actions awaited retry, or the stage contains no failed actions.
    """

    _ERROR_CODE = "StageNotRetryableException"


class TooManyTagsException(CodePipelineError):
    """The tags limit for a resource has been exceeded."""
    _ERROR_CODE = "TooManyTagsException"


class UnableToRollbackStageException(CodePipelineError):
    """Unable to roll back the stage. The cause might be if the pipeline version has
    changed since the target pipeline execution was deployed, the stage is currently
    running, or an incorrect target pipeline execution ID was provided.
    """

    _ERROR_CODE = "UnableToRollbackStageException"


class ValidationException(CodePipelineError):
    """The validation was specified in an invalid format."""
    _ERROR_CODE = "ValidationException"


class WebhookNotFoundException(CodePipelineError):
    """The specified webhook was entered in an invalid format or cannot be found."""
    _ERROR_CODE = "WebhookNotFoundException"


EXCEPTIONS: dict[str, type[CodePipelineError]] = {
    "ActionExecutionNotFoundException": ActionExecutionNotFoundException,
    "ActionNotFoundException": ActionNotFoundException,
    "ActionTypeAlreadyExistsException": ActionTypeAlreadyExistsException,
    "ActionTypeNotFoundException": ActionTypeNotFoundException,
    "ApprovalAlreadyCompletedException": ApprovalAlreadyCompletedException,
    "ConcurrentModificationException": ConcurrentModificationException,
    "ConcurrentPipelineExecutionsLimitExceededException": ConcurrentPipelineExecutionsLimitExceededException,
    "ConditionNotOverridableException": ConditionNotOverridableException,
    "ConflictException": ConflictException,
    "DuplicatedStopRequestException": DuplicatedStopRequestException,
    "InvalidActionDeclarationException": InvalidActionDeclarationException,
    "InvalidApprovalTokenException": InvalidApprovalTokenException,
    "InvalidArnException": InvalidArnException,
    "InvalidBlockerDeclarationException": InvalidBlockerDeclarationException,
    "InvalidClientTokenException": InvalidClientTokenException,
    "InvalidJobException": InvalidJobException,
    "InvalidJobStateException": InvalidJobStateException,
    "InvalidNextTokenException": InvalidNextTokenException,
    "InvalidNonceException": InvalidNonceException,
    "InvalidStageDeclarationException": InvalidStageDeclarationException,
    "InvalidStructureException": InvalidStructureException,
    "InvalidTagsException": InvalidTagsException,
    "InvalidWebhookAuthenticationParametersException": InvalidWebhookAuthenticationParametersException,
    "InvalidWebhookFilterPatternException": InvalidWebhookFilterPatternException,
    "JobNotFoundException": JobNotFoundException,
    "LimitExceededException": LimitExceededException,
    "NotLatestPipelineExecutionException": NotLatestPipelineExecutionException,
    "OutputVariablesSizeExceededException": OutputVariablesSizeExceededException,
    "PipelineExecutionNotFoundException": PipelineExecutionNotFoundException,
    "PipelineExecutionNotStoppableException": PipelineExecutionNotStoppableException,
    "PipelineExecutionOutdatedException": PipelineExecutionOutdatedException,
    "PipelineNameInUseException": PipelineNameInUseException,
    "PipelineNotFoundException": PipelineNotFoundException,
    "PipelineVersionNotFoundException": PipelineVersionNotFoundException,
    "RequestFailedException": RequestFailedException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "StageNotFoundException": StageNotFoundException,
    "StageNotRetryableException": StageNotRetryableException,
    "TooManyTagsException": TooManyTagsException,
    "UnableToRollbackStageException": UnableToRollbackStageException,
    "ValidationException": ValidationException,
    "WebhookNotFoundException": WebhookNotFoundException,
}
