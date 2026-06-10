# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class CloudWatchError(Boto3Error):
    _SERVICE = "cloudwatch"


class ConcurrentModificationException(CloudWatchError):
    """More than one process tried to modify a resource at the same time."""
    _ERROR_CODE = "ConcurrentModificationException"


class ConflictException(CloudWatchError):
    """This operation attempted to create a resource that already exists."""
    _ERROR_CODE = "ConflictException"


class DashboardInvalidInputError(CloudWatchError):
    """Some part of the dashboard data is invalid."""
    _ERROR_CODE = "InvalidParameterInput"

    @property
    def dashboard_validation_messages(self) -> list[Any] | None:
        return self.response.get("dashboardValidationMessages")


class DashboardNotFoundError(CloudWatchError):
    """The specified dashboard does not exist."""
    _ERROR_CODE = "ResourceNotFound"


class InternalServiceFault(CloudWatchError):
    """Request processing has failed due to some unknown error, exception, or failure."""
    _ERROR_CODE = "InternalServiceError"


class InvalidFormatFault(CloudWatchError):
    """Data was not syntactically valid JSON."""
    _ERROR_CODE = "InvalidFormat"


class InvalidNextToken(CloudWatchError):
    """The next token specified is invalid."""
    _ERROR_CODE = "InvalidNextToken"


class InvalidParameterCombinationException(CloudWatchError):
    """Parameters were used together that cannot be used together."""
    _ERROR_CODE = "InvalidParameterCombination"


class InvalidParameterValueException(CloudWatchError):
    """The value of an input parameter is bad or out-of-range."""
    _ERROR_CODE = "InvalidParameterValue"


class KmsAccessDeniedException(CloudWatchError):
    """The operation was denied because either the calling principal lacks the required
    Amazon Web Services Key Management Service (Amazon Web Services KMS) permission on
    the key, or the key policy does not grant Amazon CloudWatch the permissions it needs
    to use the key. Verify that the caller has `kms:Decrypt` permission on the key, and
    that the key policy grants the CloudWatch service principal the `kms:DescribeKey`,
    `kms:GenerateDataKey`, `kms:Encrypt`, `kms:Decrypt`, and `kms:ReEncrypt*`
    permissions described in AssociateDatasetKmsKey.
    """

    _ERROR_CODE = "KmsAccessDeniedException"


class KmsKeyDisabledException(CloudWatchError):
    """The specified Amazon Web Services Key Management Service (Amazon Web Services KMS)
    key is disabled or pending deletion. Re-enable the key (or restore it, if it is
    pending deletion) and retry the operation.
    """

    _ERROR_CODE = "KmsKeyDisabledException"


class KmsKeyNotFoundException(CloudWatchError):
    """The specified Amazon Web Services Key Management Service (Amazon Web Services KMS)
    key could not be found. Verify that the key Amazon Resource Name (ARN) is correct,
    that the key exists, and that it is in the same Amazon Web Services Region as the
    resource.
    """

    _ERROR_CODE = "KmsKeyNotFoundException"


class LimitExceededException(CloudWatchError):
    """The operation exceeded one or more limits."""
    _ERROR_CODE = "LimitExceededException"


class LimitExceededFault(CloudWatchError):
    """The quota for alarms for this customer has already been reached."""
    _ERROR_CODE = "LimitExceeded"


class MissingRequiredParameterException(CloudWatchError):
    """An input parameter that is required is missing."""
    _ERROR_CODE = "MissingParameter"


class ResourceNotFound(CloudWatchError):
    """The named resource does not exist."""
    _ERROR_CODE = "ResourceNotFound"


class ResourceNotFoundException(CloudWatchError):
    """The named resource does not exist."""
    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def resource_id(self) -> str | None:
        return self.response.get("ResourceId")

    @property
    def resource_type(self) -> str | None:
        return self.response.get("ResourceType")


EXCEPTIONS: dict[str, type[CloudWatchError]] = {
    "ConcurrentModificationException": ConcurrentModificationException,
    "ConflictException": ConflictException,
    "InvalidParameterInput": DashboardInvalidInputError,
    "ResourceNotFound": DashboardNotFoundError,
    "InternalServiceError": InternalServiceFault,
    "InvalidFormat": InvalidFormatFault,
    "InvalidNextToken": InvalidNextToken,
    "InvalidParameterCombination": InvalidParameterCombinationException,
    "InvalidParameterValue": InvalidParameterValueException,
    "KmsAccessDeniedException": KmsAccessDeniedException,
    "KmsKeyDisabledException": KmsKeyDisabledException,
    "KmsKeyNotFoundException": KmsKeyNotFoundException,
    "LimitExceededException": LimitExceededException,
    "LimitExceeded": LimitExceededFault,
    "MissingParameter": MissingRequiredParameterException,
    "ResourceNotFound": ResourceNotFound,
    "ResourceNotFoundException": ResourceNotFoundException,
}
