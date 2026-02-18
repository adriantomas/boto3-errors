# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class ElastiCacheError(Boto3Error):
    _SERVICE = "elasticache"


class APICallRateForCustomerExceededFault(ElastiCacheError):
    """The customer has exceeded the allowed rate of API calls."""
    _ERROR_CODE = "APICallRateForCustomerExceeded"


class AuthorizationAlreadyExistsFault(ElastiCacheError):
    """The specified Amazon EC2 security group is already authorized for the specified
    cache security group.
    """

    _ERROR_CODE = "AuthorizationAlreadyExists"


class AuthorizationNotFoundFault(ElastiCacheError):
    """The specified Amazon EC2 security group is not authorized for the specified cache
    security group.
    """

    _ERROR_CODE = "AuthorizationNotFound"


class CacheClusterAlreadyExistsFault(ElastiCacheError):
    """You already have a cluster with the given identifier."""
    _ERROR_CODE = "CacheClusterAlreadyExists"


class CacheClusterNotFoundFault(ElastiCacheError):
    """The requested cluster ID does not refer to an existing cluster."""
    _ERROR_CODE = "CacheClusterNotFound"


class CacheParameterGroupAlreadyExistsFault(ElastiCacheError):
    """A cache parameter group with the requested name already exists."""
    _ERROR_CODE = "CacheParameterGroupAlreadyExists"


class CacheParameterGroupNotFoundFault(ElastiCacheError):
    """The requested cache parameter group name does not refer to an existing cache
    parameter group.
    """

    _ERROR_CODE = "CacheParameterGroupNotFound"


class CacheParameterGroupQuotaExceededFault(ElastiCacheError):
    """The request cannot be processed because it would exceed the maximum number of cache
    security groups.
    """

    _ERROR_CODE = "CacheParameterGroupQuotaExceeded"


class CacheSecurityGroupAlreadyExistsFault(ElastiCacheError):
    """A cache security group with the specified name already exists."""
    _ERROR_CODE = "CacheSecurityGroupAlreadyExists"


class CacheSecurityGroupNotFoundFault(ElastiCacheError):
    """The requested cache security group name does not refer to an existing cache security
    group.
    """

    _ERROR_CODE = "CacheSecurityGroupNotFound"


class CacheSecurityGroupQuotaExceededFault(ElastiCacheError):
    """The request cannot be processed because it would exceed the allowed number of cache
    security groups.
    """

    _ERROR_CODE = "QuotaExceeded.CacheSecurityGroup"


class CacheSubnetGroupAlreadyExistsFault(ElastiCacheError):
    """The requested cache subnet group name is already in use by an existing cache subnet
    group.
    """

    _ERROR_CODE = "CacheSubnetGroupAlreadyExists"


class CacheSubnetGroupInUse(ElastiCacheError):
    """The requested cache subnet group is currently in use."""
    _ERROR_CODE = "CacheSubnetGroupInUse"


class CacheSubnetGroupNotFoundFault(ElastiCacheError):
    """The requested cache subnet group name does not refer to an existing cache subnet
    group.
    """

    _ERROR_CODE = "CacheSubnetGroupNotFoundFault"


class CacheSubnetGroupQuotaExceededFault(ElastiCacheError):
    """The request cannot be processed because it would exceed the allowed number of cache
    subnet groups.
    """

    _ERROR_CODE = "CacheSubnetGroupQuotaExceeded"


class CacheSubnetQuotaExceededFault(ElastiCacheError):
    """The request cannot be processed because it would exceed the allowed number of
    subnets in a cache subnet group.
    """

    _ERROR_CODE = "CacheSubnetQuotaExceededFault"


class ClusterQuotaForCustomerExceededFault(ElastiCacheError):
    """The request cannot be processed because it would exceed the allowed number of
    clusters per customer.
    """

    _ERROR_CODE = "ClusterQuotaForCustomerExceeded"


class DefaultUserAssociatedToUserGroupFault(ElastiCacheError):
    """The default user assigned to the user group."""
    _ERROR_CODE = "DefaultUserAssociatedToUserGroup"


class DefaultUserRequired(ElastiCacheError):
    """You must add default user to a user group."""
    _ERROR_CODE = "DefaultUserRequired"


class DuplicateUserNameFault(ElastiCacheError):
    """A user with this username already exists."""
    _ERROR_CODE = "DuplicateUserName"


class GlobalReplicationGroupAlreadyExistsFault(ElastiCacheError):
    """The Global datastore name already exists."""
    _ERROR_CODE = "GlobalReplicationGroupAlreadyExistsFault"


class GlobalReplicationGroupNotFoundFault(ElastiCacheError):
    """The Global datastore does not exist"""
    _ERROR_CODE = "GlobalReplicationGroupNotFoundFault"


class InsufficientCacheClusterCapacityFault(ElastiCacheError):
    """The requested cache node type is not available in the specified Availability Zone.
    For more information, see InsufficientCacheClusterCapacity in the ElastiCache User
    Guide.
    """

    _ERROR_CODE = "InsufficientCacheClusterCapacity"


class InvalidARNFault(ElastiCacheError):
    """The requested Amazon Resource Name (ARN) does not refer to an existing resource."""
    _ERROR_CODE = "InvalidARN"


class InvalidCacheClusterStateFault(ElastiCacheError):
    """The requested cluster is not in the `available` state."""
    _ERROR_CODE = "InvalidCacheClusterState"


class InvalidCacheParameterGroupStateFault(ElastiCacheError):
    """The current state of the cache parameter group does not allow the requested
    operation to occur.
    """

    _ERROR_CODE = "InvalidCacheParameterGroupState"


class InvalidCacheSecurityGroupStateFault(ElastiCacheError):
    """The current state of the cache security group does not allow deletion."""
    _ERROR_CODE = "InvalidCacheSecurityGroupState"


class InvalidCredentialsException(ElastiCacheError):
    """You must enter valid credentials."""
    _ERROR_CODE = "InvalidCredentialsException"


class InvalidGlobalReplicationGroupStateFault(ElastiCacheError):
    """The Global datastore is not available or in primary-only state."""
    _ERROR_CODE = "InvalidGlobalReplicationGroupState"


class InvalidKMSKeyFault(ElastiCacheError):
    """The KMS key supplied is not valid."""
    _ERROR_CODE = "InvalidKMSKeyFault"


class InvalidParameterCombinationException(ElastiCacheError):
    """Two or more incompatible parameters were specified."""
    _ERROR_CODE = "InvalidParameterCombination"


class InvalidParameterValueException(ElastiCacheError):
    """The value for a parameter is invalid."""
    _ERROR_CODE = "InvalidParameterValue"


class InvalidReplicationGroupStateFault(ElastiCacheError):
    """The requested replication group is not in the `available` state."""
    _ERROR_CODE = "InvalidReplicationGroupState"


class InvalidServerlessCacheSnapshotStateFault(ElastiCacheError):
    """The state of the serverless cache snapshot was not received. Available for Redis
    only.
    """

    _ERROR_CODE = "InvalidServerlessCacheSnapshotStateFault"


class InvalidServerlessCacheStateFault(ElastiCacheError):
    """The account for these credentials is not currently active."""
    _ERROR_CODE = "InvalidServerlessCacheStateFault"


class InvalidSnapshotStateFault(ElastiCacheError):
    """The current state of the snapshot does not allow the requested operation to occur."""
    _ERROR_CODE = "InvalidSnapshotState"


class InvalidSubnet(ElastiCacheError):
    """An invalid subnet identifier was specified."""
    _ERROR_CODE = "InvalidSubnet"


class InvalidUserGroupStateFault(ElastiCacheError):
    """The user group is not in an active state."""
    _ERROR_CODE = "InvalidUserGroupState"


class InvalidUserStateFault(ElastiCacheError):
    """The user is not in active state."""
    _ERROR_CODE = "InvalidUserState"


class InvalidVPCNetworkStateFault(ElastiCacheError):
    """The VPC network is in an invalid state."""
    _ERROR_CODE = "InvalidVPCNetworkStateFault"


class NoOperationFault(ElastiCacheError):
    """The operation was not performed because no changes were required."""
    _ERROR_CODE = "NoOperationFault"


class NodeGroupNotFoundFault(ElastiCacheError):
    """The node group specified by the `NodeGroupId` parameter could not be found. Please
    verify that the node group exists and that you spelled the `NodeGroupId` value
    correctly.
    """

    _ERROR_CODE = "NodeGroupNotFoundFault"


class NodeGroupsPerReplicationGroupQuotaExceededFault(ElastiCacheError):
    """The request cannot be processed because it would exceed the maximum allowed number
    of node groups (shards) in a single replication group. The default maximum is 90
    """

    _ERROR_CODE = "NodeGroupsPerReplicationGroupQuotaExceeded"


class NodeQuotaForClusterExceededFault(ElastiCacheError):
    """The request cannot be processed because it would exceed the allowed number of cache
    nodes in a single cluster.
    """

    _ERROR_CODE = "NodeQuotaForClusterExceeded"


class NodeQuotaForCustomerExceededFault(ElastiCacheError):
    """The request cannot be processed because it would exceed the allowed number of cache
    nodes per customer.
    """

    _ERROR_CODE = "NodeQuotaForCustomerExceeded"


class ReplicationGroupAlreadyExistsFault(ElastiCacheError):
    """The specified replication group already exists."""
    _ERROR_CODE = "ReplicationGroupAlreadyExists"


class ReplicationGroupAlreadyUnderMigrationFault(ElastiCacheError):
    """The targeted replication group is not available."""
    _ERROR_CODE = "ReplicationGroupAlreadyUnderMigrationFault"


class ReplicationGroupNotFoundFault(ElastiCacheError):
    """The specified replication group does not exist."""
    _ERROR_CODE = "ReplicationGroupNotFoundFault"


class ReplicationGroupNotUnderMigrationFault(ElastiCacheError):
    """The designated replication group is not available for data migration."""
    _ERROR_CODE = "ReplicationGroupNotUnderMigrationFault"


class ReservedCacheNodeAlreadyExistsFault(ElastiCacheError):
    """You already have a reservation with the given identifier."""
    _ERROR_CODE = "ReservedCacheNodeAlreadyExists"


class ReservedCacheNodeNotFoundFault(ElastiCacheError):
    """The requested reserved cache node was not found."""
    _ERROR_CODE = "ReservedCacheNodeNotFound"


class ReservedCacheNodeQuotaExceededFault(ElastiCacheError):
    """The request cannot be processed because it would exceed the user's cache node quota."""
    _ERROR_CODE = "ReservedCacheNodeQuotaExceeded"


class ReservedCacheNodesOfferingNotFoundFault(ElastiCacheError):
    """The requested cache node offering does not exist."""
    _ERROR_CODE = "ReservedCacheNodesOfferingNotFound"


class ServerlessCacheAlreadyExistsFault(ElastiCacheError):
    """A serverless cache with this name already exists."""
    _ERROR_CODE = "ServerlessCacheAlreadyExistsFault"


class ServerlessCacheNotFoundFault(ElastiCacheError):
    """The serverless cache was not found or does not exist."""
    _ERROR_CODE = "ServerlessCacheNotFoundFault"


class ServerlessCacheQuotaForCustomerExceededFault(ElastiCacheError):
    """The number of serverless caches exceeds the customer quota."""
    _ERROR_CODE = "ServerlessCacheQuotaForCustomerExceededFault"


class ServerlessCacheSnapshotAlreadyExistsFault(ElastiCacheError):
    """A serverless cache snapshot with this name already exists. Available for Redis only."""
    _ERROR_CODE = "ServerlessCacheSnapshotAlreadyExistsFault"


class ServerlessCacheSnapshotNotFoundFault(ElastiCacheError):
    """This serverless cache snapshot could not be found or does not exist. Available for
    Redis only.
    """

    _ERROR_CODE = "ServerlessCacheSnapshotNotFoundFault"


class ServerlessCacheSnapshotQuotaExceededFault(ElastiCacheError):
    """The number of serverless cache snapshots exceeds the customer snapshot quota.
    Available for Redis only.
    """

    _ERROR_CODE = "ServerlessCacheSnapshotQuotaExceededFault"


class ServiceLinkedRoleNotFoundFault(ElastiCacheError):
    """The specified service linked role (SLR) was not found."""
    _ERROR_CODE = "ServiceLinkedRoleNotFoundFault"


class ServiceUpdateNotFoundFault(ElastiCacheError):
    """The service update doesn't exist"""
    _ERROR_CODE = "ServiceUpdateNotFoundFault"


class SnapshotAlreadyExistsFault(ElastiCacheError):
    """You already have a snapshot with the given name."""
    _ERROR_CODE = "SnapshotAlreadyExistsFault"


class SnapshotFeatureNotSupportedFault(ElastiCacheError):
    """You attempted one of the following operations:

    - Creating a snapshot of a Redis cluster running on a `cache.t1.micro` cache node.
    - Creating a snapshot of a cluster that is running Memcached rather than Redis.

    Neither of these are supported by ElastiCache.
    """

    _ERROR_CODE = "SnapshotFeatureNotSupportedFault"


class SnapshotNotFoundFault(ElastiCacheError):
    """The requested snapshot name does not refer to an existing snapshot."""
    _ERROR_CODE = "SnapshotNotFoundFault"


class SnapshotQuotaExceededFault(ElastiCacheError):
    """The request cannot be processed because it would exceed the maximum number of
    snapshots.
    """

    _ERROR_CODE = "SnapshotQuotaExceededFault"


class SubnetInUse(ElastiCacheError):
    """The requested subnet is being used by another cache subnet group."""
    _ERROR_CODE = "SubnetInUse"


class SubnetNotAllowedFault(ElastiCacheError):
    """At least one subnet ID does not match the other subnet IDs. This mismatch typically
    occurs when a user sets one subnet ID to a regional Availability Zone and a
    different one to an outpost. Or when a user sets the subnet ID to an Outpost when
    not subscribed on this service.
    """

    _ERROR_CODE = "SubnetNotAllowedFault"


class TagNotFoundFault(ElastiCacheError):
    """The requested tag was not found on this resource."""
    _ERROR_CODE = "TagNotFound"


class TagQuotaPerResourceExceeded(ElastiCacheError):
    """The request cannot be processed because it would cause the resource to have more
    than the allowed number of tags. The maximum number of tags permitted on a resource
    is 50.
    """

    _ERROR_CODE = "TagQuotaPerResourceExceeded"


class TestFailoverNotAvailableFault(ElastiCacheError):
    """The `TestFailover` action is not available."""
    _ERROR_CODE = "TestFailoverNotAvailableFault"


class UserAlreadyExistsFault(ElastiCacheError):
    """A user with this ID already exists."""
    _ERROR_CODE = "UserAlreadyExists"


class UserGroupAlreadyExistsFault(ElastiCacheError):
    """The user group with this ID already exists."""
    _ERROR_CODE = "UserGroupAlreadyExists"


class UserGroupNotFoundFault(ElastiCacheError):
    """The user group was not found or does not exist"""
    _ERROR_CODE = "UserGroupNotFound"


class UserGroupQuotaExceededFault(ElastiCacheError):
    """The number of users exceeds the user group limit."""
    _ERROR_CODE = "UserGroupQuotaExceeded"


class UserNotFoundFault(ElastiCacheError):
    """The user does not exist or could not be found."""
    _ERROR_CODE = "UserNotFound"


class UserQuotaExceededFault(ElastiCacheError):
    """The quota of users has been exceeded."""
    _ERROR_CODE = "UserQuotaExceeded"


EXCEPTIONS: dict[str, type[ElastiCacheError]] = {
    "APICallRateForCustomerExceeded": APICallRateForCustomerExceededFault,
    "AuthorizationAlreadyExists": AuthorizationAlreadyExistsFault,
    "AuthorizationNotFound": AuthorizationNotFoundFault,
    "CacheClusterAlreadyExists": CacheClusterAlreadyExistsFault,
    "CacheClusterNotFound": CacheClusterNotFoundFault,
    "CacheParameterGroupAlreadyExists": CacheParameterGroupAlreadyExistsFault,
    "CacheParameterGroupNotFound": CacheParameterGroupNotFoundFault,
    "CacheParameterGroupQuotaExceeded": CacheParameterGroupQuotaExceededFault,
    "CacheSecurityGroupAlreadyExists": CacheSecurityGroupAlreadyExistsFault,
    "CacheSecurityGroupNotFound": CacheSecurityGroupNotFoundFault,
    "QuotaExceeded.CacheSecurityGroup": CacheSecurityGroupQuotaExceededFault,
    "CacheSubnetGroupAlreadyExists": CacheSubnetGroupAlreadyExistsFault,
    "CacheSubnetGroupInUse": CacheSubnetGroupInUse,
    "CacheSubnetGroupNotFoundFault": CacheSubnetGroupNotFoundFault,
    "CacheSubnetGroupQuotaExceeded": CacheSubnetGroupQuotaExceededFault,
    "CacheSubnetQuotaExceededFault": CacheSubnetQuotaExceededFault,
    "ClusterQuotaForCustomerExceeded": ClusterQuotaForCustomerExceededFault,
    "DefaultUserAssociatedToUserGroup": DefaultUserAssociatedToUserGroupFault,
    "DefaultUserRequired": DefaultUserRequired,
    "DuplicateUserName": DuplicateUserNameFault,
    "GlobalReplicationGroupAlreadyExistsFault": GlobalReplicationGroupAlreadyExistsFault,
    "GlobalReplicationGroupNotFoundFault": GlobalReplicationGroupNotFoundFault,
    "InsufficientCacheClusterCapacity": InsufficientCacheClusterCapacityFault,
    "InvalidARN": InvalidARNFault,
    "InvalidCacheClusterState": InvalidCacheClusterStateFault,
    "InvalidCacheParameterGroupState": InvalidCacheParameterGroupStateFault,
    "InvalidCacheSecurityGroupState": InvalidCacheSecurityGroupStateFault,
    "InvalidCredentialsException": InvalidCredentialsException,
    "InvalidGlobalReplicationGroupState": InvalidGlobalReplicationGroupStateFault,
    "InvalidKMSKeyFault": InvalidKMSKeyFault,
    "InvalidParameterCombination": InvalidParameterCombinationException,
    "InvalidParameterValue": InvalidParameterValueException,
    "InvalidReplicationGroupState": InvalidReplicationGroupStateFault,
    "InvalidServerlessCacheSnapshotStateFault": InvalidServerlessCacheSnapshotStateFault,
    "InvalidServerlessCacheStateFault": InvalidServerlessCacheStateFault,
    "InvalidSnapshotState": InvalidSnapshotStateFault,
    "InvalidSubnet": InvalidSubnet,
    "InvalidUserGroupState": InvalidUserGroupStateFault,
    "InvalidUserState": InvalidUserStateFault,
    "InvalidVPCNetworkStateFault": InvalidVPCNetworkStateFault,
    "NoOperationFault": NoOperationFault,
    "NodeGroupNotFoundFault": NodeGroupNotFoundFault,
    "NodeGroupsPerReplicationGroupQuotaExceeded": NodeGroupsPerReplicationGroupQuotaExceededFault,
    "NodeQuotaForClusterExceeded": NodeQuotaForClusterExceededFault,
    "NodeQuotaForCustomerExceeded": NodeQuotaForCustomerExceededFault,
    "ReplicationGroupAlreadyExists": ReplicationGroupAlreadyExistsFault,
    "ReplicationGroupAlreadyUnderMigrationFault": ReplicationGroupAlreadyUnderMigrationFault,
    "ReplicationGroupNotFoundFault": ReplicationGroupNotFoundFault,
    "ReplicationGroupNotUnderMigrationFault": ReplicationGroupNotUnderMigrationFault,
    "ReservedCacheNodeAlreadyExists": ReservedCacheNodeAlreadyExistsFault,
    "ReservedCacheNodeNotFound": ReservedCacheNodeNotFoundFault,
    "ReservedCacheNodeQuotaExceeded": ReservedCacheNodeQuotaExceededFault,
    "ReservedCacheNodesOfferingNotFound": ReservedCacheNodesOfferingNotFoundFault,
    "ServerlessCacheAlreadyExistsFault": ServerlessCacheAlreadyExistsFault,
    "ServerlessCacheNotFoundFault": ServerlessCacheNotFoundFault,
    "ServerlessCacheQuotaForCustomerExceededFault": ServerlessCacheQuotaForCustomerExceededFault,
    "ServerlessCacheSnapshotAlreadyExistsFault": ServerlessCacheSnapshotAlreadyExistsFault,
    "ServerlessCacheSnapshotNotFoundFault": ServerlessCacheSnapshotNotFoundFault,
    "ServerlessCacheSnapshotQuotaExceededFault": ServerlessCacheSnapshotQuotaExceededFault,
    "ServiceLinkedRoleNotFoundFault": ServiceLinkedRoleNotFoundFault,
    "ServiceUpdateNotFoundFault": ServiceUpdateNotFoundFault,
    "SnapshotAlreadyExistsFault": SnapshotAlreadyExistsFault,
    "SnapshotFeatureNotSupportedFault": SnapshotFeatureNotSupportedFault,
    "SnapshotNotFoundFault": SnapshotNotFoundFault,
    "SnapshotQuotaExceededFault": SnapshotQuotaExceededFault,
    "SubnetInUse": SubnetInUse,
    "SubnetNotAllowedFault": SubnetNotAllowedFault,
    "TagNotFound": TagNotFoundFault,
    "TagQuotaPerResourceExceeded": TagQuotaPerResourceExceeded,
    "TestFailoverNotAvailableFault": TestFailoverNotAvailableFault,
    "UserAlreadyExists": UserAlreadyExistsFault,
    "UserGroupAlreadyExists": UserGroupAlreadyExistsFault,
    "UserGroupNotFound": UserGroupNotFoundFault,
    "UserGroupQuotaExceeded": UserGroupQuotaExceededFault,
    "UserNotFound": UserNotFoundFault,
    "UserQuotaExceeded": UserQuotaExceededFault,
}
