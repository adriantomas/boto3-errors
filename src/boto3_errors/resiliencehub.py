# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class resiliencehubError(Boto3Error):
    _SERVICE = "resiliencehub"


class AccessDeniedException(resiliencehubError):
    """You don't have permissions to perform the requested operation. The user or role that
    is making the request must have at least one IAM permissions policy attached that
    grants the required permissions.
    """

    _ERROR_CODE = "AccessDeniedException"


class ConflictException(resiliencehubError):
    """This exception occurs when a conflict with a previous successful write is detected.
    This generally occurs when the previous write did not have time to propagate to the
    host serving the current request. A retry (with appropriate backoff logic) is the
    recommended response to this exception.
    """

    _ERROR_CODE = "ConflictException"

    @property
    def resource_id(self) -> str | None:
        """The identifier of the resource that the exception applies to."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of the resource that the exception applies to."""
        return self.response.get("resourceType")


class InternalServerException(resiliencehubError):
    """This exception occurs when there is an internal failure in the Resilience Hub
    service.
    """

    _ERROR_CODE = "InternalServerException"


class ResourceNotFoundException(resiliencehubError):
    """This exception occurs when the specified resource could not be found."""
    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def resource_id(self) -> str | None:
        """The identifier of the resource that the exception applies to."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of the resource that the exception applies to."""
        return self.response.get("resourceType")


class ServiceQuotaExceededException(resiliencehubError):
    """This exception occurs when you have exceeded your service quota. To perform the
    requested action, remove some of the relevant resources, or use Service Quotas to
    request a service quota increase.
    """

    _ERROR_CODE = "ServiceQuotaExceededException"


class ThrottlingException(resiliencehubError):
    """This exception occurs when you have exceeded the limit on the number of requests per
    second.
    """

    _ERROR_CODE = "ThrottlingException"

    @property
    def retry_after_seconds(self) -> int | None:
        """The number of seconds to wait before retrying the operation."""
        return self.response.get("retryAfterSeconds")


class ValidationException(resiliencehubError):
    """This exception occurs when a request is not valid."""
    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[resiliencehubError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
