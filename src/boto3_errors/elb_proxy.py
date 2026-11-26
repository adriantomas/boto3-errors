# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class ELBProxyError(Boto3Error):
    _SERVICE = "elb-proxy"


class AccessDeniedException(ELBProxyError):
    """The user does not have sufficient access to perform this action."""
    _ERROR_CODE = "AccessDeniedException"


class ConflictException(ELBProxyError):
    """The request conflicts with the current state of the resource."""
    _ERROR_CODE = "ConflictException"


class InternalServerException(ELBProxyError):
    """An unexpected error occurred while processing the request."""
    _ERROR_CODE = "InternalServerException"


class OperationNotPermittedException(ELBProxyError):
    """The requested operation is not permitted."""
    _ERROR_CODE = "OperationNotPermittedException"


class PriorRequestNotCompletedException(ELBProxyError):
    """The request could not be completed because a prior request has not yet completed."""
    _ERROR_CODE = "PriorRequestNotCompletedException"


class ResourceNotFoundException(ELBProxyError):
    """The request references a resource that does not exist."""
    _ERROR_CODE = "ResourceNotFoundException"


class ServiceQuotaExceededException(ELBProxyError):
    """The request would cause a service quota to be exceeded."""
    _ERROR_CODE = "ServiceQuotaExceededException"

    @property
    def quota_code(self) -> str | None:
        """The ID of the service quota that was exceeded."""
        return self.response.get("quotaCode")

    @property
    def resource_id(self) -> str | None:
        """The ID of the resource that caused the service quota to be exceeded."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of the resource that caused the service quota to be exceeded."""
        return self.response.get("resourceType")

    @property
    def service_code(self) -> str | None:
        """The code of the service associated with the exceeded quota."""
        return self.response.get("serviceCode")


class ThrottlingException(ELBProxyError):
    """The limit on the number of requests per second was exceeded."""
    _ERROR_CODE = "ThrottlingException"


class ValidationException(ELBProxyError):
    """The input does not satisfy the constraints specified by an AWS service."""
    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[ELBProxyError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "OperationNotPermittedException": OperationNotPermittedException,
    "PriorRequestNotCompletedException": PriorRequestNotCompletedException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
