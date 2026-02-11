# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class AppMeshError(Boto3Error):
    _SERVICE = "appmesh"


class BadRequestException(AppMeshError):
    """The request syntax was malformed. Check your request syntax and try again."""
    _ERROR_CODE = "BadRequestException"


class ConflictException(AppMeshError):
    """The request contains a client token that was used for a previous update resource
    call with different specifications. Try the request again with a new client token.
    """

    _ERROR_CODE = "ConflictException"


class ForbiddenException(AppMeshError):
    """You don't have permissions to perform this action."""
    _ERROR_CODE = "ForbiddenException"


class InternalServerErrorException(AppMeshError):
    """The request processing has failed because of an unknown error, exception, or
    failure.
    """

    _ERROR_CODE = "InternalServerErrorException"


class LimitExceededException(AppMeshError):
    """You have exceeded a service limit for your account. For more information, see
    Service Limits in the App Mesh User Guide.
    """

    _ERROR_CODE = "LimitExceededException"


class NotFoundException(AppMeshError):
    """The specified resource doesn't exist. Check your request syntax and try again."""
    _ERROR_CODE = "NotFoundException"


class ResourceInUseException(AppMeshError):
    """You can't delete the specified resource because it's in use or required by another
    resource.
    """

    _ERROR_CODE = "ResourceInUseException"


class ServiceUnavailableException(AppMeshError):
    """The request has failed due to a temporary failure of the service."""
    _ERROR_CODE = "ServiceUnavailableException"


class TooManyRequestsException(AppMeshError):
    """The maximum request rate permitted by the App Mesh APIs has been exceeded for your
    account. For best results, use an increasing or variable sleep interval between
    requests.
    """

    _ERROR_CODE = "TooManyRequestsException"


class TooManyTagsException(AppMeshError):
    """The request exceeds the maximum allowed number of tags allowed per resource. The
    current limit is 50 user tags per resource. You must reduce the number of tags in
    the request. None of the tags in this request were applied.
    """

    _ERROR_CODE = "TooManyTagsException"


EXCEPTIONS: dict[str, type[AppMeshError]] = {
    "BadRequestException": BadRequestException,
    "ConflictException": ConflictException,
    "ForbiddenException": ForbiddenException,
    "InternalServerErrorException": InternalServerErrorException,
    "LimitExceededException": LimitExceededException,
    "NotFoundException": NotFoundException,
    "ResourceInUseException": ResourceInUseException,
    "ServiceUnavailableException": ServiceUnavailableException,
    "TooManyRequestsException": TooManyRequestsException,
    "TooManyTagsException": TooManyTagsException,
}
