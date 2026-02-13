# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class SecurityLakeError(Boto3Error):
    _SERVICE = "securitylake"


class AccessDeniedException(SecurityLakeError):
    """You do not have sufficient access to perform this action. Access denied errors
    appear when Amazon Security Lake explicitly or implicitly denies an authorization
    request. An explicit denial occurs when a policy contains a Deny statement for the
    specific Amazon Web Services action. An implicit denial occurs when there is no
    applicable Deny statement and also no applicable Allow statement.
    """

    _ERROR_CODE = "AccessDeniedException"

    @property
    def error_code(self) -> str | None:
        """A coded string to provide more information about the access denied exception.
        You can use the error code to check the exception type.
        """
        return self.response.get("errorCode")


class BadRequestException(SecurityLakeError):
    """The request is malformed or contains an error such as an invalid parameter value or
    a missing required parameter.
    """

    _ERROR_CODE = "BadRequestException"


class ConflictException(SecurityLakeError):
    """Occurs when a conflict with a previous successful write is detected. This generally
    occurs when the previous write did not have time to propagate to the host serving
    the current request. A retry (with appropriate backoff logic) is the recommended
    response to this exception.
    """

    _ERROR_CODE = "ConflictException"

    @property
    def resource_name(self) -> str | None:
        """The resource name."""
        return self.response.get("resourceName")

    @property
    def resource_type(self) -> str | None:
        """The resource type."""
        return self.response.get("resourceType")


class InternalServerException(SecurityLakeError):
    """Internal service exceptions are sometimes caused by transient issues. Before you
    start troubleshooting, perform the operation again.
    """

    _ERROR_CODE = "InternalServerException"


class ResourceNotFoundException(SecurityLakeError):
    """The resource could not be found."""
    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def resource_name(self) -> str | None:
        """The name of the resource that could not be found."""
        return self.response.get("resourceName")

    @property
    def resource_type(self) -> str | None:
        """The type of the resource that could not be found."""
        return self.response.get("resourceType")


class ThrottlingException(SecurityLakeError):
    """The limit on the number of requests per second was exceeded."""
    _ERROR_CODE = "ThrottlingException"

    @property
    def quota_code(self) -> str | None:
        """That the rate of requests to Security Lake is exceeding the request quotas for
        your Amazon Web Services account.
        """
        return self.response.get("quotaCode")

    @property
    def retry_after_seconds(self) -> int | None:
        """Retry the request after the specified time."""
        return self.response.get("retryAfterSeconds")

    @property
    def service_code(self) -> str | None:
        """The code for the service in Service Quotas."""
        return self.response.get("serviceCode")


EXCEPTIONS: dict[str, type[SecurityLakeError]] = {
    "AccessDeniedException": AccessDeniedException,
    "BadRequestException": BadRequestException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ThrottlingException": ThrottlingException,
}
