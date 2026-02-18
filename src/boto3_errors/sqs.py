# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class SQSError(Boto3Error):
    _SERVICE = "sqs"


class BatchEntryIdsNotDistinct(SQSError):
    """Two or more batch entries in the request have the same `Id`."""
    _ERROR_CODE = "AWS.SimpleQueueService.BatchEntryIdsNotDistinct"


class BatchRequestTooLong(SQSError):
    """The length of all the messages put together is more than the limit."""
    _ERROR_CODE = "AWS.SimpleQueueService.BatchRequestTooLong"


class EmptyBatchRequest(SQSError):
    """The batch request doesn't contain any entries."""
    _ERROR_CODE = "AWS.SimpleQueueService.EmptyBatchRequest"


class InvalidAttributeName(SQSError):
    """The specified attribute doesn't exist."""
    _ERROR_CODE = "InvalidAttributeName"


class InvalidBatchEntryId(SQSError):
    """The `Id` of a batch entry in a batch request doesn't abide by the specification."""
    _ERROR_CODE = "AWS.SimpleQueueService.InvalidBatchEntryId"


class InvalidIdFormat(SQSError):
    """The specified receipt handle isn't valid for the current version."""
    _ERROR_CODE = "InvalidIdFormat"


class InvalidMessageContents(SQSError):
    """The message contains characters outside the allowed set."""
    _ERROR_CODE = "InvalidMessageContents"


class MessageNotInflight(SQSError):
    """The specified message isn't in flight."""
    _ERROR_CODE = "AWS.SimpleQueueService.MessageNotInflight"


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

    _ERROR_CODE = "AWS.SimpleQueueService.PurgeQueueInProgress"


class QueueDeletedRecently(SQSError):
    """You must wait 60 seconds after deleting a queue before you can create another queue
    with the same name.
    """

    _ERROR_CODE = "AWS.SimpleQueueService.QueueDeletedRecently"


class QueueDoesNotExist(SQSError):
    """The specified queue doesn't exist."""
    _ERROR_CODE = "AWS.SimpleQueueService.NonExistentQueue"


class QueueNameExists(SQSError):
    """A queue with this name already exists. Amazon SQS returns this error only if the
    request includes attributes whose values differ from those of the existing queue.
    """

    _ERROR_CODE = "QueueAlreadyExists"


class ReceiptHandleIsInvalid(SQSError):
    """The specified receipt handle isn't valid."""
    _ERROR_CODE = "ReceiptHandleIsInvalid"


class ResourceNotFoundException(SQSError):
    """One or more specified resources don't exist."""
    _ERROR_CODE = "ResourceNotFoundException"


class TooManyEntriesInBatchRequest(SQSError):
    """The batch request contains more entries than permissible."""
    _ERROR_CODE = "AWS.SimpleQueueService.TooManyEntriesInBatchRequest"


class UnsupportedOperation(SQSError):
    """Error code 400. Unsupported operation."""
    _ERROR_CODE = "AWS.SimpleQueueService.UnsupportedOperation"


EXCEPTIONS: dict[str, type[SQSError]] = {
    "AWS.SimpleQueueService.BatchEntryIdsNotDistinct": BatchEntryIdsNotDistinct,
    "AWS.SimpleQueueService.BatchRequestTooLong": BatchRequestTooLong,
    "AWS.SimpleQueueService.EmptyBatchRequest": EmptyBatchRequest,
    "InvalidAttributeName": InvalidAttributeName,
    "AWS.SimpleQueueService.InvalidBatchEntryId": InvalidBatchEntryId,
    "InvalidIdFormat": InvalidIdFormat,
    "InvalidMessageContents": InvalidMessageContents,
    "AWS.SimpleQueueService.MessageNotInflight": MessageNotInflight,
    "OverLimit": OverLimit,
    "AWS.SimpleQueueService.PurgeQueueInProgress": PurgeQueueInProgress,
    "AWS.SimpleQueueService.QueueDeletedRecently": QueueDeletedRecently,
    "AWS.SimpleQueueService.NonExistentQueue": QueueDoesNotExist,
    "QueueAlreadyExists": QueueNameExists,
    "ReceiptHandleIsInvalid": ReceiptHandleIsInvalid,
    "ResourceNotFoundException": ResourceNotFoundException,
    "AWS.SimpleQueueService.TooManyEntriesInBatchRequest": TooManyEntriesInBatchRequest,
    "AWS.SimpleQueueService.UnsupportedOperation": UnsupportedOperation,
}
