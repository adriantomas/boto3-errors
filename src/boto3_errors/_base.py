from botocore.exceptions import ClientError


class Boto3Error(ClientError):
    """Base class for all typed boto3 exceptions.

    Inherits from ClientError so existing ``except ClientError`` handlers
    still catch these exceptions.
    """

    _SERVICE: str = ""
    _ERROR_CODE: str = ""

    @property
    def message(self) -> str:
        """Human-readable error message from the ``Error.Message`` field."""
        return self.response["Error"]["Message"]

    @property
    def error_code(self) -> str:
        """AWS error code from the ``Error.Code`` field."""
        return self.response["Error"]["Code"]

    @property
    def http_status_code(self) -> int | None:
        """HTTP status code from ``ResponseMetadata``."""
        try:
            return self.response["ResponseMetadata"]["HTTPStatusCode"]
        except KeyError:
            return None

    @property
    def request_id(self) -> str | None:
        """AWS request ID from ``ResponseMetadata``."""
        try:
            return self.response["ResponseMetadata"]["RequestId"]
        except KeyError:
            return None
