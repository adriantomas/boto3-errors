# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class NetworkSecurityManagerError(Boto3Error):
    _SERVICE = "network-security-manager"


class AccessDeniedException(NetworkSecurityManagerError):
    """You do not have sufficient permissions to perform this action."""
    _ERROR_CODE = "AccessDeniedException"


class ConflictException(NetworkSecurityManagerError):
    """The request conflicts with the current state of the resource. For example, the
    resource was modified concurrently, or it is in a state that does not allow the
    requested operation.
    """

    _ERROR_CODE = "ConflictException"

    @property
    def resource_id(self) -> str | None:
        """The ID of the resource that is in conflict with the request."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of the resource that is in conflict with the request."""
        return self.response.get("resourceType")


class InternalServerException(NetworkSecurityManagerError):
    """The request processing failed because of an internal error in the service. This is a
    retryable error.
    """

    _ERROR_CODE = "InternalServerException"


class ResourceNotFoundException(NetworkSecurityManagerError):
    """The specified resource was not found. Verify that the resource identifier is correct
    and that the resource exists, then try your request again.
    """

    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def resource_id(self) -> str | None:
        """The ID of the resource that could not be found."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of the resource that could not be found."""
        return self.response.get("resourceType")


class ServiceQuotaExceededException(NetworkSecurityManagerError):
    """The request would exceed a service quota."""
    _ERROR_CODE = "ServiceQuotaExceededException"

    @property
    def quota_code(self) -> str | None:
        """The code that identifies the service quota that was exceeded."""
        return self.response.get("quotaCode")

    @property
    def resource_id(self) -> str | None:
        """The ID of the resource associated with the quota that was exceeded."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of the resource associated with the quota that was exceeded."""
        return self.response.get("resourceType")

    @property
    def service_code(self) -> str | None:
        """The code for the AWS service that owns the quota that was exceeded."""
        return self.response.get("serviceCode")


class ServiceUnavailableException(NetworkSecurityManagerError):
    """The service is temporarily unavailable. This is a retryable error."""
    _ERROR_CODE = "ServiceUnavailableException"

    @property
    def retry_after_seconds(self) -> int | None:
        """The number of seconds to wait before retrying the request."""
        return self.response.get("retryAfterSeconds")


class TagPolicyViolationException(NetworkSecurityManagerError):
    """The request violates a tag policy that is in effect for the account or organization."""
    _ERROR_CODE = "TagPolicyViolationException"


class ThrottlingException(NetworkSecurityManagerError):
    """The request was denied because of request throttling. Reduce your request rate and
    try again.
    """

    _ERROR_CODE = "ThrottlingException"

    @property
    def retry_after_seconds(self) -> int | None:
        """The number of seconds to wait before retrying the request."""
        return self.response.get("retryAfterSeconds")


class ValidationException(NetworkSecurityManagerError):
    """The request failed validation. For details, see the `reason` and `fieldList` members
    of the response.
    """

    _ERROR_CODE = "ValidationException"

    @property
    def field_list(self) -> list[Any] | None:
        """The list of request fields that failed validation, if any."""
        return self.response.get("fieldList")

    @property
    def reason(self) -> str | None:
        """The reason that the request failed validation."""
        return self.response.get("reason")


EXCEPTIONS: dict[str, type[NetworkSecurityManagerError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ServiceUnavailableException": ServiceUnavailableException,
    "TagPolicyViolationException": TagPolicyViolationException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
