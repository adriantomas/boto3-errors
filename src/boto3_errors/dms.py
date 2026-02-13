# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class DatabaseMigrationServiceError(Boto3Error):
    _SERVICE = "dms"


class AccessDeniedFault(DatabaseMigrationServiceError):
    """DMS was denied access to the endpoint. Check that the role is correctly configured."""
    _ERROR_CODE = "AccessDeniedFault"


class CollectorNotFoundFault(DatabaseMigrationServiceError):
    """The specified collector doesn't exist."""
    _ERROR_CODE = "CollectorNotFoundFault"


class FailedDependencyFault(DatabaseMigrationServiceError):
    """A dependency threw an exception."""
    _ERROR_CODE = "FailedDependencyFault"


class InsufficientResourceCapacityFault(DatabaseMigrationServiceError):
    """There are not enough resources allocated to the database migration."""
    _ERROR_CODE = "InsufficientResourceCapacityFault"


class InvalidCertificateFault(DatabaseMigrationServiceError):
    """The certificate was not valid."""
    _ERROR_CODE = "InvalidCertificateFault"


class InvalidOperationFault(DatabaseMigrationServiceError):
    """The action or operation requested isn't valid."""
    _ERROR_CODE = "InvalidOperationFault"


class InvalidResourceStateFault(DatabaseMigrationServiceError):
    """The resource is in a state that prevents it from being used for database migration."""
    _ERROR_CODE = "InvalidResourceStateFault"


class InvalidSubnet(DatabaseMigrationServiceError):
    """The subnet provided isn't valid."""
    _ERROR_CODE = "InvalidSubnet"


class KMSAccessDeniedFault(DatabaseMigrationServiceError):
    """The ciphertext references a key that doesn't exist or that the DMS account doesn't
    have access to.
    """

    _ERROR_CODE = "KMSAccessDeniedFault"


class KMSDisabledFault(DatabaseMigrationServiceError):
    """The specified KMS key isn't enabled."""
    _ERROR_CODE = "KMSDisabledFault"


class KMSFault(DatabaseMigrationServiceError):
    """An Key Management Service (KMS) error is preventing access to KMS."""
    _ERROR_CODE = "KMSFault"


class KMSInvalidStateFault(DatabaseMigrationServiceError):
    """The state of the specified KMS resource isn't valid for this request."""
    _ERROR_CODE = "KMSInvalidStateFault"


class KMSKeyNotAccessibleFault(DatabaseMigrationServiceError):
    """DMS cannot access the KMS key."""
    _ERROR_CODE = "KMSKeyNotAccessibleFault"


class KMSNotFoundFault(DatabaseMigrationServiceError):
    """The specified KMS entity or resource can't be found."""
    _ERROR_CODE = "KMSNotFoundFault"


class KMSThrottlingFault(DatabaseMigrationServiceError):
    """This request triggered KMS request throttling."""
    _ERROR_CODE = "KMSThrottlingFault"


class ReplicationSubnetGroupDoesNotCoverEnoughAZs(DatabaseMigrationServiceError):
    """The replication subnet group does not cover enough Availability Zones (AZs). Edit
    the replication subnet group and add more AZs.
    """

    _ERROR_CODE = "ReplicationSubnetGroupDoesNotCoverEnoughAZs"


class ResourceAlreadyExistsFault(DatabaseMigrationServiceError):
    """The resource you are attempting to create already exists."""
    _ERROR_CODE = "ResourceAlreadyExistsFault"

    @property
    def resource_arn(self) -> str | None:
        return self.response.get("resourceArn")


class ResourceNotFoundFault(DatabaseMigrationServiceError):
    """The resource could not be found."""
    _ERROR_CODE = "ResourceNotFoundFault"


class ResourceQuotaExceededFault(DatabaseMigrationServiceError):
    """The quota for this resource quota has been exceeded."""
    _ERROR_CODE = "ResourceQuotaExceededFault"


class S3AccessDeniedFault(DatabaseMigrationServiceError):
    """Insufficient privileges are preventing access to an Amazon S3 object."""
    _ERROR_CODE = "S3AccessDeniedFault"


class S3ResourceNotFoundFault(DatabaseMigrationServiceError):
    """A specified Amazon S3 bucket, bucket folder, or other object can't be found."""
    _ERROR_CODE = "S3ResourceNotFoundFault"


class SNSInvalidTopicFault(DatabaseMigrationServiceError):
    """The SNS topic is invalid."""
    _ERROR_CODE = "SNSInvalidTopicFault"


class SNSNoAuthorizationFault(DatabaseMigrationServiceError):
    """You are not authorized for the SNS subscription."""
    _ERROR_CODE = "SNSNoAuthorizationFault"


class StorageQuotaExceededFault(DatabaseMigrationServiceError):
    """The storage quota has been exceeded."""
    _ERROR_CODE = "StorageQuotaExceededFault"


class SubnetAlreadyInUse(DatabaseMigrationServiceError):
    """The specified subnet is already in use."""
    _ERROR_CODE = "SubnetAlreadyInUse"


class UpgradeDependencyFailureFault(DatabaseMigrationServiceError):
    """An upgrade dependency is preventing the database migration."""
    _ERROR_CODE = "UpgradeDependencyFailureFault"


EXCEPTIONS: dict[str, type[DatabaseMigrationServiceError]] = {
    "AccessDeniedFault": AccessDeniedFault,
    "CollectorNotFoundFault": CollectorNotFoundFault,
    "FailedDependencyFault": FailedDependencyFault,
    "InsufficientResourceCapacityFault": InsufficientResourceCapacityFault,
    "InvalidCertificateFault": InvalidCertificateFault,
    "InvalidOperationFault": InvalidOperationFault,
    "InvalidResourceStateFault": InvalidResourceStateFault,
    "InvalidSubnet": InvalidSubnet,
    "KMSAccessDeniedFault": KMSAccessDeniedFault,
    "KMSDisabledFault": KMSDisabledFault,
    "KMSFault": KMSFault,
    "KMSInvalidStateFault": KMSInvalidStateFault,
    "KMSKeyNotAccessibleFault": KMSKeyNotAccessibleFault,
    "KMSNotFoundFault": KMSNotFoundFault,
    "KMSThrottlingFault": KMSThrottlingFault,
    "ReplicationSubnetGroupDoesNotCoverEnoughAZs": ReplicationSubnetGroupDoesNotCoverEnoughAZs,
    "ResourceAlreadyExistsFault": ResourceAlreadyExistsFault,
    "ResourceNotFoundFault": ResourceNotFoundFault,
    "ResourceQuotaExceededFault": ResourceQuotaExceededFault,
    "S3AccessDeniedFault": S3AccessDeniedFault,
    "S3ResourceNotFoundFault": S3ResourceNotFoundFault,
    "SNSInvalidTopicFault": SNSInvalidTopicFault,
    "SNSNoAuthorizationFault": SNSNoAuthorizationFault,
    "StorageQuotaExceededFault": StorageQuotaExceededFault,
    "SubnetAlreadyInUse": SubnetAlreadyInUse,
    "UpgradeDependencyFailureFault": UpgradeDependencyFailureFault,
}
