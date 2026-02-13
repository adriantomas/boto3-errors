# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class BCMPricingCalculatorError(Boto3Error):
    _SERVICE = "bcm-pricing-calculator"


class AccessDeniedException(BCMPricingCalculatorError):
    """You do not have sufficient access to perform this action."""
    _ERROR_CODE = "AccessDeniedException"


class ConflictException(BCMPricingCalculatorError):
    """The request could not be processed because of conflict in the current state of the
    resource.
    """

    _ERROR_CODE = "ConflictException"

    @property
    def resource_id(self) -> str | None:
        """The identifier of the resource that was not found."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of the resource that was not found."""
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


class ServiceQuotaExceededException(BCMPricingCalculatorError):
    """The request would cause you to exceed your service quota."""
    _ERROR_CODE = "ServiceQuotaExceededException"

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

    @property
    def quota_code(self) -> str | None:
        """The quota code that was exceeded."""
        return self.response.get("quotaCode")


class ThrottlingException(BCMPricingCalculatorError):
    """The request was denied due to request throttling."""
    _ERROR_CODE = "ThrottlingException"

    @property
    def service_code(self) -> str | None:
        """The service code that exceeded the throttling limit."""
        return self.response.get("serviceCode")

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


class ValidationException(BCMPricingCalculatorError):
    """The input provided fails to satisfy the constraints specified by an Amazon Web
    Services service.
    """

    _ERROR_CODE = "ValidationException"

    @property
    def reason(self) -> str | None:
        """The reason for the validation exception."""
        return self.response.get("reason")

    @property
    def field_list(self) -> list[Any] | None:
        """The list of fields that are invalid."""
        return self.response.get("fieldList")


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
