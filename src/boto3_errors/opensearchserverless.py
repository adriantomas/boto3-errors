# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class OpenSearchServerlessError(Boto3Error):
    _SERVICE = "opensearchserverless"


class ConflictException(OpenSearchServerlessError):
    """When creating a resource, thrown when a resource with the same name already exists
    or is being created.
    """

    _ERROR_CODE = "ConflictException"


class InternalServerException(OpenSearchServerlessError):
    """Thrown when an error internal to the service occurs while processing a request."""
    _ERROR_CODE = "InternalServerException"


class OcuLimitExceededException(OpenSearchServerlessError):
    """Thrown when the collection you're attempting to create results in a number of search
    or indexing OCUs that exceeds the account limit.
    """

    _ERROR_CODE = "OcuLimitExceededException"


class ResourceNotFoundException(OpenSearchServerlessError):
    """Thrown when accessing or deleting a resource that does not exist."""
    _ERROR_CODE = "ResourceNotFoundException"


class ServiceQuotaExceededException(OpenSearchServerlessError):
    """Thrown when you attempt to create more resources than the service allows based on
    service quotas.
    """

    _ERROR_CODE = "ServiceQuotaExceededException"

    @property
    def resource_id(self) -> str | None:
        """Identifier of the resource affected."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """Type of the resource affected."""
        return self.response.get("resourceType")

    @property
    def service_code(self) -> str | None:
        """Service Quotas requirement to identify originating service."""
        return self.response.get("serviceCode")

    @property
    def quota_code(self) -> str | None:
        """Service Quotas requirement to identify originating quota."""
        return self.response.get("quotaCode")


class ValidationException(OpenSearchServerlessError):
    """Thrown when the HTTP request contains invalid input or is missing required input."""
    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[OpenSearchServerlessError]] = {
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "OcuLimitExceededException": OcuLimitExceededException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ValidationException": ValidationException,
}
