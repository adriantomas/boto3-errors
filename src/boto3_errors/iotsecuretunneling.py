# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class IoTSecureTunnelingError(Boto3Error):
    _SERVICE = "iotsecuretunneling"


class LimitExceededException(IoTSecureTunnelingError):
    """Thrown when a tunnel limit is exceeded."""
    _ERROR_CODE = "LimitExceededException"


class ResourceNotFoundException(IoTSecureTunnelingError):
    """Thrown when an operation is attempted on a resource that does not exist."""
    _ERROR_CODE = "ResourceNotFoundException"


EXCEPTIONS: dict[str, type[IoTSecureTunnelingError]] = {
    "LimitExceededException": LimitExceededException,
    "ResourceNotFoundException": ResourceNotFoundException,
}
