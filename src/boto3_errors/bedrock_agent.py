# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class BedrockAgentError(Boto3Error):
    _SERVICE = "bedrock-agent"


class AccessDeniedException(BedrockAgentError):
    """This exception is thrown when a request is denied per access permissions"""
    _ERROR_CODE = "AccessDeniedException"


class ConflictException(BedrockAgentError):
    """This exception is thrown when there is a conflict performing an operation"""
    _ERROR_CODE = "ConflictException"


class InternalServerException(BedrockAgentError):
    """This exception is thrown if there was an unexpected error during processing of
    request
    """

    _ERROR_CODE = "InternalServerException"


class ResourceNotFoundException(BedrockAgentError):
    """This exception is thrown when a resource referenced by the operation does not exist"""
    _ERROR_CODE = "ResourceNotFoundException"


class ServiceQuotaExceededException(BedrockAgentError):
    """This exception is thrown when a request is made beyond the service quota"""
    _ERROR_CODE = "ServiceQuotaExceededException"


class ThrottlingException(BedrockAgentError):
    """This exception is thrown when the number of requests exceeds the limit"""
    _ERROR_CODE = "ThrottlingException"


class ValidationException(BedrockAgentError):
    """This exception is thrown when the request's input validation fails"""
    _ERROR_CODE = "ValidationException"

    @property
    def field_list(self) -> list[Any] | None:
        return self.response.get("fieldList")


EXCEPTIONS: dict[str, type[BedrockAgentError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
