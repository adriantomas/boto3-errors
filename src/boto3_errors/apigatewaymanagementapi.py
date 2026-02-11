# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class ApiGatewayManagementApiError(Boto3Error):
    _SERVICE = "apigatewaymanagementapi"


class ForbiddenException(ApiGatewayManagementApiError):
    """The caller is not authorized to invoke this operation."""
    _ERROR_CODE = "ForbiddenException"


class GoneException(ApiGatewayManagementApiError):
    """The connection with the provided id no longer exists."""
    _ERROR_CODE = "GoneException"


class LimitExceededException(ApiGatewayManagementApiError):
    """The client is sending more than the allowed number of requests per unit of time or
    the WebSocket client side buffer is full.
    """

    _ERROR_CODE = "LimitExceededException"


class PayloadTooLargeException(ApiGatewayManagementApiError):
    """The data has exceeded the maximum size allowed."""
    _ERROR_CODE = "PayloadTooLargeException"


EXCEPTIONS: dict[str, type[ApiGatewayManagementApiError]] = {
    "ForbiddenException": ForbiddenException,
    "GoneException": GoneException,
    "LimitExceededException": LimitExceededException,
    "PayloadTooLargeException": PayloadTooLargeException,
}
