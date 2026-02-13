# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class ChimeSDKMeetingsError(Boto3Error):
    _SERVICE = "chime-sdk-meetings"


class BadRequestException(ChimeSDKMeetingsError):
    """The input parameters don't match the service's restrictions."""
    _ERROR_CODE = "BadRequestException"

    @property
    def code(self) -> str | None:
        return self.response.get("Code")

    @property
    def request_id(self) -> str | None:
        """The request id associated with the call responsible for the exception."""
        return self.response.get("RequestId")


class ConflictException(ChimeSDKMeetingsError):
    """Multiple instances of the same request have been made simultaneously."""
    _ERROR_CODE = "ConflictException"

    @property
    def code(self) -> str | None:
        return self.response.get("Code")

    @property
    def request_id(self) -> str | None:
        """The ID of the request involved in the conflict."""
        return self.response.get("RequestId")


class ForbiddenException(ChimeSDKMeetingsError):
    """The client is permanently forbidden from making the request."""
    _ERROR_CODE = "ForbiddenException"

    @property
    def code(self) -> str | None:
        return self.response.get("Code")

    @property
    def request_id(self) -> str | None:
        """The request id associated with the call responsible for the exception."""
        return self.response.get("RequestId")


class LimitExceededException(ChimeSDKMeetingsError):
    """The request exceeds the resource limit."""
    _ERROR_CODE = "LimitExceededException"

    @property
    def code(self) -> str | None:
        return self.response.get("Code")

    @property
    def request_id(self) -> str | None:
        """The request id associated with the call responsible for the exception."""
        return self.response.get("RequestId")


class NotFoundException(ChimeSDKMeetingsError):
    """One or more of the resources in the request does not exist in the system."""
    _ERROR_CODE = "NotFoundException"

    @property
    def code(self) -> str | None:
        return self.response.get("Code")

    @property
    def request_id(self) -> str | None:
        """The request ID associated with the call responsible for the exception."""
        return self.response.get("RequestId")


class ResourceNotFoundException(ChimeSDKMeetingsError):
    """The resource that you want to tag couldn't be found."""
    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def code(self) -> str | None:
        return self.response.get("Code")

    @property
    def request_id(self) -> str | None:
        """The ID of the resource that couldn't be found."""
        return self.response.get("RequestId")

    @property
    def resource_name(self) -> str | None:
        """The name of the resource that couldn't be found."""
        return self.response.get("ResourceName")


class ServiceFailureException(ChimeSDKMeetingsError):
    """The service encountered an unexpected error."""
    _ERROR_CODE = "ServiceFailureException"

    @property
    def code(self) -> str | None:
        return self.response.get("Code")

    @property
    def request_id(self) -> str | None:
        """The ID of the failed request."""
        return self.response.get("RequestId")


class ServiceUnavailableException(ChimeSDKMeetingsError):
    """The service is currently unavailable."""
    _ERROR_CODE = "ServiceUnavailableException"

    @property
    def code(self) -> str | None:
        return self.response.get("Code")

    @property
    def request_id(self) -> str | None:
        """The request id associated with the call responsible for the exception."""
        return self.response.get("RequestId")

    @property
    def retry_after_seconds(self) -> str | None:
        """The number of seconds the caller should wait before retrying."""
        return self.response.get("RetryAfterSeconds")


class ThrottlingException(ChimeSDKMeetingsError):
    """The number of customer requests exceeds the request rate limit."""
    _ERROR_CODE = "ThrottlingException"

    @property
    def code(self) -> str | None:
        return self.response.get("Code")

    @property
    def request_id(self) -> str | None:
        """The ID of the request that exceeded the throttling limit."""
        return self.response.get("RequestId")


class TooManyTagsException(ChimeSDKMeetingsError):
    """Too many tags were added to the specified resource."""
    _ERROR_CODE = "TooManyTagsException"

    @property
    def code(self) -> str | None:
        return self.response.get("Code")

    @property
    def request_id(self) -> str | None:
        """The ID of the request that contains too many tags."""
        return self.response.get("RequestId")

    @property
    def resource_name(self) -> str | None:
        """The name of the resource that received too many tags."""
        return self.response.get("ResourceName")


class UnauthorizedException(ChimeSDKMeetingsError):
    """The user isn't authorized to request a resource."""
    _ERROR_CODE = "UnauthorizedException"

    @property
    def code(self) -> str | None:
        return self.response.get("Code")

    @property
    def request_id(self) -> str | None:
        """The request id associated with the call responsible for the exception."""
        return self.response.get("RequestId")


class UnprocessableEntityException(ChimeSDKMeetingsError):
    """The request was well-formed but was unable to be followed due to semantic errors."""
    _ERROR_CODE = "UnprocessableEntityException"

    @property
    def code(self) -> str | None:
        return self.response.get("Code")

    @property
    def request_id(self) -> str | None:
        """The request id associated with the call responsible for the exception."""
        return self.response.get("RequestId")


EXCEPTIONS: dict[str, type[ChimeSDKMeetingsError]] = {
    "BadRequestException": BadRequestException,
    "ConflictException": ConflictException,
    "ForbiddenException": ForbiddenException,
    "LimitExceededException": LimitExceededException,
    "NotFoundException": NotFoundException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceFailureException": ServiceFailureException,
    "ServiceUnavailableException": ServiceUnavailableException,
    "ThrottlingException": ThrottlingException,
    "TooManyTagsException": TooManyTagsException,
    "UnauthorizedException": UnauthorizedException,
    "UnprocessableEntityException": UnprocessableEntityException,
}
