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
    """The request would exceed service quotas. For example, attempting to create more than
    20 widgets in a dashboard or exceeding the maximum number of dashboards per account.
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
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
