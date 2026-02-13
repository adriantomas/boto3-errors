# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class CognitoSyncError(Boto3Error):
    _SERVICE = "cognito-sync"


class AlreadyStreamedException(CognitoSyncError):
    """An exception thrown when a bulk publish operation is requested less than 24 hours
    after a previous bulk publish operation completed successfully.
    """

    _ERROR_CODE = "AlreadyStreamedException"


class ConcurrentModificationException(CognitoSyncError):
    """Thrown if there are parallel requests to modify a resource."""
    _ERROR_CODE = "ConcurrentModificationException"


class DuplicateRequestException(CognitoSyncError):
    """An exception thrown when there is an IN_PROGRESS bulk publish operation for the
    given identity pool.
    """

    _ERROR_CODE = "DuplicateRequestException"


class InternalErrorException(CognitoSyncError):
    """Indicates an internal service error."""
    _ERROR_CODE = "InternalErrorException"


class InvalidConfigurationException(CognitoSyncError):
    _ERROR_CODE = "InvalidConfigurationException"


class InvalidLambdaFunctionOutputException(CognitoSyncError):
    """The AWS Lambda function returned invalid output or an exception."""
    _ERROR_CODE = "InvalidLambdaFunctionOutputException"


class InvalidParameterException(CognitoSyncError):
    """Thrown when a request parameter does not comply with the associated constraints."""
    _ERROR_CODE = "InvalidParameterException"


class LambdaThrottledException(CognitoSyncError):
    """AWS Lambda throttled your account, please contact AWS Support"""
    _ERROR_CODE = "LambdaThrottledException"


class LimitExceededException(CognitoSyncError):
    """Thrown when the limit on the number of objects or operations has been exceeded."""
    _ERROR_CODE = "LimitExceededException"


class NotAuthorizedException(CognitoSyncError):
    """Thrown when a user is not authorized to access the requested resource."""
    _ERROR_CODE = "NotAuthorizedException"


class ResourceConflictException(CognitoSyncError):
    """Thrown if an update can't be applied because the resource was changed by another
    call and this would result in a conflict.
    """

    _ERROR_CODE = "ResourceConflictException"


class ResourceNotFoundException(CognitoSyncError):
    """Thrown if the resource doesn't exist."""
    _ERROR_CODE = "ResourceNotFoundException"


class TooManyRequestsException(CognitoSyncError):
    """Thrown if the request is throttled."""
    _ERROR_CODE = "TooManyRequestsException"


EXCEPTIONS: dict[str, type[CognitoSyncError]] = {
    "AlreadyStreamedException": AlreadyStreamedException,
    "ConcurrentModificationException": ConcurrentModificationException,
    "DuplicateRequestException": DuplicateRequestException,
    "InternalErrorException": InternalErrorException,
    "InvalidConfigurationException": InvalidConfigurationException,
    "InvalidLambdaFunctionOutputException": InvalidLambdaFunctionOutputException,
    "InvalidParameterException": InvalidParameterException,
    "LambdaThrottledException": LambdaThrottledException,
    "LimitExceededException": LimitExceededException,
    "NotAuthorizedException": NotAuthorizedException,
    "ResourceConflictException": ResourceConflictException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "TooManyRequestsException": TooManyRequestsException,
}
