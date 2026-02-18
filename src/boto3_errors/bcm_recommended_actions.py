# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class BCMRecommendedActionsError(Boto3Error):
    _SERVICE = "bcm-recommended-actions"


class AccessDeniedException(BCMRecommendedActionsError):
    """You do not have sufficient access to perform this action."""
    _ERROR_CODE = "AccessDeniedException"


class InternalServerException(BCMRecommendedActionsError):
    """An unexpected error occurred during the processing of your request."""
    _ERROR_CODE = "InternalServerException"


class ThrottlingException(BCMRecommendedActionsError):
    """The request was denied due to request throttling."""
    _ERROR_CODE = "ThrottlingException"


class ValidationException(BCMRecommendedActionsError):
    """The input fails to satisfy the constraints specified by an Amazon Web Services
    service.
    """

    _ERROR_CODE = "ValidationException"

    @property
    def field_list(self) -> list[Any] | None:
        """Lists each problematic field and why it failed validation."""
        return self.response.get("fieldList")

    @property
    def reason(self) -> str | None:
        """Provides a single, overarching explanation for the validation failure."""
        return self.response.get("reason")


EXCEPTIONS: dict[str, type[BCMRecommendedActionsError]] = {
    "AccessDeniedException": AccessDeniedException,
    "InternalServerException": InternalServerException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
