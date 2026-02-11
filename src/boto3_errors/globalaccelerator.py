# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class GlobalAcceleratorError(Boto3Error):
    _SERVICE = "globalaccelerator"


class AcceleratorNotDisabledException(GlobalAcceleratorError):
    """The accelerator that you specified could not be disabled."""
    _ERROR_CODE = "AcceleratorNotDisabledException"


class AcceleratorNotFoundException(GlobalAcceleratorError):
    """The accelerator that you specified doesn't exist."""
    _ERROR_CODE = "AcceleratorNotFoundException"


class AccessDeniedException(GlobalAcceleratorError):
    """You don't have access permission."""
    _ERROR_CODE = "AccessDeniedException"


class AssociatedEndpointGroupFoundException(GlobalAcceleratorError):
    """The listener that you specified has an endpoint group associated with it. You must
    remove all dependent resources from a listener before you can delete it.
    """

    _ERROR_CODE = "AssociatedEndpointGroupFoundException"


class AssociatedListenerFoundException(GlobalAcceleratorError):
    """The accelerator that you specified has a listener associated with it. You must
    remove all dependent resources from an accelerator before you can delete it.
    """

    _ERROR_CODE = "AssociatedListenerFoundException"


class AttachmentNotFoundException(GlobalAcceleratorError):
    """No cross-account attachment was found."""
    _ERROR_CODE = "AttachmentNotFoundException"


class ByoipCidrNotFoundException(GlobalAcceleratorError):
    """The CIDR that you specified was not found or is incorrect."""
    _ERROR_CODE = "ByoipCidrNotFoundException"


class ConflictException(GlobalAcceleratorError):
    """You can't use both of those options."""
    _ERROR_CODE = "ConflictException"


class EndpointAlreadyExistsException(GlobalAcceleratorError):
    """The endpoint that you specified doesn't exist."""
    _ERROR_CODE = "EndpointAlreadyExistsException"


class EndpointGroupAlreadyExistsException(GlobalAcceleratorError):
    """The endpoint group that you specified already exists."""
    _ERROR_CODE = "EndpointGroupAlreadyExistsException"


class EndpointGroupNotFoundException(GlobalAcceleratorError):
    """The endpoint group that you specified doesn't exist."""
    _ERROR_CODE = "EndpointGroupNotFoundException"


class EndpointNotFoundException(GlobalAcceleratorError):
    """The endpoint that you specified doesn't exist."""
    _ERROR_CODE = "EndpointNotFoundException"


class IncorrectCidrStateException(GlobalAcceleratorError):
    """The CIDR that you specified is not valid for this action. For example, the state of
    the CIDR might be incorrect for this action.
    """

    _ERROR_CODE = "IncorrectCidrStateException"


class InternalServiceErrorException(GlobalAcceleratorError):
    """There was an internal error for Global Accelerator."""
    _ERROR_CODE = "InternalServiceErrorException"


class InvalidArgumentException(GlobalAcceleratorError):
    """An argument that you specified is invalid."""
    _ERROR_CODE = "InvalidArgumentException"


class InvalidNextTokenException(GlobalAcceleratorError):
    """There isn't another item to return."""
    _ERROR_CODE = "InvalidNextTokenException"


class InvalidPortRangeException(GlobalAcceleratorError):
    """The port numbers that you specified are not valid numbers or are not unique for this
    accelerator.
    """

    _ERROR_CODE = "InvalidPortRangeException"


class LimitExceededException(GlobalAcceleratorError):
    """Processing your request would cause you to exceed an Global Accelerator limit."""
    _ERROR_CODE = "LimitExceededException"


class ListenerNotFoundException(GlobalAcceleratorError):
    """The listener that you specified doesn't exist."""
    _ERROR_CODE = "ListenerNotFoundException"


class TransactionInProgressException(GlobalAcceleratorError):
    """There's already a transaction in progress. Another transaction can't be processed."""
    _ERROR_CODE = "TransactionInProgressException"


EXCEPTIONS: dict[str, type[GlobalAcceleratorError]] = {
    "AcceleratorNotDisabledException": AcceleratorNotDisabledException,
    "AcceleratorNotFoundException": AcceleratorNotFoundException,
    "AccessDeniedException": AccessDeniedException,
    "AssociatedEndpointGroupFoundException": AssociatedEndpointGroupFoundException,
    "AssociatedListenerFoundException": AssociatedListenerFoundException,
    "AttachmentNotFoundException": AttachmentNotFoundException,
    "ByoipCidrNotFoundException": ByoipCidrNotFoundException,
    "ConflictException": ConflictException,
    "EndpointAlreadyExistsException": EndpointAlreadyExistsException,
    "EndpointGroupAlreadyExistsException": EndpointGroupAlreadyExistsException,
    "EndpointGroupNotFoundException": EndpointGroupNotFoundException,
    "EndpointNotFoundException": EndpointNotFoundException,
    "IncorrectCidrStateException": IncorrectCidrStateException,
    "InternalServiceErrorException": InternalServiceErrorException,
    "InvalidArgumentException": InvalidArgumentException,
    "InvalidNextTokenException": InvalidNextTokenException,
    "InvalidPortRangeException": InvalidPortRangeException,
    "LimitExceededException": LimitExceededException,
    "ListenerNotFoundException": ListenerNotFoundException,
    "TransactionInProgressException": TransactionInProgressException,
}
