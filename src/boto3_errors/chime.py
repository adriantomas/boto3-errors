# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class ChimeError(Boto3Error):
    _SERVICE = "chime"


class AccessDeniedException(ChimeError):
    """You don't have permissions to perform the requested operation."""
    _ERROR_CODE = "AccessDeniedException"

    @property
    def code(self) -> str | None:
        return self.response.get("Code")


class BadRequestException(ChimeError):
    """The input parameters don't match the service's restrictions."""
    _ERROR_CODE = "BadRequestException"

    @property
    def code(self) -> str | None:
        return self.response.get("Code")


class ConflictException(ChimeError):
    """The request could not be processed because of conflict in the current state of the
    resource.
    """

    _ERROR_CODE = "ConflictException"

    @property
    def code(self) -> str | None:
        return self.response.get("Code")


class ForbiddenException(ChimeError):
    """The client is permanently forbidden from making the request."""
    _ERROR_CODE = "ForbiddenException"

    @property
    def code(self) -> str | None:
        return self.response.get("Code")


class NotFoundException(ChimeError):
    """One or more of the resources in the request does not exist in the system."""
    _ERROR_CODE = "NotFoundException"

    @property
    def code(self) -> str | None:
        return self.response.get("Code")


class ResourceLimitExceededException(ChimeError):
    """The request exceeds the resource limit."""
    _ERROR_CODE = "ResourceLimitExceededException"

    @property
    def code(self) -> str | None:
        return self.response.get("Code")


class ServiceFailureException(ChimeError):
    """The service encountered an unexpected error."""
    _ERROR_CODE = "ServiceFailureException"

    @property
    def code(self) -> str | None:
        return self.response.get("Code")


class ServiceUnavailableException(ChimeError):
    """The service is currently unavailable."""
    _ERROR_CODE = "ServiceUnavailableException"

    @property
    def code(self) -> str | None:
        return self.response.get("Code")


class ThrottledClientException(ChimeError):
    """The client exceeded its request rate limit."""
    _ERROR_CODE = "ThrottledClientException"

    @property
    def code(self) -> str | None:
        return self.response.get("Code")


class UnauthorizedClientException(ChimeError):
    """The client is not currently authorized to make the request."""
    _ERROR_CODE = "UnauthorizedClientException"

    @property
    def code(self) -> str | None:
        return self.response.get("Code")


class UnprocessableEntityException(ChimeError):
    """The request was well-formed but was unable to be followed due to semantic errors."""
    _ERROR_CODE = "UnprocessableEntityException"

    @property
    def code(self) -> str | None:
        return self.response.get("Code")


EXCEPTIONS: dict[str, type[ChimeError]] = {
    "AccessDeniedException": AccessDeniedException,
    "BadRequestException": BadRequestException,
    "ConflictException": ConflictException,
    "ForbiddenException": ForbiddenException,
    "NotFoundException": NotFoundException,
    "ResourceLimitExceededException": ResourceLimitExceededException,
    "ServiceFailureException": ServiceFailureException,
    "ServiceUnavailableException": ServiceUnavailableException,
    "ThrottledClientException": ThrottledClientException,
    "UnauthorizedClientException": UnauthorizedClientException,
    "UnprocessableEntityException": UnprocessableEntityException,
}
