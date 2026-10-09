# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class LambdaWebError(Boto3Error):
    _SERVICE = "lambda-web"


class AccessDeniedException(LambdaWebError):
    """You do not have sufficient permissions to perform this operation."""
    _ERROR_CODE = "AccessDeniedException"


class InternalServerException(LambdaWebError):
    """An internal server error occurred. Try again later."""
    _ERROR_CODE = "InternalServerException"


class ThrottlingException(LambdaWebError):
    """The request was throttled. Reduce the frequency of requests and try again."""
    _ERROR_CODE = "ThrottlingException"

    @property
    def quota_code(self) -> str | None:
        """The quota code that was exceeded, if applicable."""
        return self.response.get("quotaCode")

    @property
    def retry_after_seconds(self) -> int | None:
        """The number of seconds to wait before retrying the request."""
        return self.response.get("retryAfterSeconds")

    @property
    def service_code(self) -> str | None:
        """The service code of the throttled service."""
        return self.response.get("serviceCode")


EXCEPTIONS: dict[str, type[LambdaWebError]] = {
    "AccessDeniedException": AccessDeniedException,
    "InternalServerException": InternalServerException,
    "ThrottlingException": ThrottlingException,
}
