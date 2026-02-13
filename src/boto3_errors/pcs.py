# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class PCSError(Boto3Error):
    _SERVICE = "pcs"


class AccessDeniedException(PCSError):
    """You don't have permission to perform the action.

     Examples

    - The launch template instance profile doesn't pass `iam:PassRole` verification.
    - There is a mismatch between the account ID and cluster ID.
    - The cluster ID doesn't exist.
    - The EC2 instance isn't present.
    """

    _ERROR_CODE = "AccessDeniedException"


class ConflictException(PCSError):
    """Your request has conflicting operations. This can occur if you're trying to perform
    more than 1 operation on the same resource at the same time.

     Examples

    - A cluster with the same name already exists.
    - A cluster isn't in `ACTIVE` status.
    - A cluster to delete is in an unstable state. For example, because it still has
      `ACTIVE` node groups or queues.
    - A queue already exists in a cluster.
    """

    _ERROR_CODE = "ConflictException"

    @property
    def resource_id(self) -> str | None:
        """The unique identifier of the resource that caused the conflict exception."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """The type or category of the resource that caused the conflict exception.""""
        return self.response.get("resourceType")


class InternalServerException(PCSError):
    """PCS can't process your request right now. Try again later."""
    _ERROR_CODE = "InternalServerException"


class ResourceNotFoundException(PCSError):
    """The requested resource can't be found. The cluster, node group, or queue you're
    attempting to get, update, list, or delete doesn't exist.

     Examples
    """

    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def resource_id(self) -> str | None:
        """The unique identifier of the resource that was not found."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """The type or category of the resource that was not found."""
        return self.response.get("resourceType")


class ServiceQuotaExceededException(PCSError):
    """You exceeded your service quota. Service quotas, also referred to as limits, are the
    maximum number of service resources or operations for your Amazon Web Services
    account. To learn how to increase your service quota, see Requesting a quota
    increase in the Service Quotas User Guide

     Examples

    - The max number of clusters or queues has been reached for the account.
    - The max number of compute node groups has been reached for the associated cluster.
    - The total of `maxInstances` across all compute node groups has been reached for
      associated cluster.
    """

    _ERROR_CODE = "ServiceQuotaExceededException"

    @property
    def service_code(self) -> str | None:
        """The service code associated with the quota that was exceeded."""
        return self.response.get("serviceCode")

    @property
    def resource_id(self) -> str | None:
        """The unique identifier of the resource that caused the quota to be exceeded."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """The type or category of the resource that caused the quota to be exceeded."""
        return self.response.get("resourceType")

    @property
    def quota_code(self) -> str | None:
        """The quota code of the service quota that was exceeded."""
        return self.response.get("quotaCode")


class ThrottlingException(PCSError):
    """Your request exceeded a request rate quota. Check the resource's request rate quota
    and try again.
    """

    _ERROR_CODE = "ThrottlingException"

    @property
    def retry_after_seconds(self) -> int | None:
        """The number of seconds to wait before retrying the request."""
        return self.response.get("retryAfterSeconds")


class ValidationException(PCSError):
    """The request isn't valid.

     Examples

    - Your request contains malformed JSON or unsupported characters.
    - The scheduler version isn't supported.
    - There are networking related errors, such as network validation failure.
    - AMI type is `CUSTOM` and the launch template doesn't define the AMI ID, or the AMI
      type is AL2 and the launch template defines the AMI.
    """

    _ERROR_CODE = "ValidationException"

    @property
    def reason(self) -> str | None:
        """The specific reason or cause of the validation error."""
        return self.response.get("reason")

    @property
    def field_list(self) -> list[Any] | None:
        """A list of fields or properties that failed validation."""
        return self.response.get("fieldList")


EXCEPTIONS: dict[str, type[PCSError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
