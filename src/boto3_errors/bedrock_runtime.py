# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class BedrockRuntimeError(Boto3Error):
    _SERVICE = "bedrock-runtime"


class AccessDeniedException(BedrockRuntimeError):
    """The request is denied because you do not have sufficient permissions to perform the
    requested action. For troubleshooting this error, see AccessDeniedException in the
    Amazon Bedrock User Guide
    """

    _ERROR_CODE = "AccessDeniedException"


class ConflictException(BedrockRuntimeError):
    """Error occurred because of a conflict while performing an operation."""
    _ERROR_CODE = "ConflictException"


class InternalServerException(BedrockRuntimeError):
    """An internal server error occurred. For troubleshooting this error, see
    InternalFailure in the Amazon Bedrock User Guide
    """

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
    """The model specified in the request is not ready to serve inference requests. The AWS
    SDK will automatically retry the operation up to 5 times. For information about
    configuring automatic retries, see Retry behavior in the AWS SDKs and Tools
    reference guide.
    """

    _ERROR_CODE = "ModelNotReadyException"


class ModelStreamErrorException(BedrockRuntimeError):
    """An error occurred while streaming the response. Retry your request."""
    _ERROR_CODE = "ModelStreamErrorException"

    @property
    def original_status_code(self) -> int | None:
        """The original status code."""
        return self.response.get("originalStatusCode")

    @property
    def original_message(self) -> str | None:
        """The original message."""
        return self.response.get("originalMessage")


class ModelTimeoutException(BedrockRuntimeError):
    """The request took too long to process. Processing time exceeded the model timeout
    length.
    """

    _ERROR_CODE = "ModelTimeoutException"


class ResourceNotFoundException(BedrockRuntimeError):
    """The specified resource ARN was not found. For troubleshooting this error, see
    ResourceNotFound in the Amazon Bedrock User Guide
    """

    _ERROR_CODE = "ResourceNotFoundException"


class ServiceQuotaExceededException(BedrockRuntimeError):
    """Your request exceeds the service quota for your account. You can view your quotas at
    Viewing service quotas. You can resubmit your request later.
    """

    _ERROR_CODE = "ServiceQuotaExceededException"


class ServiceUnavailableException(BedrockRuntimeError):
    """The service isn't currently available. For troubleshooting this error, see
    ServiceUnavailable in the Amazon Bedrock User Guide
    """

    _ERROR_CODE = "ServiceUnavailableException"


class ThrottlingException(BedrockRuntimeError):
    """Your request was denied due to exceeding the account quotas for Amazon Bedrock. For
    troubleshooting this error, see ThrottlingException in the Amazon Bedrock User Guide
    """

    _ERROR_CODE = "ThrottlingException"


class ValidationException(BedrockRuntimeError):
    """The input fails to satisfy the constraints specified by Amazon Bedrock. For
    troubleshooting this error, see ValidationError in the Amazon Bedrock User Guide
    """

    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[BedrockRuntimeError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "ModelErrorException": ModelErrorException,
    "ModelNotReadyException": ModelNotReadyException,
    "ModelStreamErrorException": ModelStreamErrorException,
    "ModelTimeoutException": ModelTimeoutException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ServiceUnavailableException": ServiceUnavailableException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
