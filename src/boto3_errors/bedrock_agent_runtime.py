# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class BedrockAgentRuntimeError(Boto3Error):
    _SERVICE = "bedrock-agent-runtime"


class AccessDeniedException(BedrockAgentRuntimeError):
    """This exception is thrown when a request is denied per access permissions"""
    _ERROR_CODE = "AccessDeniedException"


class BadGatewayException(BedrockAgentRuntimeError):
    """This exception is thrown when a request fails due to dependency like Lambda,
    Bedrock, STS resource
    """

    _ERROR_CODE = "BadGatewayException"

    @property
    def resource_name(self) -> str | None:
        return self.response.get("resourceName")


class ConflictException(BedrockAgentRuntimeError):
    """This exception is thrown when there is a conflict performing an operation"""
    _ERROR_CODE = "ConflictException"


class DependencyFailedException(BedrockAgentRuntimeError):
    """This exception is thrown when a request fails due to dependency like Lambda,
    Bedrock, STS resource due to a customer fault (i.e. bad configuration)
    """

    _ERROR_CODE = "DependencyFailedException"

    @property
    def resource_name(self) -> str | None:
        return self.response.get("resourceName")


class InternalServerException(BedrockAgentRuntimeError):
    """This exception is thrown if there was an unexpected error during processing of
    request
    """

    _ERROR_CODE = "InternalServerException"


class ResourceNotFoundException(BedrockAgentRuntimeError):
    """This exception is thrown when a resource referenced by the operation does not exist"""
    _ERROR_CODE = "ResourceNotFoundException"


class ServiceQuotaExceededException(BedrockAgentRuntimeError):
    """This exception is thrown when a request is made beyond the service quota"""
    _ERROR_CODE = "ServiceQuotaExceededException"


class ThrottlingException(BedrockAgentRuntimeError):
    """This exception is thrown when the number of requests exceeds the limit"""
    _ERROR_CODE = "ThrottlingException"


class ValidationException(BedrockAgentRuntimeError):
    """This exception is thrown when the request's input validation fails"""
    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[BedrockAgentRuntimeError]] = {
    "AccessDeniedException": AccessDeniedException,
    "BadGatewayException": BadGatewayException,
    "ConflictException": ConflictException,
    "DependencyFailedException": DependencyFailedException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
