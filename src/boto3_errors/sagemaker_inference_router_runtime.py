# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class SageMakerInferenceRouterRuntimeError(Boto3Error):
    _SERVICE = "sagemaker-inference-router-runtime"


class AccessDeniedException(SageMakerInferenceRouterRuntimeError):
    """You don't have permission to perform this action. Check that the caller is allowed
    to invoke the inference router and every destination of the routing target.
    """

    _ERROR_CODE = "AccessDeniedException"


class InternalDependencyException(SageMakerInferenceRouterRuntimeError):
    """The request failed because of an error in an internal dependency. Retry the request
    with exponential backoff.
    """

    _ERROR_CODE = "InternalDependencyException"


class InternalFailure(SageMakerInferenceRouterRuntimeError):
    """An internal error occurred. Retry the request with exponential backoff. The Amazon
    Web Services SDKs and the Amazon Web Services CLI do this by default.
    """

    _ERROR_CODE = "InternalFailure"


class ModelError(SageMakerInferenceRouterRuntimeError):
    """The model in the destination that served the request returned an error. Check
    `OriginalStatusCode`, `OriginalMessage`, and the destination's logs in Amazon
    CloudWatch.
    """

    _ERROR_CODE = "ModelError"

    @property
    def log_stream_arn(self) -> str | None:
        """The Amazon Resource Name (ARN) of the Amazon CloudWatch log stream for the
        destination that served the request.
        """
        return self.response.get("LogStreamArn")

    @property
    def original_message(self) -> str | None:
        """The error message that the model container returned."""
        return self.response.get("OriginalMessage")

    @property
    def original_status_code(self) -> int | None:
        """The HTTP status code that the model container returned."""
        return self.response.get("OriginalStatusCode")


class ModelNotReadyException(SageMakerInferenceRouterRuntimeError):
    """The destination isn't ready to serve the model, for example because an inference
    component has no copies. Retry the request later.
    """

    _ERROR_CODE = "ModelNotReadyException"


class RequestTimeoutException(SageMakerInferenceRouterRuntimeError):
    """The inference router didn't receive the complete request within 300 seconds of
    accepting it, for example because of a very slow upload. Retry the request.
    """

    _ERROR_CODE = "RequestTimeoutException"


class ServiceUnavailableException(SageMakerInferenceRouterRuntimeError):
    """The service is temporarily unavailable. For example, no destination of the routing
    target could serve the request, or a destination didn't respond. Retry the request
    with exponential backoff. The Amazon Web Services SDKs and the Amazon Web Services
    CLI do this by default.
    """

    _ERROR_CODE = "ServiceUnavailableException"


class ThrottlingException(SageMakerInferenceRouterRuntimeError):
    """The request was denied because you exceeded the request rate for the inference
    router, or because a destination throttled the request. Retry the request with
    exponential backoff.
    """

    _ERROR_CODE = "ThrottlingException"


class ValidationException(SageMakerInferenceRouterRuntimeError):
    """The request isn't valid. Check the inference router name, the routing target name,
    and the request parameters, and then try again.
    """

    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[SageMakerInferenceRouterRuntimeError]] = {
    "AccessDeniedException": AccessDeniedException,
    "InternalDependencyException": InternalDependencyException,
    "InternalFailure": InternalFailure,
    "ModelError": ModelError,
    "ModelNotReadyException": ModelNotReadyException,
    "RequestTimeoutException": RequestTimeoutException,
    "ServiceUnavailableException": ServiceUnavailableException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
