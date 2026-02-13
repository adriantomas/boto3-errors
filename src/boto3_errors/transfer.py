# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class TransferError(Boto3Error):
    _SERVICE = "transfer"


class AccessDeniedException(TransferError):
    """You do not have sufficient access to perform this action."""
    _ERROR_CODE = "AccessDeniedException"


class ConflictException(TransferError):
    """This exception is thrown when the `UpdateServer` is called for a file transfer
    protocol-enabled server that has VPC as the endpoint type and the server's
    `VpcEndpointID` is not in the available state.
    """

    _ERROR_CODE = "ConflictException"


class InternalServiceError(TransferError):
    """This exception is thrown when an error occurs in the Transfer Family service."""
    _ERROR_CODE = "InternalServiceError"


class InvalidNextTokenException(TransferError):
    """The `NextToken` parameter that was passed is invalid."""
    _ERROR_CODE = "InvalidNextTokenException"


class InvalidRequestException(TransferError):
    """This exception is thrown when the client submits a malformed request."""
    _ERROR_CODE = "InvalidRequestException"


class ResourceExistsException(TransferError):
    """The requested resource does not exist, or exists in a region other than the one
    specified for the command.
    """

    _ERROR_CODE = "ResourceExistsException"

    @property
    def resource(self) -> str | None:
        return self.response.get("Resource")

    @property
    def resource_type(self) -> str | None:
        return self.response.get("ResourceType")


class ResourceNotFoundException(TransferError):
    """This exception is thrown when a resource is not found by the Amazon Web
    ServicesTransfer Family service.
    """

    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def resource(self) -> str | None:
        return self.response.get("Resource")

    @property
    def resource_type(self) -> str | None:
        return self.response.get("ResourceType")


class ServiceUnavailableException(TransferError):
    """The request has failed because the Amazon Web ServicesTransfer Family service is not
    available.
    """

    _ERROR_CODE = "ServiceUnavailableException"


class ThrottlingException(TransferError):
    """The request was denied due to request throttling."""
    _ERROR_CODE = "ThrottlingException"

    @property
    def retry_after_seconds(self) -> str | None:
        return self.response.get("RetryAfterSeconds")


EXCEPTIONS: dict[str, type[TransferError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServiceError": InternalServiceError,
    "InvalidNextTokenException": InvalidNextTokenException,
    "InvalidRequestException": InvalidRequestException,
    "ResourceExistsException": ResourceExistsException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceUnavailableException": ServiceUnavailableException,
    "ThrottlingException": ThrottlingException,
}
