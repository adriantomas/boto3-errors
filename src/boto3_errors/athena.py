# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class AthenaError(Boto3Error):
    _SERVICE = "athena"


class InternalServerException(AthenaError):
    """Indicates a platform issue, which may be due to a transient condition or outage."""
    _ERROR_CODE = "InternalServerException"


class InvalidRequestException(AthenaError):
    """Indicates that something is wrong with the input to the request. For example, a
    required parameter may be missing or out of range.
    """

    _ERROR_CODE = "InvalidRequestException"

    @property
    def athena_error_code(self) -> str | None:
        return self.response.get("AthenaErrorCode")


class MetadataException(AthenaError):
    """An exception that Athena received when it called a custom metastore. Occurs if the
    error is not caused by user input (`InvalidRequestException`) or from the Athena
    platform (`InternalServerException`). For example, if a user-created Lambda function
    is missing permissions, the Lambda `4XX` exception is returned in a
    `MetadataException`.
    """

    _ERROR_CODE = "MetadataException"


class ResourceNotFoundException(AthenaError):
    """A resource, such as a workgroup, was not found."""
    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def resource_name(self) -> str | None:
        """The name of the Amazon resource."""
        return self.response.get("ResourceName")


class SessionAlreadyExistsException(AthenaError):
    """The specified session already exists."""
    _ERROR_CODE = "SessionAlreadyExistsException"


class TooManyRequestsException(AthenaError):
    """Indicates that the request was throttled."""
    _ERROR_CODE = "TooManyRequestsException"

    @property
    def reason(self) -> str | None:
        return self.response.get("Reason")


EXCEPTIONS: dict[str, type[AthenaError]] = {
    "InternalServerException": InternalServerException,
    "InvalidRequestException": InvalidRequestException,
    "MetadataException": MetadataException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "SessionAlreadyExistsException": SessionAlreadyExistsException,
    "TooManyRequestsException": TooManyRequestsException,
}
