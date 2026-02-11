# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class SupportError(Boto3Error):
    _SERVICE = "support"


class AttachmentIdNotFound(SupportError):
    """An attachment with the specified ID could not be found."""
    _ERROR_CODE = "AttachmentIdNotFound"


class AttachmentLimitExceeded(SupportError):
    """The limit for the number of attachment sets created in a short period of time has
    been exceeded.
    """

    _ERROR_CODE = "AttachmentLimitExceeded"


class AttachmentSetExpired(SupportError):
    """The expiration time of the attachment set has passed. The set expires 1 hour after
    it is created.
    """

    _ERROR_CODE = "AttachmentSetExpired"


class AttachmentSetIdNotFound(SupportError):
    """An attachment set with the specified ID could not be found."""
    _ERROR_CODE = "AttachmentSetIdNotFound"


class AttachmentSetSizeLimitExceeded(SupportError):
    """A limit for the size of an attachment set has been exceeded. The limits are three
    attachments and 5 MB per attachment.
    """

    _ERROR_CODE = "AttachmentSetSizeLimitExceeded"


class CaseCreationLimitExceeded(SupportError):
    """The case creation limit for the account has been exceeded."""
    _ERROR_CODE = "CaseCreationLimitExceeded"


class CaseIdNotFound(SupportError):
    """The requested `caseId` couldn't be located."""
    _ERROR_CODE = "CaseIdNotFound"


class DescribeAttachmentLimitExceeded(SupportError):
    """The limit for the number of DescribeAttachment requests in a short period of time
    has been exceeded.
    """

    _ERROR_CODE = "DescribeAttachmentLimitExceeded"


class InternalServerError(SupportError):
    """An internal server error occurred."""
    _ERROR_CODE = "InternalServerError"


class ThrottlingException(SupportError):
    """You have exceeded the maximum allowed TPS (Transactions Per Second) for the
    operations.
    """

    _ERROR_CODE = "ThrottlingException"


EXCEPTIONS: dict[str, type[SupportError]] = {
    "AttachmentIdNotFound": AttachmentIdNotFound,
    "AttachmentLimitExceeded": AttachmentLimitExceeded,
    "AttachmentSetExpired": AttachmentSetExpired,
    "AttachmentSetIdNotFound": AttachmentSetIdNotFound,
    "AttachmentSetSizeLimitExceeded": AttachmentSetSizeLimitExceeded,
    "CaseCreationLimitExceeded": CaseCreationLimitExceeded,
    "CaseIdNotFound": CaseIdNotFound,
    "DescribeAttachmentLimitExceeded": DescribeAttachmentLimitExceeded,
    "InternalServerError": InternalServerError,
    "ThrottlingException": ThrottlingException,
}
