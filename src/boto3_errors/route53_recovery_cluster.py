# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class Route53RecoveryClusterError(Boto3Error):
    _SERVICE = "route53-recovery-cluster"


class AccessDeniedException(Route53RecoveryClusterError):
    """You don't have sufficient permissions to perform this action."""
    _ERROR_CODE = "AccessDeniedException"


class ConflictException(Route53RecoveryClusterError):
    """There was a conflict with this request. Try again."""
    _ERROR_CODE = "ConflictException"

    @property
    def resource_id(self) -> str | None:
        """Identifier of the resource in use"""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """Type of the resource in use"""
        return self.response.get("resourceType")


class EndpointTemporarilyUnavailableException(Route53RecoveryClusterError):
    """The cluster endpoint isn't available. Try another cluster endpoint."""
    _ERROR_CODE = "EndpointTemporarilyUnavailableException"


class InternalServerException(Route53RecoveryClusterError):
    """There was an unexpected error during processing of the request."""
    _ERROR_CODE = "InternalServerException"

    @property
    def retry_after_seconds(self) -> int | None:
        return self.response.get("retryAfterSeconds")


class ResourceNotFoundException(Route53RecoveryClusterError):
    """The request references a routing control or control panel that was not found."""
    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def resource_id(self) -> str | None:
        """Hypothetical resource identifier that was not found"""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """Hypothetical resource type that was not found"""
        return self.response.get("resourceType")


class ServiceLimitExceededException(Route53RecoveryClusterError):
    """The request can't update that many routing control states at the same time. Try
    again with fewer routing control states.
    """

    _ERROR_CODE = "ServiceLimitExceededException"

    @property
    def limit_code(self) -> str | None:
        """The code of the limit that was exceeded."""
        return self.response.get("limitCode")

    @property
    def resource_id(self) -> str | None:
        """The resource identifier of the limit that was exceeded."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """The resource type of the limit that was exceeded."""
        return self.response.get("resourceType")

    @property
    def service_code(self) -> str | None:
        """The service code of the limit that was exceeded."""
        return self.response.get("serviceCode")


class ThrottlingException(Route53RecoveryClusterError):
    """The request was denied because of request throttling."""
    _ERROR_CODE = "ThrottlingException"

    @property
    def retry_after_seconds(self) -> int | None:
        return self.response.get("retryAfterSeconds")


class ValidationException(Route53RecoveryClusterError):
    """There was a validation error on the request."""
    _ERROR_CODE = "ValidationException"

    @property
    def fields(self) -> list[Any] | None:
        return self.response.get("fields")

    @property
    def reason(self) -> str | None:
        return self.response.get("reason")


EXCEPTIONS: dict[str, type[Route53RecoveryClusterError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "EndpointTemporarilyUnavailableException": EndpointTemporarilyUnavailableException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceLimitExceededException": ServiceLimitExceededException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
