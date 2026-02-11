# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class SageMakerA2IRuntimeError(Boto3Error):
    _SERVICE = "sagemaker-a2i-runtime"


class ConflictException(SageMakerA2IRuntimeError):
    """Your request has the same name as another active human loop but has different input
    data. You cannot start two human loops with the same name and different input data.
    """

    _ERROR_CODE = "ConflictException"


class InternalServerException(SageMakerA2IRuntimeError):
    """We couldn't process your request because of an issue with the server. Try again
    later.
    """

    _ERROR_CODE = "InternalServerException"


class ResourceNotFoundException(SageMakerA2IRuntimeError):
    """We couldn't find the requested resource. Check that your resources exists and were
    created in the same AWS Region as your request, and try your request again.
    """

    _ERROR_CODE = "ResourceNotFoundException"


class ServiceQuotaExceededException(SageMakerA2IRuntimeError):
    """You exceeded your service quota. Service quotas, also referred to as limits, are the
    maximum number of service resources or operations for your AWS account. For a list
    of Amazon A2I service quotes, see Amazon Augmented AI Service Quotes. Delete some
    resources or request an increase in your service quota. You can request a quota
    increase using Service Quotas or the AWS Support Center. To request an increase, see
    AWS Service Quotas in the AWS General Reference.
    """

    _ERROR_CODE = "ServiceQuotaExceededException"


class ThrottlingException(SageMakerA2IRuntimeError):
    """You exceeded the maximum number of requests."""
    _ERROR_CODE = "ThrottlingException"


class ValidationException(SageMakerA2IRuntimeError):
    """The request isn't valid. Check the syntax and try again."""
    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[SageMakerA2IRuntimeError]] = {
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
