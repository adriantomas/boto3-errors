# (Better) boto3 errors

[![Python 3.10 | 3.11 | 3.12 | 3.13 | 3.14](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12%20%7C%203.13%20%7C%203.14-blue.svg)](https://www.python.org/downloads/)
[![PyPI](https://img.shields.io/pypi/v/boto3_errors.svg)](https://pypi.org/project/boto3_errors/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Typed, statically-importable exception classes for every AWS service.

## Install

```bash
pip install boto3-errors
```

## Quick start

```python
import boto3
from boto3_errors import patch_client
from boto3_errors.dynamodb import ConditionalCheckFailedException

client = boto3.client("dynamodb")
patch_client(client)

try:
    client.put_item(
        TableName="users",
        Item={"pk": {"S": "user#1"}, "name": {"S": "Ada"}},
        ConditionExpression="attribute_not_exists(pk)",
    )
except ConditionalCheckFailedException as e:
    print(e.message)  # "The conditional request failed"
    print(e.error_code)  # "ConditionalCheckFailedException"
    print(e.item)  # {"pk": {"S": "user#1"}, "name": {"S": "Ada"}}
```

## The problem

Every boto3 error comes back as a `ClientError`. The only way to distinguish them is by parsing `e.response["Error"]["Code"]` — a stringly-typed dict lookup with no autocomplete, no type checking, and no IDE support. One typo in the error code string and your handler silently misses the exception.

## What you get

### Coverage

All AWS services with exception classes auto-generated from botocore's service model. The package version is aligned with botocore (e.g. boto3-errors 1.42.44 is generated from botocore 1.42.44).

### Exception hierarchy

```text
ClientError                     # botocore base — still works
└── Boto3Error                  # boto3-errors base
    └── DynamoDBError           # per-service base
        ├── ConditionalCheckFailedException
        ├── ResourceNotFoundException
        ├── TransactionCanceledException
        └── ...
```

Every exception is a `ClientError` subclass, so existing `except ClientError` handlers keep working.

### Built-in properties

Every `Boto3Error` exposes:

| Property | Type | Source |
| ------------------ | ----- | ----------------------------------- |
| `message` | `str` | `Error.Message` |
| `error_code` | `str` | `Error.Code` |
| `http_status_code` | `int` | `ResponseMetadata.HTTPStatusCode` |
| `request_id` | `str` | `ResponseMetadata.RequestId` |

### Service-specific properties

Some exceptions expose extra fields from the API response:

```python
from boto3_errors.dynamodb import (
    ConditionalCheckFailedException,
    TransactionCanceledException,
)

# ConditionalCheckFailedException.item -> dict | None
# TransactionCanceledException.cancellation_reasons -> list | None
```

## Catching at multiple levels

```python
from botocore.exceptions import ClientError
from boto3_errors import Boto3Error
from boto3_errors.dynamodb import DynamoDBError, ResourceNotFoundException

try:
    client.delete_table(TableName="nope")
except ResourceNotFoundException:
    ...  # only this specific error
except DynamoDBError:
    ...  # any DynamoDB error
except Boto3Error:
    ...  # any error from a patched service
except ClientError:
    ...  # anything else from botocore
```
