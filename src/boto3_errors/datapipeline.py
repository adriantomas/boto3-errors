# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class DataPipelineError(Boto3Error):
    _SERVICE = "datapipeline"


class InternalServiceError(DataPipelineError):
    """An internal service error occurred."""
    _ERROR_CODE = "InternalServiceError"


class InvalidRequestException(DataPipelineError):
    """The request was not valid. Verify that your request was properly formatted, that the
    signature was generated with the correct credentials, and that you haven't exceeded
    any of the service limits for your account.
    """

    _ERROR_CODE = "InvalidRequestException"


class PipelineDeletedException(DataPipelineError):
    """The specified pipeline has been deleted."""
    _ERROR_CODE = "PipelineDeletedException"


class PipelineNotFoundException(DataPipelineError):
    """The specified pipeline was not found. Verify that you used the correct user and
    account identifiers.
    """

    _ERROR_CODE = "PipelineNotFoundException"


class TaskNotFoundException(DataPipelineError):
    """The specified task was not found."""
    _ERROR_CODE = "TaskNotFoundException"


EXCEPTIONS: dict[str, type[DataPipelineError]] = {
    "InternalServiceError": InternalServiceError,
    "InvalidRequestException": InvalidRequestException,
    "PipelineDeletedException": PipelineDeletedException,
    "PipelineNotFoundException": PipelineNotFoundException,
    "TaskNotFoundException": TaskNotFoundException,
}
