# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class CognitoIdentityError(Boto3Error):
    _SERVICE = "cognito-identity"


class ConcurrentModificationException(CognitoIdentityError):
    """Thrown if there are parallel requests to modify a resource."""
    _ERROR_CODE = "ConcurrentModificationException"


class DeveloperUserAlreadyRegisteredException(CognitoIdentityError):
    """The provided developer user identifier is already registered with Cognito under a
    different identity ID.
    """

    _ERROR_CODE = "DeveloperUserAlreadyRegisteredException"


class ExternalServiceException(CognitoIdentityError):
    """An exception thrown when a dependent service such as Facebook or Twitter is not
    responding
    """

    _ERROR_CODE = "ExternalServiceException"


class InternalErrorException(CognitoIdentityError):
    """Thrown when the service encounters an error during processing the request."""
    _ERROR_CODE = "InternalErrorException"


class InvalidIdentityPoolConfigurationException(CognitoIdentityError):
    """Thrown if the identity pool has no role associated for the given auth type
    (auth/unauth) or if the AssumeRole fails.
    """

    _ERROR_CODE = "InvalidIdentityPoolConfigurationException"


class InvalidParameterException(CognitoIdentityError):
    """Thrown for missing or bad input parameter(s)."""
    _ERROR_CODE = "InvalidParameterException"


class LimitExceededException(CognitoIdentityError):
    """Thrown when the total number of user pools has exceeded a preset limit."""
    _ERROR_CODE = "LimitExceededException"


class NotAuthorizedException(CognitoIdentityError):
    """Thrown when a user is not authorized to access the requested resource."""
    _ERROR_CODE = "NotAuthorizedException"


class ResourceConflictException(CognitoIdentityError):
    """Thrown when a user tries to use a login which is already linked to another account."""
    _ERROR_CODE = "ResourceConflictException"


class ResourceNotFoundException(CognitoIdentityError):
    """Thrown when the requested resource (for example, a dataset or record) does not
    exist.
    """

    _ERROR_CODE = "ResourceNotFoundException"


class TooManyRequestsException(CognitoIdentityError):
    """Thrown when a request is throttled."""
    _ERROR_CODE = "TooManyRequestsException"


EXCEPTIONS: dict[str, type[CognitoIdentityError]] = {
    "ConcurrentModificationException": ConcurrentModificationException,
    "DeveloperUserAlreadyRegisteredException": DeveloperUserAlreadyRegisteredException,
    "ExternalServiceException": ExternalServiceException,
    "InternalErrorException": InternalErrorException,
    "InvalidIdentityPoolConfigurationException": InvalidIdentityPoolConfigurationException,
    "InvalidParameterException": InvalidParameterException,
    "LimitExceededException": LimitExceededException,
    "NotAuthorizedException": NotAuthorizedException,
    "ResourceConflictException": ResourceConflictException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "TooManyRequestsException": TooManyRequestsException,
}
