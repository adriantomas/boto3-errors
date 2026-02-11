# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class S3VectorsError(Boto3Error):
    _SERVICE = "s3vectors"


class AccessDeniedException(S3VectorsError):
    """Access denied."""
    _ERROR_CODE = "AccessDeniedException"


class ConflictException(S3VectorsError):
    """The request failed because a vector bucket name or a vector index name already
    exists. Vector bucket names must be unique within your Amazon Web Services account
    for each Amazon Web Services Region. Vector index names must be unique within your
    vector bucket. Choose a different vector bucket name or vector index name, and try
    again.
    """

    _ERROR_CODE = "ConflictException"


class InternalServerException(S3VectorsError):
    """The request failed due to an internal server error."""
    _ERROR_CODE = "InternalServerException"


class KmsDisabledException(S3VectorsError):
    """The specified Amazon Web Services KMS key isn't enabled."""
    _ERROR_CODE = "KmsDisabledException"


class KmsInvalidKeyUsageException(S3VectorsError):
    """The request was rejected for one of the following reasons:

    - The `KeyUsage` value of the KMS key is incompatible with the API operation.
    - The encryption algorithm or signing algorithm specified for the operation is
      incompatible with the type of key material in the KMS key (`KeySpec`).

    For more information, see InvalidKeyUsageException in the Amazon Web Services Key
    Management Service API Reference.
    """

    _ERROR_CODE = "KmsInvalidKeyUsageException"


class KmsInvalidStateException(S3VectorsError):
    """The key state of the KMS key isn't compatible with the operation.

    For more information, see KMSInvalidStateException in the Amazon Web Services Key
    Management Service API Reference.
    """

    _ERROR_CODE = "KmsInvalidStateException"


class KmsNotFoundException(S3VectorsError):
    """The KMS key can't be found."""
    _ERROR_CODE = "KmsNotFoundException"


class NotFoundException(S3VectorsError):
    """The request was rejected because the specified resource can't be found."""
    _ERROR_CODE = "NotFoundException"


class RequestTimeoutException(S3VectorsError):
    """The request timed out. Retry your request."""
    _ERROR_CODE = "RequestTimeoutException"


class ServiceQuotaExceededException(S3VectorsError):
    """Your request exceeds a service quota."""
    _ERROR_CODE = "ServiceQuotaExceededException"


class ServiceUnavailableException(S3VectorsError):
    """The service is unavailable. Wait briefly and retry your request. If it continues to
    fail, increase your waiting time between retries.
    """

    _ERROR_CODE = "ServiceUnavailableException"


class TooManyRequestsException(S3VectorsError):
    """The request was denied due to request throttling."""
    _ERROR_CODE = "TooManyRequestsException"


class ValidationException(S3VectorsError):
    """The requested action isn't valid."""
    _ERROR_CODE = "ValidationException"

    @property
    def field_list(self) -> list[Any] | None:
        """A list of specific validation failures that are encountered during input
        processing. Each entry in the list contains a path to the field that failed
        validation and a detailed message that explains why the validation failed. To
        satisfy multiple constraints, a field can appear multiple times in this list if
        it failed. You can use the information to identify and fix the specific
        validation issues in your request.
        """
        return self.response.get("fieldList")


EXCEPTIONS: dict[str, type[S3VectorsError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "KmsDisabledException": KmsDisabledException,
    "KmsInvalidKeyUsageException": KmsInvalidKeyUsageException,
    "KmsInvalidStateException": KmsInvalidStateException,
    "KmsNotFoundException": KmsNotFoundException,
    "NotFoundException": NotFoundException,
    "RequestTimeoutException": RequestTimeoutException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ServiceUnavailableException": ServiceUnavailableException,
    "TooManyRequestsException": TooManyRequestsException,
    "ValidationException": ValidationException,
}
