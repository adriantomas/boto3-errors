# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class SageMakerGeospatialError(Boto3Error):
    _SERVICE = "sagemaker-geospatial"


class AccessDeniedException(SageMakerGeospatialError):
    """You do not have sufficient access to perform this action."""
    _ERROR_CODE = "AccessDeniedException"


class ConflictException(SageMakerGeospatialError):
    """Updating or deleting a resource can cause an inconsistent state."""
    _ERROR_CODE = "ConflictException"

    @property
    def resource_id(self) -> str | None:
        """Identifier of the resource affected."""
        return self.response.get("ResourceId")


class InternalServerException(SageMakerGeospatialError):
    """The request processing has failed because of an unknown error, exception, or
    failure.
    """

    _ERROR_CODE = "InternalServerException"

    @property
    def resource_id(self) -> str | None:
        return self.response.get("ResourceId")


class ResourceNotFoundException(SageMakerGeospatialError):
    """The request references a resource which does not exist."""
    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def resource_id(self) -> str | None:
        """Identifier of the resource that was not found."""
        return self.response.get("ResourceId")


class ServiceQuotaExceededException(SageMakerGeospatialError):
    """You have exceeded the service quota."""
    _ERROR_CODE = "ServiceQuotaExceededException"

    @property
    def resource_id(self) -> str | None:
        """Identifier of the resource affected."""
        return self.response.get("ResourceId")


class ThrottlingException(SageMakerGeospatialError):
    """The request was denied due to request throttling."""
    _ERROR_CODE = "ThrottlingException"

    @property
    def resource_id(self) -> str | None:
        return self.response.get("ResourceId")


class ValidationException(SageMakerGeospatialError):
    """The input fails to satisfy the constraints specified by an Amazon Web Services
    service.
    """

    _ERROR_CODE = "ValidationException"

    @property
    def resource_id(self) -> str | None:
        return self.response.get("ResourceId")


EXCEPTIONS: dict[str, type[SageMakerGeospatialError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
