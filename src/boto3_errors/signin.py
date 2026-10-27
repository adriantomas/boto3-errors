# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class SigninError(Boto3Error):
    _SERVICE = "signin"


class AccessDeniedException(SigninError):
    """You do not have sufficient access to perform this action."""
    _ERROR_CODE = "AccessDeniedException"

    @property
    def error(self) -> str | None:
        """One of TOKEN_EXPIRED, AUTHCODE_EXPIRED, USER_CREDENTIALS_CHANGED, or
        INSUFFICIENT_PERMISSIONS.
        """
        return self.response.get("error")


class ConflictException(SigninError):
    """Error thrown when request conflicts with current state

    HTTP Status Code: 409 Conflict

    Used when the request conflicts with the current state of the resource
    """

    _ERROR_CODE = "ConflictException"

    @property
    def error(self) -> str | None:
        """OAuth 2.0 error code indicating conflict Will be CONFLICT"""
        return self.response.get("error")


class InternalServerException(SigninError):
    """The request failed because of an internal server error."""
    _ERROR_CODE = "InternalServerException"

    @property
    def error(self) -> str | None:
        """Will be server_error."""
        return self.response.get("error")


class InvalidGrantException(SigninError):
    """The request failed because the provided grant is invalid or expired."""
    _ERROR_CODE = "InvalidGrantException"

    @property
    def error(self) -> str | None:
        """Will be invalid_grant."""
        return self.response.get("error")


class InvalidScopeException(SigninError):
    """The request failed because the requested scope is invalid or exceeds the scope that
    can be granted.
    """

    _ERROR_CODE = "InvalidScopeException"

    @property
    def error(self) -> str | None:
        """Will be invalid_scope."""
        return self.response.get("error")


class ResourceNotFoundException(SigninError):
    """Error thrown when requested resource is not found

    HTTP Status Code: 404 Not Found

    Used when the specified resource does not exist
    """

    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def error(self) -> str | None:
        """OAuth 2.0 error code indicating resource not found Will be RESOURCE_NOT_FOUND"""
        return self.response.get("error")


class ServiceQuotaExceededException(SigninError):
    """Error thrown when service quota is exceeded

    HTTP Status Code: 402 Payment Required (used as quota exceeded indicator)

    Used when the request would cause a service quota to be exceeded
    """

    _ERROR_CODE = "ServiceQuotaExceededException"

    @property
    def error(self) -> str | None:
        """OAuth 2.0 error code indicating service quota exceeded Will be
        SERVICE_QUOTA_EXCEEDED
        """
        return self.response.get("error")


class ServiceUnavailableException(SigninError):
    """The request failed because a dependency is temporarily unavailable. You can retry
    the request.
    """

    _ERROR_CODE = "ServiceUnavailableException"

    @property
    def error(self) -> str | None:
        """Will be service_unavailable."""
        return self.response.get("error")


class TooManyRequestsError(SigninError):
    """The request failed because you exceeded the request rate limit for this operation."""
    _ERROR_CODE = "TooManyRequestsError"

    @property
    def error(self) -> str | None:
        """Will be rate_exceeded."""
        return self.response.get("error")


class ValidationException(SigninError):
    """The request failed because it contains a malformed, missing, or invalid parameter."""
    _ERROR_CODE = "ValidationException"

    @property
    def error(self) -> str | None:
        """The specific code depends on which validation failed."""
        return self.response.get("error")


EXCEPTIONS: dict[str, type[SigninError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "InvalidGrantException": InvalidGrantException,
    "InvalidScopeException": InvalidScopeException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ServiceUnavailableException": ServiceUnavailableException,
    "TooManyRequestsError": TooManyRequestsError,
    "ValidationException": ValidationException,
}
