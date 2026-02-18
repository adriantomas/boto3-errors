# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class KinesisAnalyticsV2Error(Boto3Error):
    _SERVICE = "kinesisanalyticsv2"


class CodeValidationException(KinesisAnalyticsV2Error):
    """The user-provided application code (query) is not valid. This can be a simple syntax
    error.
    """

    _ERROR_CODE = "CodeValidationException"


class ConcurrentModificationException(KinesisAnalyticsV2Error):
    """Exception thrown as a result of concurrent modifications to an application. This
    error can be the result of attempting to modify an application without using the
    current application ID.
    """

    _ERROR_CODE = "ConcurrentModificationException"


class InvalidApplicationConfigurationException(KinesisAnalyticsV2Error):
    """The user-provided application configuration is not valid."""
    _ERROR_CODE = "InvalidApplicationConfigurationException"


class InvalidArgumentException(KinesisAnalyticsV2Error):
    """The specified input parameter value is not valid."""
    _ERROR_CODE = "InvalidArgumentException"


class InvalidRequestException(KinesisAnalyticsV2Error):
    """The request JSON is not valid for the operation."""
    _ERROR_CODE = "InvalidRequestException"


class LimitExceededException(KinesisAnalyticsV2Error):
    """The number of allowed resources has been exceeded."""
    _ERROR_CODE = "LimitExceededException"


class ResourceInUseException(KinesisAnalyticsV2Error):
    """The application is not available for this operation."""
    _ERROR_CODE = "ResourceInUseException"


class ResourceNotFoundException(KinesisAnalyticsV2Error):
    """Specified application can't be found."""
    _ERROR_CODE = "ResourceNotFoundException"


class ResourceProvisionedThroughputExceededException(KinesisAnalyticsV2Error):
    """Discovery failed to get a record from the streaming source because of the Kinesis
    Streams `ProvisionedThroughputExceededException`. For more information, see
    GetRecords in the Amazon Kinesis Streams API Reference.
    """

    _ERROR_CODE = "ResourceProvisionedThroughputExceededException"


class ServiceUnavailableException(KinesisAnalyticsV2Error):
    """The service cannot complete the request."""
    _ERROR_CODE = "ServiceUnavailableException"


class TooManyTagsException(KinesisAnalyticsV2Error):
    """Application created with too many tags, or too many tags added to an application.
    Note that the maximum number of application tags includes system tags. The maximum
    number of user-defined application tags is 50.
    """

    _ERROR_CODE = "TooManyTagsException"


class UnableToDetectSchemaException(KinesisAnalyticsV2Error):
    """The data format is not valid. Kinesis Data Analytics cannot detect the schema for
    the given streaming source.
    """

    _ERROR_CODE = "UnableToDetectSchemaException"

    @property
    def processed_input_records(self) -> list[Any] | None:
        """Stream data that was modified by the processor specified in the
        `InputProcessingConfiguration` parameter.
        """
        return self.response.get("ProcessedInputRecords")

    @property
    def raw_input_records(self) -> list[Any] | None:
        """Raw stream data that was sampled to infer the schema."""
        return self.response.get("RawInputRecords")


class UnsupportedOperationException(KinesisAnalyticsV2Error):
    """The request was rejected because a specified parameter is not supported or a
    specified resource is not valid for this operation.
    """

    _ERROR_CODE = "UnsupportedOperationException"


EXCEPTIONS: dict[str, type[KinesisAnalyticsV2Error]] = {
    "CodeValidationException": CodeValidationException,
    "ConcurrentModificationException": ConcurrentModificationException,
    "InvalidApplicationConfigurationException": InvalidApplicationConfigurationException,
    "InvalidArgumentException": InvalidArgumentException,
    "InvalidRequestException": InvalidRequestException,
    "LimitExceededException": LimitExceededException,
    "ResourceInUseException": ResourceInUseException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ResourceProvisionedThroughputExceededException": ResourceProvisionedThroughputExceededException,
    "ServiceUnavailableException": ServiceUnavailableException,
    "TooManyTagsException": TooManyTagsException,
    "UnableToDetectSchemaException": UnableToDetectSchemaException,
    "UnsupportedOperationException": UnsupportedOperationException,
}
