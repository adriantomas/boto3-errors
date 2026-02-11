# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class AmplifyBackendError(Boto3Error):
    _SERVICE = "amplifybackend"


class BadRequestException(AmplifyBackendError):
    """An error returned if a request is not formed properly."""
    _ERROR_CODE = "BadRequestException"


class GatewayTimeoutException(AmplifyBackendError):
    """An error returned if there's a temporary issue with the service."""
    _ERROR_CODE = "GatewayTimeoutException"


class NotFoundException(AmplifyBackendError):
    """An error returned when a specific resource type is not found."""
    _ERROR_CODE = "NotFoundException"

    @property
    def resource_type(self) -> str | None:
        """The type of resource that is not found."""
        return self.response.get("ResourceType")


class TooManyRequestsException(AmplifyBackendError):
    """An error that is returned when a limit of a specific type has been exceeded."""
    _ERROR_CODE = "TooManyRequestsException"

    @property
    def limit_type(self) -> str | None:
        """The type of limit that was exceeded."""
        return self.response.get("LimitType")


EXCEPTIONS: dict[str, type[AmplifyBackendError]] = {
    "BadRequestException": BadRequestException,
    "GatewayTimeoutException": GatewayTimeoutException,
    "NotFoundException": NotFoundException,
    "TooManyRequestsException": TooManyRequestsException,
}
