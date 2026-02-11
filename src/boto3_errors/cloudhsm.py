# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class CloudHSMError(Boto3Error):
    _SERVICE = "cloudhsm"


class CloudHsmInternalException(CloudHSMError):
    """Indicates that an internal error occurred."""
    _ERROR_CODE = "CloudHsmInternalException"


class CloudHsmServiceException(CloudHSMError):
    """Indicates that an exception occurred in the AWS CloudHSM service."""
    _ERROR_CODE = "CloudHsmServiceException"

    @property
    def retryable(self) -> bool | None:
        """Indicates if the action can be retried."""
        return self.response.get("retryable")


class InvalidRequestException(CloudHSMError):
    """Indicates that one or more of the request parameters are not valid."""
    _ERROR_CODE = "InvalidRequestException"


EXCEPTIONS: dict[str, type[CloudHSMError]] = {
    "CloudHsmInternalException": CloudHsmInternalException,
    "CloudHsmServiceException": CloudHsmServiceException,
    "InvalidRequestException": InvalidRequestException,
}
