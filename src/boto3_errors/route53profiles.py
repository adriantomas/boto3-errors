# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class Route53ProfilesError(Boto3Error):
    _SERVICE = "route53profiles"


class AccessDeniedException(Route53ProfilesError):
    """The current account doesn't have the IAM permissions required to perform the
    specified operation.
    """

    _ERROR_CODE = "AccessDeniedException"


class ConflictException(Route53ProfilesError):
    """The request you submitted conflicts with an existing request."""
    _ERROR_CODE = "ConflictException"


class InternalServiceErrorException(Route53ProfilesError):
    """An internal server error occured. Retry your request."""
    _ERROR_CODE = "InternalServiceErrorException"


class InvalidNextTokenException(Route53ProfilesError):
    """The `NextToken` you provided isn;t valid."""
    _ERROR_CODE = "InvalidNextTokenException"


class InvalidParameterException(Route53ProfilesError):
    """One or more parameters in this request are not valid."""
    _ERROR_CODE = "InvalidParameterException"

    @property
    def field_name(self) -> str | None:
        """The parameter field name for the invalid parameter exception."""
        return self.response.get("FieldName")


class LimitExceededException(Route53ProfilesError):
    """The request caused one or more limits to be exceeded."""
    _ERROR_CODE = "LimitExceededException"

    @property
    def resource_type(self) -> str | None:
        """The resource type that caused the limits to be exceeded."""
        return self.response.get("ResourceType")


class ResourceExistsException(Route53ProfilesError):
    """The resource you are trying to associate, has already been associated."""
    _ERROR_CODE = "ResourceExistsException"

    @property
    def resource_type(self) -> str | None:
        """The resource type that caused the resource exists exception."""
        return self.response.get("ResourceType")


class ResourceNotFoundException(Route53ProfilesError):
    """The resource you are associating is not found."""
    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def resource_type(self) -> str | None:
        """The resource type that caused the resource not found exception."""
        return self.response.get("ResourceType")


class ThrottlingException(Route53ProfilesError):
    """The request was throttled. Try again in a few minutes."""
    _ERROR_CODE = "ThrottlingException"


class ValidationException(Route53ProfilesError):
    """You have provided an invalid command."""
    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[Route53ProfilesError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServiceErrorException": InternalServiceErrorException,
    "InvalidNextTokenException": InvalidNextTokenException,
    "InvalidParameterException": InvalidParameterException,
    "LimitExceededException": LimitExceededException,
    "ResourceExistsException": ResourceExistsException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
