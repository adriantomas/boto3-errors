# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class MWAAServerlessError(Boto3Error):
    _SERVICE = "mwaa-serverless"


class AccessDeniedException(MWAAServerlessError):
    """You do not have sufficient permission to perform this action."""
    _ERROR_CODE = "AccessDeniedException"


class ConflictException(MWAAServerlessError):
    """You cannot create a resource that already exists, or the resource is in a state that
    prevents the requested operation.
    """

    _ERROR_CODE = "ConflictException"

    @property
    def resource_id(self) -> str | None:
        """The unique identifier of the resource."""
        return self.response.get("ResourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of the resource."""
        return self.response.get("ResourceType")


class InternalServerException(MWAAServerlessError):
    """An unexpected server-side error occurred during request processing."""
    _ERROR_CODE = "InternalServerException"

    @property
    def retry_after_seconds(self) -> int | None:
        """The number of seconds to wait before retrying the operation."""
        return self.response.get("RetryAfterSeconds")


class OperationTimeoutException(MWAAServerlessError):
    """The operation timed out."""
    _ERROR_CODE = "OperationTimeoutException"


class ResourceNotFoundException(MWAAServerlessError):
    """The specified resource was not found. You can only access or modify a resource that
    already exists.
    """

    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def resource_id(self) -> str | None:
        """The unique identifier of the resource."""
        return self.response.get("ResourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of the resource."""
        return self.response.get("ResourceType")


class ServiceQuotaExceededException(MWAAServerlessError):
    """The request exceeds the service quota for Amazon Managed Workflows for Apache
    Airflow Serverless resources. This can occur when you attempt to create more
    workflows than allowed, exceed concurrent workflow run limits, or surpass task
    execution limits. Amazon Managed Workflows for Apache Airflow Serverless implements
    admission control using DynamoDB-based counters to manage resource utilization
    across the multi-tenant environment. Contact Amazon Web Services Support to request
    quota increases if you need higher limits for your use case.
    """

    _ERROR_CODE = "ServiceQuotaExceededException"

    @property
    def quota_code(self) -> str | None:
        """The code of the quota."""
        return self.response.get("QuotaCode")

    @property
    def resource_id(self) -> str | None:
        """The unique identifier of the resource."""
        return self.response.get("ResourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of resource affected."""
        return self.response.get("ResourceType")

    @property
    def service_code(self) -> str | None:
        """The code for the service."""
        return self.response.get("ServiceCode")


class ThrottlingException(MWAAServerlessError):
    """The request was denied because too many requests were made in a short period,
    exceeding the service rate limits. Amazon Managed Workflows for Apache Airflow
    Serverless implements throttling controls to ensure fair resource allocation across
    all customers in the multi-tenant environment. This helps maintain service stability
    and performance. If you encounter throttling, implement exponential backoff and
    retry logic in your applications, or consider distributing your API calls over a
    longer time period.
    """

    _ERROR_CODE = "ThrottlingException"

    @property
    def quota_code(self) -> str | None:
        """The code of the quota."""
        return self.response.get("QuotaCode")

    @property
    def retry_after_seconds(self) -> int | None:
        """The number of seconds to wait before retrying the operation."""
        return self.response.get("RetryAfterSeconds")

    @property
    def service_code(self) -> str | None:
        """The code for the service."""
        return self.response.get("ServiceCode")


class ValidationException(MWAAServerlessError):
    """The specified request parameters are invalid, missing, or inconsistent with Amazon
    Managed Workflows for Apache Airflow Serverless service requirements. This can occur
    when workflow definitions contain unsupported operators, when required IAM
    permissions are missing, when S3 locations are inaccessible, or when network
    configurations are invalid. The service validates workflow definitions, execution
    roles, and resource configurations to ensure compatibility with the managed Airflow
    environment and security requirements.
    """

    _ERROR_CODE = "ValidationException"

    @property
    def field_list(self) -> list[Any] | None:
        """The fields that failed validation."""
        return self.response.get("FieldList")

    @property
    def reason(self) -> str | None:
        """The reason the request failed validation."""
        return self.response.get("Reason")


EXCEPTIONS: dict[str, type[MWAAServerlessError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "OperationTimeoutException": OperationTimeoutException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
