# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class SSOOIDCError(Boto3Error):
    _SERVICE = "sso-oidc"


class AccessDeniedException(SSOOIDCError):
    """You do not have sufficient access to perform this action."""
    _ERROR_CODE = "AccessDeniedException"

    @property
    def error(self) -> str | None:
        """Single error code. For this exception the value will be `access_denied`."""
        return self.response.get("error")

    @property
    def error_description(self) -> str | None:
        """Human-readable text providing additional information, used to assist the client
        developer in understanding the error that occurred.
        """
        return self.response.get("error_description")


class AuthorizationPendingException(SSOOIDCError):
    """Indicates that a request to authorize a client with an access user session token is
    pending.
    """

    _ERROR_CODE = "AuthorizationPendingException"

    @property
    def error(self) -> str | None:
        """Single error code. For this exception the value will be `authorization_pending`."""
        return self.response.get("error")

    @property
    def error_description(self) -> str | None:
        """Human-readable text providing additional information, used to assist the client
        developer in understanding the error that occurred.
        """
        return self.response.get("error_description")


class ExpiredTokenException(SSOOIDCError):
    """Indicates that the token issued by the service is expired and is no longer valid."""
    _ERROR_CODE = "ExpiredTokenException"

    @property
    def error(self) -> str | None:
        """Single error code. For this exception the value will be `expired_token`."""
        return self.response.get("error")

    @property
    def error_description(self) -> str | None:
        """Human-readable text providing additional information, used to assist the client
        developer in understanding the error that occurred.
        """
        return self.response.get("error_description")


class InternalServerException(SSOOIDCError):
    """Indicates that an error from the service occurred while trying to process a request."""
    _ERROR_CODE = "InternalServerException"

    @property
    def error(self) -> str | None:
        """Single error code. For this exception the value will be `server_error`."""
        return self.response.get("error")

    @property
    def error_description(self) -> str | None:
        """Human-readable text providing additional information, used to assist the client
        developer in understanding the error that occurred.
        """
        return self.response.get("error_description")


class InvalidClientException(SSOOIDCError):
    """Indicates that the `clientId` or `clientSecret` in the request is invalid. For
    example, this can occur when a client sends an incorrect `clientId` or an expired
    `clientSecret`.
    """

    _ERROR_CODE = "InvalidClientException"

    @property
    def error(self) -> str | None:
        """Single error code. For this exception the value will be `invalid_client`."""
        return self.response.get("error")

    @property
    def error_description(self) -> str | None:
        """Human-readable text providing additional information, used to assist the client
        developer in understanding the error that occurred.
        """
        return self.response.get("error_description")


class InvalidClientMetadataException(SSOOIDCError):
    """Indicates that the client information sent in the request during registration is
    invalid.
    """

    _ERROR_CODE = "InvalidClientMetadataException"

    @property
    def error(self) -> str | None:
        """Single error code. For this exception the value will be
        `invalid_client_metadata`.
        """
        return self.response.get("error")

    @property
    def error_description(self) -> str | None:
        """Human-readable text providing additional information, used to assist the client
        developer in understanding the error that occurred.
        """
        return self.response.get("error_description")


class InvalidGrantException(SSOOIDCError):
    """Indicates that a request contains an invalid grant. This can occur if a client makes
    a CreateToken request with an invalid grant type.
    """

    _ERROR_CODE = "InvalidGrantException"

    @property
    def error(self) -> str | None:
        """Single error code. For this exception the value will be `invalid_grant`."""
        return self.response.get("error")

    @property
    def error_description(self) -> str | None:
        """Human-readable text providing additional information, used to assist the client
        developer in understanding the error that occurred.
        """
        return self.response.get("error_description")


class InvalidRequestException(SSOOIDCError):
    """Indicates that something is wrong with the input to the request. For example, a
    required parameter might be missing or out of range.
    """

    _ERROR_CODE = "InvalidRequestException"

    @property
    def error(self) -> str | None:
        """Single error code. For this exception the value will be `invalid_request`."""
        return self.response.get("error")

    @property
    def error_description(self) -> str | None:
        """Human-readable text providing additional information, used to assist the client
        developer in understanding the error that occurred.
        """
        return self.response.get("error_description")


class InvalidRequestRegionException(SSOOIDCError):
    """Indicates that a token provided as input to the request was issued by and is only
    usable by calling IAM Identity Center endpoints in another region.
    """

    _ERROR_CODE = "InvalidRequestRegionException"

    @property
    def endpoint(self) -> str | None:
        """Indicates the IAM Identity Center endpoint which the requester may call with
        this token.
        """
        return self.response.get("endpoint")

    @property
    def error(self) -> str | None:
        """Single error code. For this exception the value will be `invalid_request`."""
        return self.response.get("error")

    @property
    def error_description(self) -> str | None:
        """Human-readable text providing additional information, used to assist the client
        developer in understanding the error that occurred.
        """
        return self.response.get("error_description")

    @property
    def region(self) -> str | None:
        """Indicates the region which the requester may call with this token."""
        return self.response.get("region")


class InvalidScopeException(SSOOIDCError):
    """Indicates that the scope provided in the request is invalid."""
    _ERROR_CODE = "InvalidScopeException"

    @property
    def error(self) -> str | None:
        """Single error code. For this exception the value will be `invalid_scope`."""
        return self.response.get("error")

    @property
    def error_description(self) -> str | None:
        """Human-readable text providing additional information, used to assist the client
        developer in understanding the error that occurred.
        """
        return self.response.get("error_description")


class SlowDownException(SSOOIDCError):
    """Indicates that the client is making the request too frequently and is more than the
    service can handle.
    """

    _ERROR_CODE = "SlowDownException"

    @property
    def error(self) -> str | None:
        """Single error code. For this exception the value will be `slow_down`."""
        return self.response.get("error")

    @property
    def error_description(self) -> str | None:
        """Human-readable text providing additional information, used to assist the client
        developer in understanding the error that occurred.
        """
        return self.response.get("error_description")


class UnauthorizedClientException(SSOOIDCError):
    """Indicates that the client is not currently authorized to make the request. This can
    happen when a `clientId` is not issued for a public client.
    """

    _ERROR_CODE = "UnauthorizedClientException"

    @property
    def error(self) -> str | None:
        """Single error code. For this exception the value will be `unauthorized_client`."""
        return self.response.get("error")

    @property
    def error_description(self) -> str | None:
        """Human-readable text providing additional information, used to assist the client
        developer in understanding the error that occurred.
        """
        return self.response.get("error_description")


class UnsupportedGrantTypeException(SSOOIDCError):
    """Indicates that the grant type in the request is not supported by the service."""
    _ERROR_CODE = "UnsupportedGrantTypeException"

    @property
    def error(self) -> str | None:
        """Single error code. For this exception the value will be
        `unsupported_grant_type`.
        """
        return self.response.get("error")

    @property
    def error_description(self) -> str | None:
        """Human-readable text providing additional information, used to assist the client
        developer in understanding the error that occurred.
        """
        return self.response.get("error_description")


EXCEPTIONS: dict[str, type[SSOOIDCError]] = {
    "AccessDeniedException": AccessDeniedException,
    "AuthorizationPendingException": AuthorizationPendingException,
    "ExpiredTokenException": ExpiredTokenException,
    "InternalServerException": InternalServerException,
    "InvalidClientException": InvalidClientException,
    "InvalidClientMetadataException": InvalidClientMetadataException,
    "InvalidGrantException": InvalidGrantException,
    "InvalidRequestException": InvalidRequestException,
    "InvalidRequestRegionException": InvalidRequestRegionException,
    "InvalidScopeException": InvalidScopeException,
    "SlowDownException": SlowDownException,
    "UnauthorizedClientException": UnauthorizedClientException,
    "UnsupportedGrantTypeException": UnsupportedGrantTypeException,
}
