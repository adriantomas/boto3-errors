# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class OpenSearchError(Boto3Error):
    _SERVICE = "opensearch"


class AccessDeniedException(OpenSearchError):
    """An error occurred because you don't have permissions to access the resource."""
    _ERROR_CODE = "AccessDeniedException"


class BaseException(OpenSearchError):
    """An error occurred while processing the request."""
    _ERROR_CODE = "BaseException"


class ConflictException(OpenSearchError):
    """An error occurred because the client attempts to remove a resource that is currently
    in use.
    """

    _ERROR_CODE = "ConflictException"


class DependencyFailureException(OpenSearchError):
    """An exception for when a failure in one of the dependencies results in the service
    being unable to fetch details about the resource.
    """

    _ERROR_CODE = "DependencyFailureException"


class DisabledOperationException(OpenSearchError):
    """An error occured because the client wanted to access an unsupported operation."""
    _ERROR_CODE = "DisabledOperationException"


class InternalException(OpenSearchError):
    """Request processing failed because of an unknown error, exception, or internal
    failure.
    """

    _ERROR_CODE = "InternalException"


class InvalidPaginationTokenException(OpenSearchError):
    """Request processing failed because you provided an invalid pagination token."""
    _ERROR_CODE = "InvalidPaginationTokenException"


class InvalidTypeException(OpenSearchError):
    """An exception for trying to create or access a sub-resource that's either invalid or
    not supported.
    """

    _ERROR_CODE = "InvalidTypeException"


class LimitExceededException(OpenSearchError):
    """An exception for trying to create more than the allowed number of resources or sub-
    resources.
    """

    _ERROR_CODE = "LimitExceededException"


class ResourceAlreadyExistsException(OpenSearchError):
    """An exception for creating a resource that already exists."""
    _ERROR_CODE = "ResourceAlreadyExistsException"


class ResourceNotFoundException(OpenSearchError):
    """An exception for accessing or deleting a resource that doesn't exist."""
    _ERROR_CODE = "ResourceNotFoundException"


class SlotNotAvailableException(OpenSearchError):
    """An exception for attempting to schedule a domain action during an unavailable time
    slot.
    """

    _ERROR_CODE = "SlotNotAvailableException"

    @property
    def slot_suggestions(self) -> list[Any] | None:
        """Alternate time slots during which OpenSearch Service has available capacity to
        schedule a domain action.
        """
        return self.response.get("SlotSuggestions")


class ThrottlingException(OpenSearchError):
    """The request was denied due to request throttling. Reduce the frequency of your
    requests and try again.
    """

    _ERROR_CODE = "ThrottlingException"


class ValidationException(OpenSearchError):
    """An exception for accessing or deleting a resource that doesn't exist."""
    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[OpenSearchError]] = {
    "AccessDeniedException": AccessDeniedException,
    "BaseException": BaseException,
    "ConflictException": ConflictException,
    "DependencyFailureException": DependencyFailureException,
    "DisabledOperationException": DisabledOperationException,
    "InternalException": InternalException,
    "InvalidPaginationTokenException": InvalidPaginationTokenException,
    "InvalidTypeException": InvalidTypeException,
    "LimitExceededException": LimitExceededException,
    "ResourceAlreadyExistsException": ResourceAlreadyExistsException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "SlotNotAvailableException": SlotNotAvailableException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
