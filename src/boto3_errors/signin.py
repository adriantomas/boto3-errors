# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class SigninError(Boto3Error):
    _SERVICE = "signin"


class AccessDeniedException(SigninError):
    """Error thrown for access denied scenarios with flexible HTTP status mapping

    Runtime HTTP Status Code Mapping:

    - HTTP 401 (Unauthorized): TOKEN_EXPIRED, AUTHCODE_EXPIRED
    - HTTP 403 (Forbidden): USER_CREDENTIALS_CHANGED, INSUFFICIENT_PERMISSIONS

    The specific HTTP status code is determined at runtime based on the error enum
    value. Consumers should use the error field to determine the specific access denial
    reason.
    """

    _ERROR_CODE = "AccessDeniedException"

    @property
    def error(self) -> str | None:
        """OAuth 2.0 error code indicating the specific type of access denial Can be
        TOKEN_EXPIRED, AUTHCODE_EXPIRED, USER_CREDENTIALS_CHANGED, or
        INSUFFICIENT_PERMISSIONS
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
    """Error thrown when an internal server error occurs

    HTTP Status Code: 500 Internal Server Error

    Used for unexpected server-side errors that prevent request processing.
    """

    _ERROR_CODE = "InternalServerException"

    @property
    def error(self) -> str | None:
        """OAuth 2.0 error code indicating server error Will be SERVER_ERROR for internal
        server errors
        """
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


class TooManyRequestsError(SigninError):
    """Error thrown when rate limit is exceeded

    HTTP Status Code: 429 Too Many Requests

    Possible OAuth2ErrorCode values:

    - INVALID_REQUEST: Rate limiting, too many requests, abuse prevention

    Possible causes:

    - Too many token requests from the same client
    - Rate limiting based on client_id or IP address
    - Abuse prevention mechanisms triggered
    - Service protection against excessive token generation
    """

    _ERROR_CODE = "TooManyRequestsError"

    @property
    def error(self) -> str | None:
        """OAuth 2.0 error code indicating the specific type of error Will be
        INVALID_REQUEST for rate limiting scenarios
        """
        return self.response.get("error")


class ValidationException(SigninError):
    """Error thrown when request validation fails

    HTTP Status Code: 400 Bad Request

    Used for request validation errors such as malformed parameters, missing required
    fields, or invalid parameter values.
    """

    _ERROR_CODE = "ValidationException"

    @property
    def error(self) -> str | None:
        """OAuth 2.0 error code indicating validation failure Will be INVALID_REQUEST for
        validation errors
        """
        return self.response.get("error")


EXCEPTIONS: dict[str, type[SigninError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "TooManyRequestsError": TooManyRequestsError,
    "ValidationException": ValidationException,
}
