# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class IoT1ClickProjectsError(Boto3Error):
    _SERVICE = "iot1click-projects"


class InternalFailureException(IoT1ClickProjectsError):
    _ERROR_CODE = "InternalFailureException"

    @property
    def code(self) -> str | None:
        return self.response.get("code")


class InvalidRequestException(IoT1ClickProjectsError):
    _ERROR_CODE = "InvalidRequestException"

    @property
    def code(self) -> str | None:
        return self.response.get("code")


class ResourceConflictException(IoT1ClickProjectsError):
    _ERROR_CODE = "ResourceConflictException"

    @property
    def code(self) -> str | None:
        return self.response.get("code")


class ResourceNotFoundException(IoT1ClickProjectsError):
    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def code(self) -> str | None:
        return self.response.get("code")


class TooManyRequestsException(IoT1ClickProjectsError):
    _ERROR_CODE = "TooManyRequestsException"

    @property
    def code(self) -> str | None:
        return self.response.get("code")


EXCEPTIONS: dict[str, type[IoT1ClickProjectsError]] = {
    "InternalFailureException": InternalFailureException,
    "InvalidRequestException": InvalidRequestException,
    "ResourceConflictException": ResourceConflictException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "TooManyRequestsException": TooManyRequestsException,
}
