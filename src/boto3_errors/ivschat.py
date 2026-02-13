# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class ivschatError(Boto3Error):
    _SERVICE = "ivschat"


class AccessDeniedException(ivschatError):
    _ERROR_CODE = "AccessDeniedException"


class ConflictException(ivschatError):
    _ERROR_CODE = "ConflictException"

    @property
    def resource_id(self) -> str | None:
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        return self.response.get("resourceType")


class InternalServerException(ivschatError):
    _ERROR_CODE = "InternalServerException"


class PendingVerification(ivschatError):
    _ERROR_CODE = "PendingVerification"


class ResourceNotFoundException(ivschatError):
    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def resource_id(self) -> str | None:
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        return self.response.get("resourceType")


class ServiceQuotaExceededException(ivschatError):
    _ERROR_CODE = "ServiceQuotaExceededException"

    @property
    def resource_id(self) -> str | None:
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        return self.response.get("resourceType")

    @property
    def limit(self) -> int | None:
        return self.response.get("limit")


class ThrottlingException(ivschatError):
    _ERROR_CODE = "ThrottlingException"

    @property
    def resource_id(self) -> str | None:
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        return self.response.get("resourceType")

    @property
    def limit(self) -> int | None:
        return self.response.get("limit")


class ValidationException(ivschatError):
    _ERROR_CODE = "ValidationException"

    @property
    def reason(self) -> str | None:
        return self.response.get("reason")

    @property
    def field_list(self) -> list[Any] | None:
        return self.response.get("fieldList")


EXCEPTIONS: dict[str, type[ivschatError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "PendingVerification": PendingVerification,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
