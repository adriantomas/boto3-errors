# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class TaxSettingsError(Boto3Error):
    _SERVICE = "taxsettings"


class AccessDeniedException(TaxSettingsError):
    """The access is denied for the Amazon Web ServicesSupport API."""
    _ERROR_CODE = "AccessDeniedException"


class AttachmentUploadException(TaxSettingsError):
    """Failed to upload the tax exemption document to Amazon Web ServicesSupport case."""
    _ERROR_CODE = "AttachmentUploadException"


class CaseCreationLimitExceededException(TaxSettingsError):
    """You've exceeded the Amazon Web ServicesSupport case creation limit for your account."""
    _ERROR_CODE = "CaseCreationLimitExceededException"


class ConflictException(TaxSettingsError):
    """The exception when the input is creating conflict with the given state."""
    _ERROR_CODE = "ConflictException"

    @property
    def error_code(self) -> str | None:
        """409"""
        return self.response.get("errorCode")


class InternalServerException(TaxSettingsError):
    """The exception thrown when an unexpected error occurs when processing a request."""
    _ERROR_CODE = "InternalServerException"

    @property
    def error_code(self) -> str | None:
        """500"""
        return self.response.get("errorCode")


class ResourceNotFoundException(TaxSettingsError):
    """The exception thrown when the input doesn't have a resource associated to it."""
    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def error_code(self) -> str | None:
        """404"""
        return self.response.get("errorCode")


class ValidationException(TaxSettingsError):
    """The exception when the input doesn't pass validation for at least one of the input
    parameters.
    """

    _ERROR_CODE = "ValidationException"

    @property
    def error_code(self) -> str | None:
        """400"""
        return self.response.get("errorCode")

    @property
    def field_list(self) -> list[Any] | None:
        """400"""
        return self.response.get("fieldList")


EXCEPTIONS: dict[str, type[TaxSettingsError]] = {
    "AccessDeniedException": AccessDeniedException,
    "AttachmentUploadException": AttachmentUploadException,
    "CaseCreationLimitExceededException": CaseCreationLimitExceededException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ValidationException": ValidationException,
}
