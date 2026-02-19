# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class CodeStarError(Boto3Error):
    _SERVICE = "codestar"


class ConcurrentModificationException(CodeStarError):
    """Another modification is being made. That modification must complete before you can
    make your change.
    """

    _ERROR_CODE = "ConcurrentModificationException"


class InvalidNextTokenException(CodeStarError):
    """The next token is not valid."""
    _ERROR_CODE = "InvalidNextTokenException"


class InvalidServiceRoleException(CodeStarError):
    """The service role is not valid."""
    _ERROR_CODE = "InvalidServiceRoleException"


class LimitExceededException(CodeStarError):
    """A resource limit has been exceeded."""
    _ERROR_CODE = "LimitExceededException"


class ProjectAlreadyExistsException(CodeStarError):
    """An AWS CodeStar project with the same ID already exists in this region for the AWS
    account. AWS CodeStar project IDs must be unique within a region for the AWS
    account.
    """

    _ERROR_CODE = "ProjectAlreadyExistsException"


class ProjectConfigurationException(CodeStarError):
    """Project configuration information is required but not specified."""
    _ERROR_CODE = "ProjectConfigurationException"


class ProjectCreationFailedException(CodeStarError):
    """The project creation request was valid, but a nonspecific exception or error
    occurred during project creation. The project could not be created in AWS CodeStar.
    """

    _ERROR_CODE = "ProjectCreationFailedException"


class ProjectNotFoundException(CodeStarError):
    """The specified AWS CodeStar project was not found."""
    _ERROR_CODE = "ProjectNotFoundException"


class TeamMemberAlreadyAssociatedException(CodeStarError):
    """The team member is already associated with a role in this project."""
    _ERROR_CODE = "TeamMemberAlreadyAssociatedException"


class TeamMemberNotFoundException(CodeStarError):
    """The specified team member was not found."""
    _ERROR_CODE = "TeamMemberNotFoundException"


class UserProfileAlreadyExistsException(CodeStarError):
    """A user profile with that name already exists in this region for the AWS account. AWS
    CodeStar user profile names must be unique within a region for the AWS account.
    """

    _ERROR_CODE = "UserProfileAlreadyExistsException"


class UserProfileNotFoundException(CodeStarError):
    """The user profile was not found."""
    _ERROR_CODE = "UserProfileNotFoundException"


class ValidationException(CodeStarError):
    """The specified input is either not valid, or it could not be validated."""
    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[CodeStarError]] = {
    "ConcurrentModificationException": ConcurrentModificationException,
    "InvalidNextTokenException": InvalidNextTokenException,
    "InvalidServiceRoleException": InvalidServiceRoleException,
    "LimitExceededException": LimitExceededException,
    "ProjectAlreadyExistsException": ProjectAlreadyExistsException,
    "ProjectConfigurationException": ProjectConfigurationException,
    "ProjectCreationFailedException": ProjectCreationFailedException,
    "ProjectNotFoundException": ProjectNotFoundException,
    "TeamMemberAlreadyAssociatedException": TeamMemberAlreadyAssociatedException,
    "TeamMemberNotFoundException": TeamMemberNotFoundException,
    "UserProfileAlreadyExistsException": UserProfileAlreadyExistsException,
    "UserProfileNotFoundException": UserProfileNotFoundException,
    "ValidationException": ValidationException,
}
