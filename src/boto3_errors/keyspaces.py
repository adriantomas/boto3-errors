# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class KeyspacesError(Boto3Error):
    _SERVICE = "keyspaces"


class AccessDeniedException(KeyspacesError):
    """You don't have sufficient access permissions to perform this action."""
    _ERROR_CODE = "AccessDeniedException"


class ConflictException(KeyspacesError):
    """Amazon Keyspaces couldn't complete the requested action. This error may occur if you
    try to perform an action and the same or a different action is already in progress,
    or if you try to create a resource that already exists.
    """

    _ERROR_CODE = "ConflictException"


class InternalServerException(KeyspacesError):
    """Amazon Keyspaces was unable to fully process this request because of an internal
    server error.
    """

    _ERROR_CODE = "InternalServerException"


class ResourceNotFoundException(KeyspacesError):
    """The operation tried to access a keyspace, table, or type that doesn't exist. The
    resource might not be specified correctly, or its status might not be `ACTIVE`.
    """

    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def resource_arn(self) -> str | None:
        """The unique identifier in the format of Amazon Resource Name (ARN) for the
        resource couldn't be found.
        """
        return self.response.get("resourceArn")


class ServiceQuotaExceededException(KeyspacesError):
    """The operation exceeded the service quota for this resource. For more information on
    service quotas, see Quotas in the Amazon Keyspaces Developer Guide.
    """

    _ERROR_CODE = "ServiceQuotaExceededException"


class ValidationException(KeyspacesError):
    """The operation failed due to an invalid or malformed request."""
    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[KeyspacesError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ValidationException": ValidationException,
}
