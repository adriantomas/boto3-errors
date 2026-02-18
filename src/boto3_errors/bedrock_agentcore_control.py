# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class BedrockAgentCoreControlError(Boto3Error):
    _SERVICE = "bedrock-agentcore-control"


class AccessDeniedException(BedrockAgentCoreControlError):
    """This exception is thrown when a request is denied per access permissions"""
    _ERROR_CODE = "AccessDeniedException"


class ConcurrentModificationException(BedrockAgentCoreControlError):
    """Exception thrown when a resource is modified concurrently by multiple requests."""
    _ERROR_CODE = "ConcurrentModificationException"


class ConflictException(BedrockAgentCoreControlError):
    """This exception is thrown when there is a conflict performing an operation"""
    _ERROR_CODE = "ConflictException"


class DecryptionFailure(BedrockAgentCoreControlError):
    """Exception thrown when decryption of a secret fails."""
    _ERROR_CODE = "DecryptionFailure"


class EncryptionFailure(BedrockAgentCoreControlError):
    """Exception thrown when encryption of a secret fails."""
    _ERROR_CODE = "EncryptionFailure"


class InternalServerException(BedrockAgentCoreControlError):
    """This exception is thrown if there was an unexpected error during processing of
    request
    """

    _ERROR_CODE = "InternalServerException"


class ResourceLimitExceededException(BedrockAgentCoreControlError):
    """Exception thrown when a resource limit is exceeded."""
    _ERROR_CODE = "ResourceLimitExceededException"


class ResourceNotFoundException(BedrockAgentCoreControlError):
    """This exception is thrown when a resource referenced by the operation does not exist"""
    _ERROR_CODE = "ResourceNotFoundException"


class ServiceException(BedrockAgentCoreControlError):
    """An internal error occurred."""
    _ERROR_CODE = "ServiceException"


class ServiceQuotaExceededException(BedrockAgentCoreControlError):
    """This exception is thrown when a request is made beyond the service quota"""
    _ERROR_CODE = "ServiceQuotaExceededException"


class ThrottledException(BedrockAgentCoreControlError):
    """API rate limit has been exceeded."""
    _ERROR_CODE = "ThrottledException"


class ThrottlingException(BedrockAgentCoreControlError):
    """This exception is thrown when the number of requests exceeds the limit"""
    _ERROR_CODE = "ThrottlingException"


class UnauthorizedException(BedrockAgentCoreControlError):
    """This exception is thrown when the JWT bearer token is invalid or not found for OAuth
    bearer token based access
    """

    _ERROR_CODE = "UnauthorizedException"


class ValidationException(BedrockAgentCoreControlError):
    """The input fails to satisfy the constraints specified by the service."""
    _ERROR_CODE = "ValidationException"

    @property
    def field_list(self) -> list[Any] | None:
        return self.response.get("fieldList")

    @property
    def reason(self) -> str | None:
        return self.response.get("reason")


EXCEPTIONS: dict[str, type[BedrockAgentCoreControlError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConcurrentModificationException": ConcurrentModificationException,
    "ConflictException": ConflictException,
    "DecryptionFailure": DecryptionFailure,
    "EncryptionFailure": EncryptionFailure,
    "InternalServerException": InternalServerException,
    "ResourceLimitExceededException": ResourceLimitExceededException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceException": ServiceException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottledException": ThrottledException,
    "ThrottlingException": ThrottlingException,
    "UnauthorizedException": UnauthorizedException,
    "ValidationException": ValidationException,
}
