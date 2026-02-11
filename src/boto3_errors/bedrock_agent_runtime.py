# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class BedrockAgentRuntimeError(Boto3Error):
    _SERVICE = "bedrock-agent-runtime"


class AccessDeniedException(BedrockAgentRuntimeError):
    """The request is denied because of missing access permissions. Check your permissions
    and retry your request.
    """

    _ERROR_CODE = "AccessDeniedException"


class BadGatewayException(BedrockAgentRuntimeError):
    """There was an issue with a dependency due to a server issue. Retry your request."""
    _ERROR_CODE = "BadGatewayException"

    @property
    def resource_name(self) -> str | None:
        """The name of the dependency that caused the issue, such as Amazon Bedrock,
        Lambda, or STS.
        """
        return self.response.get("resourceName")


class ConflictException(BedrockAgentRuntimeError):
    """There was a conflict performing an operation. Resolve the conflict and retry your
    request.
    """

    _ERROR_CODE = "ConflictException"


class DependencyFailedException(BedrockAgentRuntimeError):
    """There was an issue with a dependency. Check the resource configurations and retry
    the request.
    """

    _ERROR_CODE = "DependencyFailedException"

    @property
    def resource_name(self) -> str | None:
        """The name of the dependency that caused the issue, such as Amazon Bedrock,
        Lambda, or STS.
        """
        return self.response.get("resourceName")


class InternalServerException(BedrockAgentRuntimeError):
    """An internal server error occurred. Retry your request."""
    _ERROR_CODE = "InternalServerException"

    @property
    def reason(self) -> str | None:
        """The reason for the exception. If the reason is
        `BEDROCK_MODEL_INVOCATION_SERVICE_UNAVAILABLE`, the model invocation service is
        unavailable. Retry your request.
        """
        return self.response.get("reason")


class ModelNotReadyException(BedrockAgentRuntimeError):
    """The model specified in the request is not ready to serve inference requests. The AWS
    SDK will automatically retry the operation up to 5 times. For information about
    configuring automatic retries, see Retry behavior in the AWS SDKs and Tools
    reference guide.
    """

    _ERROR_CODE = "ModelNotReadyException"


class ResourceNotFoundException(BedrockAgentRuntimeError):
    """The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon
    Resource Name (ARN) and try your request again.
    """

    _ERROR_CODE = "ResourceNotFoundException"


class ServiceQuotaExceededException(BedrockAgentRuntimeError):
    """The number of requests exceeds the service quota. Resubmit your request later."""
    _ERROR_CODE = "ServiceQuotaExceededException"


class ThrottlingException(BedrockAgentRuntimeError):
    """The number of requests exceeds the limit. Resubmit your request later."""
    _ERROR_CODE = "ThrottlingException"


class ValidationException(BedrockAgentRuntimeError):
    """Input validation failed. Check your request parameters and retry the request."""
    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[BedrockAgentRuntimeError]] = {
    "AccessDeniedException": AccessDeniedException,
    "BadGatewayException": BadGatewayException,
    "ConflictException": ConflictException,
    "DependencyFailedException": DependencyFailedException,
    "InternalServerException": InternalServerException,
    "ModelNotReadyException": ModelNotReadyException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
