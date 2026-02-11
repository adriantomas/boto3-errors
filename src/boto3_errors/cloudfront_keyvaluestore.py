# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class CloudFrontKeyValueStoreError(Boto3Error):
    _SERVICE = "cloudfront-keyvaluestore"


class AccessDeniedException(CloudFrontKeyValueStoreError):
    """Access denied."""
    _ERROR_CODE = "AccessDeniedException"


class ConflictException(CloudFrontKeyValueStoreError):
    """Resource is not in expected state."""
    _ERROR_CODE = "ConflictException"


class InternalServerException(CloudFrontKeyValueStoreError):
    """Internal server error."""
    _ERROR_CODE = "InternalServerException"


class ResourceNotFoundException(CloudFrontKeyValueStoreError):
    """Resource was not found."""
    _ERROR_CODE = "ResourceNotFoundException"


class ServiceQuotaExceededException(CloudFrontKeyValueStoreError):
    """Limit exceeded."""
    _ERROR_CODE = "ServiceQuotaExceededException"


class ValidationException(CloudFrontKeyValueStoreError):
    """Validation failed."""
    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[CloudFrontKeyValueStoreError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ValidationException": ValidationException,
}
