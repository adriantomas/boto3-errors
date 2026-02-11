# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class DetectiveError(Boto3Error):
    _SERVICE = "detective"


class AccessDeniedException(DetectiveError):
    """The request issuer does not have permission to access this resource or perform this
    operation.
    """

    _ERROR_CODE = "AccessDeniedException"

    @property
    def error_code(self) -> str | None:
        """The SDK default error code associated with the access denied exception."""
        return self.response.get("ErrorCode")

    @property
    def error_code_reason(self) -> str | None:
        """The SDK default explanation of why access was denied."""
        return self.response.get("ErrorCodeReason")

    @property
    def sub_error_code(self) -> str | None:
        """The error code associated with the access denied exception."""
        return self.response.get("SubErrorCode")

    @property
    def sub_error_code_reason(self) -> str | None:
        """An explanation of why access was denied."""
        return self.response.get("SubErrorCodeReason")


class ConflictException(DetectiveError):
    """The request attempted an invalid action."""
    _ERROR_CODE = "ConflictException"


class InternalServerException(DetectiveError):
    """The request was valid but failed because of a problem with the service."""
    _ERROR_CODE = "InternalServerException"


class ResourceNotFoundException(DetectiveError):
    """The request refers to a nonexistent resource."""
    _ERROR_CODE = "ResourceNotFoundException"


class ServiceQuotaExceededException(DetectiveError):
    """This request cannot be completed for one of the following reasons.

    - This request cannot be completed if it would cause the number of member accounts
      in the behavior graph to exceed the maximum allowed. A behavior graph cannot have
      more than 1,200 member accounts.
    - This request cannot be completed if the current volume ingested is above the limit
      of 10 TB per day. Detective will not allow you to add additional member accounts.
    """

    _ERROR_CODE = "ServiceQuotaExceededException"

    @property
    def resources(self) -> list[Any] | None:
        """The type of resource that has exceeded the service quota."""
        return self.response.get("Resources")


class TooManyRequestsException(DetectiveError):
    """The request cannot be completed because too many other requests are occurring at the
    same time.
    """

    _ERROR_CODE = "TooManyRequestsException"


class ValidationException(DetectiveError):
    """The request parameters are invalid."""
    _ERROR_CODE = "ValidationException"

    @property
    def error_code(self) -> str | None:
        """The error code associated with the validation failure."""
        return self.response.get("ErrorCode")

    @property
    def error_code_reason(self) -> str | None:
        """An explanation of why validation failed."""
        return self.response.get("ErrorCodeReason")


EXCEPTIONS: dict[str, type[DetectiveError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "TooManyRequestsException": TooManyRequestsException,
    "ValidationException": ValidationException,
}
