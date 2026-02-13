# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class EventBridgeError(Boto3Error):
    _SERVICE = "events"


class AccessDeniedException(EventBridgeError):
    """You do not have the necessary permissions for this action."""
    _ERROR_CODE = "AccessDeniedException"


class ConcurrentModificationException(EventBridgeError):
    """There is concurrent modification on a rule, target, archive, or replay."""
    _ERROR_CODE = "ConcurrentModificationException"


class IllegalStatusException(EventBridgeError):
    """An error occurred because a replay can be canceled only when the state is Running or
    Starting.
    """

    _ERROR_CODE = "IllegalStatusException"


class InternalException(EventBridgeError):
    """This exception occurs due to unexpected causes."""
    _ERROR_CODE = "InternalException"


class InvalidEventPatternException(EventBridgeError):
    """The event pattern is not valid."""
    _ERROR_CODE = "InvalidEventPatternException"


class InvalidStateException(EventBridgeError):
    """The specified state is not a valid state for an event source."""
    _ERROR_CODE = "InvalidStateException"


class LimitExceededException(EventBridgeError):
    """The request failed because it attempted to create resource beyond the allowed
    service quota.
    """

    _ERROR_CODE = "LimitExceededException"


class ManagedRuleException(EventBridgeError):
    """This rule was created by an Amazon Web Services service on behalf of your account.
    It is managed by that service. If you see this error in response to `DeleteRule` or
    `RemoveTargets`, you can use the `Force` parameter in those calls to delete the rule
    or remove targets from the rule. You cannot modify these managed rules by using
    `DisableRule`, `EnableRule`, `PutTargets`, `PutRule`, `TagResource`, or
    `UntagResource`.
    """

    _ERROR_CODE = "ManagedRuleException"


class OperationDisabledException(EventBridgeError):
    """The operation you are attempting is not available in this region."""
    _ERROR_CODE = "OperationDisabledException"


class PolicyLengthExceededException(EventBridgeError):
    """The event bus policy is too long. For more information, see the limits."""
    _ERROR_CODE = "PolicyLengthExceededException"


class ResourceAlreadyExistsException(EventBridgeError):
    """The resource you are trying to create already exists."""
    _ERROR_CODE = "ResourceAlreadyExistsException"


class ResourceNotFoundException(EventBridgeError):
    """An entity that you specified does not exist."""
    _ERROR_CODE = "ResourceNotFoundException"


class ThrottlingException(EventBridgeError):
    """This request cannot be completed due to throttling issues."""
    _ERROR_CODE = "ThrottlingException"


EXCEPTIONS: dict[str, type[EventBridgeError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConcurrentModificationException": ConcurrentModificationException,
    "IllegalStatusException": IllegalStatusException,
    "InternalException": InternalException,
    "InvalidEventPatternException": InvalidEventPatternException,
    "InvalidStateException": InvalidStateException,
    "LimitExceededException": LimitExceededException,
    "ManagedRuleException": ManagedRuleException,
    "OperationDisabledException": OperationDisabledException,
    "PolicyLengthExceededException": PolicyLengthExceededException,
    "ResourceAlreadyExistsException": ResourceAlreadyExistsException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ThrottlingException": ThrottlingException,
}
