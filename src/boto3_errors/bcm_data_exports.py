# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class BCMDataExportsError(Boto3Error):
    _SERVICE = "bcm-data-exports"


class InternalServerException(BCMDataExportsError):
    """An error on the server occurred during the processing of your request. Try again
    later.
    """

    _ERROR_CODE = "InternalServerException"


class ResourceNotFoundException(BCMDataExportsError):
    """The specified Amazon Resource Name (ARN) in the request doesn't exist."""
    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def resource_id(self) -> str | None:
        """The identifier of the resource that was not found."""
        return self.response.get("ResourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of the resource that was not found."""
        return self.response.get("ResourceType")


class ServiceQuotaExceededException(BCMDataExportsError):
    """You've reached the limit on the number of resources you can create, or exceeded the
    size of an individual resource.
    """

    _ERROR_CODE = "ServiceQuotaExceededException"

    @property
    def quota_code(self) -> str | None:
        """The quota code that was exceeded."""
        return self.response.get("QuotaCode")

    @property
    def resource_id(self) -> str | None:
        """The identifier of the resource that exceeded quota."""
        return self.response.get("ResourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of the resource that exceeded quota."""
        return self.response.get("ResourceType")

    @property
    def service_code(self) -> str | None:
        """The service code that exceeded quota. It will always be
        “AWSBillingAndCostManagementDataExports”.
        """
        return self.response.get("ServiceCode")


class ThrottlingException(BCMDataExportsError):
    """The request was denied due to request throttling."""
    _ERROR_CODE = "ThrottlingException"

    @property
    def quota_code(self) -> str | None:
        """The quota code that exceeded the throttling limit."""
        return self.response.get("QuotaCode")

    @property
    def service_code(self) -> str | None:
        """The service code that exceeded the throttling limit. It will always be
        “AWSBillingAndCostManagementDataExports”.
        """
        return self.response.get("ServiceCode")


class ValidationException(BCMDataExportsError):
    """The input fails to satisfy the constraints specified by an Amazon Web Services
    service.
    """

    _ERROR_CODE = "ValidationException"

    @property
    def fields(self) -> list[Any] | None:
        """The list of fields that are invalid."""
        return self.response.get("Fields")

    @property
    def reason(self) -> str | None:
        """The reason for the validation exception."""
        return self.response.get("Reason")


EXCEPTIONS: dict[str, type[BCMDataExportsError]] = {
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
