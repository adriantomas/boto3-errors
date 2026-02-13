# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class PipesError(Boto3Error):
    _SERVICE = "pipes"


class ConflictException(PipesError):
    """An action you attempted resulted in an exception."""
    _ERROR_CODE = "ConflictException"

    @property
    def resource_id(self) -> str | None:
        """The ID of the resource that caused the exception."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of resource that caused the exception."""
        return self.response.get("resourceType")


class InternalException(PipesError):
    """This exception occurs due to unexpected causes."""
    _ERROR_CODE = "InternalException"

    @property
    def retry_after_seconds(self) -> int | None:
        """The number of seconds to wait before retrying the action that caused the
        exception.
        """
        return self.response.get("retryAfterSeconds")


class NotFoundException(PipesError):
    """An entity that you specified does not exist."""
    _ERROR_CODE = "NotFoundException"


class ServiceQuotaExceededException(PipesError):
    """A quota has been exceeded."""
    _ERROR_CODE = "ServiceQuotaExceededException"

    @property
    def resource_id(self) -> str | None:
        """The ID of the resource that caused the exception."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of resource that caused the exception."""
        return self.response.get("resourceType")

    @property
    def service_code(self) -> str | None:
        """The identifier of the service that caused the exception."""
        return self.response.get("serviceCode")

    @property
    def quota_code(self) -> str | None:
        """The identifier of the quota that caused the exception."""
        return self.response.get("quotaCode")


class ThrottlingException(PipesError):
    """An action was throttled."""
    _ERROR_CODE = "ThrottlingException"

    @property
    def service_code(self) -> str | None:
        """The identifier of the service that caused the exception."""
        return self.response.get("serviceCode")

    @property
    def quota_code(self) -> str | None:
        """The identifier of the quota that caused the exception."""
        return self.response.get("quotaCode")

    @property
    def retry_after_seconds(self) -> int | None:
        """The number of seconds to wait before retrying the action that caused the
        exception.
        """
        return self.response.get("retryAfterSeconds")


class ValidationException(PipesError):
    """Indicates that an error has occurred while performing a validate operation."""
    _ERROR_CODE = "ValidationException"

    @property
    def field_list(self) -> list[Any] | None:
        """The list of fields for which validation failed and the corresponding failure
        messages.
        """
        return self.response.get("fieldList")


EXCEPTIONS: dict[str, type[PipesError]] = {
    "ConflictException": ConflictException,
    "InternalException": InternalException,
    "NotFoundException": NotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
