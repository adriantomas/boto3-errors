# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class imagebuilderError(Boto3Error):
    _SERVICE = "imagebuilder"


class AccessDeniedException(imagebuilderError):
    """You do not have permissions to perform the requested operation."""
    _ERROR_CODE = "AccessDeniedException"


class CallRateLimitExceededException(imagebuilderError):
    """You have exceeded the permitted request rate for the specific operation."""
    _ERROR_CODE = "CallRateLimitExceededException"


class ClientException(imagebuilderError):
    """These errors are usually caused by a client action, such as using an action or
    resource on behalf of a user that doesn't have permissions to use the action or
    resource, or specifying an invalid resource identifier.
    """

    _ERROR_CODE = "ClientException"


class DryRunOperationException(imagebuilderError):
    """The dry run operation of the resource was successful, and no resources or mutations
    were actually performed due to the dry run flag in the request.
    """

    _ERROR_CODE = "DryRunOperationException"


class ForbiddenException(imagebuilderError):
    """You are not authorized to perform the requested operation."""
    _ERROR_CODE = "ForbiddenException"


class IdempotentParameterMismatchException(imagebuilderError):
    """You have specified a client token for an operation using parameter values that
    differ from a previous request that used the same client token.
    """

    _ERROR_CODE = "IdempotentParameterMismatchException"


class InvalidPaginationTokenException(imagebuilderError):
    """You have provided an invalid pagination token in your request."""
    _ERROR_CODE = "InvalidPaginationTokenException"


class InvalidParameterCombinationException(imagebuilderError):
    """You have specified two or more mutually exclusive parameters. Review the error
    message for details.
    """

    _ERROR_CODE = "InvalidParameterCombinationException"


class InvalidParameterException(imagebuilderError):
    """The specified parameter is invalid. Review the available parameters for the API
    request.
    """

    _ERROR_CODE = "InvalidParameterException"


class InvalidParameterValueException(imagebuilderError):
    """The value that you provided for the specified parameter is invalid."""
    _ERROR_CODE = "InvalidParameterValueException"


class InvalidRequestException(imagebuilderError):
    """You have requested an action that that the service doesn't support."""
    _ERROR_CODE = "InvalidRequestException"


class InvalidVersionNumberException(imagebuilderError):
    """Your version number is out of bounds or does not follow the required syntax."""
    _ERROR_CODE = "InvalidVersionNumberException"


class ResourceAlreadyExistsException(imagebuilderError):
    """The resource that you are trying to create already exists."""
    _ERROR_CODE = "ResourceAlreadyExistsException"


class ResourceDependencyException(imagebuilderError):
    """You have attempted to mutate or delete a resource with a dependency that prohibits
    this action. See the error message for more details.
    """

    _ERROR_CODE = "ResourceDependencyException"


class ResourceInUseException(imagebuilderError):
    """The resource that you are trying to operate on is currently in use. Review the
    message details and retry later.
    """

    _ERROR_CODE = "ResourceInUseException"


class ResourceNotFoundException(imagebuilderError):
    """At least one of the resources referenced by your request does not exist."""
    _ERROR_CODE = "ResourceNotFoundException"


class ServiceException(imagebuilderError):
    """This exception is thrown when the service encounters an unrecoverable exception."""
    _ERROR_CODE = "ServiceException"


class ServiceQuotaExceededException(imagebuilderError):
    """You have exceeded the number of permitted resources or operations for this service.
    For service quotas, see EC2 Image Builder endpoints and quotas.
    """

    _ERROR_CODE = "ServiceQuotaExceededException"


class ServiceUnavailableException(imagebuilderError):
    """The service is unable to process your request at this time."""
    _ERROR_CODE = "ServiceUnavailableException"


class TooManyRequestsException(imagebuilderError):
    """You have attempted too many requests for the specific operation."""
    _ERROR_CODE = "TooManyRequestsException"


EXCEPTIONS: dict[str, type[imagebuilderError]] = {
    "AccessDeniedException": AccessDeniedException,
    "CallRateLimitExceededException": CallRateLimitExceededException,
    "ClientException": ClientException,
    "DryRunOperationException": DryRunOperationException,
    "ForbiddenException": ForbiddenException,
    "IdempotentParameterMismatchException": IdempotentParameterMismatchException,
    "InvalidPaginationTokenException": InvalidPaginationTokenException,
    "InvalidParameterCombinationException": InvalidParameterCombinationException,
    "InvalidParameterException": InvalidParameterException,
    "InvalidParameterValueException": InvalidParameterValueException,
    "InvalidRequestException": InvalidRequestException,
    "InvalidVersionNumberException": InvalidVersionNumberException,
    "ResourceAlreadyExistsException": ResourceAlreadyExistsException,
    "ResourceDependencyException": ResourceDependencyException,
    "ResourceInUseException": ResourceInUseException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceException": ServiceException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ServiceUnavailableException": ServiceUnavailableException,
    "TooManyRequestsException": TooManyRequestsException,
}
