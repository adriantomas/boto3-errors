# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class ComprehendError(Boto3Error):
    _SERVICE = "comprehend"


class BatchSizeLimitExceededException(ComprehendError):
    """The number of documents in the request exceeds the limit of 25. Try your request
    again with fewer documents.
    """

    _ERROR_CODE = "BatchSizeLimitExceededException"


class ConcurrentModificationException(ComprehendError):
    """Concurrent modification of the tags associated with an Amazon Comprehend resource is
    not supported.
    """

    _ERROR_CODE = "ConcurrentModificationException"


class InternalServerException(ComprehendError):
    """An internal server error occurred. Retry your request."""
    _ERROR_CODE = "InternalServerException"


class InvalidFilterException(ComprehendError):
    """The filter specified for the operation is invalid. Specify a different filter."""
    _ERROR_CODE = "InvalidFilterException"


class InvalidRequestException(ComprehendError):
    """The request is invalid."""
    _ERROR_CODE = "InvalidRequestException"

    @property
    def reason(self) -> str | None:
        return self.response.get("Reason")

    @property
    def detail(self) -> dict[str, Any] | None:
        return self.response.get("Detail")


class JobNotFoundException(ComprehendError):
    """The specified job was not found. Check the job ID and try again."""
    _ERROR_CODE = "JobNotFoundException"


class KmsKeyValidationException(ComprehendError):
    """The KMS customer managed key (CMK) entered cannot be validated. Verify the key and
    re-enter it.
    """

    _ERROR_CODE = "KmsKeyValidationException"


class ResourceInUseException(ComprehendError):
    """The specified resource name is already in use. Use a different name and try your
    request again.
    """

    _ERROR_CODE = "ResourceInUseException"


class ResourceLimitExceededException(ComprehendError):
    """The maximum number of resources per account has been exceeded. Review the resources,
    and then try your request again.
    """

    _ERROR_CODE = "ResourceLimitExceededException"


class ResourceNotFoundException(ComprehendError):
    """The specified resource ARN was not found. Check the ARN and try your request again."""
    _ERROR_CODE = "ResourceNotFoundException"


class ResourceUnavailableException(ComprehendError):
    """The specified resource is not available. Check the resource and try your request
    again.
    """

    _ERROR_CODE = "ResourceUnavailableException"


class TextSizeLimitExceededException(ComprehendError):
    """The size of the input text exceeds the limit. Use a smaller document."""
    _ERROR_CODE = "TextSizeLimitExceededException"


class TooManyRequestsException(ComprehendError):
    """The number of requests exceeds the limit. Resubmit your request later."""
    _ERROR_CODE = "TooManyRequestsException"


class TooManyTagKeysException(ComprehendError):
    """The request contains more tag keys than can be associated with a resource (50 tag
    keys per resource).
    """

    _ERROR_CODE = "TooManyTagKeysException"


class TooManyTagsException(ComprehendError):
    """The request contains more tags than can be associated with a resource (50 tags per
    resource). The maximum number of tags includes both existing tags and those included
    in your current request.
    """

    _ERROR_CODE = "TooManyTagsException"


class UnsupportedLanguageException(ComprehendError):
    """Amazon Comprehend can't process the language of the input text. For a list of
    supported languages, Supported languages in the Comprehend Developer Guide.
    """

    _ERROR_CODE = "UnsupportedLanguageException"


EXCEPTIONS: dict[str, type[ComprehendError]] = {
    "BatchSizeLimitExceededException": BatchSizeLimitExceededException,
    "ConcurrentModificationException": ConcurrentModificationException,
    "InternalServerException": InternalServerException,
    "InvalidFilterException": InvalidFilterException,
    "InvalidRequestException": InvalidRequestException,
    "JobNotFoundException": JobNotFoundException,
    "KmsKeyValidationException": KmsKeyValidationException,
    "ResourceInUseException": ResourceInUseException,
    "ResourceLimitExceededException": ResourceLimitExceededException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ResourceUnavailableException": ResourceUnavailableException,
    "TextSizeLimitExceededException": TextSizeLimitExceededException,
    "TooManyRequestsException": TooManyRequestsException,
    "TooManyTagKeysException": TooManyTagKeysException,
    "TooManyTagsException": TooManyTagsException,
    "UnsupportedLanguageException": UnsupportedLanguageException,
}
