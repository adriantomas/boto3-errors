# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class S3FilesError(Boto3Error):
    _SERVICE = "s3files"


class ConflictException(S3FilesError):
    """The request conflicts with the current state of the resource. This can occur when
    trying to create a resource that already exists or delete a resource that is in use.
    """

    _ERROR_CODE = "ConflictException"

    @property
    def error_code(self) -> str | None:
        """The error code associated with the exception."""
        return self.response.get("errorCode")

    @property
    def resource_id(self) -> str | None:
        """The identifier of the resource that caused the conflict."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of the resource that caused the conflict."""
        return self.response.get("resourceType")


class InternalServerException(S3FilesError):
    """An internal server error occurred. Retry your request."""
    _ERROR_CODE = "InternalServerException"

    @property
    def error_code(self) -> str | None:
        """The error code associated with the exception."""
        return self.response.get("errorCode")


class ResourceNotFoundException(S3FilesError):
    """The specified resource was not found. Verify that the resource exists and that you
    have permission to access it.
    """

    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def error_code(self) -> str | None:
        """The error code associated with the exception."""
        return self.response.get("errorCode")


class ServiceQuotaExceededException(S3FilesError):
    """The request would exceed a service quota. Review your service quotas and either
    delete resources or request a quota increase.
    """

    _ERROR_CODE = "ServiceQuotaExceededException"

    @property
    def error_code(self) -> str | None:
        """The error code associated with the exception."""
        return self.response.get("errorCode")


class ThrottlingException(S3FilesError):
    """The request was throttled. Retry your request using exponential backoff."""
    _ERROR_CODE = "ThrottlingException"

    @property
    def error_code(self) -> str | None:
        """The error code associated with the exception."""
        return self.response.get("errorCode")


class ValidationException(S3FilesError):
    """The input parameters are not valid. Check the parameter values and try again."""
    _ERROR_CODE = "ValidationException"

    @property
    def error_code(self) -> str | None:
        """The error code associated with the exception."""
        return self.response.get("errorCode")


EXCEPTIONS: dict[str, type[S3FilesError]] = {
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
