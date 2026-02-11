# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class CloudControlError(Boto3Error):
    _SERVICE = "cloudcontrol"


class AlreadyExistsException(CloudControlError):
    """The resource with the name requested already exists."""
    _ERROR_CODE = "AlreadyExistsException"


class ClientTokenConflictException(CloudControlError):
    """The specified client token has already been used in another resource request.

    It's best practice for client tokens to be unique for each resource operation
    request. However, client token expire after 36 hours.
    """

    _ERROR_CODE = "ClientTokenConflictException"


class ConcurrentModificationException(CloudControlError):
    """The resource is currently being modified by another operation."""
    _ERROR_CODE = "ConcurrentModificationException"


class ConcurrentOperationException(CloudControlError):
    """Another resource operation is currently being performed on this resource."""
    _ERROR_CODE = "ConcurrentOperationException"


class GeneralServiceException(CloudControlError):
    """The resource handler has returned that the downstream service generated an error
    that doesn't map to any other handler error code.
    """

    _ERROR_CODE = "GeneralServiceException"


class HandlerFailureException(CloudControlError):
    """The resource handler has failed without a returning a more specific error code. This
    can include timeouts.
    """

    _ERROR_CODE = "HandlerFailureException"


class HandlerInternalFailureException(CloudControlError):
    """The resource handler has returned that an unexpected error occurred within the
    resource handler.
    """

    _ERROR_CODE = "HandlerInternalFailureException"


class InvalidCredentialsException(CloudControlError):
    """The resource handler has returned that the credentials provided by the user are
    invalid.
    """

    _ERROR_CODE = "InvalidCredentialsException"


class InvalidRequestException(CloudControlError):
    """The resource handler has returned that invalid input from the user has generated a
    generic exception.
    """

    _ERROR_CODE = "InvalidRequestException"


class NetworkFailureException(CloudControlError):
    """The resource handler has returned that the request couldn't be completed due to
    networking issues, such as a failure to receive a response from the server.
    """

    _ERROR_CODE = "NetworkFailureException"


class NotStabilizedException(CloudControlError):
    """The resource handler has returned that the downstream resource failed to complete
    all of its ready-state checks.
    """

    _ERROR_CODE = "NotStabilizedException"


class NotUpdatableException(CloudControlError):
    """One or more properties included in this resource operation are defined as create-
    only, and therefore can't be updated.
    """

    _ERROR_CODE = "NotUpdatableException"


class PrivateTypeException(CloudControlError):
    """Cloud Control API hasn't received a valid response from the resource handler, due to
    a configuration error. This includes issues such as the resource handler returning
    an invalid response, or timing out.
    """

    _ERROR_CODE = "PrivateTypeException"


class RequestTokenNotFoundException(CloudControlError):
    """A resource operation with the specified request token can't be found."""
    _ERROR_CODE = "RequestTokenNotFoundException"


class ResourceConflictException(CloudControlError):
    """The resource is temporarily unavailable to be acted upon. For example, if the
    resource is currently undergoing an operation and can't be acted upon until that
    operation is finished.
    """

    _ERROR_CODE = "ResourceConflictException"


class ResourceNotFoundException(CloudControlError):
    """A resource with the specified identifier can't be found."""
    _ERROR_CODE = "ResourceNotFoundException"


class ServiceInternalErrorException(CloudControlError):
    """The resource handler has returned that the downstream service returned an internal
    error, typically with a `5XX HTTP` status code.
    """

    _ERROR_CODE = "ServiceInternalErrorException"


class ServiceLimitExceededException(CloudControlError):
    """The resource handler has returned that a non-transient resource limit was reached on
    the service side.
    """

    _ERROR_CODE = "ServiceLimitExceededException"


class ThrottlingException(CloudControlError):
    """The request was denied due to request throttling."""
    _ERROR_CODE = "ThrottlingException"


class TypeNotFoundException(CloudControlError):
    """The specified extension doesn't exist in the CloudFormation registry."""
    _ERROR_CODE = "TypeNotFoundException"


class UnsupportedActionException(CloudControlError):
    """The specified resource doesn't support this resource operation."""
    _ERROR_CODE = "UnsupportedActionException"


EXCEPTIONS: dict[str, type[CloudControlError]] = {
    "AlreadyExistsException": AlreadyExistsException,
    "ClientTokenConflictException": ClientTokenConflictException,
    "ConcurrentModificationException": ConcurrentModificationException,
    "ConcurrentOperationException": ConcurrentOperationException,
    "GeneralServiceException": GeneralServiceException,
    "HandlerFailureException": HandlerFailureException,
    "HandlerInternalFailureException": HandlerInternalFailureException,
    "InvalidCredentialsException": InvalidCredentialsException,
    "InvalidRequestException": InvalidRequestException,
    "NetworkFailureException": NetworkFailureException,
    "NotStabilizedException": NotStabilizedException,
    "NotUpdatableException": NotUpdatableException,
    "PrivateTypeException": PrivateTypeException,
    "RequestTokenNotFoundException": RequestTokenNotFoundException,
    "ResourceConflictException": ResourceConflictException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceInternalErrorException": ServiceInternalErrorException,
    "ServiceLimitExceededException": ServiceLimitExceededException,
    "ThrottlingException": ThrottlingException,
    "TypeNotFoundException": TypeNotFoundException,
    "UnsupportedActionException": UnsupportedActionException,
}
