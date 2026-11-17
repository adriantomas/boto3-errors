# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class OpenSearchMemoryError(Boto3Error):
    _SERVICE = "opensearchmemory"


class AccessDeniedException(OpenSearchMemoryError):
    """You don't have sufficient access to perform this operation. To use this operation,
    you must have AWS Identity and Access Management (IAM) permissions for the
    operation, and on the resource it acts on. If the space uses a customer managed AWS
    Key Management Service (AWS KMS) key, you must also have permission to use the key.
    """

    _ERROR_CODE = "AccessDeniedException"


class ConflictException(OpenSearchMemoryError):
    """The request conflicts with the current state of the resource. For example, the space
    is being created, updated, or deleted, a space with the same name already exists, or
    you reused a client token with different parameters. Wait for the space to finish
    being created, updated, or deleted, or use a different name or client token, and
    then retry.
    """

    _ERROR_CODE = "ConflictException"

    @property
    def resource_id(self) -> str | None:
        """The ID of the resource that caused the conflict."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of the resource that caused the conflict."""
        return self.response.get("resourceType")


class InternalServerException(OpenSearchMemoryError):
    """The service couldn't process the request because of an internal error. Retry the
    request.
    """

    _ERROR_CODE = "InternalServerException"


class ResourceNotFoundException(OpenSearchMemoryError):
    """The specified resource doesn't exist. Check the IDs in the request."""
    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def resource_id(self) -> str | None:
        """The ID of the resource that wasn't found."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of the resource that wasn't found."""
        return self.response.get("resourceType")


class ServiceQuotaExceededException(OpenSearchMemoryError):
    """The request would exceed a quota, such as the number of spaces in your account or
    the number of strategies in a space.
    """

    _ERROR_CODE = "ServiceQuotaExceededException"

    @property
    def quota_code(self) -> str | None:
        """The Service Quotas code of the quota that the request would exceed. Not
        currently returned.
        """
        return self.response.get("quotaCode")

    @property
    def service_code(self) -> str | None:
        """The Service Quotas code of the service. Not currently returned."""
        return self.response.get("serviceCode")


class ThrottlingException(OpenSearchMemoryError):
    """The service throttled the request. Retry the request with exponential backoff."""
    _ERROR_CODE = "ThrottlingException"

    @property
    def retry_after_seconds(self) -> int | None:
        """The number of seconds to wait before you retry the request."""
        return self.response.get("retryAfterSeconds")


class ValidationException(OpenSearchMemoryError):
    """The request isn't valid. The `reason`, `message`, and `fieldList` members describe
    the problem. Fix the request, and then try again.
    """

    _ERROR_CODE = "ValidationException"

    @property
    def field_list(self) -> list[Any] | None:
        """The fields that failed validation, if any."""
        return self.response.get("fieldList")

    @property
    def reason(self) -> str | None:
        """The reason that the request failed validation."""
        return self.response.get("reason")


EXCEPTIONS: dict[str, type[OpenSearchMemoryError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
