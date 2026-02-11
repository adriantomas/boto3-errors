# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class KeyspacesStreamsError(Boto3Error):
    _SERVICE = "keyspacesstreams"


class AccessDeniedException(KeyspacesStreamsError):
    """You don't have sufficient access permissions to perform this operation.

    This exception occurs when your IAM user or role lacks the required permissions to
    access the Amazon Keyspaces resource or perform the requested action. Check your IAM
    policies and ensure they grant the necessary permissions.
    """

    _ERROR_CODE = "AccessDeniedException"


class InternalServerException(KeyspacesStreamsError):
    """The Amazon Keyspaces service encountered an unexpected error while processing the
    request.

    This internal server error is not related to your request parameters. Retry your
    request after a brief delay. If the issue persists, contact Amazon Web Services
    Support with details of your request to help identify and resolve the problem.
    """

    _ERROR_CODE = "InternalServerException"


class ResourceNotFoundException(KeyspacesStreamsError):
    """The requested resource doesn't exist or could not be found.

    This exception occurs when you attempt to access a keyspace, table, stream, or other
    Amazon Keyspaces resource that doesn't exist or that has been deleted. Verify that
    the resource identifier is correct and that the resource exists in your account.
    """

    _ERROR_CODE = "ResourceNotFoundException"


class ThrottlingException(KeyspacesStreamsError):
    """The request rate is too high and exceeds the service's throughput limits.

    This exception occurs when you send too many requests in a short period of time.
    Implement exponential backoff in your retry strategy to handle this exception.
    Reducing your request frequency or distributing requests more evenly can help avoid
    throughput exceptions.
    """

    _ERROR_CODE = "ThrottlingException"


class ValidationException(KeyspacesStreamsError):
    """The request validation failed because one or more input parameters failed
    validation.

    This exception occurs when there are syntax errors in the request, field constraints
    are violated, or required parameters are missing. To help you fix the issue, the
    exception message provides details about which parameter failed and why.
    """

    _ERROR_CODE = "ValidationException"

    @property
    def error_code(self) -> str | None:
        """An error occurred validating your request. See the error message for details."""
        return self.response.get("errorCode")


EXCEPTIONS: dict[str, type[KeyspacesStreamsError]] = {
    "AccessDeniedException": AccessDeniedException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
