# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class MTurkError(Boto3Error):
    _SERVICE = "mturk"


class RequestError(MTurkError):
    """Your request is invalid."""
    _ERROR_CODE = "RequestError"

    @property
    def turk_error_code(self) -> str | None:
        return self.response.get("TurkErrorCode")


class ServiceFault(MTurkError):
    """Amazon Mechanical Turk is temporarily unable to process your request. Try your call
    again.
    """

    _ERROR_CODE = "ServiceFault"

    @property
    def turk_error_code(self) -> str | None:
        return self.response.get("TurkErrorCode")


EXCEPTIONS: dict[str, type[MTurkError]] = {
    "RequestError": RequestError,
    "ServiceFault": ServiceFault,
}
