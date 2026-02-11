# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class BillingError(Boto3Error):
    _SERVICE = "billing"


class AccessDeniedException(BillingError):
    """You don't have sufficient access to perform this action."""
    _ERROR_CODE = "AccessDeniedException"


class BillingViewHealthStatusException(BillingError):
    """Exception thrown when a billing view's health status prevents an operation from
    being performed. This may occur if the billing view is in a state other than
    `HEALTHY`.
    """

    _ERROR_CODE = "BillingViewHealthStatusException"


class ConflictException(BillingError):
    """The requested operation would cause a conflict with the current state of a service
    resource associated with the request. Resolve the conflict before retrying this
    request.
    """

    _ERROR_CODE = "ConflictException"

    @property
    def resource_id(self) -> str | None:
        """The identifier for the service resource associated with the request."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of resource associated with the request."""
        return self.response.get("resourceType")


class InternalServerException(BillingError):
    """The request processing failed because of an unknown error, exception, or failure."""
    _ERROR_CODE = "InternalServerException"


class ResourceNotFoundException(BillingError):
    """The specified ARN in the request doesn't exist."""
    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def resource_id(self) -> str | None:
        """Value is a list of resource IDs that were not found."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """Value is the type of resource that was not found."""
        return self.response.get("resourceType")


class ServiceQuotaExceededException(BillingError):
    """You've reached the limit of resources you can create, or exceeded the size of an
    individual resource.
    """

    _ERROR_CODE = "ServiceQuotaExceededException"

    @property
    def resource_id(self) -> str | None:
        """The ID of the resource."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of Amazon Web Services resource."""
        return self.response.get("resourceType")

    @property
    def service_code(self) -> str | None:
        """The container for the `serviceCode`."""
        return self.response.get("serviceCode")

    @property
    def quota_code(self) -> str | None:
        """The container for the `quotaCode`."""
        return self.response.get("quotaCode")


class ThrottlingException(BillingError):
    """The request was denied due to request throttling."""
    _ERROR_CODE = "ThrottlingException"


class ValidationException(BillingError):
    """The input fails to satisfy the constraints specified by an Amazon Web Services
    service.
    """

    _ERROR_CODE = "ValidationException"

    @property
    def reason(self) -> str | None:
        """The input fails to satisfy the constraints specified by an Amazon Web Services
        service.
        """
        return self.response.get("reason")

    @property
    def field_list(self) -> list[Any] | None:
        """The input fails to satisfy the constraints specified by an Amazon Web Services
        service.
        """
        return self.response.get("fieldList")


EXCEPTIONS: dict[str, type[BillingError]] = {
    "AccessDeniedException": AccessDeniedException,
    "BillingViewHealthStatusException": BillingViewHealthStatusException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
