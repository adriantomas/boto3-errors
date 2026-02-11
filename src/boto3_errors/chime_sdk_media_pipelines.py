# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class ChimeSDKMediaPipelinesError(Boto3Error):
    _SERVICE = "chime-sdk-media-pipelines"


class BadRequestException(ChimeSDKMediaPipelinesError):
    """The input parameters don't match the service's restrictions."""
    _ERROR_CODE = "BadRequestException"

    @property
    def code(self) -> str | None:
        return self.response.get("Code")

    @property
    def request_id(self) -> str | None:
        """The request ID associated with the call responsible for the exception."""
        return self.response.get("RequestId")


class ConflictException(ChimeSDKMediaPipelinesError):
    """The request could not be processed because of conflict in the current state of the
    resource.
    """

    _ERROR_CODE = "ConflictException"

    @property
    def code(self) -> str | None:
        return self.response.get("Code")

    @property
    def request_id(self) -> str | None:
        """The request ID associated with the call responsible for the exception."""
        return self.response.get("RequestId")


class ForbiddenException(ChimeSDKMediaPipelinesError):
    """The client is permanently forbidden from making the request."""
    _ERROR_CODE = "ForbiddenException"

    @property
    def code(self) -> str | None:
        return self.response.get("Code")

    @property
    def request_id(self) -> str | None:
        """The request id associated with the call responsible for the exception."""
        return self.response.get("RequestId")


class NotFoundException(ChimeSDKMediaPipelinesError):
    """One or more of the resources in the request does not exist in the system."""
    _ERROR_CODE = "NotFoundException"

    @property
    def code(self) -> str | None:
        return self.response.get("Code")

    @property
    def request_id(self) -> str | None:
        """The request ID associated with the call responsible for the exception."""
        return self.response.get("RequestId")


class ResourceLimitExceededException(ChimeSDKMediaPipelinesError):
    """The request exceeds the resource limit."""
    _ERROR_CODE = "ResourceLimitExceededException"

    @property
    def code(self) -> str | None:
        return self.response.get("Code")

    @property
    def request_id(self) -> str | None:
        """The request ID associated with the call responsible for the exception."""
        return self.response.get("RequestId")


class ServiceFailureException(ChimeSDKMediaPipelinesError):
    """The service encountered an unexpected error."""
    _ERROR_CODE = "ServiceFailureException"

    @property
    def code(self) -> str | None:
        return self.response.get("Code")

    @property
    def request_id(self) -> str | None:
        """The request ID associated with the call responsible for the exception."""
        return self.response.get("RequestId")


class ServiceUnavailableException(ChimeSDKMediaPipelinesError):
    """The service is currently unavailable."""
    _ERROR_CODE = "ServiceUnavailableException"

    @property
    def code(self) -> str | None:
        return self.response.get("Code")

    @property
    def request_id(self) -> str | None:
        """The request ID associated with the call responsible for the exception."""
        return self.response.get("RequestId")


class ThrottledClientException(ChimeSDKMediaPipelinesError):
    """The client exceeded its request rate limit."""
    _ERROR_CODE = "ThrottledClientException"

    @property
    def code(self) -> str | None:
        return self.response.get("Code")

    @property
    def request_id(self) -> str | None:
        """The request ID associated with the call responsible for the exception."""
        return self.response.get("RequestId")


class UnauthorizedClientException(ChimeSDKMediaPipelinesError):
    """The client is not currently authorized to make the request."""
    _ERROR_CODE = "UnauthorizedClientException"

    @property
    def code(self) -> str | None:
        return self.response.get("Code")

    @property
    def request_id(self) -> str | None:
        """The request ID associated with the call responsible for the exception."""
        return self.response.get("RequestId")


EXCEPTIONS: dict[str, type[ChimeSDKMediaPipelinesError]] = {
    "BadRequestException": BadRequestException,
    "ConflictException": ConflictException,
    "ForbiddenException": ForbiddenException,
    "NotFoundException": NotFoundException,
    "ResourceLimitExceededException": ResourceLimitExceededException,
    "ServiceFailureException": ServiceFailureException,
    "ServiceUnavailableException": ServiceUnavailableException,
    "ThrottledClientException": ThrottledClientException,
    "UnauthorizedClientException": UnauthorizedClientException,
}
