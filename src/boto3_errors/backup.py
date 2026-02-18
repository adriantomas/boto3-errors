# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class BackupError(Boto3Error):
    _SERVICE = "backup"


class AlreadyExistsException(BackupError):
    """The required resource already exists."""
    _ERROR_CODE = "AlreadyExistsException"

    @property
    def arn(self) -> str | None:
        return self.response.get("Arn")

    @property
    def code(self) -> str | None:
        return self.response.get("Code")

    @property
    def context(self) -> str | None:
        return self.response.get("Context")

    @property
    def creator_request_id(self) -> str | None:
        return self.response.get("CreatorRequestId")

    @property
    def type(self) -> str | None:
        return self.response.get("Type")


class ConflictException(BackupError):
    """Backup can't perform the action that you requested until it finishes performing a
    previous action. Try again later.
    """

    _ERROR_CODE = "ConflictException"

    @property
    def code(self) -> str | None:
        return self.response.get("Code")

    @property
    def context(self) -> str | None:
        return self.response.get("Context")

    @property
    def type(self) -> str | None:
        return self.response.get("Type")


class DependencyFailureException(BackupError):
    """A dependent Amazon Web Services service or resource returned an error to the Backup
    service, and the action cannot be completed.
    """

    _ERROR_CODE = "DependencyFailureException"

    @property
    def code(self) -> str | None:
        return self.response.get("Code")

    @property
    def context(self) -> str | None:
        return self.response.get("Context")

    @property
    def type(self) -> str | None:
        return self.response.get("Type")


class InvalidParameterValueException(BackupError):
    """Indicates that something is wrong with a parameter's value. For example, the value
    is out of range.
    """

    _ERROR_CODE = "InvalidParameterValueException"

    @property
    def code(self) -> str | None:
        return self.response.get("Code")

    @property
    def context(self) -> str | None:
        return self.response.get("Context")

    @property
    def type(self) -> str | None:
        return self.response.get("Type")


class InvalidRequestException(BackupError):
    """Indicates that something is wrong with the input to the request. For example, a
    parameter is of the wrong type.
    """

    _ERROR_CODE = "InvalidRequestException"

    @property
    def code(self) -> str | None:
        return self.response.get("Code")

    @property
    def context(self) -> str | None:
        return self.response.get("Context")

    @property
    def type(self) -> str | None:
        return self.response.get("Type")


class InvalidResourceStateException(BackupError):
    """Backup is already performing an action on this recovery point. It can't perform the
    action you requested until the first action finishes. Try again later.
    """

    _ERROR_CODE = "InvalidResourceStateException"

    @property
    def code(self) -> str | None:
        return self.response.get("Code")

    @property
    def context(self) -> str | None:
        return self.response.get("Context")

    @property
    def type(self) -> str | None:
        return self.response.get("Type")


class LimitExceededException(BackupError):
    """A limit in the request has been exceeded; for example, a maximum number of items
    allowed in a request.
    """

    _ERROR_CODE = "LimitExceededException"

    @property
    def code(self) -> str | None:
        return self.response.get("Code")

    @property
    def context(self) -> str | None:
        return self.response.get("Context")

    @property
    def type(self) -> str | None:
        return self.response.get("Type")


class MissingParameterValueException(BackupError):
    """Indicates that a required parameter is missing."""
    _ERROR_CODE = "MissingParameterValueException"

    @property
    def code(self) -> str | None:
        return self.response.get("Code")

    @property
    def context(self) -> str | None:
        return self.response.get("Context")

    @property
    def type(self) -> str | None:
        return self.response.get("Type")


class ResourceNotFoundException(BackupError):
    """A resource that is required for the action doesn't exist."""
    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def code(self) -> str | None:
        return self.response.get("Code")

    @property
    def context(self) -> str | None:
        return self.response.get("Context")

    @property
    def type(self) -> str | None:
        return self.response.get("Type")


class ServiceUnavailableException(BackupError):
    """The request failed due to a temporary failure of the server."""
    _ERROR_CODE = "ServiceUnavailableException"

    @property
    def code(self) -> str | None:
        return self.response.get("Code")

    @property
    def context(self) -> str | None:
        return self.response.get("Context")

    @property
    def type(self) -> str | None:
        return self.response.get("Type")


EXCEPTIONS: dict[str, type[BackupError]] = {
    "AlreadyExistsException": AlreadyExistsException,
    "ConflictException": ConflictException,
    "DependencyFailureException": DependencyFailureException,
    "InvalidParameterValueException": InvalidParameterValueException,
    "InvalidRequestException": InvalidRequestException,
    "InvalidResourceStateException": InvalidResourceStateException,
    "LimitExceededException": LimitExceededException,
    "MissingParameterValueException": MissingParameterValueException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceUnavailableException": ServiceUnavailableException,
}
