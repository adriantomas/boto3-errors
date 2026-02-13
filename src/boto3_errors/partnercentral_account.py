# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class PartnerCentralAccountError(Boto3Error):
    _SERVICE = "partnercentral-account"


class AccessDeniedException(PartnerCentralAccountError):
    """The request was denied due to insufficient permissions. The caller does not have the
    required permissions to perform this operation.
    """

    _ERROR_CODE = "AccessDeniedException"

    @property
    def reason(self) -> str | None:
        """The specific reason for the access denial."""
        return self.response.get("Reason")


class ConflictException(PartnerCentralAccountError):
    """The request could not be completed due to a conflict with the current state of the
    resource. This typically occurs when trying to create a resource that already exists
    or modify a resource that has been changed by another process.
    """

    _ERROR_CODE = "ConflictException"

    @property
    def reason(self) -> str | None:
        """The specific reason for the conflict."""
        return self.response.get("Reason")


class InternalServerException(PartnerCentralAccountError):
    """An internal server error occurred while processing the request. This is typically a
    temporary condition and the request may be retried.
    """

    _ERROR_CODE = "InternalServerException"


class ResourceNotFoundException(PartnerCentralAccountError):
    """The specified resource could not be found. This may occur when referencing a
    resource that does not exist or has been deleted.
    """

    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def reason(self) -> str | None:
        """The specific reason why the resource was not found."""
        return self.response.get("Reason")


class ServiceQuotaExceededException(PartnerCentralAccountError):
    """The request was rejected because it would exceed a service quota or limit. This may
    occur when trying to create more resources than allowed by the service limits.
    """

    _ERROR_CODE = "ServiceQuotaExceededException"

    @property
    def reason(self) -> str | None:
        """The specific reason for the service quota being exceeded."""
        return self.response.get("Reason")


class ThrottlingException(PartnerCentralAccountError):
    """The request was throttled due to too many requests being sent in a short period of
    time. The client should implement exponential backoff and retry the request.
    """

    _ERROR_CODE = "ThrottlingException"

    @property
    def service_code(self) -> str | None:
        """The service code associated with the throttling error."""
        return self.response.get("ServiceCode")

    @property
    def quota_code(self) -> str | None:
        """The quota code associated with the throttling error."""
        return self.response.get("QuotaCode")


class ValidationException(PartnerCentralAccountError):
    """The request failed validation. One or more input parameters are invalid, missing, or
    do not meet the required format or constraints.
    """

    _ERROR_CODE = "ValidationException"

    @property
    def reason(self) -> str | None:
        """The reason for the validation failure."""
        return self.response.get("Reason")

    @property
    def error_details(self) -> list[Any] | None:
        """A list of detailed validation errors that occurred during request processing."""
        return self.response.get("ErrorDetails")


EXCEPTIONS: dict[str, type[PartnerCentralAccountError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
