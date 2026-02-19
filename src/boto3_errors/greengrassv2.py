# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class GreengrassV2Error(Boto3Error):
    _SERVICE = "greengrassv2"


class AccessDeniedException(GreengrassV2Error):
    """You don't have permission to perform the action."""
    _ERROR_CODE = "AccessDeniedException"


class ConflictException(GreengrassV2Error):
    """Your request has conflicting operations. This can occur if you're trying to perform
    more than one operation on the same resource at the same time.
    """

    _ERROR_CODE = "ConflictException"

    @property
    def resource_id(self) -> str | None:
        """The ID of the resource that conflicts with the request."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of the resource that conflicts with the request."""
        return self.response.get("resourceType")


class InternalServerException(GreengrassV2Error):
    """IoT Greengrass can't process your request right now. Try again later."""
    _ERROR_CODE = "InternalServerException"

    @property
    def retry_after_seconds(self) -> int | None:
        """The amount of time to wait before you retry the request."""
        return self.response.get("retryAfterSeconds")


class RequestAlreadyInProgressException(GreengrassV2Error):
    """The request is already in progress. This exception occurs when you use a client
    token for multiple requests while IoT Greengrass is still processing an earlier
    request that uses the same client token.
    """

    _ERROR_CODE = "RequestAlreadyInProgressException"


class ResourceNotFoundException(GreengrassV2Error):
    """The requested resource can't be found."""
    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def resource_id(self) -> str | None:
        """The ID of the resource that isn't found."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of the resource that isn't found."""
        return self.response.get("resourceType")


class ServiceQuotaExceededException(GreengrassV2Error):
    """Your request exceeds a service quota. For example, you might have the maximum number
    of components that you can create.
    """

    _ERROR_CODE = "ServiceQuotaExceededException"

    @property
    def quota_code(self) -> str | None:
        """The code for the quota in Service Quotas."""
        return self.response.get("quotaCode")

    @property
    def resource_id(self) -> str | None:
        """The ID of the resource that exceeds the service quota."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of the resource that exceeds the service quota."""
        return self.response.get("resourceType")

    @property
    def service_code(self) -> str | None:
        """The code for the service in Service Quotas."""
        return self.response.get("serviceCode")


class ThrottlingException(GreengrassV2Error):
    """Your request exceeded a request rate quota. For example, you might have exceeded the
    amount of times that you can retrieve device or deployment status per second.
    """

    _ERROR_CODE = "ThrottlingException"

    @property
    def quota_code(self) -> str | None:
        """The code for the quota in Service Quotas."""
        return self.response.get("quotaCode")

    @property
    def retry_after_seconds(self) -> int | None:
        """The amount of time to wait before you retry the request."""
        return self.response.get("retryAfterSeconds")

    @property
    def service_code(self) -> str | None:
        """The code for the service in Service Quotas."""
        return self.response.get("serviceCode")


class ValidationException(GreengrassV2Error):
    """The request isn't valid. This can occur if your request contains malformed JSON or
    unsupported characters.
    """

    _ERROR_CODE = "ValidationException"

    @property
    def fields(self) -> list[Any] | None:
        """The list of fields that failed to validate."""
        return self.response.get("fields")

    @property
    def reason(self) -> str | None:
        """The reason for the validation exception."""
        return self.response.get("reason")


EXCEPTIONS: dict[str, type[GreengrassV2Error]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "RequestAlreadyInProgressException": RequestAlreadyInProgressException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
