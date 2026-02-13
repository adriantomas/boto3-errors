# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class MediaStoreDataError(Boto3Error):
    _SERVICE = "mediastore-data"


class ContainerNotFoundException(MediaStoreDataError):
    """The specified container was not found for the specified account."""
    _ERROR_CODE = "ContainerNotFoundException"


class InternalServerError(MediaStoreDataError):
    """The service is temporarily unavailable."""
    _ERROR_CODE = "InternalServerError"


class ObjectNotFoundException(MediaStoreDataError):
    """Could not perform an operation on an object that does not exist."""
    _ERROR_CODE = "ObjectNotFoundException"


class RequestedRangeNotSatisfiableException(MediaStoreDataError):
    """The requested content range is not valid."""
    _ERROR_CODE = "RequestedRangeNotSatisfiableException"


EXCEPTIONS: dict[str, type[MediaStoreDataError]] = {
    "ContainerNotFoundException": ContainerNotFoundException,
    "InternalServerError": InternalServerError,
    "ObjectNotFoundException": ObjectNotFoundException,
    "RequestedRangeNotSatisfiableException": RequestedRangeNotSatisfiableException,
}
