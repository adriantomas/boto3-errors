# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class AgentDiscoveryError(Boto3Error):
    _SERVICE = "agent-discovery"


class InternalServerException(AgentDiscoveryError):
    """Thrown on an internal defect — a bug or malformed state, not a failed dependency.

    ⚠️ Deliberately a **permanent** failure. Repeating a request that failed to
    serialize will fail identically, so treating a 500 as retryable would spin a poison
    message through redelivery forever instead of letting it reach a dead-letter queue.
    Dependency failures that *are* worth retrying use `ServiceUnavailableException` and
    its 503 instead.
    """

    _ERROR_CODE = "InternalServerException"

    @property
    def error_code(self) -> str | None:
        """ARD's Appendix B code on the ARD surface, `INTERNAL_ERROR`."""
        return self.response.get("errorCode")


class ThrottlingException(AgentDiscoveryError):
    """Thrown when the caller exceeds a rate/burst limit (D-9). ARD's code for it is
    `RATE_LIMIT_EXCEEDED`.
    """

    _ERROR_CODE = "ThrottlingException"

    @property
    def error_code(self) -> str | None:
        return self.response.get("errorCode")


class ValidationException(AgentDiscoveryError):
    """Thrown when a request fails input validation.

    `errorCode` carries ARD's Appendix B code, `INVALID_ARGUMENT`, which ARD's OpenAPI
    makes a required member of every error body on the ARD surface. The Amazon-shaped
    and internal surfaces leave it unset.
    """

    _ERROR_CODE = "ValidationException"

    @property
    def error_code(self) -> str | None:
        return self.response.get("errorCode")


EXCEPTIONS: dict[str, type[AgentDiscoveryError]] = {
    "InternalServerException": InternalServerException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
