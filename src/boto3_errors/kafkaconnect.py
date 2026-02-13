# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class KafkaConnectError(Boto3Error):
    _SERVICE = "kafkaconnect"


class BadRequestException(KafkaConnectError):
    """HTTP Status Code 400: Bad request due to incorrect input. Correct your request and
    then retry it.
    """

    _ERROR_CODE = "BadRequestException"


class ConflictException(KafkaConnectError):
    """HTTP Status Code 409: Conflict. A resource with this name already exists. Retry your
    request with another name.
    """

    _ERROR_CODE = "ConflictException"


class ForbiddenException(KafkaConnectError):
    """HTTP Status Code 403: Access forbidden. Correct your credentials and then retry your
    request.
    """

    _ERROR_CODE = "ForbiddenException"


class InternalServerErrorException(KafkaConnectError):
    """HTTP Status Code 500: Unexpected internal server error. Retrying your request might
    resolve the issue.
    """

    _ERROR_CODE = "InternalServerErrorException"


class NotFoundException(KafkaConnectError):
    """HTTP Status Code 404: Resource not found due to incorrect input. Correct your
    request and then retry it.
    """

    _ERROR_CODE = "NotFoundException"


class ServiceUnavailableException(KafkaConnectError):
    """HTTP Status Code 503: Service Unavailable. Retrying your request in some time might
    resolve the issue.
    """

    _ERROR_CODE = "ServiceUnavailableException"


class TooManyRequestsException(KafkaConnectError):
    """HTTP Status Code 429: Limit exceeded. Resource limit reached."""
    _ERROR_CODE = "TooManyRequestsException"


class UnauthorizedException(KafkaConnectError):
    """HTTP Status Code 401: Unauthorized request. The provided credentials couldn't be
    validated.
    """

    _ERROR_CODE = "UnauthorizedException"


EXCEPTIONS: dict[str, type[KafkaConnectError]] = {
    "BadRequestException": BadRequestException,
    "ConflictException": ConflictException,
    "ForbiddenException": ForbiddenException,
    "InternalServerErrorException": InternalServerErrorException,
    "NotFoundException": NotFoundException,
    "ServiceUnavailableException": ServiceUnavailableException,
    "TooManyRequestsException": TooManyRequestsException,
    "UnauthorizedException": UnauthorizedException,
}
