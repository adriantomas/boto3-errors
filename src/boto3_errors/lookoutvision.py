# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class LookoutVisionError(Boto3Error):
    _SERVICE = "lookoutvision"


class AccessDeniedException(LookoutVisionError):
    """You are not authorized to perform the action."""
    _ERROR_CODE = "AccessDeniedException"


class ConflictException(LookoutVisionError):
    """The update or deletion of a resource caused an inconsistent state."""
    _ERROR_CODE = "ConflictException"

    @property
    def resource_id(self) -> str | None:
        """The ID of the resource."""
        return self.response.get("ResourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of the resource."""
        return self.response.get("ResourceType")


class InternalServerException(LookoutVisionError):
    """Amazon Lookout for Vision experienced a service issue. Try your call again."""
    _ERROR_CODE = "InternalServerException"

    @property
    def retry_after_seconds(self) -> int | None:
        """The period of time, in seconds, before the operation can be retried."""
        return self.response.get("RetryAfterSeconds")


class ResourceNotFoundException(LookoutVisionError):
    """The resource could not be found."""
    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def resource_id(self) -> str | None:
        """The ID of the resource."""
        return self.response.get("ResourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of the resource."""
        return self.response.get("ResourceType")


class ServiceQuotaExceededException(LookoutVisionError):
    """A service quota was exceeded the allowed limit. For more information, see Limits in
    Amazon Lookout for Vision in the Amazon Lookout for Vision Developer Guide.
    """

    _ERROR_CODE = "ServiceQuotaExceededException"

    @property
    def quota_code(self) -> str | None:
        """The quota code."""
        return self.response.get("QuotaCode")

    @property
    def resource_id(self) -> str | None:
        """The ID of the resource."""
        return self.response.get("ResourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of the resource."""
        return self.response.get("ResourceType")

    @property
    def service_code(self) -> str | None:
        """The service code."""
        return self.response.get("ServiceCode")


class ThrottlingException(LookoutVisionError):
    """Amazon Lookout for Vision is temporarily unable to process the request. Try your
    call again.
    """

    _ERROR_CODE = "ThrottlingException"

    @property
    def quota_code(self) -> str | None:
        """The quota code."""
        return self.response.get("QuotaCode")

    @property
    def retry_after_seconds(self) -> int | None:
        """The period of time, in seconds, before the operation can be retried."""
        return self.response.get("RetryAfterSeconds")

    @property
    def service_code(self) -> str | None:
        """The service code."""
        return self.response.get("ServiceCode")


class ValidationException(LookoutVisionError):
    """An input validation error occured. For example, invalid characters in a project
    name, or if a pagination token is invalid.
    """

    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[LookoutVisionError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
