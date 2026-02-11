# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class AppConfigError(Boto3Error):
    _SERVICE = "appconfig"


class BadRequestException(AppConfigError):
    """The input fails to satisfy the constraints specified by an Amazon Web Services
    service.
    """

    _ERROR_CODE = "BadRequestException"

    @property
    def reason(self) -> str | None:
        return self.response.get("Reason")

    @property
    def details(self) -> dict[str, Any] | None:
        return self.response.get("Details")


class ConflictException(AppConfigError):
    """The request could not be processed because of conflict in the current state of the
    resource.
    """

    _ERROR_CODE = "ConflictException"


class InternalServerException(AppConfigError):
    """There was an internal failure in the AppConfig service."""
    _ERROR_CODE = "InternalServerException"


class PayloadTooLargeException(AppConfigError):
    """The configuration size is too large."""
    _ERROR_CODE = "PayloadTooLargeException"

    @property
    def measure(self) -> str | None:
        return self.response.get("Measure")

    @property
    def limit(self) -> float | None:
        return self.response.get("Limit")

    @property
    def size(self) -> float | None:
        return self.response.get("Size")


class ResourceNotFoundException(AppConfigError):
    """The requested resource could not be found."""
    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def resource_name(self) -> str | None:
        return self.response.get("ResourceName")


class ServiceQuotaExceededException(AppConfigError):
    """The number of one more AppConfig resources exceeds the maximum allowed. Verify that
    your environment doesn't exceed the following service quotas:

    Applications: 100 max

    Deployment strategies: 20 max

    Configuration profiles: 100 max per application

    Environments: 20 max per application

    To resolve this issue, you can delete one or more resources and try again. Or, you
    can request a quota increase. For more information about quotas and to request an
    increase, see Service quotas for AppConfig in the Amazon Web Services General
    Reference.
    """

    _ERROR_CODE = "ServiceQuotaExceededException"


EXCEPTIONS: dict[str, type[AppConfigError]] = {
    "BadRequestException": BadRequestException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "PayloadTooLargeException": PayloadTooLargeException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
}
