# Auto-generated. Do not edit manually.
from __future__ import annotations

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


class TooManyTagsException(DirectConnectError):
    """You have reached the limit on the number of tags that can be assigned."""
    _ERROR_CODE = "TooManyTagsException"


EXCEPTIONS: dict[str, type[DirectConnectError]] = {
    "DirectConnectClientException": DirectConnectClientException,
    "DirectConnectServerException": DirectConnectServerException,
    "DuplicateTagKeysException": DuplicateTagKeysException,
    "TooManyTagsException": TooManyTagsException,
}
