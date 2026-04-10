# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class BCMDashboardsError(Boto3Error):
    _SERVICE = "bcm-dashboards"


class AccessDeniedException(BCMDashboardsError):
    """You do not have sufficient permissions to perform this action. Verify your IAM
    permissions and any resource policies.
    """

    _ERROR_CODE = "AccessDeniedException"


class ConflictException(BCMDashboardsError):
    """The request could not be completed due to a conflict with the current state of the
    resource. For example, attempting to create a resource that already exists or is
    being created.
    """

    _ERROR_CODE = "ConflictException"


class InternalServerException(BCMDashboardsError):
    """An internal error occurred while processing the request. Retry your request. If the
    problem persists, contact Amazon Web Services Support.
    """

    _ERROR_CODE = "InternalServerException"


class ResourceNotFoundException(BCMDashboardsError):
    """The specified resource (dashboard, policy, or widget) was not found. Verify the ARN
    and try again.
    """

    _ERROR_CODE = "ResourceNotFoundException"


class ServiceQuotaExceededException(BCMDashboardsError):
    """The request would exceed a service quota. Review the service quotas for Amazon Web
    Services Billing and Cost Management Dashboards and retry your request.
    """

    _ERROR_CODE = "ServiceQuotaExceededException"


class ThrottlingException(BCMDashboardsError):
    """The request was denied due to request throttling. Reduce the frequency of requests
    and use exponential backoff.
    """

    _ERROR_CODE = "ThrottlingException"


class ValidationException(BCMDashboardsError):
    """The input parameters do not satisfy the requirements. Check the error message for
    specific validation details.
    """

    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[BCMDashboardsError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
