# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class LambdaMicrovmsError(Boto3Error):
    _SERVICE = "lambda-microvms"


class AccessDeniedException(LambdaMicrovmsError):
    """You do not have sufficient access to perform this action."""
    _ERROR_CODE = "AccessDeniedException"


class ConflictException(LambdaMicrovmsError):
    """The request could not be completed due to a conflict with the current state of the
    resource.
    """

    _ERROR_CODE = "ConflictException"

    @property
    def resource_id(self) -> str | None:
        """The identifier of the resource that caused the conflict."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of the resource that caused the conflict."""
        return self.response.get("resourceType")


class InternalServerException(LambdaMicrovmsError):
    """An internal server error occurred. Retry the request later."""
    _ERROR_CODE = "InternalServerException"

    @property
    def retry_after_seconds(self) -> int | None:
        """The number of seconds to wait before retrying the request."""
        return self.response.get("retryAfterSeconds")


class InvalidParameterValueException(LambdaMicrovmsError):
    """One of the parameters in the request is not valid."""
    _ERROR_CODE = "InvalidParameterValueException"

    @property
    def type(self) -> str | None:
        """The exception type."""
        return self.response.get("Type")


class ResourceConflictException(LambdaMicrovmsError):
    """The resource already exists, or another operation is in progress."""
    _ERROR_CODE = "ResourceConflictException"

    @property
    def type(self) -> str | None:
        """The exception type."""
        return self.response.get("Type")


class ResourceNotFoundException(LambdaMicrovmsError):
    """The specified resource does not exist."""
    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def resource_id(self) -> str | None:
        """The identifier of the resource that was not found."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of the resource that was not found."""
        return self.response.get("resourceType")


class ServiceException(LambdaMicrovmsError):
    """The AWS Lambda MicroVMs service encountered an internal error."""
    _ERROR_CODE = "ServiceException"

    @property
    def type(self) -> str | None:
        """The exception type."""
        return self.response.get("Type")


class ServiceQuotaExceededException(LambdaMicrovmsError):
    """You have exceeded a service quota for Lambda MicroVMs."""
    _ERROR_CODE = "ServiceQuotaExceededException"

    @property
    def quota_code(self) -> str | None:
        """The quota code of the exceeded service quota."""
        return self.response.get("quotaCode")

    @property
    def resource_id(self) -> str | None:
        """The identifier of the resource that exceeded the quota."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of the resource that exceeded the quota."""
        return self.response.get("resourceType")

    @property
    def service_code(self) -> str | None:
        """The service code of the exceeded service quota."""
        return self.response.get("serviceCode")


class ThrottlingException(LambdaMicrovmsError):
    """The request was denied due to request throttling. Retry the request later."""
    _ERROR_CODE = "ThrottlingException"

    @property
    def quota_code(self) -> str | None:
        """The quota code of the throttled service quota."""
        return self.response.get("quotaCode")

    @property
    def retry_after_seconds(self) -> int | None:
        """The number of seconds to wait before retrying the request."""
        return self.response.get("retryAfterSeconds")

    @property
    def service_code(self) -> str | None:
        """The service code of the throttled service quota."""
        return self.response.get("serviceCode")


class TooManyRequestsException(LambdaMicrovmsError):
    """The request throughput limit was exceeded. Retry the request later."""
    _ERROR_CODE = "TooManyRequestsException"

    @property
    def type(self) -> str | None:
        """The exception type."""
        return self.response.get("Type")


class ValidationException(LambdaMicrovmsError):
    """The input does not satisfy the constraints specified by the service."""
    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[LambdaMicrovmsError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "InvalidParameterValueException": InvalidParameterValueException,
    "ResourceConflictException": ResourceConflictException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceException": ServiceException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "TooManyRequestsException": TooManyRequestsException,
    "ValidationException": ValidationException,
}
