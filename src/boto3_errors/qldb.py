# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class QLDBError(Boto3Error):
    _SERVICE = "qldb"


class InvalidParameterException(QLDBError):
    """One or more parameters in the request aren't valid."""
    _ERROR_CODE = "InvalidParameterException"

    @property
    def parameter_name(self) -> str | None:
        """The name of the invalid parameter."""
        return self.response.get("ParameterName")


class LimitExceededException(QLDBError):
    """You have reached the limit on the maximum number of resources allowed."""
    _ERROR_CODE = "LimitExceededException"

    @property
    def resource_type(self) -> str | None:
        """The type of resource."""
        return self.response.get("ResourceType")


class ResourceAlreadyExistsException(QLDBError):
    """The specified resource already exists."""
    _ERROR_CODE = "ResourceAlreadyExistsException"

    @property
    def resource_name(self) -> str | None:
        """The name of the resource."""
        return self.response.get("ResourceName")

    @property
    def resource_type(self) -> str | None:
        """The type of resource."""
        return self.response.get("ResourceType")


class ResourceInUseException(QLDBError):
    """The specified resource can't be modified at this time."""
    _ERROR_CODE = "ResourceInUseException"

    @property
    def resource_name(self) -> str | None:
        """The name of the resource."""
        return self.response.get("ResourceName")

    @property
    def resource_type(self) -> str | None:
        """The type of resource."""
        return self.response.get("ResourceType")


class ResourceNotFoundException(QLDBError):
    """The specified resource doesn't exist."""
    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def resource_name(self) -> str | None:
        """The name of the resource."""
        return self.response.get("ResourceName")

    @property
    def resource_type(self) -> str | None:
        """The type of resource."""
        return self.response.get("ResourceType")


class ResourcePreconditionNotMetException(QLDBError):
    """The operation failed because a condition wasn't satisfied in advance."""
    _ERROR_CODE = "ResourcePreconditionNotMetException"

    @property
    def resource_name(self) -> str | None:
        """The name of the resource."""
        return self.response.get("ResourceName")

    @property
    def resource_type(self) -> str | None:
        """The type of resource."""
        return self.response.get("ResourceType")


EXCEPTIONS: dict[str, type[QLDBError]] = {
    "InvalidParameterException": InvalidParameterException,
    "LimitExceededException": LimitExceededException,
    "ResourceAlreadyExistsException": ResourceAlreadyExistsException,
    "ResourceInUseException": ResourceInUseException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ResourcePreconditionNotMetException": ResourcePreconditionNotMetException,
}
