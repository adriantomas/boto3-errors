# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class TranscribeError(Boto3Error):
    _SERVICE = "transcribe"


class BadRequestException(TranscribeError):
    """Your request didn't pass one or more validation tests. This can occur when a
    parameter has an invalid value, when you combine parameters in a way that isn't
    supported, when the entity you're trying to delete doesn't exist, or if it's in a
    non-terminal state (such as `IN PROGRESS`). See the exception message field for more
    information.
    """

    _ERROR_CODE = "BadRequestException"

    @property
    def reason(self) -> str | None:
        """A code that identifies why the audio in your request was rejected. Currently,
        `TranscribeAudio` returns this field, and only for problems with your audio. It
        isn't returned for other validation errors.

        Possible values:

        - `audioTooLong`: The audio is longer than the maximum duration of 1 hour.
        - `audioTooShort`: The audio is shorter than 0.5 seconds.
        - `audioFileTooLarge`: The audio is larger than the maximum size.
        - `unsupportedAudioFormat`: The media format isn't supported.
        - `unsupportedChannelCount`: You enabled `ChannelIdentification` and the audio
          has more than two channels.
        - `invalidAudio`: Amazon Transcribe couldn't decode the audio.
        - `mediaDownloadFailed`: Amazon Transcribe couldn't download the audio at your
          `MediaFileUri`.
        """
        return self.response.get("Reason")


class ConflictException(TranscribeError):
    """A resource already exists with this name. Resource names must be unique within an
    Amazon Web Services account.
    """

    _ERROR_CODE = "ConflictException"


class InternalFailureException(TranscribeError):
    """There was an internal error. Check the error message, correct the issue, and try
    your request again.
    """

    _ERROR_CODE = "InternalFailureException"


class LimitExceededException(TranscribeError):
    """You've either sent too many requests or your input file is too long. Wait before
    retrying your request, or use a smaller file and try your request again.
    """

    _ERROR_CODE = "LimitExceededException"


class NotFoundException(TranscribeError):
    """We can't find the requested resource. Check that the specified name is correct and
    try your request again.
    """

    _ERROR_CODE = "NotFoundException"


EXCEPTIONS: dict[str, type[TranscribeError]] = {
    "BadRequestException": BadRequestException,
    "ConflictException": ConflictException,
    "InternalFailureException": InternalFailureException,
    "LimitExceededException": LimitExceededException,
    "NotFoundException": NotFoundException,
}
