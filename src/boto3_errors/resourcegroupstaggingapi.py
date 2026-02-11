# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class ResourceGroupsTaggingAPIError(Boto3Error):
    _SERVICE = "resourcegroupstaggingapi"


class ConcurrentModificationException(ResourceGroupsTaggingAPIError):
    """The request failed because the target of the operation is currently being modified
    by a different request. Try again later.
    """

    _ERROR_CODE = "ConcurrentModificationException"


class ConstraintViolationException(ResourceGroupsTaggingAPIError):
    """The request failed because performing the operation would violate a constraint.

    Some of the reasons in the following list might not apply to this specific
    operation.

    - You must meet the prerequisites for using tag policies. For information, see
      Prerequisites and permissions in the Tagging Amazon Web Services resources and Tag
      Editor user guide.
    - You must enable the tag policies service principal
      (`tagpolicies.tag.amazonaws.com`) to integrate with Organizations For information,
      see EnableAWSServiceAccess.
    - You must have a tag policy attached to the organization root, an OU, or an
      account.
    """

    _ERROR_CODE = "ConstraintViolationException"


class InternalServiceException(ResourceGroupsTaggingAPIError):
    """The request processing failed because of an unknown error, exception, or failure.
    You can retry the request.
    """

    _ERROR_CODE = "InternalServiceException"


class InvalidParameterException(ResourceGroupsTaggingAPIError):
    """The request failed because of one of the following reasons:

    - A required parameter is missing.
    - A provided string parameter is malformed.
    - An provided parameter value is out of range.
    - The target ID is invalid, unsupported, or doesn't exist.
    - You can't access the Amazon S3 bucket for report storage. For more information,
      see Amazon S3 bucket policy for report storage in the Tagging Amazon Web Services
      resources and Tag Editor user guide.
    - The partition specified in an ARN parameter in the request doesn't match the
      partition where you invoked the operation. The partition is specified by the
      second field of the ARN.
    """

    _ERROR_CODE = "InvalidParameterException"


class PaginationTokenExpiredException(ResourceGroupsTaggingAPIError):
    """The request failed because the specified `PaginationToken` has expired. A
    `PaginationToken` is valid for a maximum of 15 minutes.
    """

    _ERROR_CODE = "PaginationTokenExpiredException"


class ThrottledException(ResourceGroupsTaggingAPIError):
    """The request failed because it exceeded the allowed frequency of submitted requests."""
    _ERROR_CODE = "ThrottledException"


EXCEPTIONS: dict[str, type[ResourceGroupsTaggingAPIError]] = {
    "ConcurrentModificationException": ConcurrentModificationException,
    "ConstraintViolationException": ConstraintViolationException,
    "InternalServiceException": InternalServiceException,
    "InvalidParameterException": InvalidParameterException,
    "PaginationTokenExpiredException": PaginationTokenExpiredException,
    "ThrottledException": ThrottledException,
}
