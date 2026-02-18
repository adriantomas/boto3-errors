# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class MWAAError(Boto3Error):
    _SERVICE = "mwaa"


class AccessDeniedException(MWAAError):
    """Access to the Apache Airflow Web UI or CLI has been denied due to insufficient
    permissions. To learn more, see Accessing an Amazon MWAA environment.
    """

    _ERROR_CODE = "AccessDeniedException"


class InternalServerException(MWAAError):
    """InternalServerException: An internal error has occurred."""
    _ERROR_CODE = "InternalServerException"


class ResourceNotFoundException(MWAAError):
    """ResourceNotFoundException: The resource is not available."""
    _ERROR_CODE = "ResourceNotFoundException"


class ValidationException(MWAAError):
    """ValidationException: The provided input is not valid."""
    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[MWAAError]] = {
    "AccessDeniedException": AccessDeniedException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ValidationException": ValidationException,
}
