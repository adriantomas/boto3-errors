# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class ServiceCatalogAppRegistryError(Boto3Error):
    _SERVICE = "servicecatalog-appregistry"


class ConflictException(ServiceCatalogAppRegistryError):
    """There was a conflict when processing the request (for example, a resource with the
    given name already exists within the account).
    """

    _ERROR_CODE = "ConflictException"


class InternalServerException(ServiceCatalogAppRegistryError):
    """The service is experiencing internal problems."""
    _ERROR_CODE = "InternalServerException"


class ResourceNotFoundException(ServiceCatalogAppRegistryError):
    """The specified resource does not exist."""
    _ERROR_CODE = "ResourceNotFoundException"


class ServiceQuotaExceededException(ServiceCatalogAppRegistryError):
    """The maximum number of resources per account has been reached."""
    _ERROR_CODE = "ServiceQuotaExceededException"


class ThrottlingException(ServiceCatalogAppRegistryError):
    """The maximum number of API requests has been exceeded."""
    _ERROR_CODE = "ThrottlingException"

    @property
    def service_code(self) -> str | None:
        """The originating service code."""
        return self.response.get("serviceCode")


class ValidationException(ServiceCatalogAppRegistryError):
    """The request has invalid or missing parameters."""
    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[ServiceCatalogAppRegistryError]] = {
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
