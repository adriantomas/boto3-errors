# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class ResourceGroupsTaggingAPIError(Boto3Error):
    _SERVICE = "resourcegroupstaggingapi"


class ConcurrentModificationException(ResourceGroupsTaggingAPIError):
    """The target of the operation is currently being modified by a different request. Try
    again later.
    """

    _ERROR_CODE = "ConcurrentModificationException"


class ConstraintViolationException(ResourceGroupsTaggingAPIError):
    """The request was denied because performing this operation violates a constraint.

    Some of the reasons in the following list might not apply to this specific
    operation.

    - You must meet the prerequisites for using tag policies. For information, see
      Prerequisites and Permissions for Using Tag Policies in the Organizations User
      Guide.
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
    """This error indicates one of the following:

    - A parameter is missing.
    - A malformed string was supplied for the request parameter.
    - An out-of-range value was supplied for the request parameter.
    - The target ID is invalid, unsupported, or doesn't exist.
    - You can't access the Amazon S3 bucket for report storage. For more information,
      see Additional Requirements for Organization-wide Tag Compliance Reports in the
      Organizations User Guide.
    """

    _ERROR_CODE = "InvalidParameterException"


class PaginationTokenExpiredException(ResourceGroupsTaggingAPIError):
    """A `PaginationToken` is valid for a maximum of 15 minutes. Your request was denied
    because the specified `PaginationToken` has expired.
    """

    _ERROR_CODE = "PaginationTokenExpiredException"


class ThrottledException(ResourceGroupsTaggingAPIError):
    """The request was denied to limit the frequency of submitted requests."""
    _ERROR_CODE = "ThrottledException"


EXCEPTIONS: dict[str, type[ResourceGroupsTaggingAPIError]] = {
    "ConcurrentModificationException": ConcurrentModificationException,
    "ConstraintViolationException": ConstraintViolationException,
    "InternalServiceException": InternalServiceException,
    "InvalidParameterException": InvalidParameterException,
    "PaginationTokenExpiredException": PaginationTokenExpiredException,
    "ThrottledException": ThrottledException,
}
