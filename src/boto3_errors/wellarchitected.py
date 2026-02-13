# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class WellArchitectedError(Boto3Error):
    _SERVICE = "wellarchitected"


class AccessDeniedException(WellArchitectedError):
    """User does not have sufficient access to perform this action."""
    _ERROR_CODE = "AccessDeniedException"


class ConflictException(WellArchitectedError):
    """The resource has already been processed, was deleted, or is too large."""
    _ERROR_CODE = "ConflictException"

    @property
    def resource_id(self) -> str | None:
        return self.response.get("ResourceId")

    @property
    def resource_type(self) -> str | None:
        return self.response.get("ResourceType")


class InternalServerException(WellArchitectedError):
    """There is a problem with the Well-Architected Tool API service."""
    _ERROR_CODE = "InternalServerException"


class ResourceNotFoundException(WellArchitectedError):
    """The requested resource was not found."""
    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def resource_id(self) -> str | None:
        return self.response.get("ResourceId")

    @property
    def resource_type(self) -> str | None:
        return self.response.get("ResourceType")


class ServiceQuotaExceededException(WellArchitectedError):
    """The user has reached their resource quota."""
    _ERROR_CODE = "ServiceQuotaExceededException"

    @property
    def resource_id(self) -> str | None:
        return self.response.get("ResourceId")

    @property
    def resource_type(self) -> str | None:
        return self.response.get("ResourceType")

    @property
    def quota_code(self) -> str | None:
        return self.response.get("QuotaCode")

    @property
    def service_code(self) -> str | None:
        return self.response.get("ServiceCode")


class ThrottlingException(WellArchitectedError):
    """Request was denied due to request throttling."""
    _ERROR_CODE = "ThrottlingException"

    @property
    def quota_code(self) -> str | None:
        return self.response.get("QuotaCode")

    @property
    def service_code(self) -> str | None:
        return self.response.get("ServiceCode")


class ValidationException(WellArchitectedError):
    """The user input is not valid."""
    _ERROR_CODE = "ValidationException"

    @property
    def reason(self) -> str | None:
        return self.response.get("Reason")

    @property
    def fields(self) -> list[Any] | None:
        return self.response.get("Fields")


EXCEPTIONS: dict[str, type[WellArchitectedError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
