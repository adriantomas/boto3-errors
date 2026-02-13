# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class BedrockError(Boto3Error):
    _SERVICE = "bedrock"


class AccessDeniedException(BedrockError):
    """The request is denied because of missing access permissions."""
    _ERROR_CODE = "AccessDeniedException"


class ConflictException(BedrockError):
    """Error occurred because of a conflict while performing an operation."""
    _ERROR_CODE = "ConflictException"


class InternalServerException(BedrockError):
    """An internal server error occurred. Retry your request."""
    _ERROR_CODE = "InternalServerException"


class ResourceInUseException(BedrockError):
    """Thrown when attempting to delete or modify a resource that is currently being used
    by other resources or operations. For example, trying to delete an Automated
    Reasoning policy that is referenced by an active guardrail.
    """

    _ERROR_CODE = "ResourceInUseException"


class ResourceNotFoundException(BedrockError):
    """The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon
    Resource Name (ARN) and try your request again.
    """

    _ERROR_CODE = "ResourceNotFoundException"


class ServiceQuotaExceededException(BedrockError):
    """The number of requests exceeds the service quota. Resubmit your request later."""
    _ERROR_CODE = "ServiceQuotaExceededException"


class ServiceUnavailableException(BedrockError):
    """Returned if the service cannot complete the request."""
    _ERROR_CODE = "ServiceUnavailableException"


class ThrottlingException(BedrockError):
    """The number of requests exceeds the limit. Resubmit your request later."""
    _ERROR_CODE = "ThrottlingException"


class TooManyTagsException(BedrockError):
    """The request contains more tags than can be associated with a resource (50 tags per
    resource). The maximum number of tags includes both existing tags and those included
    in your current request.
    """

    _ERROR_CODE = "TooManyTagsException"

    @property
    def resource_name(self) -> str | None:
        """The name of the resource with too many tags."""
        return self.response.get("resourceName")


class ValidationException(BedrockError):
    """Input validation failed. Check your request parameters and retry the request."""
    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[BedrockError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "ResourceInUseException": ResourceInUseException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ServiceUnavailableException": ServiceUnavailableException,
    "ThrottlingException": ThrottlingException,
    "TooManyTagsException": TooManyTagsException,
    "ValidationException": ValidationException,
}
