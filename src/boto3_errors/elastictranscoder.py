# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class ElasticTranscoderError(Boto3Error):
    _SERVICE = "elastictranscoder"


class AccessDeniedException(ElasticTranscoderError):
    """General authentication failure. The request was not signed correctly."""
    _ERROR_CODE = "AccessDeniedException"


class IncompatibleVersionException(ElasticTranscoderError):
    _ERROR_CODE = "IncompatibleVersionException"


class InternalServiceException(ElasticTranscoderError):
    """Elastic Transcoder encountered an unexpected exception while trying to fulfill the
    request.
    """

    _ERROR_CODE = "InternalServiceException"


class LimitExceededException(ElasticTranscoderError):
    """Too many operations for a given AWS account. For example, the number of pipelines
    exceeds the maximum allowed.
    """

    _ERROR_CODE = "LimitExceededException"


class ResourceInUseException(ElasticTranscoderError):
    """The resource you are attempting to change is in use. For example, you are attempting
    to delete a pipeline that is currently in use.
    """

    _ERROR_CODE = "ResourceInUseException"


class ResourceNotFoundException(ElasticTranscoderError):
    """The requested resource does not exist or is not available. For example, the pipeline
    to which you're trying to add a job doesn't exist or is still being created.
    """

    _ERROR_CODE = "ResourceNotFoundException"


class ValidationException(ElasticTranscoderError):
    """One or more required parameter values were not provided in the request."""
    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[ElasticTranscoderError]] = {
    "AccessDeniedException": AccessDeniedException,
    "IncompatibleVersionException": IncompatibleVersionException,
    "InternalServiceException": InternalServiceException,
    "LimitExceededException": LimitExceededException,
    "ResourceInUseException": ResourceInUseException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ValidationException": ValidationException,
}
