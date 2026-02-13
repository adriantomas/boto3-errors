# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class InspectorScanError(Boto3Error):
    _SERVICE = "inspector-scan"


class AccessDeniedException(InspectorScanError):
    """You do not have sufficient access to perform this action."""
    _ERROR_CODE = "AccessDeniedException"


class InternalServerException(InspectorScanError):
    """The request processing has failed because of an unknown error, exception or failure."""
    _ERROR_CODE = "InternalServerException"

    @property
    def reason(self) -> str | None:
        """The reason for the validation failure."""
        return self.response.get("reason")

    @property
    def retry_after_seconds(self) -> int | None:
        """The number of seconds to wait before retrying the request."""
        return self.response.get("retryAfterSeconds")


class ThrottlingException(InspectorScanError):
    """The request was denied due to request throttling."""
    _ERROR_CODE = "ThrottlingException"

    @property
    def retry_after_seconds(self) -> int | None:
        """The number of seconds to wait before retrying the request."""
        return self.response.get("retryAfterSeconds")


class ValidationException(InspectorScanError):
    """The request has failed validation due to missing required fields or having invalid
    inputs.
    """

    _ERROR_CODE = "ValidationException"

    @property
    def reason(self) -> str | None:
        """The reason for the validation failure."""
        return self.response.get("reason")

    @property
    def fields(self) -> list[Any] | None:
        """The fields that failed validation."""
        return self.response.get("fields")


EXCEPTIONS: dict[str, type[InspectorScanError]] = {
    "AccessDeniedException": AccessDeniedException,
    "InternalServerException": InternalServerException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
