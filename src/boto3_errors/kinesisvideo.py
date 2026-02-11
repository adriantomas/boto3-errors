# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class KinesisVideoError(Boto3Error):
    _SERVICE = "kinesisvideo"


class AccessDeniedException(KinesisVideoError):
    """You do not have required permissions to perform this operation."""
    _ERROR_CODE = "AccessDeniedException"


class AccountChannelLimitExceededException(KinesisVideoError):
    """You have reached the maximum limit of active signaling channels for this Amazon Web
    Services account in this region.
    """

    _ERROR_CODE = "AccountChannelLimitExceededException"


class AccountStreamLimitExceededException(KinesisVideoError):
    """The number of streams created for the account is too high."""
    _ERROR_CODE = "AccountStreamLimitExceededException"


class ClientLimitExceededException(KinesisVideoError):
    """Kinesis Video Streams has throttled the request because you have exceeded the limit
    of allowed client calls. Try making the call later.
    """

    _ERROR_CODE = "ClientLimitExceededException"


class DeviceStreamLimitExceededException(KinesisVideoError):
    """Not implemented."""
    _ERROR_CODE = "DeviceStreamLimitExceededException"


class InvalidArgumentException(KinesisVideoError):
    """The value for this input parameter is invalid."""
    _ERROR_CODE = "InvalidArgumentException"


class InvalidDeviceException(KinesisVideoError):
    """Not implemented."""
    _ERROR_CODE = "InvalidDeviceException"


class InvalidResourceFormatException(KinesisVideoError):
    """The format of the `StreamARN` is invalid."""
    _ERROR_CODE = "InvalidResourceFormatException"


class NoDataRetentionException(KinesisVideoError):
    """The Stream data retention in hours is equal to zero."""
    _ERROR_CODE = "NoDataRetentionException"


class NotAuthorizedException(KinesisVideoError):
    """The caller is not authorized to perform this operation."""
    _ERROR_CODE = "NotAuthorizedException"


class ResourceInUseException(KinesisVideoError):
    """When the input `StreamARN` or `ChannelARN` in `CLOUD_STORAGE_MODE` is already mapped
    to a different Kinesis Video Stream resource, or if the provided input `StreamARN`
    or `ChannelARN` is not in Active status, try one of the following :
    - The `DescribeMediaStorageConfiguration` API to determine what the stream given
      channel is mapped to.
    - The `DescribeMappedResourceConfiguration` API to determine the channel that the
      given stream is mapped to.
    - The `DescribeStream` or `DescribeSignalingChannel` API to determine the status of
      the resource.
    """

    _ERROR_CODE = "ResourceInUseException"


class ResourceNotFoundException(KinesisVideoError):
    """Amazon Kinesis Video Streams can't find the stream that you specified."""
    _ERROR_CODE = "ResourceNotFoundException"


class StreamEdgeConfigurationNotFoundException(KinesisVideoError):
    """The Exception rendered when the Amazon Kinesis Video Stream can't find a stream's
    edge configuration that you specified.
    """

    _ERROR_CODE = "StreamEdgeConfigurationNotFoundException"


class TagsPerResourceExceededLimitException(KinesisVideoError):
    """You have exceeded the limit of tags that you can associate with the resource. A
    Kinesis video stream can support up to 50 tags.
    """

    _ERROR_CODE = "TagsPerResourceExceededLimitException"


class VersionMismatchException(KinesisVideoError):
    """The stream version that you specified is not the latest version. To get the latest
    version, use the DescribeStream API.
    """

    _ERROR_CODE = "VersionMismatchException"


EXCEPTIONS: dict[str, type[KinesisVideoError]] = {
    "AccessDeniedException": AccessDeniedException,
    "AccountChannelLimitExceededException": AccountChannelLimitExceededException,
    "AccountStreamLimitExceededException": AccountStreamLimitExceededException,
    "ClientLimitExceededException": ClientLimitExceededException,
    "DeviceStreamLimitExceededException": DeviceStreamLimitExceededException,
    "InvalidArgumentException": InvalidArgumentException,
    "InvalidDeviceException": InvalidDeviceException,
    "InvalidResourceFormatException": InvalidResourceFormatException,
    "NoDataRetentionException": NoDataRetentionException,
    "NotAuthorizedException": NotAuthorizedException,
    "ResourceInUseException": ResourceInUseException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "StreamEdgeConfigurationNotFoundException": StreamEdgeConfigurationNotFoundException,
    "TagsPerResourceExceededLimitException": TagsPerResourceExceededLimitException,
    "VersionMismatchException": VersionMismatchException,
}
