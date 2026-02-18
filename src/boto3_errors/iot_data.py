# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class IoTDataPlaneError(Boto3Error):
    _SERVICE = "iot-data"


class ConflictException(IoTDataPlaneError):
    """The specified version does not match the version of the document."""
    _ERROR_CODE = "ConflictException"


class InternalFailureException(IoTDataPlaneError):
    """An unexpected error has occurred."""
    _ERROR_CODE = "InternalFailureException"


class InvalidRequestException(IoTDataPlaneError):
    """The request is not valid."""
    _ERROR_CODE = "InvalidRequestException"


class MethodNotAllowedException(IoTDataPlaneError):
    """The specified combination of HTTP verb and URI is not supported."""
    _ERROR_CODE = "MethodNotAllowedException"


class RequestEntityTooLargeException(IoTDataPlaneError):
    """The payload exceeds the maximum size allowed."""
    _ERROR_CODE = "RequestEntityTooLargeException"


class ResourceNotFoundException(IoTDataPlaneError):
    """The specified resource does not exist."""
    _ERROR_CODE = "ResourceNotFoundException"


class ServiceUnavailableException(IoTDataPlaneError):
    """The service is temporarily unavailable."""
    _ERROR_CODE = "ServiceUnavailableException"


class ThrottlingException(IoTDataPlaneError):
    """The rate exceeds the limit."""
    _ERROR_CODE = "ThrottlingException"


class UnauthorizedException(IoTDataPlaneError):
    """You are not authorized to perform this operation."""
    _ERROR_CODE = "UnauthorizedException"


class UnsupportedDocumentEncodingException(IoTDataPlaneError):
    """The document encoding is not supported."""
    _ERROR_CODE = "UnsupportedDocumentEncodingException"


EXCEPTIONS: dict[str, type[IoTDataPlaneError]] = {
    "ConflictException": ConflictException,
    "InternalFailureException": InternalFailureException,
    "InvalidRequestException": InvalidRequestException,
    "MethodNotAllowedException": MethodNotAllowedException,
    "RequestEntityTooLargeException": RequestEntityTooLargeException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceUnavailableException": ServiceUnavailableException,
    "ThrottlingException": ThrottlingException,
    "UnauthorizedException": UnauthorizedException,
    "UnsupportedDocumentEncodingException": UnsupportedDocumentEncodingException,
}
