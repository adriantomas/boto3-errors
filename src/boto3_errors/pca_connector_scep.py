# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class PcaConnectorScepError(Boto3Error):
    _SERVICE = "pca-connector-scep"


class AccessDeniedException(PcaConnectorScepError):
    """You can receive this error if you attempt to perform an operation and you don't have
    the required permissions. This can be caused by insufficient permissions in policies
    attached to your Amazon Web Services Identity and Access Management (IAM) principal.
    It can also happen because of restrictions in place from an Amazon Web Services
    Organizations service control policy (SCP) that affects your Amazon Web Services
    account.
    """

    _ERROR_CODE = "AccessDeniedException"


class BadRequestException(PcaConnectorScepError):
    """The request is malformed or contains an error such as an invalid parameter value or
    a missing required parameter.
    """

    _ERROR_CODE = "BadRequestException"


class ConflictException(PcaConnectorScepError):
    """This request can't be completed for one of the following reasons because the
    requested resource was being concurrently modified by another request.
    """

    _ERROR_CODE = "ConflictException"

    @property
    def resource_id(self) -> str | None:
        """The identifier of the Amazon Web Services resource."""
        return self.response.get("ResourceId")

    @property
    def resource_type(self) -> str | None:
        """The resource type, which can be either `Connector` or `Challenge`."""
        return self.response.get("ResourceType")


class InternalServerException(PcaConnectorScepError):
    """The request processing has failed because of an unknown error, exception or failure
    with an internal server.
    """

    _ERROR_CODE = "InternalServerException"


class ResourceNotFoundException(PcaConnectorScepError):
    """The operation tried to access a nonexistent resource. The resource might be
    incorrectly specified, or it might have a status other than `ACTIVE`.
    """

    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def resource_id(self) -> str | None:
        """The identifier of the Amazon Web Services resource."""
        return self.response.get("ResourceId")

    @property
    def resource_type(self) -> str | None:
        """The resource type, which can be either `Connector` or `Challenge`."""
        return self.response.get("ResourceType")


class ServiceQuotaExceededException(PcaConnectorScepError):
    """The request would cause a service quota to be exceeded."""
    _ERROR_CODE = "ServiceQuotaExceededException"

    @property
    def quota_code(self) -> str | None:
        """The quota identifier."""
        return self.response.get("QuotaCode")

    @property
    def resource_type(self) -> str | None:
        """The resource type, which can be either `Connector` or `Challenge`."""
        return self.response.get("ResourceType")

    @property
    def service_code(self) -> str | None:
        """Identifies the originating service."""
        return self.response.get("ServiceCode")


class ThrottlingException(PcaConnectorScepError):
    """The limit on the number of requests per second was exceeded."""
    _ERROR_CODE = "ThrottlingException"


class ValidationException(PcaConnectorScepError):
    """An input validation error occurred. For example, invalid characters in a name tag,
    or an invalid pagination token.
    """

    _ERROR_CODE = "ValidationException"

    @property
    def reason(self) -> str | None:
        """The reason for the validation error, if available. The service doesn't return a
        reason for every validation exception.
        """
        return self.response.get("Reason")


EXCEPTIONS: dict[str, type[PcaConnectorScepError]] = {
    "AccessDeniedException": AccessDeniedException,
    "BadRequestException": BadRequestException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
