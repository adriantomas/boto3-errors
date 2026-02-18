# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class RedshiftDataError(Boto3Error):
    _SERVICE = "redshift-data"


class ActiveSessionsExceededException(RedshiftDataError):
    """The Amazon Redshift Data API operation failed because the maximum number of active
    sessions exceeded.
    """

    _ERROR_CODE = "ActiveSessionsExceededException"


class ActiveStatementsExceededException(RedshiftDataError):
    """The number of active statements exceeds the limit."""
    _ERROR_CODE = "ActiveStatementsExceededException"


class BatchExecuteStatementException(RedshiftDataError):
    """An SQL statement encountered an environmental error while running."""
    _ERROR_CODE = "BatchExecuteStatementException"

    @property
    def statement_id(self) -> str | None:
        """Statement identifier of the exception."""
        return self.response.get("StatementId")


class DatabaseConnectionException(RedshiftDataError):
    """Connection to a database failed."""
    _ERROR_CODE = "DatabaseConnectionException"


class ExecuteStatementException(RedshiftDataError):
    """The SQL statement encountered an environmental error while running."""
    _ERROR_CODE = "ExecuteStatementException"

    @property
    def statement_id(self) -> str | None:
        """Statement identifier of the exception."""
        return self.response.get("StatementId")


class InternalServerException(RedshiftDataError):
    """The Amazon Redshift Data API operation failed due to invalid input."""
    _ERROR_CODE = "InternalServerException"


class QueryTimeoutException(RedshiftDataError):
    """The Amazon Redshift Data API operation failed due to timeout."""
    _ERROR_CODE = "QueryTimeoutException"


class ResourceNotFoundException(RedshiftDataError):
    """The Amazon Redshift Data API operation failed due to a missing resource."""
    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def resource_id(self) -> str | None:
        """Resource identifier associated with the exception."""
        return self.response.get("ResourceId")


class ValidationException(RedshiftDataError):
    """The Amazon Redshift Data API operation failed due to invalid input."""
    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[RedshiftDataError]] = {
    "ActiveSessionsExceededException": ActiveSessionsExceededException,
    "ActiveStatementsExceededException": ActiveStatementsExceededException,
    "BatchExecuteStatementException": BatchExecuteStatementException,
    "DatabaseConnectionException": DatabaseConnectionException,
    "ExecuteStatementException": ExecuteStatementException,
    "InternalServerException": InternalServerException,
    "QueryTimeoutException": QueryTimeoutException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ValidationException": ValidationException,
}
