# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class SageMakerFeatureStoreRuntimeError(Boto3Error):
    _SERVICE = "sagemaker-featurestore-runtime"


class AccessForbidden(SageMakerFeatureStoreRuntimeError):
    """You do not have permission to perform an action."""
    _ERROR_CODE = "AccessForbidden"


class InternalFailure(SageMakerFeatureStoreRuntimeError):
    """An internal failure occurred. Try your request again. If the problem persists,
    contact Amazon Web Services customer support.
    """

    _ERROR_CODE = "InternalFailure"


class ResourceNotFound(SageMakerFeatureStoreRuntimeError):
    """A resource that is required to perform an action was not found."""
    _ERROR_CODE = "ResourceNotFound"


class ServiceUnavailable(SageMakerFeatureStoreRuntimeError):
    """The service is currently unavailable."""
    _ERROR_CODE = "ServiceUnavailable"


class ValidationError(SageMakerFeatureStoreRuntimeError):
    """There was an error validating your request."""
    _ERROR_CODE = "ValidationError"


EXCEPTIONS: dict[str, type[SageMakerFeatureStoreRuntimeError]] = {
    "AccessForbidden": AccessForbidden,
    "InternalFailure": InternalFailure,
    "ResourceNotFound": ResourceNotFound,
    "ServiceUnavailable": ServiceUnavailable,
    "ValidationError": ValidationError,
}
