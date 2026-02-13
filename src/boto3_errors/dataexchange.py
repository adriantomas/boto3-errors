# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class DataExchangeError(Boto3Error):
    _SERVICE = "dataexchange"


class AccessDeniedException(DataExchangeError):
    """Access to the resource is denied."""
    _ERROR_CODE = "AccessDeniedException"


class ConflictException(DataExchangeError):
    """The request couldn't be completed because it conflicted with the current state of
    the resource.
    """

    _ERROR_CODE = "ConflictException"

    @property
    def resource_id(self) -> str | None:
        """The unique identifier for the resource with the conflict."""
        return self.response.get("ResourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of the resource with the conflict."""
        return self.response.get("ResourceType")


class InternalServerException(DataExchangeError):
    """An exception occurred with the service."""
    _ERROR_CODE = "InternalServerException"


class ResourceNotFoundException(DataExchangeError):
    """The resource couldn't be found."""
    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def resource_id(self) -> str | None:
        """The unique identifier for the resource that couldn't be found."""
        return self.response.get("ResourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of resource that couldn't be found."""
        return self.response.get("ResourceType")


class ServiceLimitExceededException(DataExchangeError):
    """The request has exceeded the quotas imposed by the service."""
    _ERROR_CODE = "ServiceLimitExceededException"

    @property
    def limit_name(self) -> str | None:
        """The name of the limit that was reached."""
        return self.response.get("LimitName")

    @property
    def limit_value(self) -> float | None:
        """The value of the exceeded limit."""
        return self.response.get("LimitValue")


class ThrottlingException(DataExchangeError):
    """The limit on the number of requests per second was exceeded."""
    _ERROR_CODE = "ThrottlingException"


class ValidationException(DataExchangeError):
    """The request was invalid."""
    _ERROR_CODE = "ValidationException"

    @property
    def exception_cause(self) -> str | None:
        """The unique identifier for the resource that couldn't be found."""
        return self.response.get("ExceptionCause")


EXCEPTIONS: dict[str, type[DataExchangeError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceLimitExceededException": ServiceLimitExceededException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
