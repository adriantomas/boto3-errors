# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class CostOptimizationHubError(Boto3Error):
    _SERVICE = "cost-optimization-hub"


class AccessDeniedException(CostOptimizationHubError):
    """You are not authorized to use this operation with the given parameters."""
    _ERROR_CODE = "AccessDeniedException"


class InternalServerException(CostOptimizationHubError):
    """An error on the server occurred during the processing of your request. Try again
    later.
    """

    _ERROR_CODE = "InternalServerException"


class ResourceNotFoundException(CostOptimizationHubError):
    """The specified Amazon Resource Name (ARN) in the request doesn't exist."""
    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def resource_id(self) -> str | None:
        """The identifier of the resource that was not found."""
        return self.response.get("resourceId")


class ThrottlingException(CostOptimizationHubError):
    """The request was denied due to request throttling."""
    _ERROR_CODE = "ThrottlingException"


class ValidationException(CostOptimizationHubError):
    """The input fails to satisfy the constraints specified by an Amazon Web Services
    service.
    """

    _ERROR_CODE = "ValidationException"

    @property
    def reason(self) -> str | None:
        """The reason for the validation exception."""
        return self.response.get("reason")

    @property
    def fields(self) -> list[Any] | None:
        """The list of fields that are invalid."""
        return self.response.get("fields")


EXCEPTIONS: dict[str, type[CostOptimizationHubError]] = {
    "AccessDeniedException": AccessDeniedException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
