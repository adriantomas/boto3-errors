from __future__ import annotations

from boto3_errors._base import Boto3Error
from boto3_errors.dynamodb import (
    ConditionalCheckFailedException,
    DynamoDBError,
    RequestLimitExceeded,
    TransactionCanceledException,
)


def _make_response(code: str, extra: dict | None = None) -> dict:
    resp = {
        "Error": {"Code": code, "Message": "test"},
        "ResponseMetadata": {"RequestId": "r-1", "HTTPStatusCode": 400},
    }
    if extra:
        resp.update(extra)
    return resp


class TestConditionalCheckFailed:
    def test_hierarchy(self) -> None:
        assert issubclass(ConditionalCheckFailedException, DynamoDBError)
        assert issubclass(ConditionalCheckFailedException, Boto3Error)

    def test_error_code(self) -> None:
        assert (
            ConditionalCheckFailedException._ERROR_CODE
            == "ConditionalCheckFailedException"
        )

    def test_item_property(self) -> None:
        item = {"pk": {"S": "1"}}
        exc = ConditionalCheckFailedException(
            _make_response("ConditionalCheckFailedException", {"Item": item}),
            "PutItem",
        )
        assert exc.item == item

    def test_item_missing(self) -> None:
        exc = ConditionalCheckFailedException(
            _make_response("ConditionalCheckFailedException"),
            "PutItem",
        )
        assert exc.item is None


class TestTransactionCanceled:
    def test_cancellation_reasons_property(self) -> None:
        reasons = [{"Code": "ConditionalCheckFailed", "Message": "failed"}]
        exc = TransactionCanceledException(
            _make_response(
                "TransactionCanceledException", {"CancellationReasons": reasons}
            ),
            "TransactWriteItems",
        )
        assert exc.cancellation_reasons == reasons

    def test_cancellation_reasons_missing(self) -> None:
        exc = TransactionCanceledException(
            _make_response("TransactionCanceledException"),
            "TransactWriteItems",
        )
        assert exc.cancellation_reasons is None

    def test_service_marker(self) -> None:
        assert DynamoDBError._SERVICE == "dynamodb"


class TestThrottlingReasons:
    def test_throttling_reasons_present(self) -> None:
        reasons = [{"Code": "SUBSCRIBER_LIMIT_EXCEEDED", "Message": "rate limit"}]
        exc = RequestLimitExceeded(
            _make_response("RequestLimitExceeded", {"ThrottlingReasons": reasons}),
            "Query",
        )
        assert exc.throttling_reasons == reasons

    def test_throttling_reasons_missing(self) -> None:
        exc = RequestLimitExceeded(
            _make_response("RequestLimitExceeded"),
            "Query",
        )
        assert exc.throttling_reasons is None
