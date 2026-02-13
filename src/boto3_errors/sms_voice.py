# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class PinpointSMSVoiceError(Boto3Error):
    _SERVICE = "sms-voice"


class AlreadyExistsException(PinpointSMSVoiceError):
    """The resource specified in your request already exists."""
    _ERROR_CODE = "AlreadyExistsException"


class BadRequestException(PinpointSMSVoiceError):
    """The input you provided is invalid."""
    _ERROR_CODE = "BadRequestException"


class InternalServiceErrorException(PinpointSMSVoiceError):
    """The API encountered an unexpected error and couldn't complete the request. You might
    be able to successfully issue the request again in the future.
    """

    _ERROR_CODE = "InternalServiceErrorException"


class LimitExceededException(PinpointSMSVoiceError):
    """There are too many instances of the specified resource type."""
    _ERROR_CODE = "LimitExceededException"


class NotFoundException(PinpointSMSVoiceError):
    """The resource you attempted to access doesn't exist."""
    _ERROR_CODE = "NotFoundException"


class TooManyRequestsException(PinpointSMSVoiceError):
    """You've issued too many requests to the resource. Wait a few minutes, and then try
    again.
    """

    _ERROR_CODE = "TooManyRequestsException"


EXCEPTIONS: dict[str, type[PinpointSMSVoiceError]] = {
    "AlreadyExistsException": AlreadyExistsException,
    "BadRequestException": BadRequestException,
    "InternalServiceErrorException": InternalServiceErrorException,
    "LimitExceededException": LimitExceededException,
    "NotFoundException": NotFoundException,
    "TooManyRequestsException": TooManyRequestsException,
}
