# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class DirectConnectError(Boto3Error):
    _SERVICE = "directconnect"


class DirectConnectClientException(DirectConnectError):
    """One or more parameters are not valid."""
    _ERROR_CODE = "DirectConnectClientException"


class DirectConnectServerException(DirectConnectError):
    """A server-side error occurred."""
    _ERROR_CODE = "DirectConnectServerException"


class DuplicateTagKeysException(DirectConnectError):
    """A tag key was specified more than once."""
    _ERROR_CODE = "DuplicateTagKeysException"


class LimitExceededException(DirectConnectError):
    """The rate limiter limit has been exceeded for the connection. You cannot add more
    rate limiters to virtual interfaces on this connection.
    """

    _ERROR_CODE = "LimitExceededException"


class TooManyTagsException(DirectConnectError):
    """You have reached the limit on the number of tags that can be assigned."""
    _ERROR_CODE = "TooManyTagsException"


EXCEPTIONS: dict[str, type[DirectConnectError]] = {
    "DirectConnectClientException": DirectConnectClientException,
    "DirectConnectServerException": DirectConnectServerException,
    "DuplicateTagKeysException": DuplicateTagKeysException,
    "LimitExceededException": LimitExceededException,
    "TooManyTagsException": TooManyTagsException,
}
