# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class ManagedBlockchainError(Boto3Error):
    _SERVICE = "managedblockchain"


class AccessDeniedException(ManagedBlockchainError):
    """You don't have sufficient access to perform this action."""
    _ERROR_CODE = "AccessDeniedException"


class IllegalActionException(ManagedBlockchainError):
    _ERROR_CODE = "IllegalActionException"


class InternalServiceErrorException(ManagedBlockchainError):
    """The request processing has failed because of an unknown error, exception or failure."""
    _ERROR_CODE = "InternalServiceErrorException"


class InvalidRequestException(ManagedBlockchainError):
    """The action or operation requested is invalid. Verify that the action is typed
    correctly.
    """

    _ERROR_CODE = "InvalidRequestException"


class ResourceAlreadyExistsException(ManagedBlockchainError):
    """A resource request is issued for a resource that already exists."""
    _ERROR_CODE = "ResourceAlreadyExistsException"


class ResourceLimitExceededException(ManagedBlockchainError):
    """The maximum number of resources of that type already exist. Ensure the resources
    requested are within the boundaries of the service edition and your account limits.
    """

    _ERROR_CODE = "ResourceLimitExceededException"


class ResourceNotFoundException(ManagedBlockchainError):
    """A requested resource doesn't exist. It may have been deleted or referenced
    incorrectly.
    """

    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def resource_name(self) -> str | None:
        """A requested resource doesn't exist. It may have been deleted or referenced
        inaccurately.
        """
        return self.response.get("ResourceName")


class ResourceNotReadyException(ManagedBlockchainError):
    """The requested resource exists but isn't in a status that can complete the operation."""
    _ERROR_CODE = "ResourceNotReadyException"


class ThrottlingException(ManagedBlockchainError):
    """The request or operation couldn't be performed because a service is throttling
    requests. The most common source of throttling errors is creating resources that
    exceed your service limit for this resource type. Request a limit increase or delete
    unused resources if possible.
    """

    _ERROR_CODE = "ThrottlingException"


class TooManyTagsException(ManagedBlockchainError):
    _ERROR_CODE = "TooManyTagsException"

    @property
    def resource_name(self) -> str | None:
        return self.response.get("ResourceName")


EXCEPTIONS: dict[str, type[ManagedBlockchainError]] = {
    "AccessDeniedException": AccessDeniedException,
    "IllegalActionException": IllegalActionException,
    "InternalServiceErrorException": InternalServiceErrorException,
    "InvalidRequestException": InvalidRequestException,
    "ResourceAlreadyExistsException": ResourceAlreadyExistsException,
    "ResourceLimitExceededException": ResourceLimitExceededException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ResourceNotReadyException": ResourceNotReadyException,
    "ThrottlingException": ThrottlingException,
    "TooManyTagsException": TooManyTagsException,
}
