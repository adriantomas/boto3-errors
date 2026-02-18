# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class InvoicingError(Boto3Error):
    _SERVICE = "invoicing"


class AccessDeniedException(InvoicingError):
    """You don't have sufficient access to perform this action."""
    _ERROR_CODE = "AccessDeniedException"

    @property
    def resource_name(self) -> str | None:
        """You don't have sufficient access to perform this action."""
        return self.response.get("resourceName")


class ConflictException(InvoicingError):
    """The request could not be completed due to a conflict with the current state of the
    resource. This exception occurs when a concurrent modification is detected during an
    update operation, or when attempting to create a resource that already exists.
    """

    _ERROR_CODE = "ConflictException"

    @property
    def resource_id(self) -> str | None:
        """The identifier of the resource that caused the conflict."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of resource that caused the conflict."""
        return self.response.get("resourceType")


class InternalServerException(InvoicingError):
    """The processing request failed because of an unknown error, exception, or failure."""
    _ERROR_CODE = "InternalServerException"

    @property
    def retry_after_seconds(self) -> int | None:
        """The processing request failed because of an unknown error, exception, or
        failure.
        """
        return self.response.get("retryAfterSeconds")


class ResourceNotFoundException(InvoicingError):
    """The resource could not be found."""
    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def resource_name(self) -> str | None:
        """The resource could not be found."""
        return self.response.get("resourceName")


class ServiceQuotaExceededException(InvoicingError):
    """The request was rejected because it attempted to create resources beyond the current
    Amazon Web Services account limits. The error message describes the limit exceeded.
    """

    _ERROR_CODE = "ServiceQuotaExceededException"


class ThrottlingException(InvoicingError):
    """The request was denied due to request throttling."""
    _ERROR_CODE = "ThrottlingException"


class ValidationException(InvoicingError):
    """The input fails to satisfy the constraints specified by an Amazon Web Services
    service.
    """

    _ERROR_CODE = "ValidationException"

    @property
    def field_list(self) -> list[Any] | None:
        """The input fails to satisfy the constraints specified by an Amazon Web Services
        service.
        """
        return self.response.get("fieldList")

    @property
    def reason(self) -> str | None:
        """You don't have sufficient access to perform this action."""
        return self.response.get("reason")

    @property
    def resource_name(self) -> str | None:
        """You don't have sufficient access to perform this action."""
        return self.response.get("resourceName")


EXCEPTIONS: dict[str, type[InvoicingError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
