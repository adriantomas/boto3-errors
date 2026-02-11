# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class KafkaError(Boto3Error):
    _SERVICE = "kafka"


class BadRequestException(KafkaError):
    """Returns information about an error."""
    _ERROR_CODE = "BadRequestException"

    @property
    def invalid_parameter(self) -> str | None:
        """The parameter that caused the error."""
        return self.response.get("InvalidParameter")


class ConflictException(KafkaError):
    """Returns information about an error."""
    _ERROR_CODE = "ConflictException"

    @property
    def invalid_parameter(self) -> str | None:
        """The parameter that caused the error."""
        return self.response.get("InvalidParameter")


class ForbiddenException(KafkaError):
    """Returns information about an error."""
    _ERROR_CODE = "ForbiddenException"

    @property
    def invalid_parameter(self) -> str | None:
        """The parameter that caused the error."""
        return self.response.get("InvalidParameter")


class InternalServerErrorException(KafkaError):
    """Returns information about an error."""
    _ERROR_CODE = "InternalServerErrorException"

    @property
    def invalid_parameter(self) -> str | None:
        """The parameter that caused the error."""
        return self.response.get("InvalidParameter")


class NotFoundException(KafkaError):
    """Returns information about an error."""
    _ERROR_CODE = "NotFoundException"

    @property
    def invalid_parameter(self) -> str | None:
        """The parameter that caused the error."""
        return self.response.get("InvalidParameter")


class ServiceUnavailableException(KafkaError):
    """Returns information about an error."""
    _ERROR_CODE = "ServiceUnavailableException"

    @property
    def invalid_parameter(self) -> str | None:
        """The parameter that caused the error."""
        return self.response.get("InvalidParameter")


class TooManyRequestsException(KafkaError):
    """Returns information about an error."""
    _ERROR_CODE = "TooManyRequestsException"

    @property
    def invalid_parameter(self) -> str | None:
        """The parameter that caused the error."""
        return self.response.get("InvalidParameter")


class UnauthorizedException(KafkaError):
    """Returns information about an error."""
    _ERROR_CODE = "UnauthorizedException"

    @property
    def invalid_parameter(self) -> str | None:
        """The parameter that caused the error."""
        return self.response.get("InvalidParameter")


EXCEPTIONS: dict[str, type[KafkaError]] = {
    "BadRequestException": BadRequestException,
    "ConflictException": ConflictException,
    "ForbiddenException": ForbiddenException,
    "InternalServerErrorException": InternalServerErrorException,
    "NotFoundException": NotFoundException,
    "ServiceUnavailableException": ServiceUnavailableException,
    "TooManyRequestsException": TooManyRequestsException,
    "UnauthorizedException": UnauthorizedException,
}
