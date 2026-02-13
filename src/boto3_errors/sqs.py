# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class SQSError(Boto3Error):
    _SERVICE = "sqs"


class BatchEntryIdsNotDistinct(SQSError):
    """Two or more batch entries in the request have the same `Id`."""
    _ERROR_CODE = "BatchEntryIdsNotDistinct"


class BatchRequestTooLong(SQSError):
    """The length of all the messages put together is more than the limit."""
    _ERROR_CODE = "BatchRequestTooLong"


class EmptyBatchRequest(SQSError):
    """The batch request doesn't contain any entries."""
    _ERROR_CODE = "EmptyBatchRequest"


class InvalidAddress(SQSError):
    """The specified ID is invalid."""
    _ERROR_CODE = "InvalidAddress"


class InvalidAttributeName(SQSError):
    """The specified attribute doesn't exist."""
    _ERROR_CODE = "InvalidAttributeName"


class InvalidAttributeValue(SQSError):
    """A queue attribute value is invalid."""
    _ERROR_CODE = "InvalidAttributeValue"


class InvalidBatchEntryId(SQSError):
    """The `Id` of a batch entry in a batch request doesn't abide by the specification."""
    _ERROR_CODE = "InvalidBatchEntryId"


class InvalidIdFormat(SQSError):
    """The specified receipt handle isn't valid for the current version."""
    _ERROR_CODE = "InvalidIdFormat"


class InvalidMessageContents(SQSError):
    """The message contains characters outside the allowed set."""
    _ERROR_CODE = "InvalidMessageContents"


class InvalidSecurity(SQSError):
    """The request was not made over HTTPS or did not use SigV4 for signing."""
    _ERROR_CODE = "InvalidSecurity"


class KmsAccessDenied(SQSError):
    """The caller doesn't have the required KMS access."""
    _ERROR_CODE = "KmsAccessDenied"


class KmsDisabled(SQSError):
    """The request was denied due to request throttling."""
    _ERROR_CODE = "KmsDisabled"


class KmsInvalidKeyUsage(SQSError):
    """The request was rejected for one of the following reasons:

    - The KeyUsage value of the KMS key is incompatible with the API operation.
    - The encryption algorithm or signing algorithm specified for the operation is
      incompatible with the type of key material in the KMS key (KeySpec).
    """

    _ERROR_CODE = "KmsInvalidKeyUsage"


class KmsInvalidState(SQSError):
    """The request was rejected because the state of the specified resource is not valid
    for this request.
    """

    _ERROR_CODE = "KmsInvalidState"


class KmsNotFound(SQSError):
    """The request was rejected because the specified entity or resource could not be
    found.
    """

    _ERROR_CODE = "KmsNotFound"


class KmsOptInRequired(SQSError):
    """The request was rejected because the specified key policy isn't syntactically or
    semantically correct.
    """

    _ERROR_CODE = "KmsOptInRequired"


class KmsThrottled(SQSError):
    """Amazon Web Services KMS throttles requests for the following conditions."""
    _ERROR_CODE = "KmsThrottled"


class MessageNotInflight(SQSError):
    """The specified message isn't in flight."""
    _ERROR_CODE = "MessageNotInflight"


class OverLimit(SQSError):
    """The specified action violates a limit. For example, `ReceiveMessage` returns this
    error if the maximum number of in flight messages is reached and `AddPermission`
    returns this error if the maximum number of permissions for the queue is reached.
    """

    _ERROR_CODE = "OverLimit"


class PurgeQueueInProgress(SQSError):
    """Indicates that the specified queue previously received a `PurgeQueue` request within
    the last 60 seconds (the time it can take to delete the messages in the queue).
    """

    _ERROR_CODE = "PurgeQueueInProgress"


class QueueDeletedRecently(SQSError):
    """You must wait 60 seconds after deleting a queue before you can create another queue
    with the same name.
    """

    _ERROR_CODE = "QueueDeletedRecently"


class QueueDoesNotExist(SQSError):
    """Ensure that the `QueueUrl` is correct and that the queue has not been deleted."""
    _ERROR_CODE = "QueueDoesNotExist"


class QueueNameExists(SQSError):
    """A queue with this name already exists. Amazon SQS returns this error only if the
    request includes attributes whose values differ from those of the existing queue.
    """

    _ERROR_CODE = "QueueNameExists"


class ReceiptHandleIsInvalid(SQSError):
    """The specified receipt handle isn't valid."""
    _ERROR_CODE = "ReceiptHandleIsInvalid"


class RequestThrottled(SQSError):
    """The request was denied due to request throttling.

    - Exceeds the permitted request rate for the queue or for the recipient of the
      request.
    - Ensure that the request rate is within the Amazon SQS limits for sending messages.
      For more information, see Amazon SQS quotas in the Amazon SQS Developer Guide.
    """

    _ERROR_CODE = "RequestThrottled"


class ResourceNotFoundException(SQSError):
    """One or more specified resources don't exist."""
    _ERROR_CODE = "ResourceNotFoundException"


class TooManyEntriesInBatchRequest(SQSError):
    """The batch request contains more entries than permissible. For Amazon SQS, the
    maximum number of entries you can include in a single SendMessageBatch,
    DeleteMessageBatch, or ChangeMessageVisibilityBatch request is 10.
    """

    _ERROR_CODE = "TooManyEntriesInBatchRequest"


class UnsupportedOperation(SQSError):
    """Error code 400. Unsupported operation."""
    _ERROR_CODE = "UnsupportedOperation"


EXCEPTIONS: dict[str, type[SQSError]] = {
    "BatchEntryIdsNotDistinct": BatchEntryIdsNotDistinct,
    "BatchRequestTooLong": BatchRequestTooLong,
    "EmptyBatchRequest": EmptyBatchRequest,
    "InvalidAddress": InvalidAddress,
    "InvalidAttributeName": InvalidAttributeName,
    "InvalidAttributeValue": InvalidAttributeValue,
    "InvalidBatchEntryId": InvalidBatchEntryId,
    "InvalidIdFormat": InvalidIdFormat,
    "InvalidMessageContents": InvalidMessageContents,
    "InvalidSecurity": InvalidSecurity,
    "KmsAccessDenied": KmsAccessDenied,
    "KmsDisabled": KmsDisabled,
    "KmsInvalidKeyUsage": KmsInvalidKeyUsage,
    "KmsInvalidState": KmsInvalidState,
    "KmsNotFound": KmsNotFound,
    "KmsOptInRequired": KmsOptInRequired,
    "KmsThrottled": KmsThrottled,
    "MessageNotInflight": MessageNotInflight,
    "OverLimit": OverLimit,
    "PurgeQueueInProgress": PurgeQueueInProgress,
    "QueueDeletedRecently": QueueDeletedRecently,
    "QueueDoesNotExist": QueueDoesNotExist,
    "QueueNameExists": QueueNameExists,
    "ReceiptHandleIsInvalid": ReceiptHandleIsInvalid,
    "RequestThrottled": RequestThrottled,
    "ResourceNotFoundException": ResourceNotFoundException,
    "TooManyEntriesInBatchRequest": TooManyEntriesInBatchRequest,
    "UnsupportedOperation": UnsupportedOperation,
}
