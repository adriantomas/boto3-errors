# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class ShieldError(Boto3Error):
    _SERVICE = "shield"


class AccessDeniedException(ShieldError):
    """Exception that indicates the specified `AttackId` does not exist, or the requester
    does not have the appropriate permissions to access the `AttackId`.
    """

    _ERROR_CODE = "AccessDeniedException"


class AccessDeniedForDependencyException(ShieldError):
    """In order to grant the necessary access to the Shield Response Team (SRT) the user
    submitting the request must have the `iam:PassRole` permission. This error indicates
    the user did not have the appropriate permissions. For more information, see
    Granting a User Permissions to Pass a Role to an Amazon Web Services Service.
    """

    _ERROR_CODE = "AccessDeniedForDependencyException"


class InternalErrorException(ShieldError):
    """Exception that indicates that a problem occurred with the service infrastructure.
    You can retry the request.
    """

    _ERROR_CODE = "InternalErrorException"


class InvalidOperationException(ShieldError):
    """Exception that indicates that the operation would not cause any change to occur."""
    _ERROR_CODE = "InvalidOperationException"


class InvalidPaginationTokenException(ShieldError):
    """Exception that indicates that the `NextToken` specified in the request is invalid.
    Submit the request using the `NextToken` value that was returned in the prior
    response.
    """

    _ERROR_CODE = "InvalidPaginationTokenException"


class InvalidParameterException(ShieldError):
    """Exception that indicates that the parameters passed to the API are invalid. If
    available, this exception includes details in additional properties.
    """

    _ERROR_CODE = "InvalidParameterException"

    @property
    def reason(self) -> str | None:
        """Additional information about the exception."""
        return self.response.get("reason")

    @property
    def fields(self) -> list[Any] | None:
        """Fields that caused the exception."""
        return self.response.get("fields")


class InvalidResourceException(ShieldError):
    """Exception that indicates that the resource is invalid. You might not have access to
    the resource, or the resource might not exist.
    """

    _ERROR_CODE = "InvalidResourceException"


class LimitsExceededException(ShieldError):
    """Exception that indicates that the operation would exceed a limit."""
    _ERROR_CODE = "LimitsExceededException"

    @property
    def type(self) -> str | None:
        """The type of limit that would be exceeded."""
        return self.response.get("Type")

    @property
    def limit(self) -> int | None:
        """The threshold that would be exceeded."""
        return self.response.get("Limit")


class LockedSubscriptionException(ShieldError):
    """You are trying to update a subscription that has not yet completed the 1-year
    commitment. You can change the `AutoRenew` parameter during the last 30 days of your
    subscription. This exception indicates that you are attempting to change `AutoRenew`
    prior to that period.
    """

    _ERROR_CODE = "LockedSubscriptionException"


class NoAssociatedRoleException(ShieldError):
    """The ARN of the role that you specified does not exist."""
    _ERROR_CODE = "NoAssociatedRoleException"


class OptimisticLockException(ShieldError):
    """Exception that indicates that the resource state has been modified by another
    client. Retrieve the resource and then retry your request.
    """

    _ERROR_CODE = "OptimisticLockException"


class ResourceAlreadyExistsException(ShieldError):
    """Exception indicating the specified resource already exists. If available, this
    exception includes details in additional properties.
    """

    _ERROR_CODE = "ResourceAlreadyExistsException"

    @property
    def resource_type(self) -> str | None:
        """The type of resource that already exists."""
        return self.response.get("resourceType")


class ResourceNotFoundException(ShieldError):
    """Exception indicating the specified resource does not exist. If available, this
    exception includes details in additional properties.
    """

    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def resource_type(self) -> str | None:
        """Type of resource."""
        return self.response.get("resourceType")


EXCEPTIONS: dict[str, type[ShieldError]] = {
    "AccessDeniedException": AccessDeniedException,
    "AccessDeniedForDependencyException": AccessDeniedForDependencyException,
    "InternalErrorException": InternalErrorException,
    "InvalidOperationException": InvalidOperationException,
    "InvalidPaginationTokenException": InvalidPaginationTokenException,
    "InvalidParameterException": InvalidParameterException,
    "InvalidResourceException": InvalidResourceException,
    "LimitsExceededException": LimitsExceededException,
    "LockedSubscriptionException": LockedSubscriptionException,
    "NoAssociatedRoleException": NoAssociatedRoleException,
    "OptimisticLockException": OptimisticLockException,
    "ResourceAlreadyExistsException": ResourceAlreadyExistsException,
    "ResourceNotFoundException": ResourceNotFoundException,
}
