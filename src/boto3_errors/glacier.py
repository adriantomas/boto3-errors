# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class GlacierError(Boto3Error):
    _SERVICE = "glacier"


class InsufficientCapacityException(GlacierError):
    """Returned if there is insufficient capacity to process this expedited request. This
    error only applies to expedited retrievals and not to standard or bulk retrievals.
    """

    _ERROR_CODE = "InsufficientCapacityException"

    @property
    def type(self) -> str | None:
        return self.response.get("type")

    @property
    def code(self) -> str | None:
        return self.response.get("code")


class InvalidParameterValueException(GlacierError):
    """Returned if a parameter of the request is incorrectly specified."""
    _ERROR_CODE = "InvalidParameterValueException"

    @property
    def type(self) -> str | None:
        """Client"""
        return self.response.get("type")

    @property
    def code(self) -> str | None:
        """400 Bad Request"""
        return self.response.get("code")


class LimitExceededException(GlacierError):
    """Returned if the request results in a vault or account limit being exceeded."""
    _ERROR_CODE = "LimitExceededException"

    @property
    def type(self) -> str | None:
        """Client"""
        return self.response.get("type")

    @property
    def code(self) -> str | None:
        """400 Bad Request"""
        return self.response.get("code")


class MissingParameterValueException(GlacierError):
    """Returned if a required header or parameter is missing from the request."""
    _ERROR_CODE = "MissingParameterValueException"

    @property
    def type(self) -> str | None:
        """Client."""
        return self.response.get("type")

    @property
    def code(self) -> str | None:
        """400 Bad Request"""
        return self.response.get("code")


class NoLongerSupportedException(GlacierError):
    """Returned if the request was made by a customer with no Amazon Glacier storage. The
    request is denied as the API is no longer supported for new customers. Please use
    Amazon S3 Glacier storage classes instead.
    """

    _ERROR_CODE = "NoLongerSupportedException"

    @property
    def type(self) -> str | None:
        """Client"""
        return self.response.get("type")

    @property
    def code(self) -> str | None:
        """400 Bad Request"""
        return self.response.get("code")


class PolicyEnforcedException(GlacierError):
    """Returned if a retrieval job would exceed the current data policy's retrieval rate
    limit. For more information about data retrieval policies,
    """

    _ERROR_CODE = "PolicyEnforcedException"

    @property
    def type(self) -> str | None:
        """Client"""
        return self.response.get("type")

    @property
    def code(self) -> str | None:
        """PolicyEnforcedException"""
        return self.response.get("code")


class RequestTimeoutException(GlacierError):
    """Returned if, when uploading an archive, Amazon Glacier times out while receiving the
    upload.
    """

    _ERROR_CODE = "RequestTimeoutException"

    @property
    def type(self) -> str | None:
        """Client"""
        return self.response.get("type")

    @property
    def code(self) -> str | None:
        """408 Request Timeout"""
        return self.response.get("code")


class ResourceNotFoundException(GlacierError):
    """Returned if the specified resource (such as a vault, upload ID, or job ID) doesn't
    exist.
    """

    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def type(self) -> str | None:
        """Client"""
        return self.response.get("type")

    @property
    def code(self) -> str | None:
        """404 Not Found"""
        return self.response.get("code")


class ServiceUnavailableException(GlacierError):
    """Returned if the service cannot complete the request."""
    _ERROR_CODE = "ServiceUnavailableException"

    @property
    def type(self) -> str | None:
        """Server"""
        return self.response.get("type")

    @property
    def code(self) -> str | None:
        """500 Internal Server Error"""
        return self.response.get("code")


EXCEPTIONS: dict[str, type[GlacierError]] = {
    "InsufficientCapacityException": InsufficientCapacityException,
    "InvalidParameterValueException": InvalidParameterValueException,
    "LimitExceededException": LimitExceededException,
    "MissingParameterValueException": MissingParameterValueException,
    "NoLongerSupportedException": NoLongerSupportedException,
    "PolicyEnforcedException": PolicyEnforcedException,
    "RequestTimeoutException": RequestTimeoutException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceUnavailableException": ServiceUnavailableException,
}
