# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class SMSError(Boto3Error):
    _SERVICE = "sms"


class DryRunOperationException(SMSError):
    """The user has the required permissions, so the request would have succeeded, but a
    dry run was performed.
    """

    _ERROR_CODE = "DryRunOperationException"


class InternalError(SMSError):
    """An internal error occurred."""
    _ERROR_CODE = "InternalError"


class InvalidParameterException(SMSError):
    """A specified parameter is not valid."""
    _ERROR_CODE = "InvalidParameterException"


class MissingRequiredParameterException(SMSError):
    """A required parameter is missing."""
    _ERROR_CODE = "MissingRequiredParameterException"


class NoConnectorsAvailableException(SMSError):
    """There are no connectors available."""
    _ERROR_CODE = "NoConnectorsAvailableException"


class OperationNotPermittedException(SMSError):
    """This operation is not allowed."""
    _ERROR_CODE = "OperationNotPermittedException"


class ReplicationJobAlreadyExistsException(SMSError):
    """The specified replication job already exists."""
    _ERROR_CODE = "ReplicationJobAlreadyExistsException"


class ReplicationJobNotFoundException(SMSError):
    """The specified replication job does not exist."""
    _ERROR_CODE = "ReplicationJobNotFoundException"


class ReplicationRunLimitExceededException(SMSError):
    """You have exceeded the number of on-demand replication runs you can request in a
    24-hour period.
    """

    _ERROR_CODE = "ReplicationRunLimitExceededException"


class ServerCannotBeReplicatedException(SMSError):
    """The specified server cannot be replicated."""
    _ERROR_CODE = "ServerCannotBeReplicatedException"


class TemporarilyUnavailableException(SMSError):
    """The service is temporarily unavailable."""
    _ERROR_CODE = "TemporarilyUnavailableException"


class UnauthorizedOperationException(SMSError):
    """You lack permissions needed to perform this operation. Check your IAM policies, and
    ensure that you are using the correct access keys.
    """

    _ERROR_CODE = "UnauthorizedOperationException"


EXCEPTIONS: dict[str, type[SMSError]] = {
    "DryRunOperationException": DryRunOperationException,
    "InternalError": InternalError,
    "InvalidParameterException": InvalidParameterException,
    "MissingRequiredParameterException": MissingRequiredParameterException,
    "NoConnectorsAvailableException": NoConnectorsAvailableException,
    "OperationNotPermittedException": OperationNotPermittedException,
    "ReplicationJobAlreadyExistsException": ReplicationJobAlreadyExistsException,
    "ReplicationJobNotFoundException": ReplicationJobNotFoundException,
    "ReplicationRunLimitExceededException": ReplicationRunLimitExceededException,
    "ServerCannotBeReplicatedException": ServerCannotBeReplicatedException,
    "TemporarilyUnavailableException": TemporarilyUnavailableException,
    "UnauthorizedOperationException": UnauthorizedOperationException,
}
