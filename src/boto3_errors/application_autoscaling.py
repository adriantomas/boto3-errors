# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class ApplicationAutoScalingError(Boto3Error):
    _SERVICE = "application-autoscaling"


class ConcurrentUpdateException(ApplicationAutoScalingError):
    """Concurrent updates caused an exception, for example, if you request an update to an
    Application Auto Scaling resource that already has a pending update.
    """

    _ERROR_CODE = "ConcurrentUpdateException"


class FailedResourceAccessException(ApplicationAutoScalingError):
    """Failed access to resources caused an exception. This exception is thrown when
    Application Auto Scaling is unable to retrieve the alarms associated with a scaling
    policy due to a client error, for example, if the role ARN specified for a scalable
    target does not have permission to call the CloudWatch DescribeAlarms on your
    behalf.
    """

    _ERROR_CODE = "FailedResourceAccessException"


class InternalServiceException(ApplicationAutoScalingError):
    """The service encountered an internal error."""
    _ERROR_CODE = "InternalServiceException"


class InvalidNextTokenException(ApplicationAutoScalingError):
    """The next token supplied was invalid."""
    _ERROR_CODE = "InvalidNextTokenException"


class LimitExceededException(ApplicationAutoScalingError):
    """A per-account resource limit is exceeded. For more information, see Application Auto
    Scaling service quotas.
    """

    _ERROR_CODE = "LimitExceededException"


class ObjectNotFoundException(ApplicationAutoScalingError):
    """The specified object could not be found. For any operation that depends on the
    existence of a scalable target, this exception is thrown if the scalable target with
    the specified service namespace, resource ID, and scalable dimension does not exist.
    For any operation that deletes or deregisters a resource, this exception is thrown
    if the resource cannot be found.
    """

    _ERROR_CODE = "ObjectNotFoundException"


class ResourceNotFoundException(ApplicationAutoScalingError):
    """The specified resource doesn't exist."""
    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def resource_name(self) -> str | None:
        """The name of the Application Auto Scaling resource. This value is an Amazon
        Resource Name (ARN).
        """
        return self.response.get("ResourceName")


class TooManyTagsException(ApplicationAutoScalingError):
    """The request contains too many tags. Try the request again with fewer tags."""
    _ERROR_CODE = "TooManyTagsException"

    @property
    def resource_name(self) -> str | None:
        """The name of the Application Auto Scaling resource. This value is an Amazon
        Resource Name (ARN).
        """
        return self.response.get("ResourceName")


class ValidationException(ApplicationAutoScalingError):
    """An exception was thrown for a validation issue. Review the available parameters for
    the API request.
    """

    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[ApplicationAutoScalingError]] = {
    "ConcurrentUpdateException": ConcurrentUpdateException,
    "FailedResourceAccessException": FailedResourceAccessException,
    "InternalServiceException": InternalServiceException,
    "InvalidNextTokenException": InvalidNextTokenException,
    "LimitExceededException": LimitExceededException,
    "ObjectNotFoundException": ObjectNotFoundException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "TooManyTagsException": TooManyTagsException,
    "ValidationException": ValidationException,
}
