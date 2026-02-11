# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class PartnerCentralSellingError(Boto3Error):
    _SERVICE = "partnercentral-selling"


class AccessDeniedException(PartnerCentralSellingError):
    """This error occurs when you don't have permission to perform the requested action.

    You don’t have access to this action or resource. Review IAM policies or contact
    your AWS administrator for assistance.
    """

    _ERROR_CODE = "AccessDeniedException"

    @property
    def reason(self) -> str | None:
        """The reason why access was denied for the requested operation."""
        return self.response.get("Reason")


class ConflictException(PartnerCentralSellingError):
    """This error occurs when the request can’t be processed due to a conflict with the
    target resource's current state, which could result from updating or deleting the
    resource.

    Suggested action: Fetch the latest state of the resource, verify the state, and
    retry the request.
    """

    _ERROR_CODE = "ConflictException"


class InternalServerException(PartnerCentralSellingError):
    """This error occurs when the specified resource can’t be found or doesn't exist.
    Resource ID and type might be incorrect.

    Suggested action: This is usually a transient error. Retry after the provided retry
    delay or a short interval. If the problem persists, contact AWS support.
    """

    _ERROR_CODE = "InternalServerException"


class ResourceNotFoundException(PartnerCentralSellingError):
    """This error occurs when the specified resource can't be found. The resource might not
    exist, or isn't visible with the current credentials.

    Suggested action: Verify that the resource ID is correct and the resource is in the
    expected AWS region. Check IAM permissions for accessing the resource.
    """

    _ERROR_CODE = "ResourceNotFoundException"


class ServiceQuotaExceededException(PartnerCentralSellingError):
    """This error occurs when the request would cause a service quota to be exceeded.
    Service quotas represent the maximum allowed use of a specific resource, and this
    error indicates that the request would surpass that limit.

    Suggested action: Review the Quotas for the resource, and either reduce usage or
    request a quota increase.
    """

    _ERROR_CODE = "ServiceQuotaExceededException"


class ThrottlingException(PartnerCentralSellingError):
    """This error occurs when there are too many requests sent. Review the provided quotas
    and adapt your usage to avoid throttling.

    This error occurs when there are too many requests sent. Review the provided Quotas
    and retry after the provided delay.
    """

    _ERROR_CODE = "ThrottlingException"


class ValidationException(PartnerCentralSellingError):
    """The input fails to satisfy the constraints specified by the service or business
    validation rules.

    Suggested action: Review the error message, including the failed fields and reasons,
    to correct the request payload.
    """

    _ERROR_CODE = "ValidationException"

    @property
    def reason(self) -> str | None:
        """The primary reason for this validation exception to occur.

        - REQUEST_VALIDATION_FAILED: The request format is not valid. Fix: Verify your
          request payload includes all required fields, uses correct data types and
          string formats.
        - BUSINESS_VALIDATION_FAILED: The requested change doesn't pass the business
          validation rules. Fix: Check that your change aligns with the business rules
          defined by AWS Partner Central.
        """
        return self.response.get("Reason")

    @property
    def error_list(self) -> list[Any] | None:
        """A list of issues that were discovered in the submitted request or the resource
        state.
        """
        return self.response.get("ErrorList")


EXCEPTIONS: dict[str, type[PartnerCentralSellingError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
