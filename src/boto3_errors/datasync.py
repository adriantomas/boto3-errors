# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class DataSyncError(Boto3Error):
    _SERVICE = "datasync"


class InternalException(DataSyncError):
    """This exception is thrown when an error occurs in the DataSync service."""
    _ERROR_CODE = "InternalException"

    @property
    def error_code(self) -> str | None:
        return self.response.get("errorCode")


class InvalidRequestException(DataSyncError):
    """This exception is thrown when the client submits a malformed request."""
    _ERROR_CODE = "InvalidRequestException"

    @property
    def error_code(self) -> str | None:
        return self.response.get("errorCode")

    @property
    def datasync_error_code(self) -> str | None:
        return self.response.get("datasyncErrorCode")


EXCEPTIONS: dict[str, type[DataSyncError]] = {
    "InternalException": InternalException,
    "InvalidRequestException": InvalidRequestException,
}
