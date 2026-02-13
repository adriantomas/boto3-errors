# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class ImportExportError(Boto3Error):
    _SERVICE = "importexport"


class BucketPermissionException(ImportExportError):
    """The account specified does not have the appropriate bucket permissions."""
    _ERROR_CODE = "BucketPermissionException"


class CanceledJobIdException(ImportExportError):
    """The specified job ID has been canceled and is no longer valid."""
    _ERROR_CODE = "CanceledJobIdException"


class CreateJobQuotaExceededException(ImportExportError):
    """Each account can create only a certain number of jobs per day. If you need to create
    more than this, please contact awsimportexport@amazon.com to explain your particular
    use case.
    """

    _ERROR_CODE = "CreateJobQuotaExceededException"


class ExpiredJobIdException(ImportExportError):
    """Indicates that the specified job has expired out of the system."""
    _ERROR_CODE = "ExpiredJobIdException"


class InvalidAccessKeyIdException(ImportExportError):
    """The AWS Access Key ID specified in the request did not match the manifest's
    accessKeyId value. The manifest and the request authentication must use the same AWS
    Access Key ID.
    """

    _ERROR_CODE = "InvalidAccessKeyIdException"


class InvalidAddressException(ImportExportError):
    """The address specified in the manifest is invalid."""
    _ERROR_CODE = "InvalidAddressException"


class InvalidCustomsException(ImportExportError):
    """One or more customs parameters was invalid. Please correct and resubmit."""
    _ERROR_CODE = "InvalidCustomsException"


class InvalidFileSystemException(ImportExportError):
    """File system specified in export manifest is invalid."""
    _ERROR_CODE = "InvalidFileSystemException"


class InvalidJobIdException(ImportExportError):
    """The JOBID was missing, not found, or not associated with the AWS account."""
    _ERROR_CODE = "InvalidJobIdException"


class InvalidManifestFieldException(ImportExportError):
    """One or more manifest fields was invalid. Please correct and resubmit."""
    _ERROR_CODE = "InvalidManifestFieldException"


class InvalidParameterException(ImportExportError):
    """One or more parameters had an invalid value."""
    _ERROR_CODE = "InvalidParameterException"


class InvalidVersionException(ImportExportError):
    """The client tool version is invalid."""
    _ERROR_CODE = "InvalidVersionException"


class MalformedManifestException(ImportExportError):
    """Your manifest is not well-formed."""
    _ERROR_CODE = "MalformedManifestException"


class MissingCustomsException(ImportExportError):
    """One or more required customs parameters was missing from the manifest."""
    _ERROR_CODE = "MissingCustomsException"


class MissingManifestFieldException(ImportExportError):
    """One or more required fields were missing from the manifest file. Please correct and
    resubmit.
    """

    _ERROR_CODE = "MissingManifestFieldException"


class MissingParameterException(ImportExportError):
    """One or more required parameters was missing from the request."""
    _ERROR_CODE = "MissingParameterException"


class MultipleRegionsException(ImportExportError):
    """Your manifest file contained buckets from multiple regions. A job is restricted to
    buckets from one region. Please correct and resubmit.
    """

    _ERROR_CODE = "MultipleRegionsException"


class NoSuchBucketException(ImportExportError):
    """The specified bucket does not exist. Create the specified bucket or change the
    manifest's bucket, exportBucket, or logBucket field to a bucket that the account, as
    specified by the manifest's Access Key ID, has write permissions to.
    """

    _ERROR_CODE = "NoSuchBucketException"


class UnableToCancelJobIdException(ImportExportError):
    """AWS Import/Export cannot cancel the job"""
    _ERROR_CODE = "UnableToCancelJobIdException"


class UnableToUpdateJobIdException(ImportExportError):
    """AWS Import/Export cannot update the job"""
    _ERROR_CODE = "UnableToUpdateJobIdException"


EXCEPTIONS: dict[str, type[ImportExportError]] = {
    "BucketPermissionException": BucketPermissionException,
    "CanceledJobIdException": CanceledJobIdException,
    "CreateJobQuotaExceededException": CreateJobQuotaExceededException,
    "ExpiredJobIdException": ExpiredJobIdException,
    "InvalidAccessKeyIdException": InvalidAccessKeyIdException,
    "InvalidAddressException": InvalidAddressException,
    "InvalidCustomsException": InvalidCustomsException,
    "InvalidFileSystemException": InvalidFileSystemException,
    "InvalidJobIdException": InvalidJobIdException,
    "InvalidManifestFieldException": InvalidManifestFieldException,
    "InvalidParameterException": InvalidParameterException,
    "InvalidVersionException": InvalidVersionException,
    "MalformedManifestException": MalformedManifestException,
    "MissingCustomsException": MissingCustomsException,
    "MissingManifestFieldException": MissingManifestFieldException,
    "MissingParameterException": MissingParameterException,
    "MultipleRegionsException": MultipleRegionsException,
    "NoSuchBucketException": NoSuchBucketException,
    "UnableToCancelJobIdException": UnableToCancelJobIdException,
    "UnableToUpdateJobIdException": UnableToUpdateJobIdException,
}
