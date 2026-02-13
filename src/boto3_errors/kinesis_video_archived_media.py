# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class KinesisVideoArchivedMediaError(Boto3Error):
    _SERVICE = "kinesis-video-archived-media"


class ClientLimitExceededException(KinesisVideoArchivedMediaError):
    """Kinesis Video Streams has throttled the request because you have exceeded a limit.
    Try making the call later. For information about limits, see Kinesis Video Streams
    Limits.
    """

    _ERROR_CODE = "ClientLimitExceededException"


class InvalidArgumentException(KinesisVideoArchivedMediaError):
    """A specified parameter exceeds its restrictions, is not supported, or can't be used."""
    _ERROR_CODE = "InvalidArgumentException"


class InvalidCodecPrivateDataException(KinesisVideoArchivedMediaError):
    """The codec private data in at least one of the tracks of the video stream is not
    valid for this operation.
    """

    _ERROR_CODE = "InvalidCodecPrivateDataException"


class InvalidMediaFrameException(KinesisVideoArchivedMediaError):
    """One or more frames in the requested clip could not be parsed based on the specified
    codec.
    """

    _ERROR_CODE = "InvalidMediaFrameException"


class MissingCodecPrivateDataException(KinesisVideoArchivedMediaError):
    """No codec private data was found in at least one of tracks of the video stream."""
    _ERROR_CODE = "MissingCodecPrivateDataException"


class NoDataRetentionException(KinesisVideoArchivedMediaError):
    """`GetImages` was requested for a stream that does not retain data (that is, has a
    `DataRetentionInHours` of 0).
    """

    _ERROR_CODE = "NoDataRetentionException"


class NotAuthorizedException(KinesisVideoArchivedMediaError):
    """Status Code: 403, The caller is not authorized to perform an operation on the given
    stream, or the token has expired.
    """

    _ERROR_CODE = "NotAuthorizedException"


class ResourceNotFoundException(KinesisVideoArchivedMediaError):
    """`GetImages` will throw this error when Kinesis Video Streams can't find the stream
    that you specified.

     `GetHLSStreamingSessionURL` and `GetDASHStreamingSessionURL` throw this error if a
    session with a `PlaybackMode` of `ON_DEMAND` or `LIVE_REPLAY`is requested for a
    stream that has no fragments within the requested time range, or if a session with a
    `PlaybackMode` of `LIVE` is requested for a stream that has no fragments within the
    last 30 seconds.
    """

    _ERROR_CODE = "ResourceNotFoundException"


class UnsupportedStreamMediaTypeException(KinesisVideoArchivedMediaError):
    """The type of the media (for example, h.264 or h.265 video or ACC or G.711 audio)
    could not be determined from the codec IDs of the tracks in the first fragment for a
    playback session. The codec ID for track 1 should be `V_MPEG/ISO/AVC` and,
    optionally, the codec ID for track 2 should be `A_AAC`.
    """

    _ERROR_CODE = "UnsupportedStreamMediaTypeException"


EXCEPTIONS: dict[str, type[KinesisVideoArchivedMediaError]] = {
    "ClientLimitExceededException": ClientLimitExceededException,
    "InvalidArgumentException": InvalidArgumentException,
    "InvalidCodecPrivateDataException": InvalidCodecPrivateDataException,
    "InvalidMediaFrameException": InvalidMediaFrameException,
    "MissingCodecPrivateDataException": MissingCodecPrivateDataException,
    "NoDataRetentionException": NoDataRetentionException,
    "NotAuthorizedException": NotAuthorizedException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "UnsupportedStreamMediaTypeException": UnsupportedStreamMediaTypeException,
}
