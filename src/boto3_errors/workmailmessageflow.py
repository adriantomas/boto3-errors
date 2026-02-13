# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class WorkMailMessageFlowError(Boto3Error):
    _SERVICE = "workmailmessageflow"


class InvalidContentLocation(WorkMailMessageFlowError):
    """WorkMail could not access the updated email content. Possible reasons:

    - You made the request in a region other than your S3 bucket region.
    - The S3 bucket owner is not the same as the calling AWS account.
    - You have an incomplete or missing S3 bucket policy. For more information about
      policies, see Updating message content with AWS Lambda in the WorkMail
      Administrator Guide.
    """

    _ERROR_CODE = "InvalidContentLocation"


class MessageFrozen(WorkMailMessageFlowError):
    """The requested email is not eligible for update. This is usually the case for a
    redirected email.
    """

    _ERROR_CODE = "MessageFrozen"


class MessageRejected(WorkMailMessageFlowError):
    """The requested email could not be updated due to an error in the MIME content. Check
    the error message for more information about what caused the error.
    """

    _ERROR_CODE = "MessageRejected"


class ResourceNotFoundException(WorkMailMessageFlowError):
    """The requested email message is not found."""
    _ERROR_CODE = "ResourceNotFoundException"


EXCEPTIONS: dict[str, type[WorkMailMessageFlowError]] = {
    "InvalidContentLocation": InvalidContentLocation,
    "MessageFrozen": MessageFrozen,
    "MessageRejected": MessageRejected,
    "ResourceNotFoundException": ResourceNotFoundException,
}
