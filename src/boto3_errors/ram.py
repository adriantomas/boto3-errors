# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class RAMError(Boto3Error):
    _SERVICE = "ram"


class IdempotentParameterMismatchException(RAMError):
    """The operation failed because the client token input parameter matched one that was
    used with a previous call to the operation, but at least one of the other input
    parameters is different from the previous call.
    """

    _ERROR_CODE = "IdempotentParameterMismatchException"


class InvalidClientTokenException(RAMError):
    """The operation failed because the specified client token isn't valid."""
    _ERROR_CODE = "InvalidClientTokenException"


class InvalidMaxResultsException(RAMError):
    """The operation failed because the specified value for `MaxResults` isn't valid."""
    _ERROR_CODE = "InvalidMaxResultsException"


class InvalidNextTokenException(RAMError):
    """The operation failed because the specified value for `NextToken` isn't valid. You
    must specify a value you received in the `NextToken` response of a previous call to
    this operation.
    """

    _ERROR_CODE = "InvalidNextTokenException"


class InvalidParameterException(RAMError):
    """The operation failed because a parameter you specified isn't valid."""
    _ERROR_CODE = "InvalidParameterException"


class InvalidPolicyException(RAMError):
    """The operation failed because a policy you specified isn't valid."""
    _ERROR_CODE = "InvalidPolicyException"


class InvalidResourceTypeException(RAMError):
    """The operation failed because the specified resource type isn't valid."""
    _ERROR_CODE = "InvalidResourceTypeException"


class InvalidStateTransitionException(RAMError):
    """The operation failed because the requested operation isn't valid for the resource
    share in its current state.
    """

    _ERROR_CODE = "InvalidStateTransitionException"


class MalformedArnException(RAMError):
    """The operation failed because the specified Amazon Resource Name (ARN) has a format
    that isn't valid.
    """

    _ERROR_CODE = "MalformedArnException"


class MalformedPolicyTemplateException(RAMError):
    """The operation failed because the policy template that you provided isn't valid."""
    _ERROR_CODE = "MalformedPolicyTemplateException"


class MissingRequiredParameterException(RAMError):
    """The operation failed because a required input parameter is missing."""
    _ERROR_CODE = "MissingRequiredParameterException"


class OperationNotPermittedException(RAMError):
    """The operation failed because the requested operation isn't permitted."""
    _ERROR_CODE = "OperationNotPermittedException"


class PermissionAlreadyExistsException(RAMError):
    """The operation failed because a permission with the specified name already exists in
    the requested Amazon Web Services Region. Choose a different name.
    """

    _ERROR_CODE = "PermissionAlreadyExistsException"


class PermissionLimitExceededException(RAMError):
    """The operation failed because it would exceed the maximum number of permissions you
    can create in each Amazon Web Services Region. To view the limits for your Amazon
    Web Services account, see the RAM page in the Service Quotas console.
    """

    _ERROR_CODE = "PermissionLimitExceededException"


class PermissionVersionsLimitExceededException(RAMError):
    """The operation failed because it would exceed the limit for the number of versions
    you can have for a permission. To view the limits for your Amazon Web Services
    account, see the RAM page in the Service Quotas console.
    """

    _ERROR_CODE = "PermissionVersionsLimitExceededException"


class ResourceArnNotFoundException(RAMError):
    """The operation failed because the specified Amazon Resource Name (ARN) was not found."""
    _ERROR_CODE = "ResourceArnNotFoundException"


class ResourceShareInvitationAlreadyAcceptedException(RAMError):
    """The operation failed because the specified invitation was already accepted."""
    _ERROR_CODE = "ResourceShareInvitationAlreadyAcceptedException"


class ResourceShareInvitationAlreadyRejectedException(RAMError):
    """The operation failed because the specified invitation was already rejected."""
    _ERROR_CODE = "ResourceShareInvitationAlreadyRejectedException"


class ResourceShareInvitationArnNotFoundException(RAMError):
    """The operation failed because the specified Amazon Resource Name (ARN) for an
    invitation was not found.
    """

    _ERROR_CODE = "ResourceShareInvitationArnNotFoundException"


class ResourceShareInvitationExpiredException(RAMError):
    """The operation failed because the specified invitation is past its expiration date
    and time.
    """

    _ERROR_CODE = "ResourceShareInvitationExpiredException"


class ResourceShareLimitExceededException(RAMError):
    """The operation failed because it would exceed the limit for resource shares for your
    account. You can associate up to 100 resources per call. To view the limits for your
    Amazon Web Services account, see the RAM page in the Service Quotas console.
    """

    _ERROR_CODE = "ResourceShareLimitExceededException"


class ServerInternalException(RAMError):
    """The operation failed because the service could not respond to the request due to an
    internal problem. Try again later.
    """

    _ERROR_CODE = "ServerInternalException"


class ServiceUnavailableException(RAMError):
    """The operation failed because the service isn't available. Try again later."""
    _ERROR_CODE = "ServiceUnavailableException"


class TagLimitExceededException(RAMError):
    """The operation failed because it would exceed the limit for tags for your Amazon Web
    Services account.
    """

    _ERROR_CODE = "TagLimitExceededException"


class TagPolicyViolationException(RAMError):
    """The operation failed because the specified tag key is a reserved word and can't be
    used.
    """

    _ERROR_CODE = "TagPolicyViolationException"


class ThrottlingException(RAMError):
    """The operation failed because it exceeded the rate at which you are allowed to
    perform this operation. Please try again later.
    """

    _ERROR_CODE = "ThrottlingException"


class UnknownResourceException(RAMError):
    """The operation failed because a specified resource couldn't be found."""
    _ERROR_CODE = "UnknownResourceException"


class UnmatchedPolicyPermissionException(RAMError):
    """There isn't an existing managed permission defined in RAM that has the same IAM
    permissions as the resource-based policy attached to the resource. You should first
    run PromotePermissionCreatedFromPolicy to create that managed permission.
    """

    _ERROR_CODE = "UnmatchedPolicyPermissionException"


EXCEPTIONS: dict[str, type[RAMError]] = {
    "IdempotentParameterMismatchException": IdempotentParameterMismatchException,
    "InvalidClientTokenException": InvalidClientTokenException,
    "InvalidMaxResultsException": InvalidMaxResultsException,
    "InvalidNextTokenException": InvalidNextTokenException,
    "InvalidParameterException": InvalidParameterException,
    "InvalidPolicyException": InvalidPolicyException,
    "InvalidResourceTypeException": InvalidResourceTypeException,
    "InvalidStateTransitionException": InvalidStateTransitionException,
    "MalformedArnException": MalformedArnException,
    "MalformedPolicyTemplateException": MalformedPolicyTemplateException,
    "MissingRequiredParameterException": MissingRequiredParameterException,
    "OperationNotPermittedException": OperationNotPermittedException,
    "PermissionAlreadyExistsException": PermissionAlreadyExistsException,
    "PermissionLimitExceededException": PermissionLimitExceededException,
    "PermissionVersionsLimitExceededException": PermissionVersionsLimitExceededException,
    "ResourceArnNotFoundException": ResourceArnNotFoundException,
    "ResourceShareInvitationAlreadyAcceptedException": ResourceShareInvitationAlreadyAcceptedException,
    "ResourceShareInvitationAlreadyRejectedException": ResourceShareInvitationAlreadyRejectedException,
    "ResourceShareInvitationArnNotFoundException": ResourceShareInvitationArnNotFoundException,
    "ResourceShareInvitationExpiredException": ResourceShareInvitationExpiredException,
    "ResourceShareLimitExceededException": ResourceShareLimitExceededException,
    "ServerInternalException": ServerInternalException,
    "ServiceUnavailableException": ServiceUnavailableException,
    "TagLimitExceededException": TagLimitExceededException,
    "TagPolicyViolationException": TagPolicyViolationException,
    "ThrottlingException": ThrottlingException,
    "UnknownResourceException": UnknownResourceException,
    "UnmatchedPolicyPermissionException": UnmatchedPolicyPermissionException,
}
