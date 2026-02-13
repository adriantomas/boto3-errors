# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class KinesisVideoSignalingError(Boto3Error):
    _SERVICE = "kinesis-video-signaling"


class ClientLimitExceededException(KinesisVideoSignalingError):
    """Your request was throttled because you have exceeded the limit of allowed client
    calls. Try making the call later.
    """

    _ERROR_CODE = "ClientLimitExceededException"


class InvalidArgumentException(KinesisVideoSignalingError):
    """The value for this input parameter is invalid."""
    _ERROR_CODE = "InvalidArgumentException"


class InvalidClientException(KinesisVideoSignalingError):
    """The specified client is invalid."""
    _ERROR_CODE = "InvalidClientException"


class NotAuthorizedException(KinesisVideoSignalingError):
    """The caller is not authorized to perform this operation."""
    _ERROR_CODE = "NotAuthorizedException"


class ResourceNotFoundException(KinesisVideoSignalingError):
    """The specified resource is not found."""
    _ERROR_CODE = "ResourceNotFoundException"


class SessionExpiredException(KinesisVideoSignalingError):
    """If the client session is expired. Once the client is connected, the session is valid
    for 45 minutes. Client should reconnect to the channel to continue sending/receiving
    messages.
    """

    _ERROR_CODE = "SessionExpiredException"


EXCEPTIONS: dict[str, type[KinesisVideoSignalingError]] = {
    "ClientLimitExceededException": ClientLimitExceededException,
    "InvalidArgumentException": InvalidArgumentException,
    "InvalidClientException": InvalidClientException,
    "NotAuthorizedException": NotAuthorizedException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "SessionExpiredException": SessionExpiredException,
}
