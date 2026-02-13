# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class ResourceExplorer2Error(Boto3Error):
    _SERVICE = "resource-explorer-2"


class AccessDeniedException(ResourceExplorer2Error):
    """The credentials that you used to call this operation don't have the minimum required
    permissions.
    """

    _ERROR_CODE = "AccessDeniedException"


class ConflictException(ResourceExplorer2Error):
    """If you attempted to create a view, then the request failed because either you
    specified parameters that didn’t match the original request, or you attempted to
    create a view with a name that already exists in this Amazon Web Services Region.

    If you attempted to create an index, then the request failed because either you
    specified parameters that didn't match the original request, or an index already
    exists in the current Amazon Web Services Region.

    If you attempted to update an index type to `AGGREGATOR`, then the request failed
    because you already have an `AGGREGATOR` index in a different Amazon Web Services
    Region.
    """

    _ERROR_CODE = "ConflictException"


class InternalServerException(ResourceExplorer2Error):
    """The request failed because of internal service error. Try your request again later."""
    _ERROR_CODE = "InternalServerException"


class ResourceNotFoundException(ResourceExplorer2Error):
    """You specified a resource that doesn't exist. Check the ID or ARN that you used to
    identity the resource, and try again.
    """

    _ERROR_CODE = "ResourceNotFoundException"


class ServiceQuotaExceededException(ResourceExplorer2Error):
    """The request failed because it exceeds a service quota."""
    _ERROR_CODE = "ServiceQuotaExceededException"

    @property
    def name(self) -> str | None:
        """The name of the service quota that was exceeded by the request."""
        return self.response.get("Name")

    @property
    def value(self) -> str | None:
        """The current value for the quota that the request tried to exceed."""
        return self.response.get("Value")


class ThrottlingException(ResourceExplorer2Error):
    """The request failed because you exceeded a rate limit for this operation. For more
    information, see Quotas for Resource Explorer.
    """

    _ERROR_CODE = "ThrottlingException"


class UnauthorizedException(ResourceExplorer2Error):
    """The principal making the request isn't permitted to perform the operation."""
    _ERROR_CODE = "UnauthorizedException"


class ValidationException(ResourceExplorer2Error):
    """You provided an invalid value for one of the operation's parameters. Check the
    syntax for the operation, and try again.
    """

    _ERROR_CODE = "ValidationException"

    @property
    def field_list(self) -> list[Any] | None:
        """An array of the request fields that had validation errors."""
        return self.response.get("FieldList")


EXCEPTIONS: dict[str, type[ResourceExplorer2Error]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "UnauthorizedException": UnauthorizedException,
    "ValidationException": ValidationException,
}
