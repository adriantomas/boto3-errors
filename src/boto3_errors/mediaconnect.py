# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class MediaConnectError(Boto3Error):
    _SERVICE = "mediaconnect"


class AddFlowOutputs420Exception(MediaConnectError):
    """Exception raised by Elemental MediaConnect when adding the flow output. See the
    error message for the operation for more information on the cause of this exception.
    """

    _ERROR_CODE = "AddFlowOutputs420Exception"


class BadRequestException(MediaConnectError):
    """This exception is thrown if the request contains a semantic error. The precise
    meaning depends on the API, and is documented in the error message.
    """

    _ERROR_CODE = "BadRequestException"


class ConflictException(MediaConnectError):
    """The requested operation would cause a conflict with the current state of a service
    resource associated with the request. Resolve the conflict before retrying this
    request.
    """

    _ERROR_CODE = "ConflictException"


class CreateBridge420Exception(MediaConnectError):
    """Exception raised by Elemental MediaConnect when creating the bridge. See the error
    message for the operation for more information on the cause of this exception.
    """

    _ERROR_CODE = "CreateBridge420Exception"


class CreateFlow420Exception(MediaConnectError):
    """Exception raised by Elemental MediaConnect when creating the flow. See the error
    message for the operation for more information on the cause of this exception.
    """

    _ERROR_CODE = "CreateFlow420Exception"


class CreateGateway420Exception(MediaConnectError):
    """Exception raised by Elemental MediaConnect when creating the gateway. See the error
    message for the operation for more information on the cause of this exception.
    """

    _ERROR_CODE = "CreateGateway420Exception"


class ForbiddenException(MediaConnectError):
    """You do not have sufficient access to perform this action."""
    _ERROR_CODE = "ForbiddenException"


class GrantFlowEntitlements420Exception(MediaConnectError):
    """Exception raised by Elemental MediaConnect when granting the entitlement. See the
    error message for the operation for more information on the cause of this exception.
    """

    _ERROR_CODE = "GrantFlowEntitlements420Exception"


class InternalServerErrorException(MediaConnectError):
    """The server encountered an internal error and is unable to complete the request."""
    _ERROR_CODE = "InternalServerErrorException"


class NotFoundException(MediaConnectError):
    """One or more of the resources in the request does not exist in the system."""
    _ERROR_CODE = "NotFoundException"


class RouterInputServiceQuotaExceededException(MediaConnectError):
    """The request to create a new router input would exceed the service quotas for the
    account.
    """

    _ERROR_CODE = "RouterInputServiceQuotaExceededException"


class RouterNetworkInterfaceServiceQuotaExceededException(MediaConnectError):
    """The request to create a new router network interface would exceed the service quotas
    (limits) set for the account.
    """

    _ERROR_CODE = "RouterNetworkInterfaceServiceQuotaExceededException"


class RouterOutputServiceQuotaExceededException(MediaConnectError):
    """The request to create a new router output would exceed the service quotas (limits)
    set for the account.
    """

    _ERROR_CODE = "RouterOutputServiceQuotaExceededException"


class ServiceUnavailableException(MediaConnectError):
    """The service is currently unavailable or busy."""
    _ERROR_CODE = "ServiceUnavailableException"


class TooManyRequestsException(MediaConnectError):
    """The request was denied due to request throttling."""
    _ERROR_CODE = "TooManyRequestsException"


EXCEPTIONS: dict[str, type[MediaConnectError]] = {
    "AddFlowOutputs420Exception": AddFlowOutputs420Exception,
    "BadRequestException": BadRequestException,
    "ConflictException": ConflictException,
    "CreateBridge420Exception": CreateBridge420Exception,
    "CreateFlow420Exception": CreateFlow420Exception,
    "CreateGateway420Exception": CreateGateway420Exception,
    "ForbiddenException": ForbiddenException,
    "GrantFlowEntitlements420Exception": GrantFlowEntitlements420Exception,
    "InternalServerErrorException": InternalServerErrorException,
    "NotFoundException": NotFoundException,
    "RouterInputServiceQuotaExceededException": RouterInputServiceQuotaExceededException,
    "RouterNetworkInterfaceServiceQuotaExceededException": RouterNetworkInterfaceServiceQuotaExceededException,
    "RouterOutputServiceQuotaExceededException": RouterOutputServiceQuotaExceededException,
    "ServiceUnavailableException": ServiceUnavailableException,
    "TooManyRequestsException": TooManyRequestsException,
}
