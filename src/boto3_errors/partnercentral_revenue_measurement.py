# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class PartnerCentralRevenueMeasurementError(Boto3Error):
    _SERVICE = "partnercentral-revenue-measurement"


class AccessDeniedException(PartnerCentralRevenueMeasurementError):
    """The request was denied due to insufficient permissions."""
    _ERROR_CODE = "AccessDeniedException"

    @property
    def reason(self) -> str | None:
        """The reason for the access denial."""
        return self.response.get("Reason")


class ConflictException(PartnerCentralRevenueMeasurementError):
    """The request could not be completed due to a conflict with the current state of the
    resource.
    """

    _ERROR_CODE = "ConflictException"

    @property
    def reason(self) -> str | None:
        """The reason for the conflict."""
        return self.response.get("Reason")


class InternalServerException(PartnerCentralRevenueMeasurementError):
    """An internal server error occurred. Retry your request."""
    _ERROR_CODE = "InternalServerException"


class ResourceNotFoundException(PartnerCentralRevenueMeasurementError):
    """The specified resource was not found."""
    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def reason(self) -> str | None:
        """The reason the resource was not found."""
        return self.response.get("Reason")


class ServiceQuotaExceededException(PartnerCentralRevenueMeasurementError):
    """The request would exceed a service quota limit."""
    _ERROR_CODE = "ServiceQuotaExceededException"

    @property
    def reason(self) -> str | None:
        """The reason the service quota was exceeded."""
        return self.response.get("Reason")


class ThrottlingException(PartnerCentralRevenueMeasurementError):
    """The request was throttled due to too many requests. Retry your request."""
    _ERROR_CODE = "ThrottlingException"

    @property
    def quota_code(self) -> str | None:
        """The quota code associated with the throttling error."""
        return self.response.get("QuotaCode")

    @property
    def service_code(self) -> str | None:
        """The service code associated with the throttling error."""
        return self.response.get("ServiceCode")


class ValidationException(PartnerCentralRevenueMeasurementError):
    """The request failed validation due to invalid input parameters."""
    _ERROR_CODE = "ValidationException"

    @property
    def field_list(self) -> list[Any] | None:
        """A list of fields that failed validation."""
        return self.response.get("FieldList")

    @property
    def reason(self) -> str | None:
        """The reason for the validation failure."""
        return self.response.get("Reason")


EXCEPTIONS: dict[str, type[PartnerCentralRevenueMeasurementError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
