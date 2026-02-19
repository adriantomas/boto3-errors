# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class PartnerCentralChannelError(Boto3Error):
    _SERVICE = "partnercentral-channel"


class AccessDeniedException(PartnerCentralChannelError):
    """The request was denied due to insufficient permissions."""
    _ERROR_CODE = "AccessDeniedException"

    @property
    def reason(self) -> str | None:
        """The reason for the access denial."""
        return self.response.get("reason")


class ConflictException(PartnerCentralChannelError):
    """The request could not be completed due to a conflict with the current state of the
    resource.
    """

    _ERROR_CODE = "ConflictException"

    @property
    def resource_id(self) -> str | None:
        """The identifier of the resource that caused the conflict."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of the resource that caused the conflict."""
        return self.response.get("resourceType")


class InternalServerException(PartnerCentralChannelError):
    """An internal server error occurred while processing the request."""
    _ERROR_CODE = "InternalServerException"


class ResourceNotFoundException(PartnerCentralChannelError):
    """The specified resource was not found."""
    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def resource_id(self) -> str | None:
        """The identifier of the resource that was not found."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of the resource that was not found."""
        return self.response.get("resourceType")


class ServiceQuotaExceededException(PartnerCentralChannelError):
    """The request would exceed a service quota limit."""
    _ERROR_CODE = "ServiceQuotaExceededException"

    @property
    def quota_code(self) -> str | None:
        """The code identifying the specific quota that would be exceeded."""
        return self.response.get("quotaCode")

    @property
    def resource_id(self) -> str | None:
        """The identifier of the resource that would exceed the quota."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of the resource that would exceed the quota."""
        return self.response.get("resourceType")


class ThrottlingException(PartnerCentralChannelError):
    """The request was throttled due to too many requests being sent in a short period."""
    _ERROR_CODE = "ThrottlingException"

    @property
    def quota_code(self) -> str | None:
        """The quota code associated with the throttling error."""
        return self.response.get("quotaCode")

    @property
    def service_code(self) -> str | None:
        """The service code associated with the throttling error."""
        return self.response.get("serviceCode")


class ValidationException(PartnerCentralChannelError):
    """The request failed validation due to invalid input parameters."""
    _ERROR_CODE = "ValidationException"

    @property
    def field_list(self) -> list[Any] | None:
        """A list of fields that failed validation."""
        return self.response.get("fieldList")

    @property
    def reason(self) -> str | None:
        """The reason for the validation failure."""
        return self.response.get("reason")


EXCEPTIONS: dict[str, type[PartnerCentralChannelError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
