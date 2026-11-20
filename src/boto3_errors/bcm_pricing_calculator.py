# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class BCMPricingCalculatorError(Boto3Error):
    _SERVICE = "bcm-pricing-calculator"


class AccessDeniedException(BCMPricingCalculatorError):
    """The request is denied because you don't have sufficient permissions to perform this
    operation. Verify that you have the required permissions and try again.
    """

    _ERROR_CODE = "AccessDeniedException"


class ConflictException(BCMPricingCalculatorError):
    """The request couldn't be processed because the resource is in a conflicting state.
    Verify the resource's current state and retry the request.
    """

    _ERROR_CODE = "ConflictException"

    @property
    def resource_id(self) -> str | None:
        """The identifier of the resource that is in a conflicting state."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of the resource that is in a conflicting state."""
        return self.response.get("resourceType")


class DataUnavailableException(BCMPricingCalculatorError):
    """The requested data is currently unavailable."""
    _ERROR_CODE = "DataUnavailableException"


class InternalServerException(BCMPricingCalculatorError):
    """An internal error has occurred. Retry your request, but if the problem persists,
    contact Amazon Web Services support.
    """

    _ERROR_CODE = "InternalServerException"

    @property
    def retry_after_seconds(self) -> int | None:
        """An internal error has occurred. Retry your request, but if the problem persists,
        contact Amazon Web Services support.
        """
        return self.response.get("retryAfterSeconds")


class ResourceNotFoundException(BCMPricingCalculatorError):
    """The specified resource wasn't found."""
    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def resource_id(self) -> str | None:
        """The identifier of the resource that wasn't found."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of the resource that wasn't found."""
        return self.response.get("resourceType")


class ServiceQuotaExceededException(BCMPricingCalculatorError):
    """The request would cause you to exceed your service quota."""
    _ERROR_CODE = "ServiceQuotaExceededException"

    @property
    def quota_code(self) -> str | None:
        """The quota code that was exceeded."""
        return self.response.get("quotaCode")

    @property
    def resource_id(self) -> str | None:
        """The identifier of the resource that exceeded quota."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of the resource that exceeded quota."""
        return self.response.get("resourceType")

    @property
    def service_code(self) -> str | None:
        """The service code that exceeded quota."""
        return self.response.get("serviceCode")


class ThrottlingException(BCMPricingCalculatorError):
    """The request was denied due to request throttling."""
    _ERROR_CODE = "ThrottlingException"

    @property
    def quota_code(self) -> str | None:
        """The quota code that exceeded the throttling limit."""
        return self.response.get("quotaCode")

    @property
    def retry_after_seconds(self) -> int | None:
        """The service code that exceeded the throttling limit. Retry your request, but if
        the problem persists, contact Amazon Web Services support.
        """
        return self.response.get("retryAfterSeconds")

    @property
    def service_code(self) -> str | None:
        """The service code that exceeded the throttling limit."""
        return self.response.get("serviceCode")


class ValidationException(BCMPricingCalculatorError):
    """The input provided fails to satisfy the constraints specified by an Amazon Web
    Services service.
    """

    _ERROR_CODE = "ValidationException"

    @property
    def field_list(self) -> list[Any] | None:
        """The list of fields that are invalid."""
        return self.response.get("fieldList")

    @property
    def reason(self) -> str | None:
        """The reason for the validation exception."""
        return self.response.get("reason")


EXCEPTIONS: dict[str, type[BCMPricingCalculatorError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "DataUnavailableException": DataUnavailableException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
