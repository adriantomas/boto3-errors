# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class PartnerCentralBenefitsError(Boto3Error):
    _SERVICE = "partnercentral-benefits"


class AccessDeniedException(PartnerCentralBenefitsError):
    """Thrown when the caller does not have sufficient permissions to perform the requested
    operation.
    """

    _ERROR_CODE = "AccessDeniedException"


class ConflictException(PartnerCentralBenefitsError):
    """Thrown when the request conflicts with the current state of the resource, such as
    attempting to modify a resource that has been changed by another process.
    """

    _ERROR_CODE = "ConflictException"


class InternalServerException(PartnerCentralBenefitsError):
    """Thrown when an unexpected error occurs on the server side during request processing."""
    _ERROR_CODE = "InternalServerException"


class ResourceNotFoundException(PartnerCentralBenefitsError):
    """Thrown when the requested resource cannot be found or does not exist."""
    _ERROR_CODE = "ResourceNotFoundException"


class ServiceQuotaExceededException(PartnerCentralBenefitsError):
    """Thrown when the request would exceed the service quotas or limits for the account."""
    _ERROR_CODE = "ServiceQuotaExceededException"

    @property
    def resource_id(self) -> str | None:
        """The identifier of the resource that would exceed the quota."""
        return self.response.get("ResourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of the resource that would exceed the quota."""
        return self.response.get("ResourceType")

    @property
    def quota_code(self) -> str | None:
        """The code identifying the specific quota that would be exceeded."""
        return self.response.get("QuotaCode")


class ThrottlingException(PartnerCentralBenefitsError):
    """Thrown when the request rate exceeds the allowed limits and the request is being
    throttled.
    """

    _ERROR_CODE = "ThrottlingException"


class ValidationException(PartnerCentralBenefitsError):
    """Thrown when the request contains invalid parameters or fails input validation
    requirements.
    """

    _ERROR_CODE = "ValidationException"

    @property
    def reason(self) -> str | None:
        """The reason for the validation failure."""
        return self.response.get("Reason")

    @property
    def field_list(self) -> list[Any] | None:
        """A list of fields that failed validation."""
        return self.response.get("FieldList")


EXCEPTIONS: dict[str, type[PartnerCentralBenefitsError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
