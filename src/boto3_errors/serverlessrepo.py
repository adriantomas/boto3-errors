# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class ServerlessApplicationRepositoryError(Boto3Error):
    _SERVICE = "serverlessrepo"


class BadRequestException(ServerlessApplicationRepositoryError):
    """One of the parameters in the request is invalid."""
    _ERROR_CODE = "BadRequestException"

    @property
    def error_code(self) -> str | None:
        """400"""
        return self.response.get("ErrorCode")


class ConflictException(ServerlessApplicationRepositoryError):
    """The resource already exists."""
    _ERROR_CODE = "ConflictException"

    @property
    def error_code(self) -> str | None:
        """409"""
        return self.response.get("ErrorCode")


class ForbiddenException(ServerlessApplicationRepositoryError):
    """The client is not authenticated."""
    _ERROR_CODE = "ForbiddenException"

    @property
    def error_code(self) -> str | None:
        """403"""
        return self.response.get("ErrorCode")


class InternalServerErrorException(ServerlessApplicationRepositoryError):
    """The AWS Serverless Application Repository service encountered an internal error."""
    _ERROR_CODE = "InternalServerErrorException"

    @property
    def error_code(self) -> str | None:
        """500"""
        return self.response.get("ErrorCode")


class NotFoundException(ServerlessApplicationRepositoryError):
    """The resource (for example, an access policy statement) specified in the request
    doesn't exist.
    """

    _ERROR_CODE = "NotFoundException"

    @property
    def error_code(self) -> str | None:
        """404"""
        return self.response.get("ErrorCode")


class TooManyRequestsException(ServerlessApplicationRepositoryError):
    """The client is sending more than the allowed number of requests per unit of time."""
    _ERROR_CODE = "TooManyRequestsException"

    @property
    def error_code(self) -> str | None:
        """429"""
        return self.response.get("ErrorCode")


EXCEPTIONS: dict[str, type[ServerlessApplicationRepositoryError]] = {
    "BadRequestException": BadRequestException,
    "ConflictException": ConflictException,
    "ForbiddenException": ForbiddenException,
    "InternalServerErrorException": InternalServerErrorException,
    "NotFoundException": NotFoundException,
    "TooManyRequestsException": TooManyRequestsException,
}
