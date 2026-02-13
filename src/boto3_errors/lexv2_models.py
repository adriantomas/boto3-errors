# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class LexModelsV2Error(Boto3Error):
    _SERVICE = "lexv2-models"


class ConflictException(LexModelsV2Error):
    """The action that you tried to perform couldn't be completed because the resource is
    in a conflicting state. For example, deleting a bot that is in the CREATING state.
    Try your request again.
    """

    _ERROR_CODE = "ConflictException"


class InternalServerException(LexModelsV2Error):
    """The service encountered an unexpected condition. Try your request again."""
    _ERROR_CODE = "InternalServerException"


class PreconditionFailedException(LexModelsV2Error):
    """Your request couldn't be completed because one or more request fields aren't valid.
    Check the fields in your request and try again.
    """

    _ERROR_CODE = "PreconditionFailedException"


class ResourceNotFoundException(LexModelsV2Error):
    """You asked to describe a resource that doesn't exist. Check the resource that you are
    requesting and try again.
    """

    _ERROR_CODE = "ResourceNotFoundException"


class ServiceQuotaExceededException(LexModelsV2Error):
    """You have reached a quota for your bot."""
    _ERROR_CODE = "ServiceQuotaExceededException"


class ThrottlingException(LexModelsV2Error):
    """Your request rate is too high. Reduce the frequency of requests."""
    _ERROR_CODE = "ThrottlingException"

    @property
    def retry_after_seconds(self) -> int | None:
        """The number of seconds after which the user can invoke the API again."""
        return self.response.get("retryAfterSeconds")


class ValidationException(LexModelsV2Error):
    """One of the input parameters in your request isn't valid. Check the parameters and
    try your request again.
    """

    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[LexModelsV2Error]] = {
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "PreconditionFailedException": PreconditionFailedException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
