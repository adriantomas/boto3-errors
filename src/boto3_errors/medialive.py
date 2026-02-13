# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class MediaLiveError(Boto3Error):
    _SERVICE = "medialive"


class BadGatewayException(MediaLiveError):
    """Placeholder documentation for BadGatewayException"""
    _ERROR_CODE = "BadGatewayException"


class BadRequestException(MediaLiveError):
    """Placeholder documentation for BadRequestException"""
    _ERROR_CODE = "BadRequestException"


class ConflictException(MediaLiveError):
    """Placeholder documentation for ConflictException"""
    _ERROR_CODE = "ConflictException"


class ForbiddenException(MediaLiveError):
    """Placeholder documentation for ForbiddenException"""
    _ERROR_CODE = "ForbiddenException"


class GatewayTimeoutException(MediaLiveError):
    """Placeholder documentation for GatewayTimeoutException"""
    _ERROR_CODE = "GatewayTimeoutException"


class InternalServerErrorException(MediaLiveError):
    """Placeholder documentation for InternalServerErrorException"""
    _ERROR_CODE = "InternalServerErrorException"


class NotFoundException(MediaLiveError):
    """Placeholder documentation for NotFoundException"""
    _ERROR_CODE = "NotFoundException"


class TooManyRequestsException(MediaLiveError):
    """Placeholder documentation for TooManyRequestsException"""
    _ERROR_CODE = "TooManyRequestsException"


class UnprocessableEntityException(MediaLiveError):
    """Placeholder documentation for UnprocessableEntityException"""
    _ERROR_CODE = "UnprocessableEntityException"

    @property
    def validation_errors(self) -> list[Any] | None:
        """A collection of validation error responses."""
        return self.response.get("ValidationErrors")


EXCEPTIONS: dict[str, type[MediaLiveError]] = {
    "BadGatewayException": BadGatewayException,
    "BadRequestException": BadRequestException,
    "ConflictException": ConflictException,
    "ForbiddenException": ForbiddenException,
    "GatewayTimeoutException": GatewayTimeoutException,
    "InternalServerErrorException": InternalServerErrorException,
    "NotFoundException": NotFoundException,
    "TooManyRequestsException": TooManyRequestsException,
    "UnprocessableEntityException": UnprocessableEntityException,
}
