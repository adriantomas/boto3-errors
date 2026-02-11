# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class KinesisVideoMediaError(Boto3Error):
    _SERVICE = "kinesis-video-media"


class ClientLimitExceededException(KinesisVideoMediaError):
    """Kinesis Video Streams has throttled the request because you have exceeded the limit
    of allowed client calls. Try making the call later.
    """

    _ERROR_CODE = "ClientLimitExceededException"


class ConnectionLimitExceededException(KinesisVideoMediaError):
    """Kinesis Video Streams has throttled the request because you have exceeded the limit
    of allowed client connections.
    """

    _ERROR_CODE = "ConnectionLimitExceededException"


class InvalidArgumentException(KinesisVideoMediaError):
    """The value for this input parameter is invalid."""
    _ERROR_CODE = "InvalidArgumentException"


class InvalidEndpointException(KinesisVideoMediaError):
    """Status Code: 400, Caller used wrong endpoint to write data to a stream. On receiving
    such an exception, the user must call `GetDataEndpoint` with `AccessMode` set to
    "READ" and use the endpoint Kinesis Video returns in the next `GetMedia` call.
    """

    _ERROR_CODE = "InvalidEndpointException"


class NotAuthorizedException(KinesisVideoMediaError):
    """Status Code: 403, The caller is not authorized to perform an operation on the given
    stream, or the token has expired.
    """

    _ERROR_CODE = "NotAuthorizedException"


class ResourceNotFoundException(KinesisVideoMediaError):
    """Status Code: 404, The stream with the given name does not exist."""
    _ERROR_CODE = "ResourceNotFoundException"


EXCEPTIONS: dict[str, type[KinesisVideoMediaError]] = {
    "ClientLimitExceededException": ClientLimitExceededException,
    "ConnectionLimitExceededException": ConnectionLimitExceededException,
    "InvalidArgumentException": InvalidArgumentException,
    "InvalidEndpointException": InvalidEndpointException,
    "NotAuthorizedException": NotAuthorizedException,
    "ResourceNotFoundException": ResourceNotFoundException,
}
