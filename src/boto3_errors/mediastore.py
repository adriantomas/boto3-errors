# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class MediaStoreError(Boto3Error):
    _SERVICE = "mediastore"


class ContainerInUseException(MediaStoreError):
    """The container that you specified in the request already exists or is being updated."""
    _ERROR_CODE = "ContainerInUseException"


class ContainerNotFoundException(MediaStoreError):
    """The container that you specified in the request does not exist."""
    _ERROR_CODE = "ContainerNotFoundException"


class CorsPolicyNotFoundException(MediaStoreError):
    """The CORS policy that you specified in the request does not exist."""
    _ERROR_CODE = "CorsPolicyNotFoundException"


class InternalServerError(MediaStoreError):
    """The service is temporarily unavailable."""
    _ERROR_CODE = "InternalServerError"


class LimitExceededException(MediaStoreError):
    """A service limit has been exceeded."""
    _ERROR_CODE = "LimitExceededException"


class PolicyNotFoundException(MediaStoreError):
    """The policy that you specified in the request does not exist."""
    _ERROR_CODE = "PolicyNotFoundException"


EXCEPTIONS: dict[str, type[MediaStoreError]] = {
    "ContainerInUseException": ContainerInUseException,
    "ContainerNotFoundException": ContainerNotFoundException,
    "CorsPolicyNotFoundException": CorsPolicyNotFoundException,
    "InternalServerError": InternalServerError,
    "LimitExceededException": LimitExceededException,
    "PolicyNotFoundException": PolicyNotFoundException,
}
