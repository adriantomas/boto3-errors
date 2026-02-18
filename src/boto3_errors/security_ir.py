# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class SecurityIRError(Boto3Error):
    _SERVICE = "security-ir"


class AccessDeniedException(SecurityIRError):
    _ERROR_CODE = "AccessDeniedException"


class ConflictException(SecurityIRError):
    _ERROR_CODE = "ConflictException"

    @property
    def resource_id(self) -> str | None:
        """The ID of the conflicting resource."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of the conflicting resource."""
        return self.response.get("resourceType")


class InternalServerException(SecurityIRError):
    _ERROR_CODE = "InternalServerException"

    @property
    def retry_after_seconds(self) -> int | None:
        """The number of seconds after which to retry the request."""
        return self.response.get("retryAfterSeconds")


class InvalidTokenException(SecurityIRError):
    _ERROR_CODE = "InvalidTokenException"


class ResourceNotFoundException(SecurityIRError):
    _ERROR_CODE = "ResourceNotFoundException"


class SecurityIncidentResponseNotActiveException(SecurityIRError):
    _ERROR_CODE = "SecurityIncidentResponseNotActiveException"


class ServiceQuotaExceededException(SecurityIRError):
    _ERROR_CODE = "ServiceQuotaExceededException"

    @property
    def quota_code(self) -> str | None:
        """The code of the quota."""
        return self.response.get("quotaCode")

    @property
    def resource_id(self) -> str | None:
        """The ID of the requested resource which lead to the service quota exception."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of the requested resource which lead to the service quota exception."""
        return self.response.get("resourceType")

    @property
    def service_code(self) -> str | None:
        """The service code of the quota."""
        return self.response.get("serviceCode")


class ThrottlingException(SecurityIRError):
    _ERROR_CODE = "ThrottlingException"

    @property
    def quota_code(self) -> str | None:
        """The quota code of the exception."""
        return self.response.get("quotaCode")

    @property
    def retry_after_seconds(self) -> int | None:
        """The number of seconds after which to retry the request."""
        return self.response.get("retryAfterSeconds")

    @property
    def service_code(self) -> str | None:
        """The service code of the exception."""
        return self.response.get("serviceCode")


class ValidationException(SecurityIRError):
    _ERROR_CODE = "ValidationException"

    @property
    def field_list(self) -> list[Any] | None:
        """The fields which lead to the exception."""
        return self.response.get("fieldList")

    @property
    def reason(self) -> str | None:
        """The reason for the exception."""
        return self.response.get("reason")


EXCEPTIONS: dict[str, type[SecurityIRError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "InvalidTokenException": InvalidTokenException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "SecurityIncidentResponseNotActiveException": SecurityIncidentResponseNotActiveException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
