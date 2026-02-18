# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class BedrockAgentError(Boto3Error):
    _SERVICE = "bedrock-agent"


class AccessDeniedException(BedrockAgentError):
    """The request is denied because of missing access permissions."""
    _ERROR_CODE = "AccessDeniedException"


class ConflictException(BedrockAgentError):
    """There was a conflict performing an operation."""
    _ERROR_CODE = "ConflictException"


class InternalServerException(BedrockAgentError):
    """An internal server error occurred. Retry your request."""
    _ERROR_CODE = "InternalServerException"


class ResourceNotFoundException(BedrockAgentError):
    """The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon
    Resource Name (ARN) and try your request again.
    """

    _ERROR_CODE = "ResourceNotFoundException"


class ServiceQuotaExceededException(BedrockAgentError):
    """The number of requests exceeds the service quota. Resubmit your request later."""
    _ERROR_CODE = "ServiceQuotaExceededException"


class ThrottlingException(BedrockAgentError):
    """The number of requests exceeds the limit. Resubmit your request later."""
    _ERROR_CODE = "ThrottlingException"


class ValidationException(BedrockAgentError):
    """Input validation failed. Check your request parameters and retry the request."""
    _ERROR_CODE = "ValidationException"

    @property
    def field_list(self) -> list[Any] | None:
        """A list of objects containing fields that caused validation errors and their
        corresponding validation error messages.
        """
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
