# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class ApplicationCostProfilerError(Boto3Error):
    _SERVICE = "applicationcostprofiler"


class AccessDeniedException(ApplicationCostProfilerError):
    """You do not have permission to perform this action."""
    _ERROR_CODE = "AccessDeniedException"


class InternalServerException(ApplicationCostProfilerError):
    """An internal server error occurred. Retry your request."""
    _ERROR_CODE = "InternalServerException"


class ServiceQuotaExceededException(ApplicationCostProfilerError):
    """Your request exceeds one or more of the service quotas."""
    _ERROR_CODE = "ServiceQuotaExceededException"


class ThrottlingException(ApplicationCostProfilerError):
    """The calls to AWS Application Cost Profiler API are throttled. The request was
    denied.
    """

    _ERROR_CODE = "ThrottlingException"


class ValidationException(ApplicationCostProfilerError):
    """The input fails to satisfy the constraints for the API."""
    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[ApplicationCostProfilerError]] = {
    "AccessDeniedException": AccessDeniedException,
    "InternalServerException": InternalServerException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
