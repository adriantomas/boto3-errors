# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class MarketplaceDeploymentError(Boto3Error):
    _SERVICE = "marketplace-deployment"


class AccessDeniedException(MarketplaceDeploymentError):
    """You do not have sufficient access to perform this action."""
    _ERROR_CODE = "AccessDeniedException"


class ConflictException(MarketplaceDeploymentError):
    """The request configuration has conflicts. For details, see the accompanying error
    message.
    """

    _ERROR_CODE = "ConflictException"

    @property
    def resource_id(self) -> str | None:
        """The unique identifier for the resource associated with the error."""
        return self.response.get("resourceId")


class InternalServerException(MarketplaceDeploymentError):
    """There was an internal service exception."""
    _ERROR_CODE = "InternalServerException"


class ResourceNotFoundException(MarketplaceDeploymentError):
    """The specified resource wasn't found."""
    _ERROR_CODE = "ResourceNotFoundException"


class ServiceQuotaExceededException(MarketplaceDeploymentError):
    """The maximum number of requests per account has been exceeded."""
    _ERROR_CODE = "ServiceQuotaExceededException"


class ThrottlingException(MarketplaceDeploymentError):
    """Too many requests."""
    _ERROR_CODE = "ThrottlingException"


class ValidationException(MarketplaceDeploymentError):
    """An error occurred during validation."""
    _ERROR_CODE = "ValidationException"

    @property
    def field_name(self) -> str | None:
        """The field name associated with the error."""
        return self.response.get("fieldName")


EXCEPTIONS: dict[str, type[MarketplaceDeploymentError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
