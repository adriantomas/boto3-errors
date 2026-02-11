# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class AccountError(Boto3Error):
    _SERVICE = "account"


class AccessDeniedException(AccountError):
    """The operation failed because the calling identity doesn't have the minimum required
    permissions.
    """

    _ERROR_CODE = "AccessDeniedException"

    @property
    def error_type(self) -> str | None:
        """The value populated to the `x-amzn-ErrorType` response header by API Gateway."""
        return self.response.get("errorType")


class ConflictException(AccountError):
    """The request could not be processed because of a conflict in the current status of
    the resource. For example, this happens if you try to enable a Region that is
    currently being disabled (in a status of DISABLING) or if you try to change an
    account’s root user email to an email address which is already in use.
    """

    _ERROR_CODE = "ConflictException"

    @property
    def error_type(self) -> str | None:
        """The value populated to the `x-amzn-ErrorType` response header by API Gateway."""
        return self.response.get("errorType")


class InternalServerException(AccountError):
    """The operation failed because of an error internal to Amazon Web Services. Try your
    operation again later.
    """

    _ERROR_CODE = "InternalServerException"

    @property
    def error_type(self) -> str | None:
        """The value populated to the `x-amzn-ErrorType` response header by API Gateway."""
        return self.response.get("errorType")


class ResourceNotFoundException(AccountError):
    """The operation failed because it specified a resource that can't be found."""
    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def error_type(self) -> str | None:
        """The value populated to the `x-amzn-ErrorType` response header by API Gateway."""
        return self.response.get("errorType")


class ResourceUnavailableException(AccountError):
    """The operation failed because it specified a resource that is not currently
    available.
    """

    _ERROR_CODE = "ResourceUnavailableException"

    @property
    def error_type(self) -> str | None:
        """The value populated to the `x-amzn-ErrorType` response header by API Gateway."""
        return self.response.get("errorType")


class TooManyRequestsException(AccountError):
    """The operation failed because it was called too frequently and exceeded a throttle
    limit.
    """

    _ERROR_CODE = "TooManyRequestsException"

    @property
    def error_type(self) -> str | None:
        """The value populated to the `x-amzn-ErrorType` response header by API Gateway."""
        return self.response.get("errorType")


class ValidationException(AccountError):
    """The operation failed because one of the input parameters was invalid."""
    _ERROR_CODE = "ValidationException"

    @property
    def field_list(self) -> list[Any] | None:
        """The field where the invalid entry was detected."""
        return self.response.get("fieldList")

    @property
    def reason(self) -> str | None:
        """The reason that validation failed."""
        return self.response.get("reason")


EXCEPTIONS: dict[str, type[AccountError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ResourceUnavailableException": ResourceUnavailableException,
    "TooManyRequestsException": TooManyRequestsException,
    "ValidationException": ValidationException,
}
