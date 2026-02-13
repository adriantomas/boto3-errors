# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class KinesisError(Boto3Error):
    _SERVICE = "kinesis"


class AccessDeniedException(KinesisError):
    """Specifies that you do not have the permissions required to perform this operation."""
    _ERROR_CODE = "AccessDeniedException"


class ExpiredIteratorException(KinesisError):
    """The provided iterator exceeds the maximum age allowed."""
    _ERROR_CODE = "ExpiredIteratorException"


class ExpiredNextTokenException(KinesisError):
    """The pagination token passed to the operation is expired."""
    _ERROR_CODE = "ExpiredNextTokenException"


class InternalFailureException(KinesisError):
    """The processing of the request failed because of an unknown error, exception, or
    failure.
    """

    _ERROR_CODE = "InternalFailureException"


class InvalidArgumentException(KinesisError):
    """A specified parameter exceeds its restrictions, is not supported, or can't be used.
    For more information, see the returned message.
    """

    _ERROR_CODE = "InvalidArgumentException"


class KMSAccessDeniedException(KinesisError):
    """The ciphertext references a key that doesn't exist or that you don't have access to."""
    _ERROR_CODE = "KMSAccessDeniedException"


class KMSDisabledException(KinesisError):
    """The request was rejected because the specified customer master key (CMK) isn't
    enabled.
    """

    _ERROR_CODE = "KMSDisabledException"


class KMSInvalidStateException(KinesisError):
    """The request was rejected because the state of the specified resource isn't valid for
    this request. For more information, see How Key State Affects Use of a Customer
    Master Key in the Amazon Web Services Key Management Service Developer Guide.
    """

    _ERROR_CODE = "KMSInvalidStateException"


class KMSNotFoundException(KinesisError):
    """The request was rejected because the specified entity or resource can't be found."""
    _ERROR_CODE = "KMSNotFoundException"


class KMSOptInRequired(KinesisError):
    """The Amazon Web Services access key ID needs a subscription for the service."""
    _ERROR_CODE = "KMSOptInRequired"


class KMSThrottlingException(KinesisError):
    """The request was denied due to request throttling. For more information about
    throttling, see Limits in the Amazon Web Services Key Management Service Developer
    Guide.
    """

    _ERROR_CODE = "KMSThrottlingException"


class LimitExceededException(KinesisError):
    """The requested resource exceeds the maximum number allowed, or the number of
    concurrent stream requests exceeds the maximum number allowed.
    """

    _ERROR_CODE = "LimitExceededException"


class ProvisionedThroughputExceededException(KinesisError):
    """The request rate for the stream is too high, or the requested data is too large for
    the available throughput. Reduce the frequency or size of your requests. For more
    information, see Streams Limits in the Amazon Kinesis Data Streams Developer Guide,
    and Error Retries and Exponential Backoff in Amazon Web Services in the Amazon Web
    Services General Reference.
    """

    _ERROR_CODE = "ProvisionedThroughputExceededException"


class ResourceInUseException(KinesisError):
    """The resource is not available for this operation. For successful operation, the
    resource must be in the `ACTIVE` state.
    """

    _ERROR_CODE = "ResourceInUseException"


class ResourceNotFoundException(KinesisError):
    """The requested resource could not be found. The stream might not be specified
    correctly.
    """

    _ERROR_CODE = "ResourceNotFoundException"


class ValidationException(KinesisError):
    """Specifies that you tried to invoke this API for a data stream with the on-demand
    capacity mode. This API is only supported for data streams with the provisioned
    capacity mode.
    """

    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[KinesisError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ExpiredIteratorException": ExpiredIteratorException,
    "ExpiredNextTokenException": ExpiredNextTokenException,
    "InternalFailureException": InternalFailureException,
    "InvalidArgumentException": InvalidArgumentException,
    "KMSAccessDeniedException": KMSAccessDeniedException,
    "KMSDisabledException": KMSDisabledException,
    "KMSInvalidStateException": KMSInvalidStateException,
    "KMSNotFoundException": KMSNotFoundException,
    "KMSOptInRequired": KMSOptInRequired,
    "KMSThrottlingException": KMSThrottlingException,
    "LimitExceededException": LimitExceededException,
    "ProvisionedThroughputExceededException": ProvisionedThroughputExceededException,
    "ResourceInUseException": ResourceInUseException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ValidationException": ValidationException,
}
