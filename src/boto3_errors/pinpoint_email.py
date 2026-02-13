# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class PinpointEmailError(Boto3Error):
    _SERVICE = "pinpoint-email"


class AccountSuspendedException(PinpointEmailError):
    """The message can't be sent because the account's ability to send email has been
    permanently restricted.
    """

    _ERROR_CODE = "AccountSuspendedException"


class AlreadyExistsException(PinpointEmailError):
    """The resource specified in your request already exists."""
    _ERROR_CODE = "AlreadyExistsException"


class BadRequestException(PinpointEmailError):
    """The input you provided is invalid."""
    _ERROR_CODE = "BadRequestException"


class ConcurrentModificationException(PinpointEmailError):
    """The resource is being modified by another operation or thread."""
    _ERROR_CODE = "ConcurrentModificationException"


class LimitExceededException(PinpointEmailError):
    """There are too many instances of the specified resource type."""
    _ERROR_CODE = "LimitExceededException"


class MailFromDomainNotVerifiedException(PinpointEmailError):
    """The message can't be sent because the sending domain isn't verified."""
    _ERROR_CODE = "MailFromDomainNotVerifiedException"


class MessageRejected(PinpointEmailError):
    """The message can't be sent because it contains invalid content."""
    _ERROR_CODE = "MessageRejected"


class NotFoundException(PinpointEmailError):
    """The resource you attempted to access doesn't exist."""
    _ERROR_CODE = "NotFoundException"


class SendingPausedException(PinpointEmailError):
    """The message can't be sent because the account's ability to send email is currently
    paused.
    """

    _ERROR_CODE = "SendingPausedException"


class TooManyRequestsException(PinpointEmailError):
    """Too many requests have been made to the operation."""
    _ERROR_CODE = "TooManyRequestsException"


EXCEPTIONS: dict[str, type[PinpointEmailError]] = {
    "AccountSuspendedException": AccountSuspendedException,
    "AlreadyExistsException": AlreadyExistsException,
    "BadRequestException": BadRequestException,
    "ConcurrentModificationException": ConcurrentModificationException,
    "LimitExceededException": LimitExceededException,
    "MailFromDomainNotVerifiedException": MailFromDomainNotVerifiedException,
    "MessageRejected": MessageRejected,
    "NotFoundException": NotFoundException,
    "SendingPausedException": SendingPausedException,
    "TooManyRequestsException": TooManyRequestsException,
}
