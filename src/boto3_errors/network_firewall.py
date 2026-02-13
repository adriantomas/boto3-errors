# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class NetworkFirewallError(Boto3Error):
    _SERVICE = "network-firewall"


class InsufficientCapacityException(NetworkFirewallError):
    """Amazon Web Services doesn't currently have enough available capacity to fulfill your
    request. Try your request later.
    """

    _ERROR_CODE = "InsufficientCapacityException"


class InternalServerError(NetworkFirewallError):
    """Your request is valid, but Network Firewall couldn't perform the operation because
    of a system problem. Retry your request.
    """

    _ERROR_CODE = "InternalServerError"


class InvalidOperationException(NetworkFirewallError):
    """The operation failed because it's not valid. For example, you might have tried to
    delete a rule group or firewall policy that's in use.
    """

    _ERROR_CODE = "InvalidOperationException"


class InvalidRequestException(NetworkFirewallError):
    """The operation failed because of a problem with your request. Examples include:

    - You specified an unsupported parameter name or value.
    - You tried to update a property with a value that isn't among the available types.
    - Your request references an ARN that is malformed, or corresponds to a resource
      that isn't valid in the context of the request.
    """

    _ERROR_CODE = "InvalidRequestException"


class InvalidResourcePolicyException(NetworkFirewallError):
    """The policy statement failed validation."""
    _ERROR_CODE = "InvalidResourcePolicyException"


class InvalidTokenException(NetworkFirewallError):
    """The token you provided is stale or isn't valid for the operation."""
    _ERROR_CODE = "InvalidTokenException"


class LimitExceededException(NetworkFirewallError):
    """Unable to perform the operation because doing so would violate a limit setting."""
    _ERROR_CODE = "LimitExceededException"


class LogDestinationPermissionException(NetworkFirewallError):
    """Unable to send logs to a configured logging destination."""
    _ERROR_CODE = "LogDestinationPermissionException"


class ResourceNotFoundException(NetworkFirewallError):
    """Unable to locate a resource using the parameters that you provided."""
    _ERROR_CODE = "ResourceNotFoundException"


class ResourceOwnerCheckException(NetworkFirewallError):
    """Unable to change the resource because your account doesn't own it."""
    _ERROR_CODE = "ResourceOwnerCheckException"


class ThrottlingException(NetworkFirewallError):
    """Unable to process the request due to throttling limitations."""
    _ERROR_CODE = "ThrottlingException"


class UnsupportedOperationException(NetworkFirewallError):
    """The operation you requested isn't supported by Network Firewall."""
    _ERROR_CODE = "UnsupportedOperationException"


EXCEPTIONS: dict[str, type[NetworkFirewallError]] = {
    "InsufficientCapacityException": InsufficientCapacityException,
    "InternalServerError": InternalServerError,
    "InvalidOperationException": InvalidOperationException,
    "InvalidRequestException": InvalidRequestException,
    "InvalidResourcePolicyException": InvalidResourcePolicyException,
    "InvalidTokenException": InvalidTokenException,
    "LimitExceededException": LimitExceededException,
    "LogDestinationPermissionException": LogDestinationPermissionException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ResourceOwnerCheckException": ResourceOwnerCheckException,
    "ThrottlingException": ThrottlingException,
    "UnsupportedOperationException": UnsupportedOperationException,
}
