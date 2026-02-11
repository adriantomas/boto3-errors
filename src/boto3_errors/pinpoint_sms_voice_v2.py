# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class PinpointSMSVoiceV2Error(Boto3Error):
    _SERVICE = "pinpoint-sms-voice-v2"


class AccessDeniedException(PinpointSMSVoiceV2Error):
    """The request was denied because you don't have sufficient permissions to access the
    resource.
    """

    _ERROR_CODE = "AccessDeniedException"

    @property
    def reason(self) -> str | None:
        """The reason for the exception."""
        return self.response.get("Reason")


class ConflictException(PinpointSMSVoiceV2Error):
    """Your request has conflicting operations. This can occur if you're trying to perform
    more than one operation on the same resource at the same time or it could be that
    the requested action isn't valid for the current state or configuration of the
    resource.
    """

    _ERROR_CODE = "ConflictException"

    @property
    def reason(self) -> str | None:
        """The reason for the exception."""
        return self.response.get("Reason")

    @property
    def resource_type(self) -> str | None:
        """The type of resource that caused the exception."""
        return self.response.get("ResourceType")

    @property
    def resource_id(self) -> str | None:
        """The unique identifier of the request."""
        return self.response.get("ResourceId")


class InternalServerException(PinpointSMSVoiceV2Error):
    """The API encountered an unexpected error and couldn't complete the request. You might
    be able to successfully issue the request again in the future.
    """

    _ERROR_CODE = "InternalServerException"

    @property
    def request_id(self) -> str | None:
        """The unique identifier of the request."""
        return self.response.get("RequestId")


class ResourceNotFoundException(PinpointSMSVoiceV2Error):
    """A requested resource couldn't be found."""
    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def resource_type(self) -> str | None:
        """The type of resource that caused the exception."""
        return self.response.get("ResourceType")

    @property
    def resource_id(self) -> str | None:
        """The unique identifier of the resource."""
        return self.response.get("ResourceId")


class ServiceQuotaExceededException(PinpointSMSVoiceV2Error):
    """The request would cause a service quota to be exceeded."""
    _ERROR_CODE = "ServiceQuotaExceededException"

    @property
    def reason(self) -> str | None:
        """The reason for the exception."""
        return self.response.get("Reason")


class ThrottlingException(PinpointSMSVoiceV2Error):
    """An error that occurred because too many requests were sent during a certain amount
    of time.
    """

    _ERROR_CODE = "ThrottlingException"


class ValidationException(PinpointSMSVoiceV2Error):
    """A validation exception for a field."""
    _ERROR_CODE = "ValidationException"

    @property
    def reason(self) -> str | None:
        """The reason for the exception."""
        return self.response.get("Reason")

    @property
    def fields(self) -> list[Any] | None:
        """The field that failed validation."""
        return self.response.get("Fields")


EXCEPTIONS: dict[str, type[PinpointSMSVoiceV2Error]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
