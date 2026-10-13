# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class LambdaWebError(Boto3Error):
    _SERVICE = "lambda-web"


class AccessDeniedException(LambdaWebError):
    """You don't have permission to perform this operation. Check the IAM policies for your
    identity and any resource-based policy on the web function.
    """

    _ERROR_CODE = "AccessDeniedException"


class ConflictException(LambdaWebError):
    """The request conflicts with the current state of the resource. For example, the
    resource is being modified by another request, you tried to delete a revision that
    is serving traffic on an endpoint, or the policy revision ID that you specified
    doesn't match the current policy. Resolve the conflict and try again.
    """

    _ERROR_CODE = "ConflictException"

    @property
    def resource_id(self) -> str | None:
        """The identifier of the resource in conflict."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of the resource in conflict."""
        return self.response.get("resourceType")


class InternalServerException(LambdaWebError):
    """The request failed because of an internal error in the service. Retry the request.
    If the error persists, open a support case.
    """

    _ERROR_CODE = "InternalServerException"


class ResourceNotFoundException(LambdaWebError):
    """The specified web function, revision, endpoint, or resource-based policy doesn't
    exist. Verify the resource identifier and try again.
    """

    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def resource_id(self) -> str | None:
        """The identifier of the resource that was not found."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of the resource that was not found."""
        return self.response.get("resourceType")


class ServiceQuotaExceededException(LambdaWebError):
    """The request would exceed a service quota, such as the maximum number of web
    functions in your account or the maximum number of revisions or endpoints per web
    function. Request a quota increase or reduce usage and try again.
    """

    _ERROR_CODE = "ServiceQuotaExceededException"

    @property
    def quota_code(self) -> str | None:
        """The quota code of the exceeded quota."""
        return self.response.get("quotaCode")

    @property
    def resource_id(self) -> str | None:
        """The identifier of the resource that exceeded the quota."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of resource that exceeded the quota."""
        return self.response.get("resourceType")

    @property
    def service_code(self) -> str | None:
        """The service code of the service that owns the quota."""
        return self.response.get("serviceCode")


class ThrottlingException(LambdaWebError):
    """The request was denied because it exceeded the request rate that Lambda allows for
    your account. Reduce the frequency of requests and retry with exponential backoff.
    """

    _ERROR_CODE = "ThrottlingException"

    @property
    def quota_code(self) -> str | None:
        """The quota code that was exceeded, if applicable."""
        return self.response.get("quotaCode")

    @property
    def retry_after_seconds(self) -> int | None:
        """The number of seconds to wait before retrying the request."""
        return self.response.get("retryAfterSeconds")

    @property
    def service_code(self) -> str | None:
        """The service code of the throttled service."""
        return self.response.get("serviceCode")


class ValidationException(LambdaWebError):
    """The request failed validation because a parameter was missing, malformed, or outside
    the allowed range. Check the request parameters and try again.
    """

    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[LambdaWebError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
