# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class CostandUsageReportServiceError(Boto3Error):
    _SERVICE = "cur"


class DuplicateReportNameException(CostandUsageReportServiceError):
    """A report with the specified name already exists in the account. Specify a different
    report name.
    """

    _ERROR_CODE = "DuplicateReportNameException"


class InternalErrorException(CostandUsageReportServiceError):
    """An error on the server occurred during the processing of your request. Try again
    later.
    """

    _ERROR_CODE = "InternalErrorException"


class ReportLimitReachedException(CostandUsageReportServiceError):
    """This account already has five reports defined. To define a new report, you must
    delete an existing report.
    """

    _ERROR_CODE = "ReportLimitReachedException"


class ResourceNotFoundException(CostandUsageReportServiceError):
    """The specified report (`ReportName`) in the request doesn't exist."""
    _ERROR_CODE = "ResourceNotFoundException"


class ValidationException(CostandUsageReportServiceError):
    """The input fails to satisfy the constraints specified by an Amazon Web Services
    service.
    """

    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[CostandUsageReportServiceError]] = {
    "DuplicateReportNameException": DuplicateReportNameException,
    "InternalErrorException": InternalErrorException,
    "ReportLimitReachedException": ReportLimitReachedException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ValidationException": ValidationException,
}
