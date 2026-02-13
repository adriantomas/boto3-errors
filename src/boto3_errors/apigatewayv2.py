# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class ApiGatewayV2Error(Boto3Error):
    _SERVICE = "apigatewayv2"


class AccessDeniedException(ApiGatewayV2Error):
    _ERROR_CODE = "AccessDeniedException"


class BadRequestException(ApiGatewayV2Error):
    """The request is not valid, for example, the input is incomplete or incorrect. See the
    accompanying error message for details.
    """

    _ERROR_CODE = "BadRequestException"


class ConflictException(ApiGatewayV2Error):
    """The requested operation would cause a conflict with the current state of a service
    resource associated with the request. Resolve the conflict before retrying this
    request. See the accompanying error message for details.
    """

    _ERROR_CODE = "ConflictException"


class NotFoundException(ApiGatewayV2Error):
    """The resource specified in the request was not found. See the message field for more
    information.
    """

    _ERROR_CODE = "NotFoundException"

    @property
    def resource_type(self) -> str | None:
        """The resource type."""
        return self.response.get("ResourceType")


class TooManyRequestsException(ApiGatewayV2Error):
    """A limit has been exceeded. See the accompanying error message for details."""
    _ERROR_CODE = "TooManyRequestsException"

    @property
    def limit_type(self) -> str | None:
        """The limit type."""
        return self.response.get("LimitType")


EXCEPTIONS: dict[str, type[ApiGatewayV2Error]] = {
    "AccessDeniedException": AccessDeniedException,
    "BadRequestException": BadRequestException,
    "ConflictException": ConflictException,
    "NotFoundException": NotFoundException,
    "TooManyRequestsException": TooManyRequestsException,
}
