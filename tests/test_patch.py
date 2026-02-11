from __future__ import annotations

from typing import Any
from unittest.mock import MagicMock

import pytest
from botocore.exceptions import ClientError

from boto3_errors._base import Boto3Error
from boto3_errors._patch import patch_client


def _make_client(service: str, error_code: str | None = None) -> MagicMock:
    """Create a mock boto3 client that raises ClientError on _make_api_call."""
    client = MagicMock()
    client._service_model.service_name = service
    client._boto3_errors_patched = False

    if error_code is not None:
        response = {
            "Error": {"Code": error_code, "Message": "Boom"},
            "ResponseMetadata": {"RequestId": "req-1", "HTTPStatusCode": 400},
        }

        def side_effect(op: str, params: dict[str, Any]) -> dict[str, Any]:  # noqa: ARG001
            raise ClientError(response, op)

        client._make_api_call = MagicMock(side_effect=side_effect)
    else:
        client._make_api_call = MagicMock(return_value={"ok": True})

    return client


class TestPatchClient:
    def test_reraises_as_typed_exception(self) -> None:
        from boto3_errors.dynamodb import (  # noqa: PLC0415
            ConditionalCheckFailedException,
        )

        client = _make_client("dynamodb", "ConditionalCheckFailedException")
        patch_client(client)

        with pytest.raises(ConditionalCheckFailedException) as exc_info:
            client._make_api_call("PutItem", {})

        assert exc_info.value.message == "Boom"
        assert isinstance(exc_info.value, ClientError)

    def test_unknown_code_reraises_original(self) -> None:
        client = _make_client("dynamodb", "SomeUnknownError")
        patch_client(client)

        with pytest.raises(ClientError) as exc_info:
            client._make_api_call("PutItem", {})

        assert not isinstance(exc_info.value, Boto3Error)

    def test_no_error_passes_through(self) -> None:
        client = _make_client("dynamodb")
        patch_client(client)

        result = client._make_api_call("GetItem", {})
        assert result == {"ok": True}

    def test_idempotent(self) -> None:
        client = _make_client("dynamodb")
        patch_client(client)
        first_call = client._make_api_call
        patch_client(client)
        assert client._make_api_call is first_call

    def test_unknown_service_is_noop(self) -> None:
        client = _make_client("no_such_service_xyz")
        patch_client(client)
        # Should not raise, and _make_api_call is unchanged
        result = client._make_api_call("Op", {})
        assert result == {"ok": True}

    def test_error_code_override(self) -> None:
        """IAM ConcurrentModification error code override."""
        from boto3_errors.iam import ConcurrentModificationException  # noqa: PLC0415

        client = _make_client("iam", "ConcurrentModification")
        patch_client(client)

        with pytest.raises(ConcurrentModificationException):
            client._make_api_call("UpdateRole", {})

    def test_lambda_module_name(self) -> None:
        """Service 'lambda' maps to module 'lambda_'."""
        from boto3_errors.lambda_ import ResourceNotFoundException  # noqa: PLC0415

        client = _make_client("lambda", "ResourceNotFoundException")
        patch_client(client)

        with pytest.raises(ResourceNotFoundException):
            client._make_api_call("GetFunction", {})
