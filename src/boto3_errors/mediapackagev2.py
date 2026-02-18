# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class MediaPackageV2Error(Boto3Error):
    _SERVICE = "mediapackagev2"


class AccessDeniedException(MediaPackageV2Error):
    """You don't have permissions to perform the requested operation. The user or role that
    is making the request must have at least one IAM permissions policy attached that
    grants the required permissions. For more information, see Access Management in the
    IAM User Guide.
    """

    _ERROR_CODE = "AccessDeniedException"


class ConflictException(MediaPackageV2Error):
    """Updating or deleting this resource can cause an inconsistent state."""
    _ERROR_CODE = "ConflictException"

    @property
    def conflict_exception_type(self) -> str | None:
        """The type of ConflictException."""
        return self.response.get("ConflictExceptionType")


class InternalServerException(MediaPackageV2Error):
    """Indicates that an error from the service occurred while trying to process a request."""
    _ERROR_CODE = "InternalServerException"


class ResourceNotFoundException(MediaPackageV2Error):
    """The specified resource doesn't exist."""
    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def resource_type_not_found(self) -> str | None:
        """The specified resource type wasn't found."""
        return self.response.get("ResourceTypeNotFound")


class ServiceQuotaExceededException(MediaPackageV2Error):
    """The request would cause a service quota to be exceeded."""
    _ERROR_CODE = "ServiceQuotaExceededException"


class ThrottlingException(MediaPackageV2Error):
    """The request throughput limit was exceeded."""
    _ERROR_CODE = "ThrottlingException"


class ValidationException(MediaPackageV2Error):
    """The input failed to meet the constraints specified by the AWS service."""
    _ERROR_CODE = "ValidationException"

    @property
    def validation_exception_type(self) -> str | None:
        """The type of ValidationException."""
        return self.response.get("ValidationExceptionType")


EXCEPTIONS: dict[str, type[MediaPackageV2Error]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
