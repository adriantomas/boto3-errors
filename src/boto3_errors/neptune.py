# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class NeptuneError(Boto3Error):
    _SERVICE = "neptune"


class AuthorizationNotFoundFault(NeptuneError):
    """Specified CIDRIP or EC2 security group is not authorized for the specified DB
    security group.

    Neptune may not also be authorized via IAM to perform necessary actions on your
    behalf.
    """

    _ERROR_CODE = "AuthorizationNotFound"


class CertificateNotFoundFault(NeptuneError):
    """CertificateIdentifier does not refer to an existing certificate."""
    _ERROR_CODE = "CertificateNotFound"


class DBClusterAlreadyExistsFault(NeptuneError):
    """User already has a DB cluster with the given identifier."""
    _ERROR_CODE = "DBClusterAlreadyExistsFault"


class DBClusterEndpointAlreadyExistsFault(NeptuneError):
    """The specified custom endpoint cannot be created because it already exists."""
    _ERROR_CODE = "DBClusterEndpointAlreadyExistsFault"


class DBClusterEndpointNotFoundFault(NeptuneError):
    """The specified custom endpoint doesn't exist."""
    _ERROR_CODE = "DBClusterEndpointNotFoundFault"


class DBClusterEndpointQuotaExceededFault(NeptuneError):
    """The cluster already has the maximum number of custom endpoints."""
    _ERROR_CODE = "DBClusterEndpointQuotaExceededFault"


class DBClusterNotFoundFault(NeptuneError):
    """DBClusterIdentifier does not refer to an existing DB cluster."""
    _ERROR_CODE = "DBClusterNotFoundFault"


class DBClusterParameterGroupNotFoundFault(NeptuneError):
    """DBClusterParameterGroupName does not refer to an existing DB Cluster parameter
    group.
    """

    _ERROR_CODE = "DBClusterParameterGroupNotFound"


class DBClusterQuotaExceededFault(NeptuneError):
    """User attempted to create a new DB cluster and the user has already reached the
    maximum allowed DB cluster quota.
    """

    _ERROR_CODE = "DBClusterQuotaExceededFault"


class DBClusterRoleAlreadyExistsFault(NeptuneError):
    """The specified IAM role Amazon Resource Name (ARN) is already associated with the
    specified DB cluster.
    """

    _ERROR_CODE = "DBClusterRoleAlreadyExists"


class DBClusterRoleNotFoundFault(NeptuneError):
    """The specified IAM role Amazon Resource Name (ARN) is not associated with the
    specified DB cluster.
    """

    _ERROR_CODE = "DBClusterRoleNotFound"


class DBClusterRoleQuotaExceededFault(NeptuneError):
    """You have exceeded the maximum number of IAM roles that can be associated with the
    specified DB cluster.
    """

    _ERROR_CODE = "DBClusterRoleQuotaExceeded"


class DBClusterSnapshotAlreadyExistsFault(NeptuneError):
    """User already has a DB cluster snapshot with the given identifier."""
    _ERROR_CODE = "DBClusterSnapshotAlreadyExistsFault"


class DBClusterSnapshotNotFoundFault(NeptuneError):
    """DBClusterSnapshotIdentifier does not refer to an existing DB cluster snapshot."""
    _ERROR_CODE = "DBClusterSnapshotNotFoundFault"


class DBInstanceAlreadyExistsFault(NeptuneError):
    """User already has a DB instance with the given identifier."""
    _ERROR_CODE = "DBInstanceAlreadyExists"


class DBInstanceNotFoundFault(NeptuneError):
    """DBInstanceIdentifier does not refer to an existing DB instance."""
    _ERROR_CODE = "DBInstanceNotFound"


class DBParameterGroupAlreadyExistsFault(NeptuneError):
    """A DB parameter group with the same name exists."""
    _ERROR_CODE = "DBParameterGroupAlreadyExists"


class DBParameterGroupNotFoundFault(NeptuneError):
    """DBParameterGroupName does not refer to an existing DB parameter group."""
    _ERROR_CODE = "DBParameterGroupNotFound"


class DBParameterGroupQuotaExceededFault(NeptuneError):
    """Request would result in user exceeding the allowed number of DB parameter groups."""
    _ERROR_CODE = "DBParameterGroupQuotaExceeded"


class DBSecurityGroupNotFoundFault(NeptuneError):
    """DBSecurityGroupName does not refer to an existing DB security group."""
    _ERROR_CODE = "DBSecurityGroupNotFound"


class DBSnapshotAlreadyExistsFault(NeptuneError):
    """DBSnapshotIdentifier is already used by an existing snapshot."""
    _ERROR_CODE = "DBSnapshotAlreadyExists"


class DBSnapshotNotFoundFault(NeptuneError):
    """DBSnapshotIdentifier does not refer to an existing DB snapshot."""
    _ERROR_CODE = "DBSnapshotNotFound"


class DBSubnetGroupAlreadyExistsFault(NeptuneError):
    """DBSubnetGroupName is already used by an existing DB subnet group."""
    _ERROR_CODE = "DBSubnetGroupAlreadyExists"


class DBSubnetGroupDoesNotCoverEnoughAZs(NeptuneError):
    """Subnets in the DB subnet group should cover at least two Availability Zones unless
    there is only one Availability Zone.
    """

    _ERROR_CODE = "DBSubnetGroupDoesNotCoverEnoughAZs"


class DBSubnetGroupNotFoundFault(NeptuneError):
    """DBSubnetGroupName does not refer to an existing DB subnet group."""
    _ERROR_CODE = "DBSubnetGroupNotFoundFault"


class DBSubnetGroupQuotaExceededFault(NeptuneError):
    """Request would result in user exceeding the allowed number of DB subnet groups."""
    _ERROR_CODE = "DBSubnetGroupQuotaExceeded"


class DBSubnetQuotaExceededFault(NeptuneError):
    """Request would result in user exceeding the allowed number of subnets in a DB subnet
    groups.
    """

    _ERROR_CODE = "DBSubnetQuotaExceededFault"


class DBUpgradeDependencyFailureFault(NeptuneError):
    """The DB upgrade failed because a resource the DB depends on could not be modified."""
    _ERROR_CODE = "DBUpgradeDependencyFailure"


class DomainNotFoundFault(NeptuneError):
    """Domain does not refer to an existing Active Directory Domain."""
    _ERROR_CODE = "DomainNotFoundFault"


class EventSubscriptionQuotaExceededFault(NeptuneError):
    """You have exceeded the number of events you can subscribe to."""
    _ERROR_CODE = "EventSubscriptionQuotaExceeded"


class GlobalClusterAlreadyExistsFault(NeptuneError):
    """The `GlobalClusterIdentifier` already exists. Choose a new global database
    identifier (unique name) to create a new global database cluster.
    """

    _ERROR_CODE = "GlobalClusterAlreadyExistsFault"


class GlobalClusterNotFoundFault(NeptuneError):
    """The `GlobalClusterIdentifier` doesn't refer to an existing global database cluster."""
    _ERROR_CODE = "GlobalClusterNotFoundFault"


class GlobalClusterQuotaExceededFault(NeptuneError):
    """The number of global database clusters for this account is already at the maximum
    allowed.
    """

    _ERROR_CODE = "GlobalClusterQuotaExceededFault"


class InstanceQuotaExceededFault(NeptuneError):
    """Request would result in user exceeding the allowed number of DB instances."""
    _ERROR_CODE = "InstanceQuotaExceeded"


class InsufficientDBClusterCapacityFault(NeptuneError):
    """The DB cluster does not have enough capacity for the current operation."""
    _ERROR_CODE = "InsufficientDBClusterCapacityFault"


class InsufficientDBInstanceCapacityFault(NeptuneError):
    """Specified DB instance class is not available in the specified Availability Zone."""
    _ERROR_CODE = "InsufficientDBInstanceCapacity"


class InsufficientStorageClusterCapacityFault(NeptuneError):
    """There is insufficient storage available for the current action. You may be able to
    resolve this error by updating your subnet group to use different Availability Zones
    that have more storage available.
    """

    _ERROR_CODE = "InsufficientStorageClusterCapacity"


class InvalidDBClusterEndpointStateFault(NeptuneError):
    """The requested operation cannot be performed on the endpoint while the endpoint is in
    this state.
    """

    _ERROR_CODE = "InvalidDBClusterEndpointStateFault"


class InvalidDBClusterSnapshotStateFault(NeptuneError):
    """The supplied value is not a valid DB cluster snapshot state."""
    _ERROR_CODE = "InvalidDBClusterSnapshotStateFault"


class InvalidDBClusterStateFault(NeptuneError):
    """The DB cluster is not in a valid state."""
    _ERROR_CODE = "InvalidDBClusterStateFault"


class InvalidDBInstanceStateFault(NeptuneError):
    """The specified DB instance is not in the available state."""
    _ERROR_CODE = "InvalidDBInstanceState"


class InvalidDBParameterGroupStateFault(NeptuneError):
    """The DB parameter group is in use or is in an invalid state. If you are attempting to
    delete the parameter group, you cannot delete it when the parameter group is in this
    state.
    """

    _ERROR_CODE = "InvalidDBParameterGroupState"


class InvalidDBSecurityGroupStateFault(NeptuneError):
    """The state of the DB security group does not allow deletion."""
    _ERROR_CODE = "InvalidDBSecurityGroupState"


class InvalidDBSnapshotStateFault(NeptuneError):
    """The state of the DB snapshot does not allow deletion."""
    _ERROR_CODE = "InvalidDBSnapshotState"


class InvalidDBSubnetGroupStateFault(NeptuneError):
    """The DB subnet group cannot be deleted because it is in use."""
    _ERROR_CODE = "InvalidDBSubnetGroupStateFault"


class InvalidDBSubnetStateFault(NeptuneError):
    """The DB subnet is not in the available state."""
    _ERROR_CODE = "InvalidDBSubnetStateFault"


class InvalidEventSubscriptionStateFault(NeptuneError):
    """The event subscription is in an invalid state."""
    _ERROR_CODE = "InvalidEventSubscriptionState"


class InvalidGlobalClusterStateFault(NeptuneError):
    """The global cluster is in an invalid state and can't perform the requested operation."""
    _ERROR_CODE = "InvalidGlobalClusterStateFault"


class InvalidRestoreFault(NeptuneError):
    """Cannot restore from vpc backup to non-vpc DB instance."""
    _ERROR_CODE = "InvalidRestoreFault"


class InvalidSubnet(NeptuneError):
    """The requested subnet is invalid, or multiple subnets were requested that are not all
    in a common VPC.
    """

    _ERROR_CODE = "InvalidSubnet"


class InvalidVPCNetworkStateFault(NeptuneError):
    """DB subnet group does not cover all Availability Zones after it is created because
    users' change.
    """

    _ERROR_CODE = "InvalidVPCNetworkStateFault"


class KMSKeyNotAccessibleFault(NeptuneError):
    """Error accessing KMS key."""
    _ERROR_CODE = "KMSKeyNotAccessibleFault"


class OptionGroupNotFoundFault(NeptuneError):
    """The designated option group could not be found."""
    _ERROR_CODE = "OptionGroupNotFoundFault"


class ProvisionedIopsNotAvailableInAZFault(NeptuneError):
    """Provisioned IOPS not available in the specified Availability Zone."""
    _ERROR_CODE = "ProvisionedIopsNotAvailableInAZFault"


class ResourceNotFoundFault(NeptuneError):
    """The specified resource ID was not found."""
    _ERROR_CODE = "ResourceNotFoundFault"


class SNSInvalidTopicFault(NeptuneError):
    """The SNS topic is invalid."""
    _ERROR_CODE = "SNSInvalidTopic"


class SNSNoAuthorizationFault(NeptuneError):
    """There is no SNS authorization."""
    _ERROR_CODE = "SNSNoAuthorization"


class SNSTopicArnNotFoundFault(NeptuneError):
    """The ARN of the SNS topic could not be found."""
    _ERROR_CODE = "SNSTopicArnNotFound"


class SharedSnapshotQuotaExceededFault(NeptuneError):
    """You have exceeded the maximum number of accounts that you can share a manual DB
    snapshot with.
    """

    _ERROR_CODE = "SharedSnapshotQuotaExceeded"


class SnapshotQuotaExceededFault(NeptuneError):
    """Request would result in user exceeding the allowed number of DB snapshots."""
    _ERROR_CODE = "SnapshotQuotaExceeded"


class SourceNotFoundFault(NeptuneError):
    """The source could not be found."""
    _ERROR_CODE = "SourceNotFound"


class StorageQuotaExceededFault(NeptuneError):
    """Request would result in user exceeding the allowed amount of storage available
    across all DB instances.
    """

    _ERROR_CODE = "StorageQuotaExceeded"


class StorageTypeNotSupportedFault(NeptuneError):
    """StorageType specified cannot be associated with the DB Instance."""
    _ERROR_CODE = "StorageTypeNotSupported"


class SubnetAlreadyInUse(NeptuneError):
    """The DB subnet is already in use in the Availability Zone."""
    _ERROR_CODE = "SubnetAlreadyInUse"


class SubscriptionAlreadyExistFault(NeptuneError):
    """This subscription already exists."""
    _ERROR_CODE = "SubscriptionAlreadyExist"


class SubscriptionCategoryNotFoundFault(NeptuneError):
    """The designated subscription category could not be found."""
    _ERROR_CODE = "SubscriptionCategoryNotFound"


class SubscriptionNotFoundFault(NeptuneError):
    """The designated subscription could not be found."""
    _ERROR_CODE = "SubscriptionNotFound"


EXCEPTIONS: dict[str, type[NeptuneError]] = {
    "AuthorizationNotFound": AuthorizationNotFoundFault,
    "CertificateNotFound": CertificateNotFoundFault,
    "DBClusterAlreadyExistsFault": DBClusterAlreadyExistsFault,
    "DBClusterEndpointAlreadyExistsFault": DBClusterEndpointAlreadyExistsFault,
    "DBClusterEndpointNotFoundFault": DBClusterEndpointNotFoundFault,
    "DBClusterEndpointQuotaExceededFault": DBClusterEndpointQuotaExceededFault,
    "DBClusterNotFoundFault": DBClusterNotFoundFault,
    "DBClusterParameterGroupNotFound": DBClusterParameterGroupNotFoundFault,
    "DBClusterQuotaExceededFault": DBClusterQuotaExceededFault,
    "DBClusterRoleAlreadyExists": DBClusterRoleAlreadyExistsFault,
    "DBClusterRoleNotFound": DBClusterRoleNotFoundFault,
    "DBClusterRoleQuotaExceeded": DBClusterRoleQuotaExceededFault,
    "DBClusterSnapshotAlreadyExistsFault": DBClusterSnapshotAlreadyExistsFault,
    "DBClusterSnapshotNotFoundFault": DBClusterSnapshotNotFoundFault,
    "DBInstanceAlreadyExists": DBInstanceAlreadyExistsFault,
    "DBInstanceNotFound": DBInstanceNotFoundFault,
    "DBParameterGroupAlreadyExists": DBParameterGroupAlreadyExistsFault,
    "DBParameterGroupNotFound": DBParameterGroupNotFoundFault,
    "DBParameterGroupQuotaExceeded": DBParameterGroupQuotaExceededFault,
    "DBSecurityGroupNotFound": DBSecurityGroupNotFoundFault,
    "DBSnapshotAlreadyExists": DBSnapshotAlreadyExistsFault,
    "DBSnapshotNotFound": DBSnapshotNotFoundFault,
    "DBSubnetGroupAlreadyExists": DBSubnetGroupAlreadyExistsFault,
    "DBSubnetGroupDoesNotCoverEnoughAZs": DBSubnetGroupDoesNotCoverEnoughAZs,
    "DBSubnetGroupNotFoundFault": DBSubnetGroupNotFoundFault,
    "DBSubnetGroupQuotaExceeded": DBSubnetGroupQuotaExceededFault,
    "DBSubnetQuotaExceededFault": DBSubnetQuotaExceededFault,
    "DBUpgradeDependencyFailure": DBUpgradeDependencyFailureFault,
    "DomainNotFoundFault": DomainNotFoundFault,
    "EventSubscriptionQuotaExceeded": EventSubscriptionQuotaExceededFault,
    "GlobalClusterAlreadyExistsFault": GlobalClusterAlreadyExistsFault,
    "GlobalClusterNotFoundFault": GlobalClusterNotFoundFault,
    "GlobalClusterQuotaExceededFault": GlobalClusterQuotaExceededFault,
    "InstanceQuotaExceeded": InstanceQuotaExceededFault,
    "InsufficientDBClusterCapacityFault": InsufficientDBClusterCapacityFault,
    "InsufficientDBInstanceCapacity": InsufficientDBInstanceCapacityFault,
    "InsufficientStorageClusterCapacity": InsufficientStorageClusterCapacityFault,
    "InvalidDBClusterEndpointStateFault": InvalidDBClusterEndpointStateFault,
    "InvalidDBClusterSnapshotStateFault": InvalidDBClusterSnapshotStateFault,
    "InvalidDBClusterStateFault": InvalidDBClusterStateFault,
    "InvalidDBInstanceState": InvalidDBInstanceStateFault,
    "InvalidDBParameterGroupState": InvalidDBParameterGroupStateFault,
    "InvalidDBSecurityGroupState": InvalidDBSecurityGroupStateFault,
    "InvalidDBSnapshotState": InvalidDBSnapshotStateFault,
    "InvalidDBSubnetGroupStateFault": InvalidDBSubnetGroupStateFault,
    "InvalidDBSubnetStateFault": InvalidDBSubnetStateFault,
    "InvalidEventSubscriptionState": InvalidEventSubscriptionStateFault,
    "InvalidGlobalClusterStateFault": InvalidGlobalClusterStateFault,
    "InvalidRestoreFault": InvalidRestoreFault,
    "InvalidSubnet": InvalidSubnet,
    "InvalidVPCNetworkStateFault": InvalidVPCNetworkStateFault,
    "KMSKeyNotAccessibleFault": KMSKeyNotAccessibleFault,
    "OptionGroupNotFoundFault": OptionGroupNotFoundFault,
    "ProvisionedIopsNotAvailableInAZFault": ProvisionedIopsNotAvailableInAZFault,
    "ResourceNotFoundFault": ResourceNotFoundFault,
    "SNSInvalidTopic": SNSInvalidTopicFault,
    "SNSNoAuthorization": SNSNoAuthorizationFault,
    "SNSTopicArnNotFound": SNSTopicArnNotFoundFault,
    "SharedSnapshotQuotaExceeded": SharedSnapshotQuotaExceededFault,
    "SnapshotQuotaExceeded": SnapshotQuotaExceededFault,
    "SourceNotFound": SourceNotFoundFault,
    "StorageQuotaExceeded": StorageQuotaExceededFault,
    "StorageTypeNotSupported": StorageTypeNotSupportedFault,
    "SubnetAlreadyInUse": SubnetAlreadyInUse,
    "SubscriptionAlreadyExist": SubscriptionAlreadyExistFault,
    "SubscriptionCategoryNotFound": SubscriptionCategoryNotFoundFault,
    "SubscriptionNotFound": SubscriptionNotFoundFault,
}
