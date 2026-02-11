from __future__ import annotations

from botocore.exceptions import ClientError

from boto3_errors._base import Boto3Error

MOCK_RESPONSE = {
    "Error": {
        "Code": "SomeError",
        "Message": "Something went wrong",
    },
    "ResponseMetadata": {
        "RequestId": "abc-123",
        "HTTPStatusCode": 400,
    },
}


def _make_error(response: dict | None = None) -> Boto3Error:
    return Boto3Error(response or MOCK_RESPONSE, "PutItem")


class TestBoto3ErrorProperties:
    def test_message(self) -> None:
        assert _make_error().message == "Something went wrong"

    def test_error_code(self) -> None:
        assert _make_error().error_code == "SomeError"

    def test_http_status_code(self) -> None:
        assert _make_error().http_status_code == 400  # noqa: PLR2004

    def test_request_id(self) -> None:
        assert _make_error().request_id == "abc-123"

    def test_operation_name(self) -> None:
        assert _make_error().operation_name == "PutItem"

    def test_isinstance_client_error(self) -> None:
        assert isinstance(_make_error(), ClientError)

    def test_missing_metadata_defaults(self) -> None:
        err = _make_error({"Error": {"Code": "X", "Message": "x"}})
        assert err.http_status_code == 0
        assert err.request_id == ""
