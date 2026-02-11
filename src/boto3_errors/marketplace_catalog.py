# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class MarketplaceCatalogError(Boto3Error):
    _SERVICE = "marketplace-catalog"


class AccessDeniedException(MarketplaceCatalogError):
    """Access is denied.

    HTTP status code: 403
    """

    _ERROR_CODE = "AccessDeniedException"


class InternalServiceException(MarketplaceCatalogError):
    """There was an internal service exception.

    HTTP status code: 500
    """

    _ERROR_CODE = "InternalServiceException"


class ResourceInUseException(MarketplaceCatalogError):
    """The resource is currently in use."""
    _ERROR_CODE = "ResourceInUseException"


class ResourceNotFoundException(MarketplaceCatalogError):
    """The specified resource wasn't found.

    HTTP status code: 404
    """

    _ERROR_CODE = "ResourceNotFoundException"


class ResourceNotSupportedException(MarketplaceCatalogError):
    """Currently, the specified resource is not supported."""
    _ERROR_CODE = "ResourceNotSupportedException"


class ServiceQuotaExceededException(MarketplaceCatalogError):
    """The maximum number of open requests per account has been exceeded."""
    _ERROR_CODE = "ServiceQuotaExceededException"


class ThrottlingException(MarketplaceCatalogError):
    """Too many requests.

    HTTP status code: 429
    """

    _ERROR_CODE = "ThrottlingException"


class ValidationException(MarketplaceCatalogError):
    """An error occurred during validation.

    HTTP status code: 422
    """

    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[MarketplaceCatalogError]] = {
    "AccessDeniedException": AccessDeniedException,
    "InternalServiceException": InternalServiceException,
    "ResourceInUseException": ResourceInUseException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ResourceNotSupportedException": ResourceNotSupportedException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
