# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class BackupStorageError(Boto3Error):
    _SERVICE = "backupstorage"


class AccessDeniedException(BackupStorageError):
    _ERROR_CODE = "AccessDeniedException"


class DataAlreadyExistsException(BackupStorageError):
    """Non-retryable exception. Attempted to create already existing object or chunk. This
    message contains a checksum of already presented data.
    """

    _ERROR_CODE = "DataAlreadyExistsException"

    @property
    def checksum(self) -> str | None:
        """Data checksum used"""
        return self.response.get("Checksum")

    @property
    def checksum_algorithm(self) -> str | None:
        """Checksum algorithm used"""
        return self.response.get("ChecksumAlgorithm")


class IllegalArgumentException(BackupStorageError):
    """Non-retryable exception, indicates client error (wrong argument passed to API). See
    exception message for details.
    """

    _ERROR_CODE = "IllegalArgumentException"


class KMSInvalidKeyUsageException(BackupStorageError):
    """Non-retryable exception. Indicates the KMS key usage is incorrect. See exception
    message for details.
    """

    _ERROR_CODE = "KMSInvalidKeyUsageException"


class NotReadableInputStreamException(BackupStorageError):
    """Retryalble exception. Indicated issues while reading an input stream due to the
    networking issues or connection drop on the client side.
    """

    _ERROR_CODE = "NotReadableInputStreamException"


class ResourceNotFoundException(BackupStorageError):
    """Non-retryable exception. Attempted to make an operation on non-existing or expired
    resource.
    """

    _ERROR_CODE = "ResourceNotFoundException"


class RetryableException(BackupStorageError):
    """Retryable exception. In general indicates internal failure that can be fixed by
    retry.
    """

    _ERROR_CODE = "RetryableException"


class ServiceInternalException(BackupStorageError):
    """Deprecated. To be removed from the model."""
    _ERROR_CODE = "ServiceInternalException"


class ServiceUnavailableException(BackupStorageError):
    """Retryable exception, indicates internal server error."""
    _ERROR_CODE = "ServiceUnavailableException"


class ThrottlingException(BackupStorageError):
    """Increased rate over throttling limits. Can be retried with exponential backoff."""
    _ERROR_CODE = "ThrottlingException"


EXCEPTIONS: dict[str, type[BackupStorageError]] = {
    "AccessDeniedException": AccessDeniedException,
    "DataAlreadyExistsException": DataAlreadyExistsException,
    "IllegalArgumentException": IllegalArgumentException,
    "KMSInvalidKeyUsageException": KMSInvalidKeyUsageException,
    "NotReadableInputStreamException": NotReadableInputStreamException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "RetryableException": RetryableException,
    "ServiceInternalException": ServiceInternalException,
    "ServiceUnavailableException": ServiceUnavailableException,
    "ThrottlingException": ThrottlingException,
}
