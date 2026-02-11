# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class DocDBError(Boto3Error):
    _SERVICE = "docdb"


class AuthorizationNotFoundFault(DocDBError):
    """The specified CIDR IP or Amazon EC2 security group isn't authorized for the
    specified security group.

    Amazon DocumentDB also might not be authorized to perform necessary actions on your
    behalf using IAM.
    """

    _ERROR_CODE = "AuthorizationNotFound"


class CertificateNotFoundFault(DocDBError):
    """`CertificateIdentifier` doesn't refer to an existing certificate."""
    _ERROR_CODE = "CertificateNotFound"


class DBClusterAlreadyExistsFault(DocDBError):
    """You already have a cluster with the given identifier."""
    _ERROR_CODE = "DBClusterAlreadyExistsFault"


class DBClusterNotFoundFault(DocDBError):
    """`DBClusterIdentifier` doesn't refer to an existing cluster."""
    _ERROR_CODE = "DBClusterNotFoundFault"


class DBClusterParameterGroupNotFoundFault(DocDBError):
    """`DBClusterParameterGroupName` doesn't refer to an existing cluster parameter group."""
    _ERROR_CODE = "DBClusterParameterGroupNotFound"


class DBClusterQuotaExceededFault(DocDBError):
    """The cluster can't be created because you have reached the maximum allowed quota of
    clusters.
    """

    _ERROR_CODE = "DBClusterQuotaExceededFault"


class DBClusterSnapshotAlreadyExistsFault(DocDBError):
    """You already have a cluster snapshot with the given identifier."""
    _ERROR_CODE = "DBClusterSnapshotAlreadyExistsFault"


class DBClusterSnapshotNotFoundFault(DocDBError):
    """`DBClusterSnapshotIdentifier` doesn't refer to an existing cluster snapshot."""
    _ERROR_CODE = "DBClusterSnapshotNotFoundFault"


class DBInstanceAlreadyExistsFault(DocDBError):
    """You already have a instance with the given identifier."""
    _ERROR_CODE = "DBInstanceAlreadyExists"


class DBInstanceNotFoundFault(DocDBError):
    """`DBInstanceIdentifier` doesn't refer to an existing instance."""
    _ERROR_CODE = "DBInstanceNotFound"


class DBParameterGroupAlreadyExistsFault(DocDBError):
    """A parameter group with the same name already exists."""
    _ERROR_CODE = "DBParameterGroupAlreadyExists"


class DBParameterGroupNotFoundFault(DocDBError):
    """`DBParameterGroupName` doesn't refer to an existing parameter group."""
    _ERROR_CODE = "DBParameterGroupNotFound"


class DBParameterGroupQuotaExceededFault(DocDBError):
    """This request would cause you to exceed the allowed number of parameter groups."""
    _ERROR_CODE = "DBParameterGroupQuotaExceeded"


class DBSecurityGroupNotFoundFault(DocDBError):
    """`DBSecurityGroupName` doesn't refer to an existing security group."""
    _ERROR_CODE = "DBSecurityGroupNotFound"


class DBSnapshotAlreadyExistsFault(DocDBError):
    """`DBSnapshotIdentifier` is already being used by an existing snapshot."""
    _ERROR_CODE = "DBSnapshotAlreadyExists"


class DBSnapshotNotFoundFault(DocDBError):
    """`DBSnapshotIdentifier` doesn't refer to an existing snapshot."""
    _ERROR_CODE = "DBSnapshotNotFound"


class DBSubnetGroupAlreadyExistsFault(DocDBError):
    """`DBSubnetGroupName` is already being used by an existing subnet group."""
    _ERROR_CODE = "DBSubnetGroupAlreadyExists"


class DBSubnetGroupDoesNotCoverEnoughAZs(DocDBError):
    """Subnets in the subnet group should cover at least two Availability Zones unless
    there is only one Availability Zone.
    """

    _ERROR_CODE = "DBSubnetGroupDoesNotCoverEnoughAZs"


class DBSubnetGroupNotFoundFault(DocDBError):
    """`DBSubnetGroupName` doesn't refer to an existing subnet group."""
    _ERROR_CODE = "DBSubnetGroupNotFoundFault"


class DBSubnetGroupQuotaExceededFault(DocDBError):
    """The request would cause you to exceed the allowed number of subnet groups."""
    _ERROR_CODE = "DBSubnetGroupQuotaExceeded"


class DBSubnetQuotaExceededFault(DocDBError):
    """The request would cause you to exceed the allowed number of subnets in a subnet
    group.
    """

    _ERROR_CODE = "DBSubnetQuotaExceededFault"


class DBUpgradeDependencyFailureFault(DocDBError):
    """The upgrade failed because a resource that the depends on can't be modified."""
    _ERROR_CODE = "DBUpgradeDependencyFailure"


class EventSubscriptionQuotaExceededFault(DocDBError):
    """You have reached the maximum number of event subscriptions."""
    _ERROR_CODE = "EventSubscriptionQuotaExceeded"


class GlobalClusterAlreadyExistsFault(DocDBError):
    """The `GlobalClusterIdentifier` already exists. Choose a new global cluster identifier
    (unique name) to create a new global cluster.
    """

    _ERROR_CODE = "GlobalClusterAlreadyExistsFault"


class GlobalClusterNotFoundFault(DocDBError):
    """The `GlobalClusterIdentifier` doesn't refer to an existing global cluster."""
    _ERROR_CODE = "GlobalClusterNotFoundFault"


class GlobalClusterQuotaExceededFault(DocDBError):
    """The number of global clusters for this account is already at the maximum allowed."""
    _ERROR_CODE = "GlobalClusterQuotaExceededFault"


class InstanceQuotaExceededFault(DocDBError):
    """The request would cause you to exceed the allowed number of instances."""
    _ERROR_CODE = "InstanceQuotaExceeded"


class InsufficientDBClusterCapacityFault(DocDBError):
    """The cluster doesn't have enough capacity for the current operation."""
    _ERROR_CODE = "InsufficientDBClusterCapacityFault"


class InsufficientDBInstanceCapacityFault(DocDBError):
    """The specified instance class isn't available in the specified Availability Zone."""
    _ERROR_CODE = "InsufficientDBInstanceCapacity"


class InsufficientStorageClusterCapacityFault(DocDBError):
    """There is not enough storage available for the current action. You might be able to
    resolve this error by updating your subnet group to use different Availability Zones
    that have more storage available.
    """

    _ERROR_CODE = "InsufficientStorageClusterCapacity"


class InvalidDBClusterSnapshotStateFault(DocDBError):
    """The provided value isn't a valid cluster snapshot state."""
    _ERROR_CODE = "InvalidDBClusterSnapshotStateFault"


class InvalidDBClusterStateFault(DocDBError):
    """The cluster isn't in a valid state."""
    _ERROR_CODE = "InvalidDBClusterStateFault"


class InvalidDBInstanceStateFault(DocDBError):
    """The specified instance isn't in the available state."""
    _ERROR_CODE = "InvalidDBInstanceState"


class InvalidDBParameterGroupStateFault(DocDBError):
    """The parameter group is in use, or it is in a state that is not valid. If you are
    trying to delete the parameter group, you can't delete it when the parameter group
    is in this state.
    """

    _ERROR_CODE = "InvalidDBParameterGroupState"


class InvalidDBSecurityGroupStateFault(DocDBError):
    """The state of the security group doesn't allow deletion."""
    _ERROR_CODE = "InvalidDBSecurityGroupState"


class InvalidDBSnapshotStateFault(DocDBError):
    """The state of the snapshot doesn't allow deletion."""
    _ERROR_CODE = "InvalidDBSnapshotState"


class InvalidDBSubnetGroupStateFault(DocDBError):
    """The subnet group can't be deleted because it's in use."""
    _ERROR_CODE = "InvalidDBSubnetGroupStateFault"


class InvalidDBSubnetStateFault(DocDBError):
    """The subnet isn't in the available state."""
    _ERROR_CODE = "InvalidDBSubnetStateFault"


class InvalidEventSubscriptionStateFault(DocDBError):
    """Someone else might be modifying a subscription. Wait a few seconds, and try again."""
    _ERROR_CODE = "InvalidEventSubscriptionState"


class InvalidGlobalClusterStateFault(DocDBError):
    """The requested operation can't be performed while the cluster is in this state."""
    _ERROR_CODE = "InvalidGlobalClusterStateFault"


class InvalidRestoreFault(DocDBError):
    """You cannot restore from a virtual private cloud (VPC) backup to a non-VPC DB
    instance.
    """

    _ERROR_CODE = "InvalidRestoreFault"


class InvalidSubnet(DocDBError):
    """The requested subnet is not valid, or multiple subnets were requested that are not
    all in a common virtual private cloud (VPC).
    """

    _ERROR_CODE = "InvalidSubnet"


class InvalidVPCNetworkStateFault(DocDBError):
    """The subnet group doesn't cover all Availability Zones after it is created because of
    changes that were made.
    """

    _ERROR_CODE = "InvalidVPCNetworkStateFault"


class KMSKeyNotAccessibleFault(DocDBError):
    """An error occurred when accessing an KMS key."""
    _ERROR_CODE = "KMSKeyNotAccessibleFault"


class NetworkTypeNotSupported(DocDBError):
    """The network type is not supported by either `DBSubnetGroup` or the DB engine
    version.
    """

    _ERROR_CODE = "NetworkTypeNotSupported"


class ResourceNotFoundFault(DocDBError):
    """The specified resource ID was not found."""
    _ERROR_CODE = "ResourceNotFoundFault"


class SNSInvalidTopicFault(DocDBError):
    """Amazon SNS has responded that there is a problem with the specified topic."""
    _ERROR_CODE = "SNSInvalidTopic"


class SNSNoAuthorizationFault(DocDBError):
    """You do not have permission to publish to the SNS topic Amazon Resource Name (ARN)."""
    _ERROR_CODE = "SNSNoAuthorization"


class SNSTopicArnNotFoundFault(DocDBError):
    """The SNS topic Amazon Resource Name (ARN) does not exist."""
    _ERROR_CODE = "SNSTopicArnNotFound"


class SharedSnapshotQuotaExceededFault(DocDBError):
    """You have exceeded the maximum number of accounts that you can share a manual DB
    snapshot with.
    """

    _ERROR_CODE = "SharedSnapshotQuotaExceeded"


class SnapshotQuotaExceededFault(DocDBError):
    """The request would cause you to exceed the allowed number of snapshots."""
    _ERROR_CODE = "SnapshotQuotaExceeded"


class SourceNotFoundFault(DocDBError):
    """The requested source could not be found."""
    _ERROR_CODE = "SourceNotFound"


class StorageQuotaExceededFault(DocDBError):
    """The request would cause you to exceed the allowed amount of storage available across
    all instances.
    """

    _ERROR_CODE = "StorageQuotaExceeded"


class StorageTypeNotSupportedFault(DocDBError):
    """Storage of the specified `StorageType` can't be associated with the DB instance."""
    _ERROR_CODE = "StorageTypeNotSupported"


class SubnetAlreadyInUse(DocDBError):
    """The subnet is already in use in the Availability Zone."""
    _ERROR_CODE = "SubnetAlreadyInUse"


class SubscriptionAlreadyExistFault(DocDBError):
    """The provided subscription name already exists."""
    _ERROR_CODE = "SubscriptionAlreadyExist"


class SubscriptionCategoryNotFoundFault(DocDBError):
    """The provided category does not exist."""
    _ERROR_CODE = "SubscriptionCategoryNotFound"


class SubscriptionNotFoundFault(DocDBError):
    """The subscription name does not exist."""
    _ERROR_CODE = "SubscriptionNotFound"


EXCEPTIONS: dict[str, type[DocDBError]] = {
    "AuthorizationNotFound": AuthorizationNotFoundFault,
    "CertificateNotFound": CertificateNotFoundFault,
    "DBClusterAlreadyExistsFault": DBClusterAlreadyExistsFault,
    "DBClusterNotFoundFault": DBClusterNotFoundFault,
    "DBClusterParameterGroupNotFound": DBClusterParameterGroupNotFoundFault,
    "DBClusterQuotaExceededFault": DBClusterQuotaExceededFault,
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
    "EventSubscriptionQuotaExceeded": EventSubscriptionQuotaExceededFault,
    "GlobalClusterAlreadyExistsFault": GlobalClusterAlreadyExistsFault,
    "GlobalClusterNotFoundFault": GlobalClusterNotFoundFault,
    "GlobalClusterQuotaExceededFault": GlobalClusterQuotaExceededFault,
    "InstanceQuotaExceeded": InstanceQuotaExceededFault,
    "InsufficientDBClusterCapacityFault": InsufficientDBClusterCapacityFault,
    "InsufficientDBInstanceCapacity": InsufficientDBInstanceCapacityFault,
    "InsufficientStorageClusterCapacity": InsufficientStorageClusterCapacityFault,
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
    "NetworkTypeNotSupported": NetworkTypeNotSupported,
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
