# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class DocDBElasticError(Boto3Error):
    _SERVICE = "docdb-elastic"


class AccessDeniedException(DocDBElasticError):
    """An exception that occurs when there are not sufficient permissions to perform an
    action.
    """

    _ERROR_CODE = "AccessDeniedException"


class ConflictException(DocDBElasticError):
    """There was an access conflict."""
    _ERROR_CODE = "ConflictException"

    @property
    def resource_id(self) -> str | None:
        """The ID of the resource where there was an access conflict."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of the resource where there was an access conflict."""
        return self.response.get("resourceType")


class InternalServerException(DocDBElasticError):
    """There was an internal server error."""
    _ERROR_CODE = "InternalServerException"


class ResourceNotFoundException(DocDBElasticError):
    """The specified resource could not be located."""
    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def resource_id(self) -> str | None:
        """The ID of the resource that could not be located."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of the resource that could not be found."""
        return self.response.get("resourceType")


class ServiceQuotaExceededException(DocDBElasticError):
    """The service quota for the action was exceeded."""
    _ERROR_CODE = "ServiceQuotaExceededException"


class ThrottlingException(DocDBElasticError):
    """ThrottlingException will be thrown when request was denied due to request
    throttling.
    """

    _ERROR_CODE = "ThrottlingException"

    @property
    def retry_after_seconds(self) -> int | None:
        """The number of seconds to wait before retrying the operation."""
        return self.response.get("retryAfterSeconds")


class ValidationException(DocDBElasticError):
    """A structure defining a validation exception."""
    _ERROR_CODE = "ValidationException"

    @property
    def field_list(self) -> list[Any] | None:
        """A list of the fields in which the validation exception occurred."""
        return self.response.get("fieldList")

    @property
    def reason(self) -> str | None:
        """The reason why the validation exception occurred (one of `unknownOperation`,
        `cannotParse`, `fieldValidationFailed`, or `other`).
        """
        return self.response.get("reason")


EXCEPTIONS: dict[str, type[DocDBElasticError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
