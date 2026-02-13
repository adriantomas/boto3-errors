# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class TextractError(Boto3Error):
    _SERVICE = "textract"


class AccessDeniedException(TextractError):
    """You aren't authorized to perform the action. Use the Amazon Resource Name (ARN) of
    an authorized user or IAM role to perform the operation.
    """

    _ERROR_CODE = "AccessDeniedException"


class BadDocumentException(TextractError):
    """Amazon Textract isn't able to read the document. For more information on the
    document limits in Amazon Textract, see limits.
    """

    _ERROR_CODE = "BadDocumentException"


class ConflictException(TextractError):
    """Updating or deleting a resource can cause an inconsistent state."""
    _ERROR_CODE = "ConflictException"


class DocumentTooLargeException(TextractError):
    """The document can't be processed because it's too large. The maximum document size
    for synchronous operations 10 MB. The maximum document size for asynchronous
    operations is 500 MB for PDF files.
    """

    _ERROR_CODE = "DocumentTooLargeException"


class HumanLoopQuotaExceededException(TextractError):
    """Indicates you have exceeded the maximum number of active human in the loop workflows
    available
    """

    _ERROR_CODE = "HumanLoopQuotaExceededException"

    @property
    def resource_type(self) -> str | None:
        """The resource type."""
        return self.response.get("ResourceType")

    @property
    def quota_code(self) -> str | None:
        """The quota code."""
        return self.response.get("QuotaCode")

    @property
    def service_code(self) -> str | None:
        """The service code."""
        return self.response.get("ServiceCode")


class IdempotentParameterMismatchException(TextractError):
    """A `ClientRequestToken` input parameter was reused with an operation, but at least
    one of the other input parameters is different from the previous call to the
    operation.
    """

    _ERROR_CODE = "IdempotentParameterMismatchException"


class InternalServerError(TextractError):
    """Amazon Textract experienced a service issue. Try your call again."""
    _ERROR_CODE = "InternalServerError"


class InvalidJobIdException(TextractError):
    """An invalid job identifier was passed to an asynchronous analysis operation."""
    _ERROR_CODE = "InvalidJobIdException"


class InvalidKMSKeyException(TextractError):
    """Indicates you do not have decrypt permissions with the KMS key entered, or the KMS
    key was entered incorrectly.
    """

    _ERROR_CODE = "InvalidKMSKeyException"


class InvalidParameterException(TextractError):
    """An input parameter violated a constraint. For example, in synchronous operations, an
    `InvalidParameterException` exception occurs when neither of the `S3Object` or
    `Bytes` values are supplied in the `Document` request parameter. Validate your
    parameter before calling the API operation again.
    """

    _ERROR_CODE = "InvalidParameterException"


class InvalidS3ObjectException(TextractError):
    """Amazon Textract is unable to access the S3 object that's specified in the request.
    for more information, Configure Access to Amazon S3 For troubleshooting information,
    see Troubleshooting Amazon S3
    """

    _ERROR_CODE = "InvalidS3ObjectException"


class LimitExceededException(TextractError):
    """An Amazon Textract service limit was exceeded. For example, if you start too many
    asynchronous jobs concurrently, calls to start operations
    (`StartDocumentTextDetection`, for example) raise a LimitExceededException exception
    (HTTP status code: 400) until the number of concurrently running jobs is below the
    Amazon Textract service limit.
    """

    _ERROR_CODE = "LimitExceededException"


class ProvisionedThroughputExceededException(TextractError):
    """The number of requests exceeded your throughput limit. If you want to increase this
    limit, contact Amazon Textract.
    """

    _ERROR_CODE = "ProvisionedThroughputExceededException"


class ResourceNotFoundException(TextractError):
    """Returned when an operation tried to access a nonexistent resource."""
    _ERROR_CODE = "ResourceNotFoundException"


class ServiceQuotaExceededException(TextractError):
    """Returned when a request cannot be completed as it would exceed a maximum service
    quota.
    """

    _ERROR_CODE = "ServiceQuotaExceededException"


class ThrottlingException(TextractError):
    """Amazon Textract is temporarily unable to process the request. Try your call again."""
    _ERROR_CODE = "ThrottlingException"


class UnsupportedDocumentException(TextractError):
    """The format of the input document isn't supported. Documents for operations can be in
    PNG, JPEG, PDF, or TIFF format.
    """

    _ERROR_CODE = "UnsupportedDocumentException"


class ValidationException(TextractError):
    """Indicates that a request was not valid. Check request for proper formatting."""
    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[TextractError]] = {
    "AccessDeniedException": AccessDeniedException,
    "BadDocumentException": BadDocumentException,
    "ConflictException": ConflictException,
    "DocumentTooLargeException": DocumentTooLargeException,
    "HumanLoopQuotaExceededException": HumanLoopQuotaExceededException,
    "IdempotentParameterMismatchException": IdempotentParameterMismatchException,
    "InternalServerError": InternalServerError,
    "InvalidJobIdException": InvalidJobIdException,
    "InvalidKMSKeyException": InvalidKMSKeyException,
    "InvalidParameterException": InvalidParameterException,
    "InvalidS3ObjectException": InvalidS3ObjectException,
    "LimitExceededException": LimitExceededException,
    "ProvisionedThroughputExceededException": ProvisionedThroughputExceededException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "UnsupportedDocumentException": UnsupportedDocumentException,
    "ValidationException": ValidationException,
}
