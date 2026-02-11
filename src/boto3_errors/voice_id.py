# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class VoiceIDError(Boto3Error):
    _SERVICE = "voice-id"


class AccessDeniedException(VoiceIDError):
    """You do not have sufficient permissions to perform this action. Check the error
    message and try again.
    """

    _ERROR_CODE = "AccessDeniedException"


class ConflictException(VoiceIDError):
    """The request failed due to a conflict. Check the `ConflictType` and error message for
    more details.
    """

    _ERROR_CODE = "ConflictException"

    @property
    def conflict_type(self) -> str | None:
        """The type of conflict which caused a ConflictException. Possible types and the
        corresponding error messages are as follows:

        - `DOMAIN_NOT_ACTIVE`: The domain is not active.
        - `CANNOT_CHANGE_SPEAKER_AFTER_ENROLLMENT`: You cannot change the speaker ID
          after an enrollment has been requested.
        - `ENROLLMENT_ALREADY_EXISTS`: There is already an enrollment for this session.
        - `SPEAKER_NOT_SET`: You must set the speaker ID before requesting an
          enrollment.
        - `SPEAKER_OPTED_OUT`: You cannot request an enrollment for an opted out
          speaker.
        - `CONCURRENT_CHANGES`: The request could not be processed as the resource was
          modified by another request during execution.
        """
        return self.response.get("ConflictType")


class InternalServerException(VoiceIDError):
    """The request failed due to an unknown error on the server side."""
    _ERROR_CODE = "InternalServerException"


class ResourceNotFoundException(VoiceIDError):
    """The specified resource cannot be found. Check the `ResourceType` and error message
    for more details.
    """

    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def resource_type(self) -> str | None:
        """The type of resource which cannot not be found. Possible types are `BATCH_JOB`,
        `COMPLIANCE_CONSENT`, `DOMAIN`, `FRAUDSTER`, `SESSION` and `SPEAKER`.
        """
        return self.response.get("ResourceType")


class ServiceQuotaExceededException(VoiceIDError):
    """The request exceeded the service quota. Refer to Voice ID Service Quotas and try
    your request again.
    """

    _ERROR_CODE = "ServiceQuotaExceededException"


class ThrottlingException(VoiceIDError):
    """The request was denied due to request throttling. Please slow down your request
    rate. Refer to Amazon Connect Voice ID Service API throttling quotas and try your
    request again.
    """

    _ERROR_CODE = "ThrottlingException"


class ValidationException(VoiceIDError):
    """The request failed one or more validations; check the error message for more
    details.
    """

    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[VoiceIDError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
