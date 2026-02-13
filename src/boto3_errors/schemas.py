# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class schemasError(Boto3Error):
    _SERVICE = "schemas"


class BadRequestException(schemasError):
    _ERROR_CODE = "BadRequestException"

    @property
    def code(self) -> str | None:
        """The error code."""
        return self.response.get("Code")


class ConflictException(schemasError):
    _ERROR_CODE = "ConflictException"

    @property
    def code(self) -> str | None:
        """The error code."""
        return self.response.get("Code")


class ForbiddenException(schemasError):
    _ERROR_CODE = "ForbiddenException"

    @property
    def code(self) -> str | None:
        """The error code."""
        return self.response.get("Code")


class GoneException(schemasError):
    _ERROR_CODE = "GoneException"

    @property
    def code(self) -> str | None:
        """The error code."""
        return self.response.get("Code")


class InternalServerErrorException(schemasError):
    _ERROR_CODE = "InternalServerErrorException"

    @property
    def code(self) -> str | None:
        """The error code."""
        return self.response.get("Code")


class NotFoundException(schemasError):
    _ERROR_CODE = "NotFoundException"

    @property
    def code(self) -> str | None:
        """The error code."""
        return self.response.get("Code")


class PreconditionFailedException(schemasError):
    _ERROR_CODE = "PreconditionFailedException"

    @property
    def code(self) -> str | None:
        """The error code."""
        return self.response.get("Code")


class ServiceUnavailableException(schemasError):
    _ERROR_CODE = "ServiceUnavailableException"

    @property
    def code(self) -> str | None:
        """The error code."""
        return self.response.get("Code")


class TooManyRequestsException(schemasError):
    _ERROR_CODE = "TooManyRequestsException"

    @property
    def code(self) -> str | None:
        """The error code."""
        return self.response.get("Code")


class UnauthorizedException(schemasError):
    _ERROR_CODE = "UnauthorizedException"

    @property
    def code(self) -> str | None:
        """The error code."""
        return self.response.get("Code")


EXCEPTIONS: dict[str, type[schemasError]] = {
    "BadRequestException": BadRequestException,
    "ConflictException": ConflictException,
    "ForbiddenException": ForbiddenException,
    "GoneException": GoneException,
    "InternalServerErrorException": InternalServerErrorException,
    "NotFoundException": NotFoundException,
    "PreconditionFailedException": PreconditionFailedException,
    "ServiceUnavailableException": ServiceUnavailableException,
    "TooManyRequestsException": TooManyRequestsException,
    "UnauthorizedException": UnauthorizedException,
}
