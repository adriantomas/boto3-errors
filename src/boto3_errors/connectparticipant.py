# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class ConnectParticipantError(Boto3Error):
    _SERVICE = "connectparticipant"


class AccessDeniedException(ConnectParticipantError):
    """You do not have sufficient access to perform this action."""
    _ERROR_CODE = "AccessDeniedException"


class ConflictException(ConnectParticipantError):
    """The requested operation conflicts with the current state of a service resource
    associated with the request.
    """

    _ERROR_CODE = "ConflictException"


class InternalServerException(ConnectParticipantError):
    """This exception occurs when there is an internal failure in the Amazon Connect
    service.
    """

    _ERROR_CODE = "InternalServerException"


class ResourceNotFoundException(ConnectParticipantError):
    """The resource was not found."""
    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def resource_id(self) -> str | None:
        """The identifier of the resource."""
        return self.response.get("ResourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of Amazon Connect resource."""
        return self.response.get("ResourceType")


class ServiceQuotaExceededException(ConnectParticipantError):
    """The number of attachments per contact exceeds the quota."""
    _ERROR_CODE = "ServiceQuotaExceededException"


class ThrottlingException(ConnectParticipantError):
    """The request was denied due to request throttling."""
    _ERROR_CODE = "ThrottlingException"


class ValidationException(ConnectParticipantError):
    """The input fails to satisfy the constraints specified by Amazon Connect."""
    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[ConnectParticipantError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
