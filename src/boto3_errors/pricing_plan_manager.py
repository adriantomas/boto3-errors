# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class PricingPlanManagerError(Boto3Error):
    _SERVICE = "pricing-plan-manager"


class AccessDeniedException(PricingPlanManagerError):
    """You do not have the required permissions to perform this operation. Verify that your
    IAM policy grants access to this action.
    """

    _ERROR_CODE = "AccessDeniedException"


class ConflictException(PricingPlanManagerError):
    """The request conflicts with the current state of the resource. This typically occurs
    when the `ETag` value in the `If-Match` header does not match the current version of
    the subscription. Retrieve the latest version and retry.
    """

    _ERROR_CODE = "ConflictException"

    @property
    def resource_id(self) -> str | None:
        """The identifier of the resource that has a conflicting state."""
        return self.response.get("resourceId")


class InternalServerException(PricingPlanManagerError):
    """An unexpected error occurred on the server. Retry the request."""
    _ERROR_CODE = "InternalServerException"


class ResourceNotFoundException(PricingPlanManagerError):
    """The specified subscription was not found. Verify that the ARN is correct and that
    the subscription belongs to your account.
    """

    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def resource_id(self) -> str | None:
        """The identifier of the resource that was not found."""
        return self.response.get("resourceId")


class ServiceQuotaExceededException(PricingPlanManagerError):
    """The request would exceed a service limit. You have reached the maximum number of
    subscriptions allowed for your account.
    """

    _ERROR_CODE = "ServiceQuotaExceededException"


class ThrottlingException(PricingPlanManagerError):
    """The request rate exceeds the allowed limit. Wait briefly and retry the request."""
    _ERROR_CODE = "ThrottlingException"


class ValidationException(PricingPlanManagerError):
    """The request failed a business rule validation. For example, the specified resource
    might already be associated with another subscription, or the subscription might not
    be in the required state for this operation.
    """

    _ERROR_CODE = "ValidationException"

    @property
    def resource_id(self) -> str | None:
        """The identifier of the resource that failed validation."""
        return self.response.get("resourceId")


EXCEPTIONS: dict[str, type[PricingPlanManagerError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
