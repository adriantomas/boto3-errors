# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class KinesisVideoWebRTCStorageError(Boto3Error):
    _SERVICE = "kinesis-video-webrtc-storage"


class AccessDeniedException(KinesisVideoWebRTCStorageError):
    """You do not have required permissions to perform this operation."""
    _ERROR_CODE = "AccessDeniedException"


class ClientLimitExceededException(KinesisVideoWebRTCStorageError):
    """Kinesis Video Streams has throttled the request because you have exceeded the limit
    of allowed client calls. Try making the call later.
    """

    _ERROR_CODE = "ClientLimitExceededException"


class InvalidArgumentException(KinesisVideoWebRTCStorageError):
    """The value for this input parameter is invalid."""
    _ERROR_CODE = "InvalidArgumentException"


class ResourceNotFoundException(KinesisVideoWebRTCStorageError):
    """The specified resource is not found."""
    _ERROR_CODE = "ResourceNotFoundException"


EXCEPTIONS: dict[str, type[KinesisVideoWebRTCStorageError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ClientLimitExceededException": ClientLimitExceededException,
    "InvalidArgumentException": InvalidArgumentException,
    "ResourceNotFoundException": ResourceNotFoundException,
}
