# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class IoT1ClickDevicesServiceError(Boto3Error):
    _SERVICE = "iot1click-devices"


class ForbiddenException(IoT1ClickDevicesServiceError):
    _ERROR_CODE = "ForbiddenException"

    @property
    def code(self) -> str | None:
        """403"""
        return self.response.get("Code")


class InternalFailureException(IoT1ClickDevicesServiceError):
    _ERROR_CODE = "InternalFailureException"

    @property
    def code(self) -> str | None:
        """500"""
        return self.response.get("Code")


class InvalidRequestException(IoT1ClickDevicesServiceError):
    _ERROR_CODE = "InvalidRequestException"

    @property
    def code(self) -> str | None:
        """400"""
        return self.response.get("Code")


class PreconditionFailedException(IoT1ClickDevicesServiceError):
    _ERROR_CODE = "PreconditionFailedException"

    @property
    def code(self) -> str | None:
        """412"""
        return self.response.get("Code")


class RangeNotSatisfiableException(IoT1ClickDevicesServiceError):
    _ERROR_CODE = "RangeNotSatisfiableException"

    @property
    def code(self) -> str | None:
        """416"""
        return self.response.get("Code")


class ResourceConflictException(IoT1ClickDevicesServiceError):
    _ERROR_CODE = "ResourceConflictException"

    @property
    def code(self) -> str | None:
        """409"""
        return self.response.get("Code")


class ResourceNotFoundException(IoT1ClickDevicesServiceError):
    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def code(self) -> str | None:
        """404"""
        return self.response.get("Code")


EXCEPTIONS: dict[str, type[IoT1ClickDevicesServiceError]] = {
    "ForbiddenException": ForbiddenException,
    "InternalFailureException": InternalFailureException,
    "InvalidRequestException": InvalidRequestException,
    "PreconditionFailedException": PreconditionFailedException,
    "RangeNotSatisfiableException": RangeNotSatisfiableException,
    "ResourceConflictException": ResourceConflictException,
    "ResourceNotFoundException": ResourceNotFoundException,
}
