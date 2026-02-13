# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class QBusinessError(Boto3Error):
    _SERVICE = "qbusiness"


class AccessDeniedException(QBusinessError):
    """You don't have access to perform this action. Make sure you have the required
    permission policies and user accounts and try again.
    """

    _ERROR_CODE = "AccessDeniedException"


class ConflictException(QBusinessError):
    """You are trying to perform an action that conflicts with the current status of your
    resource. Fix any inconsistencies with your resources and try again.
    """

    _ERROR_CODE = "ConflictException"

    @property
    def resource_id(self) -> str | None:
        """The identifier of the resource affected."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of the resource affected."""
        return self.response.get("resourceType")


class ExternalResourceException(QBusinessError):
    """An external resource that you configured with your application is returning errors
    and preventing this operation from succeeding. Fix those errors and try again.
    """

    _ERROR_CODE = "ExternalResourceException"


class InternalServerException(QBusinessError):
    """An issue occurred with the internal server used for your Amazon Q Business service.
    Wait some minutes and try again, or contact Support for help.
    """

    _ERROR_CODE = "InternalServerException"


class LicenseNotFoundException(QBusinessError):
    """You don't have permissions to perform the action because your license is inactive.
    Ask your admin to activate your license and try again after your licence is active.
    """

    _ERROR_CODE = "LicenseNotFoundException"


class MediaTooLargeException(QBusinessError):
    """The requested media object is too large to be returned."""
    _ERROR_CODE = "MediaTooLargeException"


class ResourceNotFoundException(QBusinessError):
    """The application or plugin resource you want to use doesn’t exist. Make sure you have
    provided the correct resource and try again.
    """

    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def resource_id(self) -> str | None:
        """The identifier of the resource affected."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of the resource affected."""
        return self.response.get("resourceType")


class ServiceQuotaExceededException(QBusinessError):
    """You have exceeded the set limits for your Amazon Q Business service."""
    _ERROR_CODE = "ServiceQuotaExceededException"

    @property
    def resource_id(self) -> str | None:
        """The identifier of the resource affected."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of the resource affected."""
        return self.response.get("resourceType")


class ThrottlingException(QBusinessError):
    """The request was denied due to throttling. Reduce the number of requests and try
    again.
    """

    _ERROR_CODE = "ThrottlingException"


class ValidationException(QBusinessError):
    """The input doesn't meet the constraints set by the Amazon Q Business service. Provide
    the correct input and try again.
    """

    _ERROR_CODE = "ValidationException"

    @property
    def reason(self) -> str | None:
        """The reason for the `ValidationException`."""
        return self.response.get("reason")

    @property
    def fields(self) -> list[Any] | None:
        """The input field(s) that failed validation."""
        return self.response.get("fields")


EXCEPTIONS: dict[str, type[QBusinessError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "ExternalResourceException": ExternalResourceException,
    "InternalServerException": InternalServerException,
    "LicenseNotFoundException": LicenseNotFoundException,
    "MediaTooLargeException": MediaTooLargeException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
