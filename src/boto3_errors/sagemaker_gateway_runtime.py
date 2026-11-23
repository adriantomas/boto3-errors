# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class SageMakerGatewayRuntimeError(Boto3Error):
    _SERVICE = "sagemaker-gateway-runtime"


class AccessDeniedException(SageMakerGatewayRuntimeError):
    """The caller is not authorized to invoke this gateway. Invoking requires the
    `sagemaker:InvokeGlobalInferenceGateway` permission, or
    `sagemaker:InvokeGlobalInferenceGatewayWithResponseStream` for the streaming
    operation, on the gateway ARN. A message starting `inference gateway` means the
    inference gateway serving the model refused the request with a 401 or 403, for
    example for its customer identity token. Its status code is in the message (the
    response status is 403), and up to 256 bytes of its error message are quoted.
    """

    _ERROR_CODE = "AccessDeniedException"


class BadGatewayException(SageMakerGatewayRuntimeError):
    """502 -- The gateway could not get a usable response from the inference gateway. The
    `Message` prefix says why:

    - `Global Inference Gateway: could not reach the inference gateway: <reason>` -- the
      request could not be sent, or the connection closed before a response arrived (for
      example, the connection failed, or the inference gateway closed it after reading
      the request).
    - `Global Inference Gateway: timed out waiting for the inference gateway` -- on the
      buffered operation, the inference gateway stopped sending partway through the
      response body and the gateway's read timeout expired. (The same text on a
      GatewayTimeoutException means no response arrived.)
    - Any other `Global Inference Gateway:` message -- the gateway ended a response
      before it was complete, for example because it exceeded the 10 MiB limit of the
      buffered operation, the request exceeded its maximum duration, or the inference
      gateway was taken out of service.
    - `inference gateway: <status> <message>` -- the inference gateway serving the model
      returned a 502, 500, 503 or another 5xx error. Its status code is in the message
      (the response status is 502), and up to 256 bytes of its error message are quoted.
    - `inference gateway: response ended unexpectedly` -- the inference gateway's
      connection failed while it was sending the response.

    The inference gateway names a component in the prefix when it reports one:
    `inference gateway (<component>):`, where the component is `config` (the inference
    gateway's configuration and proxy layer), `scheduler` (its request scheduler),
    `model selector` (its model selector) or `model server` (the model server).

    Not modeled as retryable: a 502 can mean the inference already ran, and the gateway
    may already have tried another inference gateway. Standard SDK retry modes may still
    retry a 5xx status, which would run (and bill) the inference again; set max attempts
    to 1 if a repeated inference is unacceptable.
    """

    _ERROR_CODE = "BadGatewayException"


class GatewayTimeoutException(SageMakerGatewayRuntimeError):
    """504 -- The inference gateway did not respond in time. The `Message` prefix says
    whose time limit expired:

    - `Global Inference Gateway: timed out waiting for the inference gateway` -- the
      gateway's limit on the wait for the first part of the response.
    - `inference gateway: <status> <message>` -- the inference gateway serving the model
      returned a 504, or a 408 because it timed out waiting for the request to arrive.
      Its status code is in the message (the response status is 504), and up to 256
      bytes of its error message are quoted.

    The inference gateway names a component in the prefix when it reports one:
    `inference gateway (<component>):`, where the component is `config` (the inference
    gateway's configuration and proxy layer), `scheduler` (its request scheduler),
    `model selector` (its model selector) or `model server` (the model server).

    Not modeled as retryable: a timeout does not prove the inference did not run, and
    the gateway may already have tried another inference gateway. Standard SDK retry
    modes may still retry a 5xx status, which could run (and bill) the inference again;
    set max attempts to 1 if a repeated inference is unacceptable.
    """

    _ERROR_CODE = "GatewayTimeoutException"


class InternalServerException(SageMakerGatewayRuntimeError):
    """An unexpected internal failure occurred."""
    _ERROR_CODE = "InternalServerException"


class InternalStreamFailure(SageMakerGatewayRuntimeError):
    """A failure after the stream started. The `Message` says where it came from: `Global
    Inference Gateway:` when a gateway time limit expired or the inference gateway was
    taken out of service, or `inference gateway: response ended unexpectedly` when the
    inference gateway's connection failed while it was sending the response. The stream
    ends after this event.
    """

    _ERROR_CODE = "InternalStreamFailure"


class ModelStreamError(SageMakerGatewayRuntimeError):
    """Reserved for a model error during the stream. Not currently sent; a failure after
    the stream starts is reported as InternalStreamFailure.
    """

    _ERROR_CODE = "ModelStreamError"

    @property
    def error_code(self) -> str | None:
        """The error code: `StreamBroken` if the model server's stream broke before it
        completed, or `ModelInvocationTimeExceeded` if the model exceeded its allowed
        invocation time.
        """
        return self.response.get("ErrorCode")


class PayloadTooLargeException(SageMakerGatewayRuntimeError):
    """The request body exceeds the 10 MiB limit. Reduce the size of the payload and send
    the request again.
    """

    _ERROR_CODE = "PayloadTooLargeException"


class ResourceNotFoundException(SageMakerGatewayRuntimeError):
    """No gateway with this ID exists in this account and Region, or no target of the
    gateway serves the model named in the request body. A model that is served but has
    no available target right now returns ServiceUnavailableException instead. A message
    starting `inference gateway` means the inference gateway serving the model returned
    a 404; up to 256 bytes of its error message are quoted.
    """

    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def resource_id(self) -> str | None:
        """The ID of the resource that was not found: the gateway ID, or the model name."""
        return self.response.get("ResourceId")

    @property
    def resource_type(self) -> str | None:
        """The kind of resource that was not found: the gateway, or the model."""
        return self.response.get("ResourceType")


class ServiceUnavailableException(SageMakerGatewayRuntimeError):
    """The service is temporarily unable to serve the request, for example because no
    capacity is available for the requested model. The request was not dispatched for
    inference. A 503 returned by the inference gateway serving the model after dispatch
    is reported as BadGatewayException, with the 503 in its `Message`, not as this
    error.
    """

    _ERROR_CODE = "ServiceUnavailableException"


class ThrottlingException(SageMakerGatewayRuntimeError):
    """The request was throttled before it was dispatched for inference. Retry the request
    with backoff, after the `Retry-After` seconds when the response carries one. A
    message starting `inference gateway` means the last inference gateway tried for the
    model returned a 429. The gateway may have tried others first, and they may have
    failed for other reasons. Up to 256 bytes of its error message are quoted.
    """

    _ERROR_CODE = "ThrottlingException"


EXCEPTIONS: dict[str, type[SageMakerGatewayRuntimeError]] = {
    "AccessDeniedException": AccessDeniedException,
    "BadGatewayException": BadGatewayException,
    "GatewayTimeoutException": GatewayTimeoutException,
    "InternalServerException": InternalServerException,
    "InternalStreamFailure": InternalStreamFailure,
    "ModelStreamError": ModelStreamError,
    "PayloadTooLargeException": PayloadTooLargeException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceUnavailableException": ServiceUnavailableException,
    "ThrottlingException": ThrottlingException,
}
