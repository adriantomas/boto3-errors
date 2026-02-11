# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class ElasticBeanstalkError(Boto3Error):
    _SERVICE = "elasticbeanstalk"


class CodeBuildNotInServiceRegionException(ElasticBeanstalkError):
    """AWS CodeBuild is not available in the specified region."""
    _ERROR_CODE = "CodeBuildNotInServiceRegionException"


class ElasticBeanstalkServiceException(ElasticBeanstalkError):
    """A generic service exception has occurred."""
    _ERROR_CODE = "ElasticBeanstalkServiceException"


class InsufficientPrivilegesException(ElasticBeanstalkError):
    """The specified account does not have sufficient privileges for one or more AWS
    services.
    """

    _ERROR_CODE = "InsufficientPrivilegesException"


class InvalidRequestException(ElasticBeanstalkError):
    """One or more input parameters is not valid. Please correct the input parameters and
    try the operation again.
    """

    _ERROR_CODE = "InvalidRequestException"


class ManagedActionInvalidStateException(ElasticBeanstalkError):
    """Cannot modify the managed action in its current state."""
    _ERROR_CODE = "ManagedActionInvalidStateException"


class OperationInProgressException(ElasticBeanstalkError):
    """Unable to perform the specified operation because another operation that effects an
    element in this activity is already in progress.
    """

    _ERROR_CODE = "OperationInProgressFailure"


class PlatformVersionStillReferencedException(ElasticBeanstalkError):
    """You cannot delete the platform version because there are still environments running
    on it.
    """

    _ERROR_CODE = "PlatformVersionStillReferencedException"


class ResourceNotFoundException(ElasticBeanstalkError):
    """A resource doesn't exist for the specified Amazon Resource Name (ARN)."""
    _ERROR_CODE = "ResourceNotFoundException"


class ResourceTypeNotSupportedException(ElasticBeanstalkError):
    """The type of the specified Amazon Resource Name (ARN) isn't supported for this
    operation.
    """

    _ERROR_CODE = "ResourceTypeNotSupportedException"


class S3LocationNotInServiceRegionException(ElasticBeanstalkError):
    """The specified S3 bucket does not belong to the S3 region in which the service is
    running. The following regions are supported:

    - IAD/us-east-1
    - PDX/us-west-2
    - DUB/eu-west-1
    """

    _ERROR_CODE = "S3LocationNotInServiceRegionException"


class S3SubscriptionRequiredException(ElasticBeanstalkError):
    """The specified account does not have a subscription to Amazon S3."""
    _ERROR_CODE = "S3SubscriptionRequiredException"


class SourceBundleDeletionException(ElasticBeanstalkError):
    """Unable to delete the Amazon S3 source bundle associated with the application
    version. The application version was deleted successfully.
    """

    _ERROR_CODE = "SourceBundleDeletionFailure"


class TooManyApplicationVersionsException(ElasticBeanstalkError):
    """The specified account has reached its limit of application versions."""
    _ERROR_CODE = "TooManyApplicationVersionsException"


class TooManyApplicationsException(ElasticBeanstalkError):
    """The specified account has reached its limit of applications."""
    _ERROR_CODE = "TooManyApplicationsException"


class TooManyBucketsException(ElasticBeanstalkError):
    """The specified account has reached its limit of Amazon S3 buckets."""
    _ERROR_CODE = "TooManyBucketsException"


class TooManyConfigurationTemplatesException(ElasticBeanstalkError):
    """The specified account has reached its limit of configuration templates."""
    _ERROR_CODE = "TooManyConfigurationTemplatesException"


class TooManyEnvironmentsException(ElasticBeanstalkError):
    """The specified account has reached its limit of environments."""
    _ERROR_CODE = "TooManyEnvironmentsException"


class TooManyPlatformsException(ElasticBeanstalkError):
    """You have exceeded the maximum number of allowed platforms associated with the
    account.
    """

    _ERROR_CODE = "TooManyPlatformsException"


class TooManyTagsException(ElasticBeanstalkError):
    """The number of tags in the resource would exceed the number of tags that each
    resource can have.

    To calculate this, the operation considers both the number of tags the resource
    already has and the tags this operation would add if it succeeded.
    """

    _ERROR_CODE = "TooManyTagsException"


EXCEPTIONS: dict[str, type[ElasticBeanstalkError]] = {
    "CodeBuildNotInServiceRegionException": CodeBuildNotInServiceRegionException,
    "ElasticBeanstalkServiceException": ElasticBeanstalkServiceException,
    "InsufficientPrivilegesException": InsufficientPrivilegesException,
    "InvalidRequestException": InvalidRequestException,
    "ManagedActionInvalidStateException": ManagedActionInvalidStateException,
    "OperationInProgressFailure": OperationInProgressException,
    "PlatformVersionStillReferencedException": PlatformVersionStillReferencedException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ResourceTypeNotSupportedException": ResourceTypeNotSupportedException,
    "S3LocationNotInServiceRegionException": S3LocationNotInServiceRegionException,
    "S3SubscriptionRequiredException": S3SubscriptionRequiredException,
    "SourceBundleDeletionFailure": SourceBundleDeletionException,
    "TooManyApplicationVersionsException": TooManyApplicationVersionsException,
    "TooManyApplicationsException": TooManyApplicationsException,
    "TooManyBucketsException": TooManyBucketsException,
    "TooManyConfigurationTemplatesException": TooManyConfigurationTemplatesException,
    "TooManyEnvironmentsException": TooManyEnvironmentsException,
    "TooManyPlatformsException": TooManyPlatformsException,
    "TooManyTagsException": TooManyTagsException,
}
