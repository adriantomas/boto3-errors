# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class BedrockRuntimeError(Boto3Error):
    _SERVICE = "bedrock-runtime"


class AccessDeniedException(BedrockRuntimeError):
    """The request is denied because of missing access permissions."""
    _ERROR_CODE = "AccessDeniedException"


class InternalServerException(BedrockRuntimeError):
    """An internal server error occurred. Retry your request."""
    _ERROR_CODE = "InternalServerException"


class ModelErrorException(BedrockRuntimeError):
    """The request failed due to an error while processing the model."""
    _ERROR_CODE = "ModelErrorException"

    @property
    def original_status_code(self) -> int | None:
        """The original status code."""
        return self.response.get("originalStatusCode")

    @property
    def resource_name(self) -> str | None:
        """The resource name."""
        return self.response.get("resourceName")


class ModelNotReadyException(BedrockRuntimeError):
    """The model specified in the request is not ready to serve inference requests."""
    _ERROR_CODE = "ModelNotReadyException"


class ModelStreamErrorException(BedrockRuntimeError):
    """An error occurred while streaming the response."""
    _ERROR_CODE = "ModelStreamErrorException"

    @property
    def original_message(self) -> str | None:
        """The original message."""
        return self.response.get("originalMessage")

    @property
    def original_status_code(self) -> int | None:
        """The original status code."""
        return self.response.get("originalStatusCode")


class ModelTimeoutException(BedrockRuntimeError):
    """The request took too long to process. Processing time exceeded the model timeout
    length.
    """

    _ERROR_CODE = "ModelTimeoutException"


class ResourceNotFoundException(BedrockRuntimeError):
    """The specified resource ARN was not found. Check the ARN and try your request again."""
    _ERROR_CODE = "ResourceNotFoundException"


class ServiceQuotaExceededException(BedrockRuntimeError):
    """The number of requests exceeds the service quota. Resubmit your request later."""
    _ERROR_CODE = "ServiceQuotaExceededException"


class ThrottlingException(BedrockRuntimeError):
    """The number of requests exceeds the limit. Resubmit your request later."""
    _ERROR_CODE = "ThrottlingException"


class ValidationException(BedrockRuntimeError):
    """Input validation failed. Check your request parameters and retry the request."""
    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[BedrockRuntimeError]] = {
    "AccessDeniedException": AccessDeniedException,
    "InternalServerException": InternalServerException,
    "ModelErrorException": ModelErrorException,
    "ModelNotReadyException": ModelNotReadyException,
    "ModelStreamErrorException": ModelStreamErrorException,
    "ModelTimeoutException": ModelTimeoutException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
