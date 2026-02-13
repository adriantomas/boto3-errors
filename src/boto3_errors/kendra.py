# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class kendraError(Boto3Error):
    _SERVICE = "kendra"


class AccessDeniedException(kendraError):
    """You don't have sufficient access to perform this action. Please ensure you have the
    required permission policies and user accounts and try again.
    """

    _ERROR_CODE = "AccessDeniedException"


class ConflictException(kendraError):
    """A conflict occurred with the request. Please fix any inconsistences with your
    resources and try again.
    """

    _ERROR_CODE = "ConflictException"


class FeaturedResultsConflictException(kendraError):
    """An error message with a list of conflicting queries used across different sets of
    featured results. This occurred with the request for a new featured results set.
    Check that the queries you specified for featured results are unique per featured
    results set for each index.
    """

    _ERROR_CODE = "FeaturedResultsConflictException"

    @property
    def conflicting_items(self) -> list[Any] | None:
        """A list of the conflicting queries, including the query text, the name for the
        featured results set, and the identifier of the featured results set.
        """
        return self.response.get("ConflictingItems")


class InternalServerException(kendraError):
    """An issue occurred with the internal server used for your Amazon Kendra service.
    Please wait a few minutes and try again, or contact Support for help.
    """

    _ERROR_CODE = "InternalServerException"


class InvalidRequestException(kendraError):
    """The input to the request is not valid. Please provide the correct input and try
    again.
    """

    _ERROR_CODE = "InvalidRequestException"


class ResourceAlreadyExistException(kendraError):
    """The resource you want to use already exists. Please check you have provided the
    correct resource and try again.
    """

    _ERROR_CODE = "ResourceAlreadyExistException"


class ResourceInUseException(kendraError):
    """The resource you want to use is currently in use. Please check you have provided the
    correct resource and try again.
    """

    _ERROR_CODE = "ResourceInUseException"


class ResourceNotFoundException(kendraError):
    """The resource you want to use doesn’t exist. Please check you have provided the
    correct resource and try again.
    """

    _ERROR_CODE = "ResourceNotFoundException"


class ResourceUnavailableException(kendraError):
    """The resource you want to use isn't available. Please check you have provided the
    correct resource and try again.
    """

    _ERROR_CODE = "ResourceUnavailableException"


class ServiceQuotaExceededException(kendraError):
    """You have exceeded the set limits for your Amazon Kendra service. Please see Quotas
    for more information, or contact Support to inquire about an increase of limits.
    """

    _ERROR_CODE = "ServiceQuotaExceededException"


class ThrottlingException(kendraError):
    """The request was denied due to request throttling. Please reduce the number of
    requests and try again.
    """

    _ERROR_CODE = "ThrottlingException"


class ValidationException(kendraError):
    """The input fails to satisfy the constraints set by the Amazon Kendra service. Please
    provide the correct input and try again.
    """

    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[kendraError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "FeaturedResultsConflictException": FeaturedResultsConflictException,
    "InternalServerException": InternalServerException,
    "InvalidRequestException": InvalidRequestException,
    "ResourceAlreadyExistException": ResourceAlreadyExistException,
    "ResourceInUseException": ResourceInUseException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ResourceUnavailableException": ResourceUnavailableException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
