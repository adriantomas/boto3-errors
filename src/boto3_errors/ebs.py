# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class EBSError(Boto3Error):
    _SERVICE = "ebs"


class AccessDeniedException(EBSError):
    """You do not have sufficient access to perform this action."""
    _ERROR_CODE = "AccessDeniedException"

    @property
    def reason(self) -> str | None:
        """The reason for the exception."""
        return self.response.get("Reason")


class ConcurrentLimitExceededException(EBSError):
    """You have reached the limit for concurrent API requests. For more information, see
    Optimizing performance of the EBS direct APIs in the Amazon Elastic Compute Cloud
    User Guide.
    """

    _ERROR_CODE = "ConcurrentLimitExceededException"


class ConflictException(EBSError):
    """The request uses the same client token as a previous, but non-identical request."""
    _ERROR_CODE = "ConflictException"


class InternalServerException(EBSError):
    """An internal error has occurred. For more information see Error retries."""
    _ERROR_CODE = "InternalServerException"


class RequestThrottledException(EBSError):
    """The number of API requests has exceeded the maximum allowed API request throttling
    limit for the snapshot. For more information see Error retries.
    """

    _ERROR_CODE = "RequestThrottledException"

    @property
    def reason(self) -> str | None:
        """The reason for the exception."""
        return self.response.get("Reason")


class ResourceNotFoundException(EBSError):
    """The specified resource does not exist."""
    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def reason(self) -> str | None:
        """The reason for the exception."""
        return self.response.get("Reason")


class ServiceQuotaExceededException(EBSError):
    """Your current service quotas do not allow you to perform this action."""
    _ERROR_CODE = "ServiceQuotaExceededException"

    @property
    def reason(self) -> str | None:
        """The reason for the exception."""
        return self.response.get("Reason")


class ValidationException(EBSError):
    """The input fails to satisfy the constraints of the EBS direct APIs."""
    _ERROR_CODE = "ValidationException"

    @property
    def reason(self) -> str | None:
        """The reason for the validation exception."""
        return self.response.get("Reason")


EXCEPTIONS: dict[str, type[EBSError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConcurrentLimitExceededException": ConcurrentLimitExceededException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "RequestThrottledException": RequestThrottledException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ValidationException": ValidationException,
}
