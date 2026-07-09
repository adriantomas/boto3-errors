# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class LambdaCoreError(Boto3Error):
    _SERVICE = "lambda-core"


class InvalidParameterValueException(LambdaCoreError):
    """One of the parameters in the request is not valid. Check the error message for
    details about which parameter failed validation.
    """

    _ERROR_CODE = "InvalidParameterValueException"

    @property
    def type(self) -> str | None:
        """The exception type."""
        return self.response.get("Type")


class NetworkConnectorLimitExceededException(LambdaCoreError):
    """The account has reached the maximum number of network connectors allowed. Delete
    unused connectors or request a limit increase through Service Quotas.
    """

    _ERROR_CODE = "NetworkConnectorLimitExceededException"

    @property
    def type(self) -> str | None:
        """The exception type."""
        return self.response.get("Type")


class ResourceConflictException(LambdaCoreError):
    """The request could not be completed due to a conflict with the current state of the
    resource. For example, attempting to update a connector that is not in `ACTIVE`
    state.
    """

    _ERROR_CODE = "ResourceConflictException"

    @property
    def type(self) -> str | None:
        """The exception type."""
        return self.response.get("Type")


class ResourceNotFoundException(LambdaCoreError):
    """The specified network connector does not exist. Verify the identifier (ID, name, or
    ARN) and Region.
    """

    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def type(self) -> str | None:
        """The exception type."""
        return self.response.get("Type")


class ServiceException(LambdaCoreError):
    """An internal service error occurred. Retry the request with exponential backoff."""
    _ERROR_CODE = "ServiceException"

    @property
    def type(self) -> str | None:
        """The exception type."""
        return self.response.get("Type")


class TooManyRequestsException(LambdaCoreError):
    """The request was throttled due to exceeding the allowed request rate. Retry the
    request after a brief wait using exponential backoff.
    """

    _ERROR_CODE = "TooManyRequestsException"

    @property
    def reason(self) -> str | None:
        """The reason for the throttling."""
        return self.response.get("Reason")

    @property
    def type(self) -> str | None:
        """The exception type."""
        return self.response.get("Type")

    @property
    def retry_after_seconds(self) -> str | None:
        """The number of seconds to wait before retrying the request."""
        return self.response.get("retryAfterSeconds")


EXCEPTIONS: dict[str, type[LambdaCoreError]] = {
    "InvalidParameterValueException": InvalidParameterValueException,
    "NetworkConnectorLimitExceededException": NetworkConnectorLimitExceededException,
    "ResourceConflictException": ResourceConflictException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceException": ServiceException,
    "TooManyRequestsException": TooManyRequestsException,
}
