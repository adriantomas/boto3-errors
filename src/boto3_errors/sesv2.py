# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class SESv2Error(Boto3Error):
    _SERVICE = "sesv2"


class AccountSuspendedException(SESv2Error):
    """The message can't be sent because the account's ability to send email has been
    permanently restricted.
    """

    _ERROR_CODE = "AccountSuspendedException"


class AlreadyExistsException(SESv2Error):
    """The resource specified in your request already exists."""
    _ERROR_CODE = "AlreadyExistsException"


class BadRequestException(SESv2Error):
    """The input you provided is invalid."""
    _ERROR_CODE = "BadRequestException"


class ConcurrentModificationException(SESv2Error):
    """The resource is being modified by another operation or thread."""
    _ERROR_CODE = "ConcurrentModificationException"


class ConflictException(SESv2Error):
    """If there is already an ongoing account details update under review."""
    _ERROR_CODE = "ConflictException"


class InternalServiceErrorException(SESv2Error):
    """The request couldn't be processed because an error occurred with the Amazon SES API
    v2.
    """

    _ERROR_CODE = "InternalServiceErrorException"


class InvalidNextTokenException(SESv2Error):
    """The specified request includes an invalid or expired token."""
    _ERROR_CODE = "InvalidNextTokenException"


class LimitExceededException(SESv2Error):
    """There are too many instances of the specified resource type."""
    _ERROR_CODE = "LimitExceededException"


class MailFromDomainNotVerifiedException(SESv2Error):
    """The message can't be sent because the sending domain isn't verified."""
    _ERROR_CODE = "MailFromDomainNotVerifiedException"


class MessageRejected(SESv2Error):
    """The message can't be sent because it contains invalid content."""
    _ERROR_CODE = "MessageRejected"


class NotFoundException(SESv2Error):
    """The resource you attempted to access doesn't exist."""
    _ERROR_CODE = "NotFoundException"


class SendingPausedException(SESv2Error):
    """The message can't be sent because the account's ability to send email is currently
    paused.
    """

    _ERROR_CODE = "SendingPausedException"


class TooManyRequestsException(SESv2Error):
    """Too many requests have been made to the operation."""
    _ERROR_CODE = "TooManyRequestsException"


EXCEPTIONS: dict[str, type[SESv2Error]] = {
    "AccountSuspendedException": AccountSuspendedException,
    "AlreadyExistsException": AlreadyExistsException,
    "BadRequestException": BadRequestException,
    "ConcurrentModificationException": ConcurrentModificationException,
    "ConflictException": ConflictException,
    "InternalServiceErrorException": InternalServiceErrorException,
    "InvalidNextTokenException": InvalidNextTokenException,
    "LimitExceededException": LimitExceededException,
    "MailFromDomainNotVerifiedException": MailFromDomainNotVerifiedException,
    "MessageRejected": MessageRejected,
    "NotFoundException": NotFoundException,
    "SendingPausedException": SendingPausedException,
    "TooManyRequestsException": TooManyRequestsException,
}
