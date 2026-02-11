# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class SNSError(Boto3Error):
    _SERVICE = "sns"


class AuthorizationErrorException(SNSError):
    """Indicates that the user has been denied access to the requested resource."""
    _ERROR_CODE = "AuthorizationError"


class BatchEntryIdsNotDistinctException(SNSError):
    """Two or more batch entries in the request have the same `Id`."""
    _ERROR_CODE = "BatchEntryIdsNotDistinct"


class BatchRequestTooLongException(SNSError):
    """The length of all the batch messages put together is more than the limit."""
    _ERROR_CODE = "BatchRequestTooLong"


class ConcurrentAccessException(SNSError):
    """Can't perform multiple operations on a tag simultaneously. Perform the operations
    sequentially.
    """

    _ERROR_CODE = "ConcurrentAccess"


class EmptyBatchRequestException(SNSError):
    """The batch request doesn't contain any entries."""
    _ERROR_CODE = "EmptyBatchRequest"


class EndpointDisabledException(SNSError):
    """Exception error indicating endpoint disabled."""
    _ERROR_CODE = "EndpointDisabled"


class FilterPolicyLimitExceededException(SNSError):
    """Indicates that the number of filter polices in your Amazon Web Services account
    exceeds the limit. To add more filter polices, submit an Amazon SNS Limit Increase
    case in the Amazon Web ServicesSupport Center.
    """

    _ERROR_CODE = "FilterPolicyLimitExceeded"


class InternalErrorException(SNSError):
    """Indicates an internal service error."""
    _ERROR_CODE = "InternalError"


class InvalidBatchEntryIdException(SNSError):
    """The `Id` of a batch entry in a batch request doesn't abide by the specification."""
    _ERROR_CODE = "InvalidBatchEntryId"


class InvalidParameterException(SNSError):
    """Indicates that a request parameter does not comply with the associated constraints."""
    _ERROR_CODE = "InvalidParameter"


class InvalidParameterValueException(SNSError):
    """Indicates that a request parameter does not comply with the associated constraints."""
    _ERROR_CODE = "ParameterValueInvalid"


class InvalidSecurityException(SNSError):
    """The credential signature isn't valid. You must use an HTTPS endpoint and sign your
    request using Signature Version 4.
    """

    _ERROR_CODE = "InvalidSecurity"


class InvalidStateException(SNSError):
    """Indicates that the specified state is not a valid state for an event source."""
    _ERROR_CODE = "InvalidState"


class KMSAccessDeniedException(SNSError):
    """The ciphertext references a key that doesn't exist or that you don't have access to."""
    _ERROR_CODE = "KMSAccessDenied"


class KMSDisabledException(SNSError):
    """The request was rejected because the specified Amazon Web Services KMS key isn't
    enabled.
    """

    _ERROR_CODE = "KMSDisabled"


class KMSInvalidStateException(SNSError):
    """The request was rejected because the state of the specified resource isn't valid for
    this request. For more information, see Key states of Amazon Web Services KMS keys
    in the Key Management Service Developer Guide.
    """

    _ERROR_CODE = "KMSInvalidState"


class KMSNotFoundException(SNSError):
    """The request was rejected because the specified entity or resource can't be found."""
    _ERROR_CODE = "KMSNotFound"


class KMSOptInRequired(SNSError):
    """The Amazon Web Services access key ID needs a subscription for the service."""
    _ERROR_CODE = "KMSOptInRequired"


class KMSThrottlingException(SNSError):
    """The request was denied due to request throttling. For more information about
    throttling, see Limits in the Key Management Service Developer Guide.
    """

    _ERROR_CODE = "KMSThrottling"


class NotFoundException(SNSError):
    """Indicates that the requested resource does not exist."""
    _ERROR_CODE = "NotFound"


class OptedOutException(SNSError):
    """Indicates that the specified phone number opted out of receiving SMS messages from
    your Amazon Web Services account. You can't send SMS messages to phone numbers that
    opt out.
    """

    _ERROR_CODE = "OptedOut"


class PlatformApplicationDisabledException(SNSError):
    """Exception error indicating platform application disabled."""
    _ERROR_CODE = "PlatformApplicationDisabled"


class ReplayLimitExceededException(SNSError):
    """Indicates that the request parameter has exceeded the maximum number of concurrent
    message replays.
    """

    _ERROR_CODE = "ReplayLimitExceeded"


class ResourceNotFoundException(SNSError):
    """Can’t perform the action on the specified resource. Make sure that the resource
    exists.
    """

    _ERROR_CODE = "ResourceNotFound"


class StaleTagException(SNSError):
    """A tag has been added to a resource with the same ARN as a deleted resource. Wait a
    short while and then retry the operation.
    """

    _ERROR_CODE = "StaleTag"


class SubscriptionLimitExceededException(SNSError):
    """Indicates that the customer already owns the maximum allowed number of
    subscriptions.
    """

    _ERROR_CODE = "SubscriptionLimitExceeded"


class TagLimitExceededException(SNSError):
    """Can't add more than 50 tags to a topic."""
    _ERROR_CODE = "TagLimitExceeded"


class TagPolicyException(SNSError):
    """The request doesn't comply with the IAM tag policy. Correct your request and then
    retry it.
    """

    _ERROR_CODE = "TagPolicy"


class ThrottledException(SNSError):
    """Indicates that the rate at which requests have been submitted for this action
    exceeds the limit for your Amazon Web Services account.
    """

    _ERROR_CODE = "Throttled"


class TooManyEntriesInBatchRequestException(SNSError):
    """The batch request contains more entries than permissible (more than 10)."""
    _ERROR_CODE = "TooManyEntriesInBatchRequest"


class TopicLimitExceededException(SNSError):
    """Indicates that the customer already owns the maximum allowed number of topics."""
    _ERROR_CODE = "TopicLimitExceeded"


class UserErrorException(SNSError):
    """Indicates that a request parameter does not comply with the associated constraints."""
    _ERROR_CODE = "UserError"


class ValidationException(SNSError):
    """Indicates that a parameter in the request is invalid."""
    _ERROR_CODE = "ValidationException"


class VerificationException(SNSError):
    """Indicates that the one-time password (OTP) used for verification is invalid."""
    _ERROR_CODE = "VerificationException"

    @property
    def status(self) -> str | None:
        """The status of the verification error."""
        return self.response.get("Status")


EXCEPTIONS: dict[str, type[SNSError]] = {
    "AuthorizationError": AuthorizationErrorException,
    "BatchEntryIdsNotDistinct": BatchEntryIdsNotDistinctException,
    "BatchRequestTooLong": BatchRequestTooLongException,
    "ConcurrentAccess": ConcurrentAccessException,
    "EmptyBatchRequest": EmptyBatchRequestException,
    "EndpointDisabled": EndpointDisabledException,
    "FilterPolicyLimitExceeded": FilterPolicyLimitExceededException,
    "InternalError": InternalErrorException,
    "InvalidBatchEntryId": InvalidBatchEntryIdException,
    "InvalidParameter": InvalidParameterException,
    "ParameterValueInvalid": InvalidParameterValueException,
    "InvalidSecurity": InvalidSecurityException,
    "InvalidState": InvalidStateException,
    "KMSAccessDenied": KMSAccessDeniedException,
    "KMSDisabled": KMSDisabledException,
    "KMSInvalidState": KMSInvalidStateException,
    "KMSNotFound": KMSNotFoundException,
    "KMSOptInRequired": KMSOptInRequired,
    "KMSThrottling": KMSThrottlingException,
    "NotFound": NotFoundException,
    "OptedOut": OptedOutException,
    "PlatformApplicationDisabled": PlatformApplicationDisabledException,
    "ReplayLimitExceeded": ReplayLimitExceededException,
    "ResourceNotFound": ResourceNotFoundException,
    "StaleTag": StaleTagException,
    "SubscriptionLimitExceeded": SubscriptionLimitExceededException,
    "TagLimitExceeded": TagLimitExceededException,
    "TagPolicy": TagPolicyException,
    "Throttled": ThrottledException,
    "TooManyEntriesInBatchRequest": TooManyEntriesInBatchRequestException,
    "TopicLimitExceeded": TopicLimitExceededException,
    "UserError": UserErrorException,
    "ValidationException": ValidationException,
    "VerificationException": VerificationException,
}
