# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class ApplicationInsightsError(Boto3Error):
    _SERVICE = "application-insights"


class AccessDeniedException(ApplicationInsightsError):
    """User does not have permissions to perform this action."""
    _ERROR_CODE = "AccessDeniedException"


class BadRequestException(ApplicationInsightsError):
    """The request is not understood by the server."""
    _ERROR_CODE = "BadRequestException"


class InternalServerException(ApplicationInsightsError):
    """The server encountered an internal error and is unable to complete the request."""
    _ERROR_CODE = "InternalServerException"


class ResourceInUseException(ApplicationInsightsError):
    """The resource is already created or in use."""
    _ERROR_CODE = "ResourceInUseException"


class ResourceNotFoundException(ApplicationInsightsError):
    """The resource does not exist in the customer account."""
    _ERROR_CODE = "ResourceNotFoundException"


class TagsAlreadyExistException(ApplicationInsightsError):
    """Tags are already registered for the specified application ARN."""
    _ERROR_CODE = "TagsAlreadyExistException"


class TooManyTagsException(ApplicationInsightsError):
    """The number of the provided tags is beyond the limit, or the number of total tags you
    are trying to attach to the specified resource exceeds the limit.
    """

    _ERROR_CODE = "TooManyTagsException"

    @property
    def resource_name(self) -> str | None:
        """The name of the resource with too many tags."""
        return self.response.get("ResourceName")


class ValidationException(ApplicationInsightsError):
    """The parameter is not valid."""
    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[ApplicationInsightsError]] = {
    "AccessDeniedException": AccessDeniedException,
    "BadRequestException": BadRequestException,
    "InternalServerException": InternalServerException,
    "ResourceInUseException": ResourceInUseException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "TagsAlreadyExistException": TagsAlreadyExistException,
    "TooManyTagsException": TooManyTagsException,
    "ValidationException": ValidationException,
}
