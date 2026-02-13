# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class KendraRankingError(Boto3Error):
    _SERVICE = "kendra-ranking"


class AccessDeniedException(KendraRankingError):
    """You don’t have sufficient access to perform this action. Please ensure you have the
    required permission policies and user accounts and try again.
    """

    _ERROR_CODE = "AccessDeniedException"


class ConflictException(KendraRankingError):
    """A conflict occurred with the request. Please fix any inconsistencies with your
    resources and try again.
    """

    _ERROR_CODE = "ConflictException"


class InternalServerException(KendraRankingError):
    """An issue occurred with the internal server used for your Amazon Kendra Intelligent
    Ranking service. Please wait a few minutes and try again, or contact Support for
    help.
    """

    _ERROR_CODE = "InternalServerException"


class ResourceNotFoundException(KendraRankingError):
    """The resource you want to use doesn't exist. Please check you have provided the
    correct resource and try again.
    """

    _ERROR_CODE = "ResourceNotFoundException"


class ResourceUnavailableException(KendraRankingError):
    """The resource you want to use is unavailable. Please check you have provided the
    correct resource information and try again.
    """

    _ERROR_CODE = "ResourceUnavailableException"


class ServiceQuotaExceededException(KendraRankingError):
    """You have exceeded the set limits for your Amazon Kendra Intelligent Ranking service.
    Please see Quotas for more information, or contact Support to inquire about an
    increase of limits.
    """

    _ERROR_CODE = "ServiceQuotaExceededException"


class ThrottlingException(KendraRankingError):
    """The request was denied due to request throttling. Please reduce the number of
    requests and try again.
    """

    _ERROR_CODE = "ThrottlingException"


class ValidationException(KendraRankingError):
    """The input fails to satisfy the constraints set by the Amazon Kendra Intelligent
    Ranking service. Please provide the correct input and try again.
    """

    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[KendraRankingError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ResourceUnavailableException": ResourceUnavailableException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
