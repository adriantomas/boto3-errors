# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class SageMakerError(Boto3Error):
    _SERVICE = "sagemaker"


class ConflictException(SageMakerError):
    """There was a conflict when you attempted to modify a SageMaker entity such as an
    `Experiment` or `Artifact`.
    """

    _ERROR_CODE = "ConflictException"


class ResourceInUse(SageMakerError):
    """Resource being accessed is in use."""
    _ERROR_CODE = "ResourceInUse"


class ResourceLimitExceeded(SageMakerError):
    """You have exceeded an SageMaker resource limit. For example, you might have too many
    training jobs created.
    """

    _ERROR_CODE = "ResourceLimitExceeded"


class ResourceNotFound(SageMakerError):
    """Resource being access is not found."""
    _ERROR_CODE = "ResourceNotFound"


EXCEPTIONS: dict[str, type[SageMakerError]] = {
    "ConflictException": ConflictException,
    "ResourceInUse": ResourceInUse,
    "ResourceLimitExceeded": ResourceLimitExceeded,
    "ResourceNotFound": ResourceNotFound,
}
