# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class DLMError(Boto3Error):
    _SERVICE = "dlm"


class InternalServerException(DLMError):
    """The service failed in an unexpected way."""
    _ERROR_CODE = "InternalServerException"

    @property
    def code(self) -> str | None:
        return self.response.get("Code")


class InvalidRequestException(DLMError):
    """Bad request. The request is missing required parameters or has invalid parameters."""
    _ERROR_CODE = "InvalidRequestException"

    @property
    def code(self) -> str | None:
        return self.response.get("Code")

    @property
    def required_parameters(self) -> list[Any] | None:
        """The request omitted one or more required parameters."""
        return self.response.get("RequiredParameters")

    @property
    def mutually_exclusive_parameters(self) -> list[Any] | None:
        """The request included parameters that cannot be provided together."""
        return self.response.get("MutuallyExclusiveParameters")


class LimitExceededException(DLMError):
    """The request failed because a limit was exceeded."""
    _ERROR_CODE = "LimitExceededException"

    @property
    def code(self) -> str | None:
        return self.response.get("Code")

    @property
    def resource_type(self) -> str | None:
        """Value is the type of resource for which a limit was exceeded."""
        return self.response.get("ResourceType")


class ResourceNotFoundException(DLMError):
    """A requested resource was not found."""
    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def code(self) -> str | None:
        return self.response.get("Code")

    @property
    def resource_type(self) -> str | None:
        """Value is the type of resource that was not found."""
        return self.response.get("ResourceType")

    @property
    def resource_ids(self) -> list[Any] | None:
        """Value is a list of resource IDs that were not found."""
        return self.response.get("ResourceIds")


EXCEPTIONS: dict[str, type[DLMError]] = {
    "InternalServerException": InternalServerException,
    "InvalidRequestException": InvalidRequestException,
    "LimitExceededException": LimitExceededException,
    "ResourceNotFoundException": ResourceNotFoundException,
}
