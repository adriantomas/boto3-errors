# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class EventBridgeV2Error(Boto3Error):
    _SERVICE = "eventbridgev2"


class AccessDeniedException(EventBridgeV2Error):
    """The caller does not have the permissions required to perform the operation. This
    error is also returned when the operation cannot use the AWS KMS key for the event
    bus.
    """

    _ERROR_CODE = "AccessDeniedException"


class ConcurrentModificationException(EventBridgeV2Error):
    """Another change to the resource is already in progress. Retry the request."""
    _ERROR_CODE = "ConcurrentModificationException"


class ConflictException(EventBridgeV2Error):
    """A client-supplied precondition (e.g. ExpectedRevisionId on a resource-policy write)
    did not match the current state of the resource. Retrying the same request will fail
    again; re-read the resource and re-evaluate before retrying.

    A conditional request is not retry-safe on its own. If an earlier attempt committed
    but its response never reached the caller, retrying fails with this error, which is
    indistinguishable from another writer having won. Compare the resource's current
    contents with what the request intended: a successful attempt stores a revision ID
    the caller never saw, so the revision alone cannot tell the two apart, but matching
    contents mean the change took effect.
    """

    _ERROR_CODE = "ConflictException"


class IdempotentParameterMismatchException(EventBridgeV2Error):
    """The request reuses the client token of an earlier request with different parameters.
    Use a new client token, or resend the earlier request unchanged.
    """

    _ERROR_CODE = "IdempotentParameterMismatchException"


class InternalException(EventBridgeV2Error):
    """The request failed because of an internal service error. Retry the request."""
    _ERROR_CODE = "InternalException"


class InvalidInputException(EventBridgeV2Error):
    """A request parameter is missing or not valid."""
    _ERROR_CODE = "InvalidInputException"


class InvalidStateException(EventBridgeV2Error):
    """The resource is not in a state that allows the operation. For example, an event bus
    that is still being created cannot accept events.
    """

    _ERROR_CODE = "InvalidStateException"


class LimitExceededException(EventBridgeV2Error):
    """The request would exceed a service quota for the account."""
    _ERROR_CODE = "LimitExceededException"


class PolicyLengthExceededException(EventBridgeV2Error):
    """The policy document is larger than the account's resource policy size quota, or
    larger than the service maximum.
    """

    _ERROR_CODE = "PolicyLengthExceededException"


class PublicPolicyException(EventBridgeV2Error):
    """The policy was rejected because it would grant public access to the event bus. A
    statement grants public access when its principal is a wildcard and no condition
    limits the callers to specific AWS accounts or principals. To fix it, replace the
    wildcard principal with specific principals, or add a condition that limits the
    callers to specific AWS accounts. Conditions on event content (events:source,
    events:detail-type, events:Metadata/*) do not identify the caller and do not make a
    wildcard principal non-public. Returned only for the "default" policy; the "AWS_RAM"
    policy is composed by AWS Resource Access Manager and never grants public access.
    """

    _ERROR_CODE = "PublicPolicyException"


class ResourceAlreadyExistsException(EventBridgeV2Error):
    """A resource with the same name already exists."""
    _ERROR_CODE = "ResourceAlreadyExistsException"


class ResourceInUseException(EventBridgeV2Error):
    """The resource is in use and cannot be deleted. For example, an event bus with
    subscribers or event sources cannot be deleted until they are deleted.
    """

    _ERROR_CODE = "ResourceInUseException"


class ResourceNotFoundException(EventBridgeV2Error):
    """The resource does not exist."""
    _ERROR_CODE = "ResourceNotFoundException"


class SchemaRegistryUnavailableException(EventBridgeV2Error):
    """The configured schema registry could not be reached. Retry the request."""
    _ERROR_CODE = "SchemaRegistryUnavailableException"


class ThrottlingException(EventBridgeV2Error):
    """The request was throttled because it exceeds a request rate limit. Retry the request
    with backoff.
    """

    _ERROR_CODE = "ThrottlingException"


EXCEPTIONS: dict[str, type[EventBridgeV2Error]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConcurrentModificationException": ConcurrentModificationException,
    "ConflictException": ConflictException,
    "IdempotentParameterMismatchException": IdempotentParameterMismatchException,
    "InternalException": InternalException,
    "InvalidInputException": InvalidInputException,
    "InvalidStateException": InvalidStateException,
    "LimitExceededException": LimitExceededException,
    "PolicyLengthExceededException": PolicyLengthExceededException,
    "PublicPolicyException": PublicPolicyException,
    "ResourceAlreadyExistsException": ResourceAlreadyExistsException,
    "ResourceInUseException": ResourceInUseException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "SchemaRegistryUnavailableException": SchemaRegistryUnavailableException,
    "ThrottlingException": ThrottlingException,
}
