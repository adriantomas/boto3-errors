# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class ComprehendMedicalError(Boto3Error):
    _SERVICE = "comprehendmedical"


class InternalServerException(ComprehendMedicalError):
    """An internal server error occurred. Retry your request."""
    _ERROR_CODE = "InternalServerException"


class InvalidEncodingException(ComprehendMedicalError):
    """The input text was not in valid UTF-8 character encoding. Check your text then retry
    your request.
    """

    _ERROR_CODE = "InvalidEncodingException"


class InvalidRequestException(ComprehendMedicalError):
    """The request that you made is invalid. Check your request to determine why it's
    invalid and then retry the request.
    """

    _ERROR_CODE = "InvalidRequestException"


class ResourceNotFoundException(ComprehendMedicalError):
    """The resource identified by the specified Amazon Resource Name (ARN) was not found.
    Check the ARN and try your request again.
    """

    _ERROR_CODE = "ResourceNotFoundException"


class ServiceUnavailableException(ComprehendMedicalError):
    """The Amazon Comprehend Medical service is temporarily unavailable. Please wait and
    then retry your request.
    """

    _ERROR_CODE = "ServiceUnavailableException"


class TextSizeLimitExceededException(ComprehendMedicalError):
    """The size of the text you submitted exceeds the size limit. Reduce the size of the
    text or use a smaller document and then retry your request.
    """

    _ERROR_CODE = "TextSizeLimitExceededException"


class TooManyRequestsException(ComprehendMedicalError):
    """You have made too many requests within a short period of time. Wait for a short time
    and then try your request again. Contact customer support for more information about
    a service limit increase.
    """

    _ERROR_CODE = "TooManyRequestsException"


class ValidationException(ComprehendMedicalError):
    """The filter that you specified for the operation is invalid. Check the filter values
    that you entered and try your request again.
    """

    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[ComprehendMedicalError]] = {
    "InternalServerException": InternalServerException,
    "InvalidEncodingException": InvalidEncodingException,
    "InvalidRequestException": InvalidRequestException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceUnavailableException": ServiceUnavailableException,
    "TextSizeLimitExceededException": TextSizeLimitExceededException,
    "TooManyRequestsException": TooManyRequestsException,
    "ValidationException": ValidationException,
}
