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


class RestApiClientException(MWAAError):
    """An exception indicating that a client-side error occurred during the Apache Airflow
    REST API call.
    """

    _ERROR_CODE = "RestApiClientException"

    @property
    def rest_api_status_code(self) -> int | None:
        """The HTTP status code returned by the Apache Airflow REST API call."""
        return self.response.get("RestApiStatusCode")

    @property
    def rest_api_response(self) -> dict[str, Any] | None:
        """The error response data from the Apache Airflow REST API call, provided as a
        JSON object.
        """
        return self.response.get("RestApiResponse")


class RestApiServerException(MWAAError):
    """An exception indicating that a server-side error occurred during the Apache Airflow
    REST API call.
    """

    _ERROR_CODE = "RestApiServerException"

    @property
    def rest_api_status_code(self) -> int | None:
        """The HTTP status code returned by the Apache Airflow REST API call."""
        return self.response.get("RestApiStatusCode")

    @property
    def rest_api_response(self) -> dict[str, Any] | None:
        """The error response data from the Apache Airflow REST API call, provided as a
        JSON object.
        """
        return self.response.get("RestApiResponse")


class ValidationException(MWAAError):
    """ValidationException: The provided input is not valid."""
    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[MWAAError]] = {
    "AccessDeniedException": AccessDeniedException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "RestApiClientException": RestApiClientException,
    "RestApiServerException": RestApiServerException,
    "ValidationException": ValidationException,
}
