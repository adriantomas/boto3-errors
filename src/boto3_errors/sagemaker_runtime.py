# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class SageMakerRuntimeError(Boto3Error):
    _SERVICE = "sagemaker-runtime"


class InternalDependencyException(SageMakerRuntimeError):
    """Your request caused an exception with an internal dependency. Contact customer
    support.
    """

    _ERROR_CODE = "InternalDependencyException"


class InternalFailure(SageMakerRuntimeError):
    """An internal failure occurred."""
    _ERROR_CODE = "InternalFailure"


class InternalStreamFailure(SageMakerRuntimeError):
    """The stream processing failed because of an unknown error, exception or failure. Try
    your request again.
    """

    _ERROR_CODE = "InternalStreamFailure"


class ModelError(SageMakerRuntimeError):
    """Model (owned by the customer in the container) returned 4xx or 5xx error code."""
    _ERROR_CODE = "ModelError"

    @property
    def log_stream_arn(self) -> str | None:
        """The Amazon Resource Name (ARN) of the log stream."""
        return self.response.get("LogStreamArn")

    @property
    def original_message(self) -> str | None:
        """Original message."""
        return self.response.get("OriginalMessage")

    @property
    def original_status_code(self) -> int | None:
        """Original status code."""
        return self.response.get("OriginalStatusCode")


class ModelNotReadyException(SageMakerRuntimeError):
    """Either a serverless endpoint variant's resources are still being provisioned, or a
    multi-model endpoint is still downloading or loading the target model. Wait and try
    your request again.
    """

    _ERROR_CODE = "ModelNotReadyException"


class ModelStreamError(SageMakerRuntimeError):
    """An error occurred while streaming the response body. This error can have the
    following error codes: ModelInvocationTimeExceeded

    The model failed to finish sending the response within the timeout period allowed by
    Amazon SageMaker. StreamBroken

    The Transmission Control Protocol (TCP) connection between the client and the model
    was reset or closed.
    """

    _ERROR_CODE = "ModelStreamError"

    @property
    def error_code(self) -> str | None:
        """This error can have the following error codes: ModelInvocationTimeExceeded

        The model failed to finish sending the response within the timeout period
        allowed by Amazon SageMaker. StreamBroken

        The Transmission Control Protocol (TCP) connection between the client and the
        model was reset or closed.
        """
        return self.response.get("ErrorCode")


class ServiceUnavailable(SageMakerRuntimeError):
    """The service is unavailable. Try your call again."""
    _ERROR_CODE = "ServiceUnavailable"


class ValidationError(SageMakerRuntimeError):
    """Inspect your request and try again."""
    _ERROR_CODE = "ValidationError"


EXCEPTIONS: dict[str, type[SageMakerRuntimeError]] = {
    "InternalDependencyException": InternalDependencyException,
    "InternalFailure": InternalFailure,
    "InternalStreamFailure": InternalStreamFailure,
    "ModelError": ModelError,
    "ModelNotReadyException": ModelNotReadyException,
    "ModelStreamError": ModelStreamError,
    "ServiceUnavailable": ServiceUnavailable,
    "ValidationError": ValidationError,
}
