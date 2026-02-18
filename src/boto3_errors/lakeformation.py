# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class LakeFormationError(Boto3Error):
    _SERVICE = "lakeformation"


class AccessDeniedException(LakeFormationError):
    """Access to a resource was denied."""
    _ERROR_CODE = "AccessDeniedException"


class AlreadyExistsException(LakeFormationError):
    """A resource to be created or added already exists."""
    _ERROR_CODE = "AlreadyExistsException"


class ConcurrentModificationException(LakeFormationError):
    """Two processes are trying to modify a resource simultaneously."""
    _ERROR_CODE = "ConcurrentModificationException"


class EntityNotFoundException(LakeFormationError):
    """A specified entity does not exist."""
    _ERROR_CODE = "EntityNotFoundException"


class ExpiredException(LakeFormationError):
    """Contains details about an error where the query request expired."""
    _ERROR_CODE = "ExpiredException"


class GlueEncryptionException(LakeFormationError):
    """An encryption operation failed."""
    _ERROR_CODE = "GlueEncryptionException"


class InternalServiceException(LakeFormationError):
    """An internal service error occurred."""
    _ERROR_CODE = "InternalServiceException"


class InvalidInputException(LakeFormationError):
    """The input provided was not valid."""
    _ERROR_CODE = "InvalidInputException"


class OperationTimeoutException(LakeFormationError):
    """The operation timed out."""
    _ERROR_CODE = "OperationTimeoutException"


class PermissionTypeMismatchException(LakeFormationError):
    """The engine does not support filtering data based on the enforced permissions. For
    example, if you call the `GetTemporaryGlueTableCredentials` operation with
    `SupportedPermissionType` equal to `ColumnPermission`, but cell-level permissions
    exist on the table, this exception is thrown.
    """

    _ERROR_CODE = "PermissionTypeMismatchException"


class ResourceNotReadyException(LakeFormationError):
    """Contains details about an error related to a resource which is not ready for a
    transaction.
    """

    _ERROR_CODE = "ResourceNotReadyException"


class ResourceNumberLimitExceededException(LakeFormationError):
    """A resource numerical limit was exceeded."""
    _ERROR_CODE = "ResourceNumberLimitExceededException"


class StatisticsNotReadyYetException(LakeFormationError):
    """Contains details about an error related to statistics not being ready."""
    _ERROR_CODE = "StatisticsNotReadyYetException"


class ThrottledException(LakeFormationError):
    """Contains details about an error where the query request was throttled."""
    _ERROR_CODE = "ThrottledException"


class TransactionCanceledException(LakeFormationError):
    """Contains details about an error related to a transaction that was cancelled."""
    _ERROR_CODE = "TransactionCanceledException"


class TransactionCommitInProgressException(LakeFormationError):
    """Contains details about an error related to a transaction commit that was in
    progress.
    """

    _ERROR_CODE = "TransactionCommitInProgressException"


class TransactionCommittedException(LakeFormationError):
    """Contains details about an error where the specified transaction has already been
    committed and cannot be used for `UpdateTableObjects`.
    """

    _ERROR_CODE = "TransactionCommittedException"


class WorkUnitsNotReadyYetException(LakeFormationError):
    """Contains details about an error related to work units not being ready."""
    _ERROR_CODE = "WorkUnitsNotReadyYetException"


EXCEPTIONS: dict[str, type[LakeFormationError]] = {
    "AccessDeniedException": AccessDeniedException,
    "AlreadyExistsException": AlreadyExistsException,
    "ConcurrentModificationException": ConcurrentModificationException,
    "EntityNotFoundException": EntityNotFoundException,
    "ExpiredException": ExpiredException,
    "GlueEncryptionException": GlueEncryptionException,
    "InternalServiceException": InternalServiceException,
    "InvalidInputException": InvalidInputException,
    "OperationTimeoutException": OperationTimeoutException,
    "PermissionTypeMismatchException": PermissionTypeMismatchException,
    "ResourceNotReadyException": ResourceNotReadyException,
    "ResourceNumberLimitExceededException": ResourceNumberLimitExceededException,
    "StatisticsNotReadyYetException": StatisticsNotReadyYetException,
    "ThrottledException": ThrottledException,
    "TransactionCanceledException": TransactionCanceledException,
    "TransactionCommitInProgressException": TransactionCommitInProgressException,
    "TransactionCommittedException": TransactionCommittedException,
    "WorkUnitsNotReadyYetException": WorkUnitsNotReadyYetException,
}
