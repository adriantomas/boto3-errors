# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class PollyError(Boto3Error):
    _SERVICE = "polly"


class EngineNotSupportedException(PollyError):
    """This engine is not compatible with the voice that you have designated. Choose a new
    voice that is compatible with the engine or change the engine and restart the
    operation.
    """

    _ERROR_CODE = "EngineNotSupportedException"


class InvalidLexiconException(PollyError):
    """Amazon Polly can't find the specified lexicon. Verify that the lexicon's name is
    spelled correctly, and then try again.
    """

    _ERROR_CODE = "InvalidLexiconException"


class InvalidNextTokenException(PollyError):
    """The NextToken is invalid. Verify that it's spelled correctly, and then try again."""
    _ERROR_CODE = "InvalidNextTokenException"


class InvalidS3BucketException(PollyError):
    """The provided Amazon S3 bucket name is invalid. Please check your input with S3
    bucket naming requirements and try again.
    """

    _ERROR_CODE = "InvalidS3BucketException"


class InvalidS3KeyException(PollyError):
    """The provided Amazon S3 key prefix is invalid. Please provide a valid S3 object key
    name.
    """

    _ERROR_CODE = "InvalidS3KeyException"


class InvalidSampleRateException(PollyError):
    """The specified sample rate is not valid."""
    _ERROR_CODE = "InvalidSampleRateException"


class InvalidSnsTopicArnException(PollyError):
    """The provided SNS topic ARN is invalid. Please provide a valid SNS topic ARN and try
    again.
    """

    _ERROR_CODE = "InvalidSnsTopicArnException"


class InvalidSsmlException(PollyError):
    """The SSML you provided is invalid. Verify the SSML syntax, spelling of tags and
    values, and then try again.
    """

    _ERROR_CODE = "InvalidSsmlException"


class InvalidTaskIdException(PollyError):
    """The provided Task ID is not valid. Please provide a valid Task ID and try again."""
    _ERROR_CODE = "InvalidTaskIdException"


class LanguageNotSupportedException(PollyError):
    """The language specified is not currently supported by Amazon Polly in this capacity."""
    _ERROR_CODE = "LanguageNotSupportedException"


class LexiconNotFoundException(PollyError):
    """Amazon Polly can't find the specified lexicon. This could be caused by a lexicon
    that is missing, its name is misspelled or specifying a lexicon that is in a
    different region.

    Verify that the lexicon exists, is in the region (see ListLexicons) and that you
    spelled its name is spelled correctly. Then try again.
    """

    _ERROR_CODE = "LexiconNotFoundException"


class LexiconSizeExceededException(PollyError):
    """The maximum size of the specified lexicon would be exceeded by this operation."""
    _ERROR_CODE = "LexiconSizeExceededException"


class MarksNotSupportedForFormatException(PollyError):
    """Speech marks are not supported for the `OutputFormat` selected. Speech marks are
    only available for content in `json` format.
    """

    _ERROR_CODE = "MarksNotSupportedForFormatException"


class MaxLexemeLengthExceededException(PollyError):
    """The maximum size of the lexeme would be exceeded by this operation."""
    _ERROR_CODE = "MaxLexemeLengthExceededException"


class MaxLexiconsNumberExceededException(PollyError):
    """The maximum number of lexicons would be exceeded by this operation."""
    _ERROR_CODE = "MaxLexiconsNumberExceededException"


class ServiceFailureException(PollyError):
    """An unknown condition has caused a service failure."""
    _ERROR_CODE = "ServiceFailureException"


class SsmlMarksNotSupportedForTextTypeException(PollyError):
    """SSML speech marks are not supported for plain text-type input."""
    _ERROR_CODE = "SsmlMarksNotSupportedForTextTypeException"


class SynthesisTaskNotFoundException(PollyError):
    """The Speech Synthesis task with requested Task ID cannot be found."""
    _ERROR_CODE = "SynthesisTaskNotFoundException"


class TextLengthExceededException(PollyError):
    """The value of the "Text" parameter is longer than the accepted limits. For the
    `SynthesizeSpeech` API, the limit for input text is a maximum of 6000 characters
    total, of which no more than 3000 can be billed characters. For the
    `StartSpeechSynthesisTask` API, the maximum is 200,000 characters, of which no more
    than 100,000 can be billed characters. SSML tags are not counted as billed
    characters.
    """

    _ERROR_CODE = "TextLengthExceededException"


class UnsupportedPlsAlphabetException(PollyError):
    """The alphabet specified by the lexicon is not a supported alphabet. Valid values are
    `x-sampa` and `ipa`.
    """

    _ERROR_CODE = "UnsupportedPlsAlphabetException"


class UnsupportedPlsLanguageException(PollyError):
    """The language specified in the lexicon is unsupported. For a list of supported
    languages, see Lexicon Attributes.
    """

    _ERROR_CODE = "UnsupportedPlsLanguageException"


EXCEPTIONS: dict[str, type[PollyError]] = {
    "EngineNotSupportedException": EngineNotSupportedException,
    "InvalidLexiconException": InvalidLexiconException,
    "InvalidNextTokenException": InvalidNextTokenException,
    "InvalidS3BucketException": InvalidS3BucketException,
    "InvalidS3KeyException": InvalidS3KeyException,
    "InvalidSampleRateException": InvalidSampleRateException,
    "InvalidSnsTopicArnException": InvalidSnsTopicArnException,
    "InvalidSsmlException": InvalidSsmlException,
    "InvalidTaskIdException": InvalidTaskIdException,
    "LanguageNotSupportedException": LanguageNotSupportedException,
    "LexiconNotFoundException": LexiconNotFoundException,
    "LexiconSizeExceededException": LexiconSizeExceededException,
    "MarksNotSupportedForFormatException": MarksNotSupportedForFormatException,
    "MaxLexemeLengthExceededException": MaxLexemeLengthExceededException,
    "MaxLexiconsNumberExceededException": MaxLexiconsNumberExceededException,
    "ServiceFailureException": ServiceFailureException,
    "SsmlMarksNotSupportedForTextTypeException": SsmlMarksNotSupportedForTextTypeException,
    "SynthesisTaskNotFoundException": SynthesisTaskNotFoundException,
    "TextLengthExceededException": TextLengthExceededException,
    "UnsupportedPlsAlphabetException": UnsupportedPlsAlphabetException,
    "UnsupportedPlsLanguageException": UnsupportedPlsLanguageException,
}
