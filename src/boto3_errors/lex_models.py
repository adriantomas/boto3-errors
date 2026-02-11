# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class LexModelBuildingServiceError(Boto3Error):
    _SERVICE = "lex-models"


class AccessDeniedException(LexModelBuildingServiceError):
    """Your IAM user or role does not have permission to call the Amazon Lex V2 APIs
    required to migrate your bot.
    """

    _ERROR_CODE = "AccessDeniedException"


class BadRequestException(LexModelBuildingServiceError):
    """The request is not well formed. For example, a value is invalid or a required field
    is missing. Check the field values, and try again.
    """

    _ERROR_CODE = "BadRequestException"


class ConflictException(LexModelBuildingServiceError):
    """There was a conflict processing the request. Try your request again."""
    _ERROR_CODE = "ConflictException"


class InternalFailureException(LexModelBuildingServiceError):
    """An internal Amazon Lex error occurred. Try your request again."""
    _ERROR_CODE = "InternalFailureException"


class LimitExceededException(LexModelBuildingServiceError):
    """The request exceeded a limit. Try your request again."""
    _ERROR_CODE = "LimitExceededException"

    @property
    def retry_after_seconds(self) -> str | None:
        return self.response.get("retryAfterSeconds")


class NotFoundException(LexModelBuildingServiceError):
    """The resource specified in the request was not found. Check the resource and try
    again.
    """

    _ERROR_CODE = "NotFoundException"


class PreconditionFailedException(LexModelBuildingServiceError):
    """The checksum of the resource that you are trying to change does not match the
    checksum in the request. Check the resource's checksum and try again.
    """

    _ERROR_CODE = "PreconditionFailedException"


class ResourceInUseException(LexModelBuildingServiceError):
    """The resource that you are attempting to delete is referred to by another resource.
    Use this information to remove references to the resource that you are trying to
    delete.

    The body of the exception contains a JSON object that describes the resource.

     `{ "resourceType": BOT | BOTALIAS | BOTCHANNEL | INTENT,`

     `"resourceReference": {`

     `"name": string, "version": string } }`
    """

    _ERROR_CODE = "ResourceInUseException"

    @property
    def reference_type(self) -> str | None:
        return self.response.get("referenceType")

    @property
    def example_reference(self) -> dict[str, Any] | None:
        return self.response.get("exampleReference")


EXCEPTIONS: dict[str, type[LexModelBuildingServiceError]] = {
    "AccessDeniedException": AccessDeniedException,
    "BadRequestException": BadRequestException,
    "ConflictException": ConflictException,
    "InternalFailureException": InternalFailureException,
    "LimitExceededException": LimitExceededException,
    "NotFoundException": NotFoundException,
    "PreconditionFailedException": PreconditionFailedException,
    "ResourceInUseException": ResourceInUseException,
}
