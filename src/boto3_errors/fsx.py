# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class FSxError(Boto3Error):
    _SERVICE = "fsx"


class AccessPointAlreadyOwnedByYou(FSxError):
    """An access point with that name already exists in the Amazon Web Services Region in
    your Amazon Web Services account.
    """

    _ERROR_CODE = "AccessPointAlreadyOwnedByYou"

    @property
    def error_code(self) -> str | None:
        """An error code indicating that an access point with that name already exists in
        the Amazon Web Services Region in your Amazon Web Services account.
        """
        return self.response.get("ErrorCode")


class ActiveDirectoryError(FSxError):
    """An Active Directory error."""
    _ERROR_CODE = "ActiveDirectoryError"

    @property
    def active_directory_id(self) -> str | None:
        """The directory ID of the directory that an error pertains to."""
        return self.response.get("ActiveDirectoryId")

    @property
    def type(self) -> str | None:
        """The type of Active Directory error."""
        return self.response.get("Type")


class BackupBeingCopied(FSxError):
    """You can't delete a backup while it's being copied."""
    _ERROR_CODE = "BackupBeingCopied"

    @property
    def backup_id(self) -> str | None:
        return self.response.get("BackupId")


class BackupInProgress(FSxError):
    """Another backup is already under way. Wait for completion before initiating
    additional backups of this file system.
    """

    _ERROR_CODE = "BackupInProgress"


class BackupNotFound(FSxError):
    """No Amazon FSx backups were found based upon the supplied parameters."""
    _ERROR_CODE = "BackupNotFound"


class BackupRestoring(FSxError):
    """You can't delete a backup while it's being used to restore a file system."""
    _ERROR_CODE = "BackupRestoring"

    @property
    def file_system_id(self) -> str | None:
        """The ID of a file system being restored from the backup."""
        return self.response.get("FileSystemId")


class BadRequest(FSxError):
    """A generic error indicating a failure with a client request."""
    _ERROR_CODE = "BadRequest"


class DataRepositoryAssociationNotFound(FSxError):
    """No data repository associations were found based upon the supplied parameters."""
    _ERROR_CODE = "DataRepositoryAssociationNotFound"


class DataRepositoryTaskEnded(FSxError):
    """The data repository task could not be canceled because the task has already ended."""
    _ERROR_CODE = "DataRepositoryTaskEnded"


class DataRepositoryTaskExecuting(FSxError):
    """An existing data repository task is currently executing on the file system. Wait
    until the existing task has completed, then create the new task.
    """

    _ERROR_CODE = "DataRepositoryTaskExecuting"


class DataRepositoryTaskNotFound(FSxError):
    """The data repository task or tasks you specified could not be found."""
    _ERROR_CODE = "DataRepositoryTaskNotFound"


class FileCacheNotFound(FSxError):
    """No caches were found based upon supplied parameters."""
    _ERROR_CODE = "FileCacheNotFound"


class FileSystemNotFound(FSxError):
    """No Amazon FSx file systems were found based upon supplied parameters."""
    _ERROR_CODE = "FileSystemNotFound"


class IncompatibleParameterError(FSxError):
    """The error returned when a second request is received with the same client request
    token but different parameters settings. A client request token should always
    uniquely identify a single request.
    """

    _ERROR_CODE = "IncompatibleParameterError"

    @property
    def parameter(self) -> str | None:
        """A parameter that is incompatible with the earlier request."""
        return self.response.get("Parameter")


class IncompatibleRegionForMultiAZ(FSxError):
    """Amazon FSx doesn't support Multi-AZ Windows File Server copy backup in the
    destination Region, so the copied backup can't be restored.
    """

    _ERROR_CODE = "IncompatibleRegionForMultiAZ"


class InternalServerError(FSxError):
    """A generic error indicating a server-side failure."""
    _ERROR_CODE = "InternalServerError"


class InvalidAccessPoint(FSxError):
    """The access point specified doesn't exist."""
    _ERROR_CODE = "InvalidAccessPoint"

    @property
    def error_code(self) -> str | None:
        """An error code indicating that the access point specified doesn't exist."""
        return self.response.get("ErrorCode")


class InvalidDataRepositoryType(FSxError):
    """You have filtered the response to a data repository type that is not supported."""
    _ERROR_CODE = "InvalidDataRepositoryType"


class InvalidDestinationKmsKey(FSxError):
    """The Key Management Service (KMS) key of the destination backup is not valid."""
    _ERROR_CODE = "InvalidDestinationKmsKey"


class InvalidExportPath(FSxError):
    """The path provided for data repository export isn't valid."""
    _ERROR_CODE = "InvalidExportPath"


class InvalidImportPath(FSxError):
    """The path provided for data repository import isn't valid."""
    _ERROR_CODE = "InvalidImportPath"


class InvalidNetworkSettings(FSxError):
    """One or more network settings specified in the request are invalid."""
    _ERROR_CODE = "InvalidNetworkSettings"

    @property
    def invalid_route_table_id(self) -> str | None:
        """The route table ID is either invalid or not part of the VPC specified."""
        return self.response.get("InvalidRouteTableId")

    @property
    def invalid_security_group_id(self) -> str | None:
        """The security group ID is either invalid or not part of the VPC specified."""
        return self.response.get("InvalidSecurityGroupId")

    @property
    def invalid_subnet_id(self) -> str | None:
        """The subnet ID that is either invalid or not part of the VPC specified."""
        return self.response.get("InvalidSubnetId")


class InvalidPerUnitStorageThroughput(FSxError):
    """An invalid value for `PerUnitStorageThroughput` was provided. Please create your
    file system again, using a valid value.
    """

    _ERROR_CODE = "InvalidPerUnitStorageThroughput"


class InvalidRegion(FSxError):
    """The Region provided for `SourceRegion` is not valid or is in a different Amazon Web
    Services partition.
    """

    _ERROR_CODE = "InvalidRegion"


class InvalidRequest(FSxError):
    """The action or operation requested is invalid. Verify that the action is typed
    correctly.
    """

    _ERROR_CODE = "InvalidRequest"

    @property
    def error_code(self) -> str | None:
        """An error code indicating that the action or operation requested is invalid."""
        return self.response.get("ErrorCode")


class InvalidSourceKmsKey(FSxError):
    """The Key Management Service (KMS) key of the source backup is not valid."""
    _ERROR_CODE = "InvalidSourceKmsKey"


class MissingFileCacheConfiguration(FSxError):
    """A cache configuration is required for this operation."""
    _ERROR_CODE = "MissingFileCacheConfiguration"


class MissingFileSystemConfiguration(FSxError):
    """A file system configuration is required for this operation."""
    _ERROR_CODE = "MissingFileSystemConfiguration"


class MissingVolumeConfiguration(FSxError):
    """A volume configuration is required for this operation."""
    _ERROR_CODE = "MissingVolumeConfiguration"


class NotServiceResourceError(FSxError):
    """The resource specified for the tagging operation is not a resource type owned by
    Amazon FSx. Use the API of the relevant service to perform the operation.
    """

    _ERROR_CODE = "NotServiceResourceError"

    @property
    def resource_arn(self) -> str | None:
        """The Amazon Resource Name (ARN) of the non-Amazon FSx resource."""
        return self.response.get("ResourceARN")


class ResourceDoesNotSupportTagging(FSxError):
    """The resource specified does not support tagging."""
    _ERROR_CODE = "ResourceDoesNotSupportTagging"

    @property
    def resource_arn(self) -> str | None:
        """The Amazon Resource Name (ARN) of the resource that doesn't support tagging."""
        return self.response.get("ResourceARN")


class ResourceNotFound(FSxError):
    """The resource specified by the Amazon Resource Name (ARN) can't be found."""
    _ERROR_CODE = "ResourceNotFound"

    @property
    def resource_arn(self) -> str | None:
        """The resource ARN of the resource that can't be found."""
        return self.response.get("ResourceARN")


class S3AccessPointAttachmentNotFound(FSxError):
    """The access point specified was not found."""
    _ERROR_CODE = "S3AccessPointAttachmentNotFound"


class ServiceLimitExceeded(FSxError):
    """An error indicating that a particular service limit was exceeded. You can increase
    some service limits by contacting Amazon Web Services Support.
    """

    _ERROR_CODE = "ServiceLimitExceeded"

    @property
    def limit(self) -> str | None:
        """Enumeration of the service limit that was exceeded."""
        return self.response.get("Limit")


class SnapshotNotFound(FSxError):
    """No Amazon FSx snapshots were found based on the supplied parameters."""
    _ERROR_CODE = "SnapshotNotFound"


class SourceBackupUnavailable(FSxError):
    """The request was rejected because the lifecycle status of the source backup isn't
    `AVAILABLE`.
    """

    _ERROR_CODE = "SourceBackupUnavailable"

    @property
    def backup_id(self) -> str | None:
        return self.response.get("BackupId")


class StorageVirtualMachineNotFound(FSxError):
    """No FSx for ONTAP SVMs were found based upon the supplied parameters."""
    _ERROR_CODE = "StorageVirtualMachineNotFound"


class TooManyAccessPoints(FSxError):
    """You have reached the maximum number of S3 access points attachments allowed for your
    account in this Amazon Web Services Region, or for the file system. For more
    information, or to request an increase, see Service quotas on FSx resources in the
    FSx for OpenZFS User Guide.
    """

    _ERROR_CODE = "TooManyAccessPoints"

    @property
    def error_code(self) -> str | None:
        """An error code indicating that you have reached the maximum number of S3 access
        points attachments allowed for your account in this Amazon Web Services Region,
        or for the file system.
        """
        return self.response.get("ErrorCode")


class UnsupportedOperation(FSxError):
    """The requested operation is not supported for this resource or API."""
    _ERROR_CODE = "UnsupportedOperation"


class VolumeNotFound(FSxError):
    """No Amazon FSx volumes were found based upon the supplied parameters."""
    _ERROR_CODE = "VolumeNotFound"


EXCEPTIONS: dict[str, type[FSxError]] = {
    "AccessPointAlreadyOwnedByYou": AccessPointAlreadyOwnedByYou,
    "ActiveDirectoryError": ActiveDirectoryError,
    "BackupBeingCopied": BackupBeingCopied,
    "BackupInProgress": BackupInProgress,
    "BackupNotFound": BackupNotFound,
    "BackupRestoring": BackupRestoring,
    "BadRequest": BadRequest,
    "DataRepositoryAssociationNotFound": DataRepositoryAssociationNotFound,
    "DataRepositoryTaskEnded": DataRepositoryTaskEnded,
    "DataRepositoryTaskExecuting": DataRepositoryTaskExecuting,
    "DataRepositoryTaskNotFound": DataRepositoryTaskNotFound,
    "FileCacheNotFound": FileCacheNotFound,
    "FileSystemNotFound": FileSystemNotFound,
    "IncompatibleParameterError": IncompatibleParameterError,
    "IncompatibleRegionForMultiAZ": IncompatibleRegionForMultiAZ,
    "InternalServerError": InternalServerError,
    "InvalidAccessPoint": InvalidAccessPoint,
    "InvalidDataRepositoryType": InvalidDataRepositoryType,
    "InvalidDestinationKmsKey": InvalidDestinationKmsKey,
    "InvalidExportPath": InvalidExportPath,
    "InvalidImportPath": InvalidImportPath,
    "InvalidNetworkSettings": InvalidNetworkSettings,
    "InvalidPerUnitStorageThroughput": InvalidPerUnitStorageThroughput,
    "InvalidRegion": InvalidRegion,
    "InvalidRequest": InvalidRequest,
    "InvalidSourceKmsKey": InvalidSourceKmsKey,
    "MissingFileCacheConfiguration": MissingFileCacheConfiguration,
    "MissingFileSystemConfiguration": MissingFileSystemConfiguration,
    "MissingVolumeConfiguration": MissingVolumeConfiguration,
    "NotServiceResourceError": NotServiceResourceError,
    "ResourceDoesNotSupportTagging": ResourceDoesNotSupportTagging,
    "ResourceNotFound": ResourceNotFound,
    "S3AccessPointAttachmentNotFound": S3AccessPointAttachmentNotFound,
    "ServiceLimitExceeded": ServiceLimitExceeded,
    "SnapshotNotFound": SnapshotNotFound,
    "SourceBackupUnavailable": SourceBackupUnavailable,
    "StorageVirtualMachineNotFound": StorageVirtualMachineNotFound,
    "TooManyAccessPoints": TooManyAccessPoints,
    "UnsupportedOperation": UnsupportedOperation,
    "VolumeNotFound": VolumeNotFound,
}
