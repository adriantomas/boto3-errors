# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class EMRError(Boto3Error):
    _SERVICE = "emr"


class InternalServerError(EMRError):
    """Indicates that an error occurred while processing the request and that the request
    was not completed.
    """

    _ERROR_CODE = "InternalServerError"


class InternalServerException(EMRError):
    """This exception occurs when there is an internal failure in the Amazon EMR service."""
    _ERROR_CODE = "InternalServerException"


class InvalidRequestException(EMRError):
    """This exception occurs when there is something wrong with user input."""
    _ERROR_CODE = "InvalidRequestException"

    @property
    def error_code(self) -> str | None:
        """The error code associated with the exception."""
        return self.response.get("ErrorCode")


EXCEPTIONS: dict[str, type[EMRError]] = {
    "InternalServerError": InternalServerError,
    "InternalServerException": InternalServerException,
    "InvalidRequestException": InvalidRequestException,
}
