# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class RDSDataError(Boto3Error):
    _SERVICE = "rds-data"


class AccessDeniedException(RDSDataError):
    """You don't have sufficient access to perform this action."""
    _ERROR_CODE = "AccessDeniedException"


class BadRequestException(RDSDataError):
    """There is an error in the call or in a SQL statement. (This error only appears in
    calls from Aurora Serverless v1 databases.)
    """

    _ERROR_CODE = "BadRequestException"


class DatabaseErrorException(RDSDataError):
    """There was an error in processing the SQL statement."""
    _ERROR_CODE = "DatabaseErrorException"


class DatabaseNotFoundException(RDSDataError):
    """The DB cluster doesn't have a DB instance."""
    _ERROR_CODE = "DatabaseNotFoundException"


class DatabaseResumingException(RDSDataError):
    """A request was cancelled because the Aurora Serverless v2 DB instance was paused. The
    Data API request automatically resumes the DB instance. Wait a few seconds and try
    again.
    """

    _ERROR_CODE = "DatabaseResumingException"


class DatabaseUnavailableException(RDSDataError):
    """The writer instance in the DB cluster isn't available."""
    _ERROR_CODE = "DatabaseUnavailableException"


class ForbiddenException(RDSDataError):
    """There are insufficient privileges to make the call."""
    _ERROR_CODE = "ForbiddenException"


class HttpEndpointNotEnabledException(RDSDataError):
    """The HTTP endpoint for using RDS Data API isn't enabled for the DB cluster."""
    _ERROR_CODE = "HttpEndpointNotEnabledException"


class InternalServerErrorException(RDSDataError):
    """An internal error occurred."""
    _ERROR_CODE = "InternalServerErrorException"


class InvalidResourceStateException(RDSDataError):
    """The resource is in an invalid state."""
    _ERROR_CODE = "InvalidResourceStateException"


class InvalidSecretException(RDSDataError):
    """The Secrets Manager secret used with the request isn't valid."""
    _ERROR_CODE = "InvalidSecretException"


class NotFoundException(RDSDataError):
    """The `resourceArn`, `secretArn`, or `transactionId` value can't be found."""
    _ERROR_CODE = "NotFoundException"


class SecretsErrorException(RDSDataError):
    """There was a problem with the Secrets Manager secret used with the request, caused by
    one of the following conditions:

    - RDS Data API timed out retrieving the secret.
    - The secret provided wasn't found.
    - The secret couldn't be decrypted.
    """

    _ERROR_CODE = "SecretsErrorException"


class ServiceUnavailableError(RDSDataError):
    """The service specified by the `resourceArn` parameter isn't available."""
    _ERROR_CODE = "ServiceUnavailableError"


class StatementTimeoutException(RDSDataError):
    """The execution of the SQL statement timed out."""
    _ERROR_CODE = "StatementTimeoutException"

    @property
    def db_connection_id(self) -> int | None:
        """The database connection ID that executed the SQL statement."""
        return self.response.get("dbConnectionId")


class TransactionNotFoundException(RDSDataError):
    """The transaction ID wasn't found."""
    _ERROR_CODE = "TransactionNotFoundException"


class UnsupportedResultException(RDSDataError):
    """There was a problem with the result because of one of the following conditions:

    - It contained an unsupported data type.
    - It contained a multidimensional array.
    - The size was too large.
    """

    _ERROR_CODE = "UnsupportedResultException"


EXCEPTIONS: dict[str, type[RDSDataError]] = {
    "AccessDeniedException": AccessDeniedException,
    "BadRequestException": BadRequestException,
    "DatabaseErrorException": DatabaseErrorException,
    "DatabaseNotFoundException": DatabaseNotFoundException,
    "DatabaseResumingException": DatabaseResumingException,
    "DatabaseUnavailableException": DatabaseUnavailableException,
    "ForbiddenException": ForbiddenException,
    "HttpEndpointNotEnabledException": HttpEndpointNotEnabledException,
    "InternalServerErrorException": InternalServerErrorException,
    "InvalidResourceStateException": InvalidResourceStateException,
    "InvalidSecretException": InvalidSecretException,
    "NotFoundException": NotFoundException,
    "SecretsErrorException": SecretsErrorException,
    "ServiceUnavailableError": ServiceUnavailableError,
    "StatementTimeoutException": StatementTimeoutException,
    "TransactionNotFoundException": TransactionNotFoundException,
    "UnsupportedResultException": UnsupportedResultException,
}
