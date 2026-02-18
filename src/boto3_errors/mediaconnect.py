# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class MediaConnectError(Boto3Error):
    _SERVICE = "mediaconnect"


class AddFlowOutputs420Exception(MediaConnectError):
    """Exception raised by AWS Elemental MediaConnect. See the error message and
    documentation for the operation for more information on the cause of this exception.
    """

    _ERROR_CODE = "AddFlowOutputs420Exception"


class BadRequestException(MediaConnectError):
    """Exception raised by AWS Elemental MediaConnect. See the error message and
    documentation for the operation for more information on the cause of this exception.
    """

    _ERROR_CODE = "BadRequestException"


class ConflictException(MediaConnectError):
    """Exception raised by AWS Elemental MediaConnect. See the error message and
    documentation for the operation for more information on the cause of this exception.
    """

    _ERROR_CODE = "ConflictException"


class CreateBridge420Exception(MediaConnectError):
    """Exception raised by AWS Elemental MediaConnect. See the error message and
    documentation for the operation for more information on the cause of this exception.
    """

    _ERROR_CODE = "CreateBridge420Exception"


class CreateFlow420Exception(MediaConnectError):
    """Exception raised by AWS Elemental MediaConnect. See the error message and
    documentation for the operation for more information on the cause of this exception.
    """

    _ERROR_CODE = "CreateFlow420Exception"


class CreateGateway420Exception(MediaConnectError):
    """Exception raised by AWS Elemental MediaConnect. See the error message and
    documentation for the operation for more information on the cause of this exception.
    """

    _ERROR_CODE = "CreateGateway420Exception"


class ForbiddenException(MediaConnectError):
    """Exception raised by AWS Elemental MediaConnect. See the error message and
    documentation for the operation for more information on the cause of this exception.
    """

    _ERROR_CODE = "ForbiddenException"


class GrantFlowEntitlements420Exception(MediaConnectError):
    """Exception raised by AWS Elemental MediaConnect. See the error message and
    documentation for the operation for more information on the cause of this exception.
    """

    _ERROR_CODE = "GrantFlowEntitlements420Exception"


class InternalServerErrorException(MediaConnectError):
    """Exception raised by AWS Elemental MediaConnect. See the error message and
    documentation for the operation for more information on the cause of this exception.
    """

    _ERROR_CODE = "InternalServerErrorException"


class NotFoundException(MediaConnectError):
    """Exception raised by AWS Elemental MediaConnect. See the error message and
    documentation for the operation for more information on the cause of this exception.
    """

    _ERROR_CODE = "NotFoundException"


class ServiceUnavailableException(MediaConnectError):
    """Exception raised by AWS Elemental MediaConnect. See the error message and
    documentation for the operation for more information on the cause of this exception.
    """

    _ERROR_CODE = "ServiceUnavailableException"


class TooManyRequestsException(MediaConnectError):
    """Exception raised by AWS Elemental MediaConnect. See the error message and
    documentation for the operation for more information on the cause of this exception.
    """

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
    "ServiceUnavailableException": ServiceUnavailableException,
    "TooManyRequestsException": TooManyRequestsException,
}
