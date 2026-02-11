# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class S3ControlError(Boto3Error):
    _SERVICE = "s3control"


class BadRequestException(S3ControlError):
    _ERROR_CODE = "BadRequestException"


class BucketAlreadyExists(S3ControlError):
    """The requested Outposts bucket name is not available. The bucket namespace is shared
    by all users of the Outposts in this Region. Select a different name and try again.
    """

    _ERROR_CODE = "BucketAlreadyExists"


class BucketAlreadyOwnedByYou(S3ControlError):
    """The Outposts bucket you tried to create already exists, and you own it."""
    _ERROR_CODE = "BucketAlreadyOwnedByYou"


class IdempotencyException(S3ControlError):
    _ERROR_CODE = "IdempotencyException"


class InternalServiceException(S3ControlError):
    _ERROR_CODE = "InternalServiceException"


class InvalidNextTokenException(S3ControlError):
    _ERROR_CODE = "InvalidNextTokenException"


class InvalidRequestException(S3ControlError):
    _ERROR_CODE = "InvalidRequestException"


class JobStatusException(S3ControlError):
    _ERROR_CODE = "JobStatusException"


class NoSuchPublicAccessBlockConfiguration(S3ControlError):
    """Amazon S3 throws this exception if you make a `GetPublicAccessBlock` request against
    an account that doesn't have a `PublicAccessBlockConfiguration` set.
    """

    _ERROR_CODE = "NoSuchPublicAccessBlockConfiguration"


class NotFoundException(S3ControlError):
    _ERROR_CODE = "NotFoundException"


class TooManyRequestsException(S3ControlError):
    _ERROR_CODE = "TooManyRequestsException"


class TooManyTagsException(S3ControlError):
    """Amazon S3 throws this exception if you have too many tags in your tag set."""
    _ERROR_CODE = "TooManyTagsException"


EXCEPTIONS: dict[str, type[S3ControlError]] = {
    "BadRequestException": BadRequestException,
    "BucketAlreadyExists": BucketAlreadyExists,
    "BucketAlreadyOwnedByYou": BucketAlreadyOwnedByYou,
    "IdempotencyException": IdempotencyException,
    "InternalServiceException": InternalServiceException,
    "InvalidNextTokenException": InvalidNextTokenException,
    "InvalidRequestException": InvalidRequestException,
    "JobStatusException": JobStatusException,
    "NoSuchPublicAccessBlockConfiguration": NoSuchPublicAccessBlockConfiguration,
    "NotFoundException": NotFoundException,
    "TooManyRequestsException": TooManyRequestsException,
    "TooManyTagsException": TooManyTagsException,
}
