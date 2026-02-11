# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class FirehoseError(Boto3Error):
    _SERVICE = "firehose"


class ConcurrentModificationException(FirehoseError):
    """Another modification has already happened. Fetch `VersionId` again and use it to
    update the destination.
    """

    _ERROR_CODE = "ConcurrentModificationException"


class InvalidArgumentException(FirehoseError):
    """The specified input parameter has a value that is not valid."""
    _ERROR_CODE = "InvalidArgumentException"


class InvalidKMSResourceException(FirehoseError):
    """Firehose throws this exception when an attempt to put records or to start or stop
    Firehose stream encryption fails. This happens when the KMS service throws one of
    the following exception types: `AccessDeniedException`, `InvalidStateException`,
    `DisabledException`, or `NotFoundException`.
    """

    _ERROR_CODE = "InvalidKMSResourceException"

    @property
    def code(self) -> str | None:
        return self.response.get("code")


class InvalidSourceException(FirehoseError):
    """Only requests from CloudWatch Logs are supported when CloudWatch Logs decompression
    is enabled.
    """

    _ERROR_CODE = "InvalidSourceException"

    @property
    def code(self) -> str | None:
        return self.response.get("code")


class LimitExceededException(FirehoseError):
    """You have already reached the limit for a requested resource."""
    _ERROR_CODE = "LimitExceededException"


class ResourceInUseException(FirehoseError):
    """The resource is already in use and not available for this operation."""
    _ERROR_CODE = "ResourceInUseException"


class ResourceNotFoundException(FirehoseError):
    """The specified resource could not be found."""
    _ERROR_CODE = "ResourceNotFoundException"


class ServiceUnavailableException(FirehoseError):
    """The service is unavailable. Back off and retry the operation. If you continue to see
    the exception, throughput limits for the Firehose stream may have been exceeded. For
    more information about limits and how to request an increase, see Amazon Firehose
    Limits.
    """

    _ERROR_CODE = "ServiceUnavailableException"


EXCEPTIONS: dict[str, type[FirehoseError]] = {
    "ConcurrentModificationException": ConcurrentModificationException,
    "InvalidArgumentException": InvalidArgumentException,
    "InvalidKMSResourceException": InvalidKMSResourceException,
    "InvalidSourceException": InvalidSourceException,
    "LimitExceededException": LimitExceededException,
    "ResourceInUseException": ResourceInUseException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceUnavailableException": ServiceUnavailableException,
}
