# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class FMSError(Boto3Error):
    _SERVICE = "fms"


class InternalErrorException(FMSError):
    """The operation failed because of a system problem, even though the request was valid.
    Retry your request.
    """

    _ERROR_CODE = "InternalErrorException"


class InvalidInputException(FMSError):
    """The parameters of the request were invalid."""
    _ERROR_CODE = "InvalidInputException"


class InvalidOperationException(FMSError):
    """The operation failed because there was nothing to do or the operation wasn't
    possible. For example, you might have submitted an `AssociateAdminAccount` request
    for an account ID that was already set as the Firewall Manager administrator. Or you
    might have tried to access a Region that's disabled by default, and that you need to
    enable for the Firewall Manager administrator account and for Organizations before
    you can access it.
    """

    _ERROR_CODE = "InvalidOperationException"


class InvalidTypeException(FMSError):
    """The value of the `Type` parameter is invalid."""
    _ERROR_CODE = "InvalidTypeException"


class LimitExceededException(FMSError):
    """The operation exceeds a resource limit, for example, the maximum number of `policy`
    objects that you can create for an Amazon Web Services account. For more
    information, see Firewall Manager Limits in the WAF Developer Guide.
    """

    _ERROR_CODE = "LimitExceededException"


class ResourceNotFoundException(FMSError):
    """The specified resource was not found."""
    _ERROR_CODE = "ResourceNotFoundException"


EXCEPTIONS: dict[str, type[FMSError]] = {
    "InternalErrorException": InternalErrorException,
    "InvalidInputException": InvalidInputException,
    "InvalidOperationException": InvalidOperationException,
    "InvalidTypeException": InvalidTypeException,
    "LimitExceededException": LimitExceededException,
    "ResourceNotFoundException": ResourceNotFoundException,
}
