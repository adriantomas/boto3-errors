from __future__ import annotations

from typing import Any

from botocore.exceptions import ClientError


class Boto3Error(ClientError):
    """Base class for all typed boto3 exceptions.

    Inherits from ClientError so existing ``except ClientError`` handlers
    still catch these exceptions.
    """

    _SERVICE: str = ""
    _ERROR_CODE: str = ""

    # Widen from botocore-stubs' TypedDict so that generated properties
    # can ``self.response.get("SomeField")`` without returning ``object``.
    response: dict[str, Any]  # type: ignore[assignment]

    @property
    def message(self) -> str:
        """Human-readable error message from the ``Error.Message`` field."""
        return self.response.get("Error", {}).get("Message", "")  # type: ignore[no-any-return]

    @property
    def error_code(self) -> str:
        """AWS error code from the ``Error.Code`` field."""
        return self.response.get("Error", {}).get("Code", "")  # type: ignore[no-any-return]

    @property
    def http_status_code(self) -> int:
        """HTTP status code from ``ResponseMetadata``."""
        return self.response.get("ResponseMetadata", {}).get("HTTPStatusCode", 0)  # type: ignore[no-any-return]

    @property
    def request_id(self) -> str:
        """AWS request ID from ``ResponseMetadata``."""
        return self.response.get("ResponseMetadata", {}).get("RequestId", "")  # type: ignore[no-any-return]
