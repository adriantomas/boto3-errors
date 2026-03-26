# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class uxcError(Boto3Error):
    _SERVICE = "uxc"


class AccessDeniedException(uxcError):
    """You don't have sufficient access to perform this operation. Verify that your IAM
    policy includes the required `uxc:` permissions for the operation that you are
    calling. For more information on IAM permissions, see Amazon Web Services managed
    policies for Amazon Web Services Management Console.
    """

    _ERROR_CODE = "AccessDeniedException"


class InternalServerException(uxcError):
    """The service encountered an internal error. Try your request again later."""
    _ERROR_CODE = "InternalServerException"


class ThrottlingException(uxcError):
    """The request was denied because of request throttling. Reduce the frequency of your
    requests.
    """

    _ERROR_CODE = "ThrottlingException"


class ValidationException(uxcError):
    """The input fails to satisfy the constraints specified by an Amazon Web Services
    service.
    """

    _ERROR_CODE = "ValidationException"

    @property
    def field_list(self) -> list[Any] | None:
        """The list of fields that are invalid."""
        return self.response.get("fieldList")


EXCEPTIONS: dict[str, type[uxcError]] = {
    "AccessDeniedException": AccessDeniedException,
    "InternalServerException": InternalServerException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
