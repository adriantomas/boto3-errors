# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class TranslateError(Boto3Error):
    _SERVICE = "translate"


class ConcurrentModificationException(TranslateError):
    """Another modification is being made. That modification must complete before you can
    make your change.
    """

    _ERROR_CODE = "ConcurrentModificationException"


class ConflictException(TranslateError):
    """There was a conflict processing the request. Try your request again."""
    _ERROR_CODE = "ConflictException"


class DetectedLanguageLowConfidenceException(TranslateError):
    """The confidence that Amazon Comprehend accurately detected the source language is
    low. If a low confidence level is acceptable for your application, you can use the
    language in the exception to call Amazon Translate again. For more information, see
    the DetectDominantLanguage operation in the Amazon Comprehend Developer Guide.
    """

    _ERROR_CODE = "DetectedLanguageLowConfidenceException"

    @property
    def detected_language_code(self) -> str | None:
        """The language code of the auto-detected language from Amazon Comprehend."""
        return self.response.get("DetectedLanguageCode")


class InternalServerException(TranslateError):
    """An internal server error occurred. Retry your request."""
    _ERROR_CODE = "InternalServerException"


class InvalidFilterException(TranslateError):
    """The filter specified for the operation is not valid. Specify a different filter."""
    _ERROR_CODE = "InvalidFilterException"


class InvalidParameterValueException(TranslateError):
    """The value of the parameter is not valid. Review the value of the parameter you are
    using to correct it, and then retry your operation.
    """

    _ERROR_CODE = "InvalidParameterValueException"


class InvalidRequestException(TranslateError):
    """The request that you made is not valid. Check your request to determine why it's not
    valid and then retry the request.
    """

    _ERROR_CODE = "InvalidRequestException"


class LimitExceededException(TranslateError):
    """The specified limit has been exceeded. Review your request and retry it with a
    quantity below the stated limit.
    """

    _ERROR_CODE = "LimitExceededException"


class ResourceNotFoundException(TranslateError):
    """The resource you are looking for has not been found. Review the resource you're
    looking for and see if a different resource will accomplish your needs before
    retrying the revised request.
    """

    _ERROR_CODE = "ResourceNotFoundException"


class ServiceUnavailableException(TranslateError):
    """The Amazon Translate service is temporarily unavailable. Wait a bit and then retry
    your request.
    """

    _ERROR_CODE = "ServiceUnavailableException"


class TextSizeLimitExceededException(TranslateError):
    """The size of the text you submitted exceeds the size limit. Reduce the size of the
    text or use a smaller document and then retry your request.
    """

    _ERROR_CODE = "TextSizeLimitExceededException"


class TooManyRequestsException(TranslateError):
    """You have made too many requests within a short period of time. Wait for a short time
    and then try your request again.
    """

    _ERROR_CODE = "TooManyRequestsException"


class TooManyTagsException(TranslateError):
    """You have added too many tags to this resource. The maximum is 50 tags."""
    _ERROR_CODE = "TooManyTagsException"

    @property
    def resource_arn(self) -> str | None:
        return self.response.get("ResourceArn")


class UnsupportedDisplayLanguageCodeException(TranslateError):
    """Requested display language code is not supported."""
    _ERROR_CODE = "UnsupportedDisplayLanguageCodeException"

    @property
    def display_language_code(self) -> str | None:
        """Language code passed in with the request."""
        return self.response.get("DisplayLanguageCode")


class UnsupportedLanguagePairException(TranslateError):
    """Amazon Translate does not support translation from the language of the source text
    into the requested target language. For more information, see Supported languages.
    """

    _ERROR_CODE = "UnsupportedLanguagePairException"

    @property
    def source_language_code(self) -> str | None:
        """The language code for the language of the input text."""
        return self.response.get("SourceLanguageCode")

    @property
    def target_language_code(self) -> str | None:
        """The language code for the language of the translated text."""
        return self.response.get("TargetLanguageCode")


EXCEPTIONS: dict[str, type[TranslateError]] = {
    "ConcurrentModificationException": ConcurrentModificationException,
    "ConflictException": ConflictException,
    "DetectedLanguageLowConfidenceException": DetectedLanguageLowConfidenceException,
    "InternalServerException": InternalServerException,
    "InvalidFilterException": InvalidFilterException,
    "InvalidParameterValueException": InvalidParameterValueException,
    "InvalidRequestException": InvalidRequestException,
    "LimitExceededException": LimitExceededException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceUnavailableException": ServiceUnavailableException,
    "TextSizeLimitExceededException": TextSizeLimitExceededException,
    "TooManyRequestsException": TooManyRequestsException,
    "TooManyTagsException": TooManyTagsException,
    "UnsupportedDisplayLanguageCodeException": UnsupportedDisplayLanguageCodeException,
    "UnsupportedLanguagePairException": UnsupportedLanguagePairException,
}
