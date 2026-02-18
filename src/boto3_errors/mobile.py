# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class MobileError(Boto3Error):
    _SERVICE = "mobile"


class AccountActionRequiredException(MobileError):
    """Account Action is required in order to continue the request."""
    _ERROR_CODE = "AccountActionRequiredException"


class BadRequestException(MobileError):
    """The request cannot be processed because some parameter is not valid or the project
    state prevents the operation from being performed.
    """

    _ERROR_CODE = "BadRequestException"


class InternalFailureException(MobileError):
    """The service has encountered an unexpected error condition which prevents it from
    servicing the request.
    """

    _ERROR_CODE = "InternalFailureException"


class LimitExceededException(MobileError):
    """There are too many AWS Mobile Hub projects in the account or the account has
    exceeded the maximum number of resources in some AWS service. You should create
    another sub-account using AWS Organizations or remove some resources and retry your
    request.
    """

    _ERROR_CODE = "LimitExceededException"

    @property
    def retry_after_seconds(self) -> str | None:
        return self.response.get("retryAfterSeconds")


class NotFoundException(MobileError):
    """No entity can be found with the specified identifier."""
    _ERROR_CODE = "NotFoundException"


class ServiceUnavailableException(MobileError):
    """The service is temporarily unavailable. The request should be retried after some
    time delay.
    """

    _ERROR_CODE = "ServiceUnavailableException"

    @property
    def retry_after_seconds(self) -> str | None:
        return self.response.get("retryAfterSeconds")


class TooManyRequestsException(MobileError):
    """Too many requests have been received for this AWS account in too short a time. The
    request should be retried after some time delay.
    """

    _ERROR_CODE = "TooManyRequestsException"

    @property
    def retry_after_seconds(self) -> str | None:
        return self.response.get("retryAfterSeconds")


class UnauthorizedException(MobileError):
    """Credentials of the caller are insufficient to authorize the request."""
    _ERROR_CODE = "UnauthorizedException"


EXCEPTIONS: dict[str, type[MobileError]] = {
    "AccountActionRequiredException": AccountActionRequiredException,
    "BadRequestException": BadRequestException,
    "InternalFailureException": InternalFailureException,
    "LimitExceededException": LimitExceededException,
    "NotFoundException": NotFoundException,
    "ServiceUnavailableException": ServiceUnavailableException,
    "TooManyRequestsException": TooManyRequestsException,
    "UnauthorizedException": UnauthorizedException,
}
