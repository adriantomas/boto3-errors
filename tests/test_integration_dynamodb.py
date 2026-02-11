import uuid
from collections.abc import Generator

import boto3
import pytest
from botocore.client import BaseClient
from botocore.config import Config
from botocore.exceptions import ClientError
from testcontainers.core.container import DockerContainer
from testcontainers.core.wait_strategies import HttpWaitStrategy

from boto3_errors._base import Boto3Error
from boto3_errors._patch import patch_client
from boto3_errors.dynamodb import (
    ConditionalCheckFailedException,
    ResourceInUseException,
    ResourceNotFoundException,
    TransactionCanceledException,
)

pytestmark = pytest.mark.integration

FAKE_CREDENTIALS = "testing"

TABLE_DEF = {
    "KeySchema": [{"AttributeName": "pk", "KeyType": "HASH"}],
    "AttributeDefinitions": [{"AttributeName": "pk", "AttributeType": "S"}],
    "BillingMode": "PAY_PER_REQUEST",
}


@pytest.fixture(scope="module")
def dynamodb_container() -> Generator[DockerContainer, None, None]:
    """Start a local DynamoDB container for integration tests."""
    container = DockerContainer(
        "amazon/dynamodb-local:latest",
        command="-jar DynamoDBLocal.jar -inMemory -sharedDb",
        ports=[8000],
        _wait_strategy=HttpWaitStrategy(8000).for_status_code(400),
    )
    with container:
        yield container


@pytest.fixture(scope="module")
def dynamodb_client(
    dynamodb_container: DockerContainer,
) -> BaseClient:
    """Create a boto3 DynamoDB client pointing at the local container."""
    host = dynamodb_container.get_container_host_ip()
    port = dynamodb_container.get_exposed_port(8000)
    return boto3.client(
        "dynamodb",
        endpoint_url=f"http://{host}:{port}",
        region_name="us-east-1",
        aws_access_key_id=FAKE_CREDENTIALS,
        aws_secret_access_key=FAKE_CREDENTIALS,
        config=Config(retries={"max_attempts": 0}),
    )


@pytest.fixture(scope="module")
def patched_client(dynamodb_client: BaseClient) -> BaseClient:
    """Patch and return the DynamoDB client."""
    patch_client(dynamodb_client)
    return dynamodb_client


@pytest.fixture
def test_table(
    patched_client: BaseClient,
) -> Generator[str, None, None]:
    """Create a temporary DynamoDB table, yield its name, then delete it."""
    table_name = f"test-{uuid.uuid4().hex[:8]}"
    patched_client.create_table(TableName=table_name, **TABLE_DEF)
    yield table_name
    patched_client.delete_table(TableName=table_name)


class TestResourceNotFoundException:
    def test_describe_nonexistent_table(
        self,
        patched_client: BaseClient,
    ) -> None:
        with pytest.raises(ResourceNotFoundException) as exc_info:
            patched_client.describe_table(TableName="nonexistent")

        exc = exc_info.value
        assert exc.error_code == "ResourceNotFoundException"
        assert exc.http_status_code == 400  # noqa: PLR2004
        assert isinstance(exc, ClientError)


class TestConditionalCheckFailedException:
    def test_condition_expression_fails(
        self,
        patched_client: BaseClient,
        test_table: str,
    ) -> None:
        item = {"pk": {"S": "key1"}, "data": {"S": "hello"}}
        patched_client.put_item(TableName=test_table, Item=item)

        with pytest.raises(ConditionalCheckFailedException) as exc_info:
            patched_client.put_item(
                TableName=test_table,
                Item={"pk": {"S": "key1"}, "data": {"S": "world"}},
                ConditionExpression="attribute_not_exists(pk)",
                ReturnValuesOnConditionCheckFailure="ALL_OLD",
            )

        exc = exc_info.value
        assert exc.error_code == "ConditionalCheckFailedException"
        assert exc.item is not None
        assert exc.item["pk"]["S"] == "key1"


class TestTransactionCanceledException:
    def test_transact_write_with_failing_condition(
        self,
        patched_client: BaseClient,
        test_table: str,
    ) -> None:
        patched_client.put_item(
            TableName=test_table,
            Item={"pk": {"S": "txkey"}},
        )

        with pytest.raises(TransactionCanceledException) as exc_info:
            patched_client.transact_write_items(
                TransactItems=[
                    {
                        "Put": {
                            "TableName": test_table,
                            "Item": {"pk": {"S": "txkey"}, "v": {"S": "new"}},
                            "ConditionExpression": "attribute_not_exists(pk)",
                        }
                    }
                ]
            )

        exc = exc_info.value
        assert exc.error_code == "TransactionCanceledException"
        assert exc.cancellation_reasons is not None
        assert len(exc.cancellation_reasons) > 0


class TestResourceInUseException:
    def test_create_existing_table(
        self,
        patched_client: BaseClient,
        test_table: str,
    ) -> None:
        with pytest.raises(ResourceInUseException) as exc_info:
            patched_client.create_table(TableName=test_table, **TABLE_DEF)

        assert exc_info.value.error_code == "ResourceInUseException"


class TestValidationException:
    def test_malformed_update_expression_falls_through(
        self,
        patched_client: BaseClient,
        test_table: str,
    ) -> None:
        """ValidationException is not in the DynamoDB module.

        It falls through as a plain ClientError.
        """
        with pytest.raises(ClientError) as exc_info:
            patched_client.update_item(
                TableName=test_table,
                Key={"pk": {"S": "key1"}},
                UpdateExpression="INVALID EXPRESSION ~~~",
            )

        assert exc_info.value.response["Error"]["Code"] == "ValidationException"
        # Should be plain ClientError, not a typed subclass
        assert type(exc_info.value).__name__ == "ClientError"


class TestUnpatchedClientContrast:
    def test_unpatched_raises_plain_client_error(
        self,
        dynamodb_container: DockerContainer,
    ) -> None:
        host = dynamodb_container.get_container_host_ip()
        port = dynamodb_container.get_exposed_port(8000)
        unpatched = boto3.client(
            "dynamodb",
            endpoint_url=f"http://{host}:{port}",
            region_name="us-east-1",
            aws_access_key_id=FAKE_CREDENTIALS,
            aws_secret_access_key=FAKE_CREDENTIALS,
            config=Config(retries={"max_attempts": 0}),
        )

        with pytest.raises(ClientError) as exc_info:
            unpatched.describe_table(TableName="nonexistent")

        assert not isinstance(exc_info.value, Boto3Error)
