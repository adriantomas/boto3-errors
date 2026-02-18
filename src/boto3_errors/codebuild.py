# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class CodeBuildError(Boto3Error):
    _SERVICE = "codebuild"


class AccountLimitExceededException(CodeBuildError):
    """An Amazon Web Services service limit was exceeded for the calling Amazon Web
    Services account.
    """

    _ERROR_CODE = "AccountLimitExceededException"


class InvalidInputException(CodeBuildError):
    """The input value that was provided is not valid."""
    _ERROR_CODE = "InvalidInputException"


class OAuthProviderException(CodeBuildError):
    """There was a problem with the underlying OAuth provider."""
    _ERROR_CODE = "OAuthProviderException"


class ResourceAlreadyExistsException(CodeBuildError):
    """The specified Amazon Web Services resource cannot be created, because an Amazon Web
    Services resource with the same settings already exists.
    """

    _ERROR_CODE = "ResourceAlreadyExistsException"


class ResourceNotFoundException(CodeBuildError):
    """The specified Amazon Web Services resource cannot be found."""
    _ERROR_CODE = "ResourceNotFoundException"


EXCEPTIONS: dict[str, type[CodeBuildError]] = {
    "AccountLimitExceededException": AccountLimitExceededException,
    "InvalidInputException": InvalidInputException,
    "OAuthProviderException": OAuthProviderException,
    "ResourceAlreadyExistsException": ResourceAlreadyExistsException,
    "ResourceNotFoundException": ResourceNotFoundException,
}
