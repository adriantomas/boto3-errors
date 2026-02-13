# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class APIGatewayError(Boto3Error):
    _SERVICE = "apigateway"


class BadRequestException(APIGatewayError):
    """The submitted request is not valid, for example, the input is incomplete or
    incorrect. See the accompanying error message for details.
    """

    _ERROR_CODE = "BadRequestException"


class ConflictException(APIGatewayError):
    """The request configuration has conflicts. For details, see the accompanying error
    message.
    """

    _ERROR_CODE = "ConflictException"


class LimitExceededException(APIGatewayError):
    """The request exceeded the rate limit. Retry after the specified time period."""
    _ERROR_CODE = "LimitExceededException"

    @property
    def retry_after_seconds(self) -> str | None:
        return self.response.get("retryAfterSeconds")


class NotFoundException(APIGatewayError):
    """The requested resource is not found. Make sure that the request URI is correct."""
    _ERROR_CODE = "NotFoundException"


class ServiceUnavailableException(APIGatewayError):
    """The requested service is not available. For details see the accompanying error
    message. Retry after the specified time period.
    """

    _ERROR_CODE = "ServiceUnavailableException"

    @property
    def retry_after_seconds(self) -> str | None:
        return self.response.get("retryAfterSeconds")


class TooManyRequestsException(APIGatewayError):
    """The request has reached its throttling limit. Retry after the specified time period."""
    _ERROR_CODE = "TooManyRequestsException"

    @property
    def retry_after_seconds(self) -> str | None:
        return self.response.get("retryAfterSeconds")


class UnauthorizedException(APIGatewayError):
    """The request is denied because the caller has insufficient permissions."""
    _ERROR_CODE = "UnauthorizedException"


EXCEPTIONS: dict[str, type[APIGatewayError]] = {
    "BadRequestException": BadRequestException,
    "ConflictException": ConflictException,
    "LimitExceededException": LimitExceededException,
    "NotFoundException": NotFoundException,
    "ServiceUnavailableException": ServiceUnavailableException,
    "TooManyRequestsException": TooManyRequestsException,
    "UnauthorizedException": UnauthorizedException,
}
