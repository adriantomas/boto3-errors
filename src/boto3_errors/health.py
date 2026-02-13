# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class HealthError(Boto3Error):
    _SERVICE = "health"


class ConcurrentModificationException(HealthError):
    """EnableHealthServiceAccessForOrganization is already in progress. Wait for the action
    to complete before trying again. To get the current status, use the
    DescribeHealthServiceStatusForOrganization operation.
    """

    _ERROR_CODE = "ConcurrentModificationException"


class InvalidPaginationToken(HealthError):
    """The specified pagination token (`nextToken`) is not valid."""
    _ERROR_CODE = "InvalidPaginationToken"


class UnsupportedLocale(HealthError):
    """The specified locale is not supported."""
    _ERROR_CODE = "UnsupportedLocale"


EXCEPTIONS: dict[str, type[HealthError]] = {
    "ConcurrentModificationException": ConcurrentModificationException,
    "InvalidPaginationToken": InvalidPaginationToken,
    "UnsupportedLocale": UnsupportedLocale,
}
