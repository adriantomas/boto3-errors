# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class KinesisAnalyticsError(Boto3Error):
    _SERVICE = "kinesisanalytics"


class CodeValidationException(KinesisAnalyticsError):
    """User-provided application code (query) is invalid. This can be a simple syntax
    error.
    """

    _ERROR_CODE = "CodeValidationException"


class ConcurrentModificationException(KinesisAnalyticsError):
    """Exception thrown as a result of concurrent modification to an application. For
    example, two individuals attempting to edit the same application at the same time.
    """

    _ERROR_CODE = "ConcurrentModificationException"


class InvalidApplicationConfigurationException(KinesisAnalyticsError):
    """User-provided application configuration is not valid."""
    _ERROR_CODE = "InvalidApplicationConfigurationException"


class InvalidArgumentException(KinesisAnalyticsError):
    """Specified input parameter value is invalid."""
    _ERROR_CODE = "InvalidArgumentException"


class LimitExceededException(KinesisAnalyticsError):
    """Exceeded the number of applications allowed."""
    _ERROR_CODE = "LimitExceededException"


class ResourceInUseException(KinesisAnalyticsError):
    """Application is not available for this operation."""
    _ERROR_CODE = "ResourceInUseException"


class ResourceNotFoundException(KinesisAnalyticsError):
    """Specified application can't be found."""
    _ERROR_CODE = "ResourceNotFoundException"


class ResourceProvisionedThroughputExceededException(KinesisAnalyticsError):
    """Discovery failed to get a record from the streaming source because of the Amazon
    Kinesis Streams ProvisionedThroughputExceededException. For more information, see
    GetRecords in the Amazon Kinesis Streams API Reference.
    """

    _ERROR_CODE = "ResourceProvisionedThroughputExceededException"


class ServiceUnavailableException(KinesisAnalyticsError):
    """The service is unavailable. Back off and retry the operation."""
    _ERROR_CODE = "ServiceUnavailableException"


class TooManyTagsException(KinesisAnalyticsError):
    """Application created with too many tags, or too many tags added to an application.
    Note that the maximum number of application tags includes system tags. The maximum
    number of user-defined application tags is 50.
    """

    _ERROR_CODE = "TooManyTagsException"


class UnableToDetectSchemaException(KinesisAnalyticsError):
    """Data format is not valid. Amazon Kinesis Analytics is not able to detect schema for
    the given streaming source.
    """

    _ERROR_CODE = "UnableToDetectSchemaException"

    @property
    def raw_input_records(self) -> list[Any] | None:
        return self.response.get("RawInputRecords")

    @property
    def processed_input_records(self) -> list[Any] | None:
        return self.response.get("ProcessedInputRecords")


class UnsupportedOperationException(KinesisAnalyticsError):
    """The request was rejected because a specified parameter is not supported or a
    specified resource is not valid for this operation.
    """

    _ERROR_CODE = "UnsupportedOperationException"


EXCEPTIONS: dict[str, type[KinesisAnalyticsError]] = {
    "CodeValidationException": CodeValidationException,
    "ConcurrentModificationException": ConcurrentModificationException,
    "InvalidApplicationConfigurationException": InvalidApplicationConfigurationException,
    "InvalidArgumentException": InvalidArgumentException,
    "LimitExceededException": LimitExceededException,
    "ResourceInUseException": ResourceInUseException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ResourceProvisionedThroughputExceededException": ResourceProvisionedThroughputExceededException,
    "ServiceUnavailableException": ServiceUnavailableException,
    "TooManyTagsException": TooManyTagsException,
    "UnableToDetectSchemaException": UnableToDetectSchemaException,
    "UnsupportedOperationException": UnsupportedOperationException,
}
