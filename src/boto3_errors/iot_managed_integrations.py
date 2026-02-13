# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class IoTManagedIntegrationsError(Boto3Error):
    _SERVICE = "iot-managed-integrations"


class AccessDeniedException(IoTManagedIntegrationsError):
    """User is not authorized."""
    _ERROR_CODE = "AccessDeniedException"


class ConflictException(IoTManagedIntegrationsError):
    """There is a conflict with the request."""
    _ERROR_CODE = "ConflictException"


class InternalFailureException(IoTManagedIntegrationsError):
    """An unexpected error has occurred."""
    _ERROR_CODE = "InternalFailureException"


class InternalServerException(IoTManagedIntegrationsError):
    """Internal error from the service that indicates an unexpected error or that the
    service is unavailable.
    """

    _ERROR_CODE = "InternalServerException"


class InvalidRequestException(IoTManagedIntegrationsError):
    """The request is not valid."""
    _ERROR_CODE = "InvalidRequestException"


class LimitExceededException(IoTManagedIntegrationsError):
    """The request exceeds a service limit or quota. Adjust your request parameters and try
    again.
    """

    _ERROR_CODE = "LimitExceededException"


class ResourceNotFoundException(IoTManagedIntegrationsError):
    """The specified resource does not exist."""
    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def resource_id(self) -> str | None:
        """Id of the affected resource"""
        return self.response.get("ResourceId")

    @property
    def resource_type(self) -> str | None:
        """Type of the affected resource"""
        return self.response.get("ResourceType")


class ServiceQuotaExceededException(IoTManagedIntegrationsError):
    """The service quota has been exceeded for this request."""
    _ERROR_CODE = "ServiceQuotaExceededException"


class ServiceUnavailableException(IoTManagedIntegrationsError):
    """The service is temporarily unavailable."""
    _ERROR_CODE = "ServiceUnavailableException"


class ThrottlingException(IoTManagedIntegrationsError):
    """The rate exceeds the limit."""
    _ERROR_CODE = "ThrottlingException"


class UnauthorizedException(IoTManagedIntegrationsError):
    """You are not authorized to perform this operation."""
    _ERROR_CODE = "UnauthorizedException"


class ValidationException(IoTManagedIntegrationsError):
    """A validation error occurred when performing the API request."""
    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[IoTManagedIntegrationsError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalFailureException": InternalFailureException,
    "InternalServerException": InternalServerException,
    "InvalidRequestException": InvalidRequestException,
    "LimitExceededException": LimitExceededException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ServiceUnavailableException": ServiceUnavailableException,
    "ThrottlingException": ThrottlingException,
    "UnauthorizedException": UnauthorizedException,
    "ValidationException": ValidationException,
}
