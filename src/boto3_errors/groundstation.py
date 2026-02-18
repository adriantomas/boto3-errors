# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class GroundStationError(Boto3Error):
    _SERVICE = "groundstation"


class DependencyException(GroundStationError):
    """Dependency encountered an error."""
    _ERROR_CODE = "DependencyException"

    @property
    def parameter_name(self) -> str | None:
        return self.response.get("parameterName")


class InvalidParameterException(GroundStationError):
    """One or more parameters are not valid."""
    _ERROR_CODE = "InvalidParameterException"

    @property
    def parameter_name(self) -> str | None:
        return self.response.get("parameterName")


class ResourceLimitExceededException(GroundStationError):
    """Account limits for this resource have been exceeded."""
    _ERROR_CODE = "ResourceLimitExceededException"

    @property
    def parameter_name(self) -> str | None:
        return self.response.get("parameterName")


class ResourceNotFoundException(GroundStationError):
    """Resource was not found."""
    _ERROR_CODE = "ResourceNotFoundException"


EXCEPTIONS: dict[str, type[GroundStationError]] = {
    "DependencyException": DependencyException,
    "InvalidParameterException": InvalidParameterException,
    "ResourceLimitExceededException": ResourceLimitExceededException,
    "ResourceNotFoundException": ResourceNotFoundException,
}
