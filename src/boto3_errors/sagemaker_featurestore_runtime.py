# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class SageMakerFeatureStoreRuntimeError(Boto3Error):
    _SERVICE = "sagemaker-featurestore-runtime"


class AccessForbidden(SageMakerFeatureStoreRuntimeError):
    """You do not have permission to perform an action."""
    _ERROR_CODE = "AccessForbidden"


class ConflictException(SageMakerFeatureStoreRuntimeError):
    """The service rejected the update because the provided `EventTime` is older than the
    record's current `EventTime`. To persist the update, retrieve the record's latest
    `EventTime` and resubmit the request with an `EventTime` that is equal to or newer
    than the current value.
    """

    _ERROR_CODE = "ConflictException"


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
    "ConflictException": ConflictException,
    "InternalFailure": InternalFailure,
    "ResourceNotFound": ResourceNotFound,
    "ServiceUnavailable": ServiceUnavailable,
    "ValidationError": ValidationError,
}
