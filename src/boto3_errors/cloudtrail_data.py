# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class CloudTrailDataError(Boto3Error):
    _SERVICE = "cloudtrail-data"


class ChannelInsufficientPermission(CloudTrailDataError):
    """The caller's account ID must be the same as the channel owner's account ID."""
    _ERROR_CODE = "ChannelInsufficientPermission"


class ChannelNotFound(CloudTrailDataError):
    """The channel could not be found."""
    _ERROR_CODE = "ChannelNotFound"


class ChannelUnsupportedSchema(CloudTrailDataError):
    """The schema type of the event is not supported."""
    _ERROR_CODE = "ChannelUnsupportedSchema"


class DuplicatedAuditEventId(CloudTrailDataError):
    """Two or more entries in the request have the same event ID."""
    _ERROR_CODE = "DuplicatedAuditEventId"


class InvalidChannelARN(CloudTrailDataError):
    """The specified channel ARN is not a valid channel ARN."""
    _ERROR_CODE = "InvalidChannelARN"


class UnsupportedOperationException(CloudTrailDataError):
    """The operation requested is not supported in this region or account."""
    _ERROR_CODE = "UnsupportedOperationException"


EXCEPTIONS: dict[str, type[CloudTrailDataError]] = {
    "ChannelInsufficientPermission": ChannelInsufficientPermission,
    "ChannelNotFound": ChannelNotFound,
    "ChannelUnsupportedSchema": ChannelUnsupportedSchema,
    "DuplicatedAuditEventId": DuplicatedAuditEventId,
    "InvalidChannelARN": InvalidChannelARN,
    "UnsupportedOperationException": UnsupportedOperationException,
}
