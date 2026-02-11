# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class DeviceFarmError(Boto3Error):
    _SERVICE = "devicefarm"


class ArgumentException(DeviceFarmError):
    """An invalid argument was specified."""
    _ERROR_CODE = "ArgumentException"


class CannotDeleteException(DeviceFarmError):
    """The requested object could not be deleted."""
    _ERROR_CODE = "CannotDeleteException"


class IdempotencyException(DeviceFarmError):
    """An entity with the same name already exists."""
    _ERROR_CODE = "IdempotencyException"


class InternalServiceException(DeviceFarmError):
    """An internal exception was raised in the service. Contact aws-devicefarm-
    support@amazon.com if you see this error.
    """

    _ERROR_CODE = "InternalServiceException"


class InvalidOperationException(DeviceFarmError):
    """There was an error with the update request, or you do not have sufficient
    permissions to update this VPC endpoint configuration.
    """

    _ERROR_CODE = "InvalidOperationException"


class LimitExceededException(DeviceFarmError):
    """A limit was exceeded."""
    _ERROR_CODE = "LimitExceededException"


class NotEligibleException(DeviceFarmError):
    """Exception gets thrown when a user is not eligible to perform the specified
    transaction.
    """

    _ERROR_CODE = "NotEligibleException"


class NotFoundException(DeviceFarmError):
    """The specified entity was not found."""
    _ERROR_CODE = "NotFoundException"


class ServiceAccountException(DeviceFarmError):
    """There was a problem with the service account."""
    _ERROR_CODE = "ServiceAccountException"


class TagOperationException(DeviceFarmError):
    """The operation was not successful. Try again."""
    _ERROR_CODE = "TagOperationException"

    @property
    def resource_name(self) -> str | None:
        return self.response.get("resourceName")


class TagPolicyException(DeviceFarmError):
    """The request doesn't comply with the AWS Identity and Access Management (IAM) tag
    policy. Correct your request and then retry it.
    """

    _ERROR_CODE = "TagPolicyException"

    @property
    def resource_name(self) -> str | None:
        return self.response.get("resourceName")


class TooManyTagsException(DeviceFarmError):
    """The list of tags on the repository is over the limit. The maximum number of tags
    that can be applied to a repository is 50.
    """

    _ERROR_CODE = "TooManyTagsException"

    @property
    def resource_name(self) -> str | None:
        return self.response.get("resourceName")


EXCEPTIONS: dict[str, type[DeviceFarmError]] = {
    "ArgumentException": ArgumentException,
    "CannotDeleteException": CannotDeleteException,
    "IdempotencyException": IdempotencyException,
    "InternalServiceException": InternalServiceException,
    "InvalidOperationException": InvalidOperationException,
    "LimitExceededException": LimitExceededException,
    "NotEligibleException": NotEligibleException,
    "NotFoundException": NotFoundException,
    "ServiceAccountException": ServiceAccountException,
    "TagOperationException": TagOperationException,
    "TagPolicyException": TagPolicyException,
    "TooManyTagsException": TooManyTagsException,
}
