# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class StorageGatewayError(Boto3Error):
    _SERVICE = "storagegateway"


class InternalServerError(StorageGatewayError):
    """An internal server error has occurred during the request. For more information, see
    the error and message fields.
    """

    _ERROR_CODE = "InternalServerError"

    @property
    def error(self) -> dict[str, Any] | None:
        """A StorageGatewayError that provides more information about the cause of the
        error.
        """
        return self.response.get("error")


class InvalidGatewayRequestException(StorageGatewayError):
    """An exception occurred because an invalid gateway request was issued to the service.
    For more information, see the error and message fields.
    """

    _ERROR_CODE = "InvalidGatewayRequestException"

    @property
    def error(self) -> dict[str, Any] | None:
        """A StorageGatewayError that provides more detail about the cause of the error."""
        return self.response.get("error")


class ServiceUnavailableError(StorageGatewayError):
    """An internal server error has occurred because the service is unavailable. For more
    information, see the error and message fields.
    """

    _ERROR_CODE = "ServiceUnavailableError"

    @property
    def error(self) -> dict[str, Any] | None:
        """A StorageGatewayError that provides more information about the cause of the
        error.
        """
        return self.response.get("error")


EXCEPTIONS: dict[str, type[StorageGatewayError]] = {
    "InternalServerError": InternalServerError,
    "InvalidGatewayRequestException": InvalidGatewayRequestException,
    "ServiceUnavailableError": ServiceUnavailableError,
}
