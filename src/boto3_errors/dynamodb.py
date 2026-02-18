# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class DynamoDBError(Boto3Error):
    _SERVICE = "dynamodb"


class BackupInUseException(DynamoDBError):
    """There is another ongoing conflicting backup control plane operation on the table.
    The backup is either being created, deleted or restored to a table.
    """

    _ERROR_CODE = "BackupInUseException"


class BackupNotFoundException(DynamoDBError):
    """Backup not found for the given BackupARN."""
    _ERROR_CODE = "BackupNotFoundException"


class ConditionalCheckFailedException(DynamoDBError):
    """A condition specified in the operation could not be evaluated."""
    _ERROR_CODE = "ConditionalCheckFailedException"

    @property
    def item(self) -> dict[str, Any] | None:
        """Item which caused the `ConditionalCheckFailedException`."""
        return self.response.get("Item")


class ContinuousBackupsUnavailableException(DynamoDBError):
    """Backups have not yet been enabled for this table."""
    _ERROR_CODE = "ContinuousBackupsUnavailableException"


class DuplicateItemException(DynamoDBError):
    """There was an attempt to insert an item with the same primary key as an item that
    already exists in the DynamoDB table.
    """

    _ERROR_CODE = "DuplicateItemException"


class ExportConflictException(DynamoDBError):
    """There was a conflict when writing to the specified S3 bucket."""
    _ERROR_CODE = "ExportConflictException"


class ExportNotFoundException(DynamoDBError):
    """The specified export was not found."""
    _ERROR_CODE = "ExportNotFoundException"


class GlobalTableAlreadyExistsException(DynamoDBError):
    """The specified global table already exists."""
    _ERROR_CODE = "GlobalTableAlreadyExistsException"


class GlobalTableNotFoundException(DynamoDBError):
    """The specified global table does not exist."""
    _ERROR_CODE = "GlobalTableNotFoundException"


class IdempotentParameterMismatchException(DynamoDBError):
    """DynamoDB rejected the request because you retried a request with a different payload
    but with an idempotent token that was already used.
    """

    _ERROR_CODE = "IdempotentParameterMismatchException"


class ImportConflictException(DynamoDBError):
    """There was a conflict when importing from the specified S3 source. This can occur
    when the current import conflicts with a previous import request that had the same
    client token.
    """

    _ERROR_CODE = "ImportConflictException"


class ImportNotFoundException(DynamoDBError):
    """The specified import was not found."""
    _ERROR_CODE = "ImportNotFoundException"


class IndexNotFoundException(DynamoDBError):
    """The operation tried to access a nonexistent index."""
    _ERROR_CODE = "IndexNotFoundException"


class InternalServerError(DynamoDBError):
    """An error occurred on the server side."""
    _ERROR_CODE = "InternalServerError"


class InvalidExportTimeException(DynamoDBError):
    """The specified `ExportTime` is outside of the point in time recovery window."""
    _ERROR_CODE = "InvalidExportTimeException"


class InvalidRestoreTimeException(DynamoDBError):
    """An invalid restore time was specified. RestoreDateTime must be between
    EarliestRestorableDateTime and LatestRestorableDateTime.
    """

    _ERROR_CODE = "InvalidRestoreTimeException"


class ItemCollectionSizeLimitExceededException(DynamoDBError):
    """An item collection is too large. This exception is only returned for tables that
    have one or more local secondary indexes.
    """

    _ERROR_CODE = "ItemCollectionSizeLimitExceededException"


class LimitExceededException(DynamoDBError):
    """There is no limit to the number of daily on-demand backups that can be taken.

    For most purposes, up to 500 simultaneous table operations are allowed per account.
    These operations include `CreateTable`, `UpdateTable`,
    `DeleteTable`,`UpdateTimeToLive`, `RestoreTableFromBackup`, and
    `RestoreTableToPointInTime`.

    When you are creating a table with one or more secondary indexes, you can have up to
    250 such requests running at a time. However, if the table or index specifications
    are complex, then DynamoDB might temporarily reduce the number of concurrent
    operations.

    When importing into DynamoDB, up to 50 simultaneous import table operations are
    allowed per account.

    There is a soft account quota of 2,500 tables.

    GetRecords was called with a value of more than 1000 for the limit request
    parameter.

    More than 2 processes are reading from the same streams shard at the same time.
    Exceeding this limit may result in request throttling.
    """

    _ERROR_CODE = "LimitExceededException"


class PointInTimeRecoveryUnavailableException(DynamoDBError):
    """Point in time recovery has not yet been enabled for this source table."""
    _ERROR_CODE = "PointInTimeRecoveryUnavailableException"


class ProvisionedThroughputExceededException(DynamoDBError):
    """Your request rate is too high. The Amazon Web Services SDKs for DynamoDB
    automatically retry requests that receive this exception. Your request is eventually
    successful, unless your retry queue is too large to finish. Reduce the frequency of
    requests and use exponential backoff. For more information, go to Error Retries and
    Exponential Backoff in the Amazon DynamoDB Developer Guide.
    """

    _ERROR_CODE = "ProvisionedThroughputExceededException"


class ReplicaAlreadyExistsException(DynamoDBError):
    """The specified replica is already part of the global table."""
    _ERROR_CODE = "ReplicaAlreadyExistsException"


class ReplicaNotFoundException(DynamoDBError):
    """The specified replica is no longer part of the global table."""
    _ERROR_CODE = "ReplicaNotFoundException"


class RequestLimitExceeded(DynamoDBError):
    """Throughput exceeds the current throughput quota for your account. Please contact
    Amazon Web Services Support to request a quota increase.
    """

    _ERROR_CODE = "RequestLimitExceeded"


class ResourceInUseException(DynamoDBError):
    """The operation conflicts with the resource's availability. For example, you attempted
    to recreate an existing table, or tried to delete a table currently in the
    `CREATING` state.
    """

    _ERROR_CODE = "ResourceInUseException"


class ResourceNotFoundException(DynamoDBError):
    """The operation tried to access a nonexistent table or index. The resource might not
    be specified correctly, or its status might not be `ACTIVE`.
    """

    _ERROR_CODE = "ResourceNotFoundException"


class TableAlreadyExistsException(DynamoDBError):
    """A target table with the specified name already exists."""
    _ERROR_CODE = "TableAlreadyExistsException"


class TableInUseException(DynamoDBError):
    """A target table with the specified name is either being created or deleted."""
    _ERROR_CODE = "TableInUseException"


class TableNotFoundException(DynamoDBError):
    """A source table with the name `TableName` does not currently exist within the
    subscriber's account or the subscriber is operating in the wrong Amazon Web Services
    Region.
    """

    _ERROR_CODE = "TableNotFoundException"


class TransactionCanceledException(DynamoDBError):
    """The entire transaction request was canceled.

    DynamoDB cancels a `TransactWriteItems` request under the following circumstances:

    - A condition in one of the condition expressions is not met.
    - A table in the `TransactWriteItems` request is in a different account or region.
    - More than one action in the `TransactWriteItems` operation targets the same item.
    - There is insufficient provisioned capacity for the transaction to be completed.
    - An item size becomes too large (larger than 400 KB), or a local secondary index
      (LSI) becomes too large, or a similar validation error occurs because of changes
      made by the transaction.
    - There is a user error, such as an invalid data format.
    - There is an ongoing `TransactWriteItems` operation that conflicts with a
      concurrent `TransactWriteItems` request. In this case the `TransactWriteItems`
      operation fails with a `TransactionCanceledException`.

    DynamoDB cancels a `TransactGetItems` request under the following circumstances:

    - There is an ongoing `TransactGetItems` operation that conflicts with a concurrent
      `PutItem`, `UpdateItem`, `DeleteItem` or `TransactWriteItems` request. In this
      case the `TransactGetItems` operation fails with a `TransactionCanceledException`.
    - A table in the `TransactGetItems` request is in a different account or region.
    - There is insufficient provisioned capacity for the transaction to be completed.
    - There is a user error, such as an invalid data format.

    Note:

    If using Java, DynamoDB lists the cancellation reasons on the `CancellationReasons`
    property. This property is not set for other languages. Transaction cancellation
    reasons are ordered in the order of requested items, if an item has no error it will
    have `None` code and `Null` message.

    Cancellation reason codes and possible error messages:

    - No Errors:

      - Code: `None`
      - Message: `null`

    - Conditional Check Failed:

      - Code: `ConditionalCheckFailed`
      - Message: The conditional request failed.

    - Item Collection Size Limit Exceeded:

      - Code: `ItemCollectionSizeLimitExceeded`
      - Message: Collection size exceeded.

    - Transaction Conflict:

      - Code: `TransactionConflict`
      - Message: Transaction is ongoing for the item.

    - Provisioned Throughput Exceeded:

      - Code: `ProvisionedThroughputExceeded`
      - Messages:

        - The level of configured provisioned throughput for the table was exceeded.
          Consider increasing your provisioning level with the UpdateTable API.

    Note: This Message is received when provisioned throughput is exceeded is on a
    provisioned DynamoDB table.

        - The level of configured provisioned throughput for one or more global
          secondary indexes of the table was exceeded. Consider increasing your
          provisioning level for the under-provisioned global secondary indexes with the
          UpdateTable API.

    Note: This message is returned when provisioned throughput is exceeded is on a
    provisioned GSI.

    - Throttling Error:

      - Code: `ThrottlingError`
      - Messages:

        - Throughput exceeds the current capacity of your table or index. DynamoDB is
          automatically scaling your table or index so please try again shortly. If
          exceptions persist, check if you have a hot key:
          https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-partition-
          key-design.html.

    Note: This message is returned when writes get throttled on an On-Demand table as
    DynamoDB is automatically scaling the table.

        - Throughput exceeds the current capacity for one or more global secondary
          indexes. DynamoDB is automatically scaling your index so please try again
          shortly.

    Note: This message is returned when writes get throttled on an On-Demand GSI as
    DynamoDB is automatically scaling the GSI.

    - Validation Error:

      - Code: `ValidationError`
      - Messages:

        - One or more parameter values were invalid.
        - The update expression attempted to update the secondary index key beyond
          allowed size limits.
        - The update expression attempted to update the secondary index key to
          unsupported type.
        - An operand in the update expression has an incorrect data type.
        - Item size to update has exceeded the maximum allowed size.
        - Number overflow. Attempting to store a number with magnitude larger than
          supported range.
        - Type mismatch for attribute to update.
        - Nesting Levels have exceeded supported limits.
        - The document path provided in the update expression is invalid for update.
        - The provided expression refers to an attribute that does not exist in the
          item.
    """

    _ERROR_CODE = "TransactionCanceledException"

    @property
    def cancellation_reasons(self) -> list[Any] | None:
        """A list of cancellation reasons."""
        return self.response.get("CancellationReasons")


class TransactionConflictException(DynamoDBError):
    """Operation was rejected because there is an ongoing transaction for the item."""
    _ERROR_CODE = "TransactionConflictException"


class TransactionInProgressException(DynamoDBError):
    """The transaction with the given request token is already in progress.

     Recommended Settings

    Note:

     This is a general recommendation for handling the `TransactionInProgressException`.
    These settings help ensure that the client retries will trigger completion of the
    ongoing `TransactWriteItems` request.

    - Set `clientExecutionTimeout` to a value that allows at least one retry to be
      processed after 5 seconds have elapsed since the first attempt for the
      `TransactWriteItems` operation.
    - Set `socketTimeout` to a value a little lower than the `requestTimeout` setting.
    - `requestTimeout` should be set based on the time taken for the individual retries
      of a single HTTP request for your use case, but setting it to 1 second or higher
      should work well to reduce chances of retries and `TransactionInProgressException`
      errors.
    - Use exponential backoff when retrying and tune backoff if needed.

     Assuming default retry policy, example timeout settings based on the guidelines
    above are as follows:

    Example timeline:

    - 0-1000 first attempt
    - 1000-1500 first sleep/delay (default retry policy uses 500 ms as base delay for
      4xx errors)
    - 1500-2500 second attempt
    - 2500-3500 second sleep/delay (500 * 2, exponential backoff)
    - 3500-4500 third attempt
    - 4500-6500 third sleep/delay (500 * 2^2)
    - 6500-7500 fourth attempt (this can trigger inline recovery since 5 seconds have
      elapsed since the first attempt reached TC)
    """

    _ERROR_CODE = "TransactionInProgressException"


EXCEPTIONS: dict[str, type[DynamoDBError]] = {
    "BackupInUseException": BackupInUseException,
    "BackupNotFoundException": BackupNotFoundException,
    "ConditionalCheckFailedException": ConditionalCheckFailedException,
    "ContinuousBackupsUnavailableException": ContinuousBackupsUnavailableException,
    "DuplicateItemException": DuplicateItemException,
    "ExportConflictException": ExportConflictException,
    "ExportNotFoundException": ExportNotFoundException,
    "GlobalTableAlreadyExistsException": GlobalTableAlreadyExistsException,
    "GlobalTableNotFoundException": GlobalTableNotFoundException,
    "IdempotentParameterMismatchException": IdempotentParameterMismatchException,
    "ImportConflictException": ImportConflictException,
    "ImportNotFoundException": ImportNotFoundException,
    "IndexNotFoundException": IndexNotFoundException,
    "InternalServerError": InternalServerError,
    "InvalidExportTimeException": InvalidExportTimeException,
    "InvalidRestoreTimeException": InvalidRestoreTimeException,
    "ItemCollectionSizeLimitExceededException": ItemCollectionSizeLimitExceededException,
    "LimitExceededException": LimitExceededException,
    "PointInTimeRecoveryUnavailableException": PointInTimeRecoveryUnavailableException,
    "ProvisionedThroughputExceededException": ProvisionedThroughputExceededException,
    "ReplicaAlreadyExistsException": ReplicaAlreadyExistsException,
    "ReplicaNotFoundException": ReplicaNotFoundException,
    "RequestLimitExceeded": RequestLimitExceeded,
    "ResourceInUseException": ResourceInUseException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "TableAlreadyExistsException": TableAlreadyExistsException,
    "TableInUseException": TableInUseException,
    "TableNotFoundException": TableNotFoundException,
    "TransactionCanceledException": TransactionCanceledException,
    "TransactionConflictException": TransactionConflictException,
    "TransactionInProgressException": TransactionInProgressException,
}
