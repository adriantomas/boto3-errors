# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class BatchError(Boto3Error):
    _SERVICE = "batch"


class ClientException(BatchError):
    """These errors are usually caused by a client action. One example cause is using an
    action or resource on behalf of a user that doesn't have permissions to use the
    action or resource. Another cause is specifying an identifier that's not valid.
    """

    _ERROR_CODE = "ClientException"


class ServerException(BatchError):
    """These errors are usually caused by a server issue."""
    _ERROR_CODE = "ServerException"


EXCEPTIONS: dict[str, type[BatchError]] = {
    "ClientException": ClientException,
    "ServerException": ServerException,
}
