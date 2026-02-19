# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class RekognitionError(Boto3Error):
    _SERVICE = "rekognition"


class AccessDeniedException(RekognitionError):
    """You are not authorized to perform the action."""
    _ERROR_CODE = "AccessDeniedException"


class ConflictException(RekognitionError):
    """A User with the same Id already exists within the collection, or the update or
    deletion of the User caused an inconsistent state. **
    """

    _ERROR_CODE = "ConflictException"


class HumanLoopQuotaExceededException(RekognitionError):
    """The number of in-progress human reviews you have has exceeded the number allowed."""
    _ERROR_CODE = "HumanLoopQuotaExceededException"

    @property
    def quota_code(self) -> str | None:
        """The quota code."""
        return self.response.get("QuotaCode")

    @property
    def resource_type(self) -> str | None:
        """The resource type."""
        return self.response.get("ResourceType")

    @property
    def service_code(self) -> str | None:
        """The service code."""
        return self.response.get("ServiceCode")


class IdempotentParameterMismatchException(RekognitionError):
    """A `ClientRequestToken` input parameter was reused with an operation, but at least
    one of the other input parameters is different from the previous call to the
    operation.
    """

    _ERROR_CODE = "IdempotentParameterMismatchException"


class ImageTooLargeException(RekognitionError):
    """The input image size exceeds the allowed limit. If you are calling
    DetectProtectiveEquipment, the image size or resolution exceeds the allowed limit.
    For more information, see Guidelines and quotas in Amazon Rekognition in the Amazon
    Rekognition Developer Guide.
    """

    _ERROR_CODE = "ImageTooLargeException"


class InternalServerError(RekognitionError):
    """Amazon Rekognition experienced a service issue. Try your call again."""
    _ERROR_CODE = "InternalServerError"


class InvalidImageFormatException(RekognitionError):
    """The provided image format is not supported."""
    _ERROR_CODE = "InvalidImageFormatException"


class InvalidManifestException(RekognitionError):
    """Indicates that a provided manifest file is empty or larger than the allowed limit."""
    _ERROR_CODE = "InvalidManifestException"


class InvalidPaginationTokenException(RekognitionError):
    """Pagination token in the request is not valid."""
    _ERROR_CODE = "InvalidPaginationTokenException"


class InvalidParameterException(RekognitionError):
    """Input parameter violated a constraint. Validate your parameter before calling the
    API operation again.
    """

    _ERROR_CODE = "InvalidParameterException"


class InvalidPolicyRevisionIdException(RekognitionError):
    """The supplied revision id for the project policy is invalid."""
    _ERROR_CODE = "InvalidPolicyRevisionIdException"


class InvalidS3ObjectException(RekognitionError):
    """Amazon Rekognition is unable to access the S3 object specified in the request."""
    _ERROR_CODE = "InvalidS3ObjectException"


class LimitExceededException(RekognitionError):
    """An Amazon Rekognition service limit was exceeded. For example, if you start too many
    jobs concurrently, subsequent calls to start operations (ex: `StartLabelDetection`)
    will raise a `LimitExceededException` exception (HTTP status code: 400) until the
    number of concurrently running jobs is below the Amazon Rekognition service limit.
    """

    _ERROR_CODE = "LimitExceededException"


class MalformedPolicyDocumentException(RekognitionError):
    """The format of the project policy document that you supplied to `PutProjectPolicy` is
    incorrect.
    """

    _ERROR_CODE = "MalformedPolicyDocumentException"


class ProvisionedThroughputExceededException(RekognitionError):
    """The number of requests exceeded your throughput limit. If you want to increase this
    limit, contact Amazon Rekognition.
    """

    _ERROR_CODE = "ProvisionedThroughputExceededException"


class ResourceAlreadyExistsException(RekognitionError):
    """A resource with the specified ID already exists."""
    _ERROR_CODE = "ResourceAlreadyExistsException"


class ResourceInUseException(RekognitionError):
    """The specified resource is already being used."""
    _ERROR_CODE = "ResourceInUseException"


class ResourceNotFoundException(RekognitionError):
    """The resource specified in the request cannot be found."""
    _ERROR_CODE = "ResourceNotFoundException"


class ResourceNotReadyException(RekognitionError):
    """The requested resource isn't ready. For example, this exception occurs when you call
    `DetectCustomLabels` with a model version that isn't deployed.
    """

    _ERROR_CODE = "ResourceNotReadyException"


class ServiceQuotaExceededException(RekognitionError):
    """The size of the collection exceeds the allowed limit. For more information, see
    Guidelines and quotas in Amazon Rekognition in the Amazon Rekognition Developer
    Guide.
    """

    _ERROR_CODE = "ServiceQuotaExceededException"


class SessionNotFoundException(RekognitionError):
    """Occurs when a given sessionId is not found."""
    _ERROR_CODE = "SessionNotFoundException"


class ThrottlingException(RekognitionError):
    """Amazon Rekognition is temporarily unable to process the request. Try your call
    again.
    """

    _ERROR_CODE = "ThrottlingException"


class VideoTooLargeException(RekognitionError):
    """The file size or duration of the supplied media is too large. The maximum file size
    is 10GB. The maximum duration is 6 hours.
    """

    _ERROR_CODE = "VideoTooLargeException"


EXCEPTIONS: dict[str, type[RekognitionError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "HumanLoopQuotaExceededException": HumanLoopQuotaExceededException,
    "IdempotentParameterMismatchException": IdempotentParameterMismatchException,
    "ImageTooLargeException": ImageTooLargeException,
    "InternalServerError": InternalServerError,
    "InvalidImageFormatException": InvalidImageFormatException,
    "InvalidManifestException": InvalidManifestException,
    "InvalidPaginationTokenException": InvalidPaginationTokenException,
    "InvalidParameterException": InvalidParameterException,
    "InvalidPolicyRevisionIdException": InvalidPolicyRevisionIdException,
    "InvalidS3ObjectException": InvalidS3ObjectException,
    "LimitExceededException": LimitExceededException,
    "MalformedPolicyDocumentException": MalformedPolicyDocumentException,
    "ProvisionedThroughputExceededException": ProvisionedThroughputExceededException,
    "ResourceAlreadyExistsException": ResourceAlreadyExistsException,
    "ResourceInUseException": ResourceInUseException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ResourceNotReadyException": ResourceNotReadyException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "SessionNotFoundException": SessionNotFoundException,
    "ThrottlingException": ThrottlingException,
    "VideoTooLargeException": VideoTooLargeException,
}
