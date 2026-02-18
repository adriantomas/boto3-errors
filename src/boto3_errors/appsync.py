# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class AppSyncError(Boto3Error):
    _SERVICE = "appsync"


class AccessDeniedException(AppSyncError):
    """You don't have access to perform this operation on this resource."""
    _ERROR_CODE = "AccessDeniedException"


class ApiKeyLimitExceededException(AppSyncError):
    """The API key exceeded a limit. Try your request again."""
    _ERROR_CODE = "ApiKeyLimitExceededException"


class ApiKeyValidityOutOfBoundsException(AppSyncError):
    """The API key expiration must be set to a value between 1 and 365 days from creation
    (for `CreateApiKey`) or from update (for `UpdateApiKey`).
    """

    _ERROR_CODE = "ApiKeyValidityOutOfBoundsException"


class ApiLimitExceededException(AppSyncError):
    """The GraphQL API exceeded a limit. Try your request again."""
    _ERROR_CODE = "ApiLimitExceededException"


class BadRequestException(AppSyncError):
    """The request is not well formed. For example, a value is invalid or a required field
    is missing. Check the field values, and then try again.
    """

    _ERROR_CODE = "BadRequestException"

    @property
    def detail(self) -> dict[str, Any] | None:
        return self.response.get("detail")

    @property
    def reason(self) -> str | None:
        return self.response.get("reason")


class ConcurrentModificationException(AppSyncError):
    """Another modification is in progress at this time and it must complete before you can
    make your change.
    """

    _ERROR_CODE = "ConcurrentModificationException"


class ConflictException(AppSyncError):
    """A conflict with a previous successful update is detected. This typically occurs when
    the previous update did not have time to propagate before the next update was made.
    A retry (with appropriate backoff logic) is the recommended response to this
    exception.
    """

    _ERROR_CODE = "ConflictException"


class GraphQLSchemaException(AppSyncError):
    """The GraphQL schema is not valid."""
    _ERROR_CODE = "GraphQLSchemaException"


class InternalFailureException(AppSyncError):
    """An internal AppSync error occurred. Try your request again."""
    _ERROR_CODE = "InternalFailureException"


class LimitExceededException(AppSyncError):
    """The request exceeded a limit. Try your request again."""
    _ERROR_CODE = "LimitExceededException"


class NotFoundException(AppSyncError):
    """The resource specified in the request was not found. Check the resource, and then
    try again.
    """

    _ERROR_CODE = "NotFoundException"


class ServiceQuotaExceededException(AppSyncError):
    """The operation exceeded the service quota for this resource."""
    _ERROR_CODE = "ServiceQuotaExceededException"


class UnauthorizedException(AppSyncError):
    """You aren't authorized to perform this operation."""
    _ERROR_CODE = "UnauthorizedException"


EXCEPTIONS: dict[str, type[AppSyncError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ApiKeyLimitExceededException": ApiKeyLimitExceededException,
    "ApiKeyValidityOutOfBoundsException": ApiKeyValidityOutOfBoundsException,
    "ApiLimitExceededException": ApiLimitExceededException,
    "BadRequestException": BadRequestException,
    "ConcurrentModificationException": ConcurrentModificationException,
    "ConflictException": ConflictException,
    "GraphQLSchemaException": GraphQLSchemaException,
    "InternalFailureException": InternalFailureException,
    "LimitExceededException": LimitExceededException,
    "NotFoundException": NotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "UnauthorizedException": UnauthorizedException,
}
