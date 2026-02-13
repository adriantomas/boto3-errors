# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class MemoryDBError(Boto3Error):
    _SERVICE = "memorydb"


class ACLAlreadyExistsFault(MemoryDBError):
    """An ACL with the specified name already exists."""
    _ERROR_CODE = "ACLAlreadyExistsFault"


class ACLNotFoundFault(MemoryDBError):
    """The specified ACL does not exist."""
    _ERROR_CODE = "ACLNotFoundFault"


class ACLQuotaExceededFault(MemoryDBError):
    """The request cannot be processed because it would exceed the maximum number of ACLs
    allowed.
    """

    _ERROR_CODE = "ACLQuotaExceededFault"


class APICallRateForCustomerExceededFault(MemoryDBError):
    """The customer has exceeded the maximum number of API requests allowed per time
    period.
    """

    _ERROR_CODE = "APICallRateForCustomerExceededFault"


class ClusterAlreadyExistsFault(MemoryDBError):
    """A cluster with the specified name already exists."""
    _ERROR_CODE = "ClusterAlreadyExistsFault"


class ClusterNotFoundFault(MemoryDBError):
    """The specified cluster does not exist."""
    _ERROR_CODE = "ClusterNotFoundFault"


class ClusterQuotaForCustomerExceededFault(MemoryDBError):
    """The request cannot be processed because it would exceed the maximum number of
    clusters allowed for this customer.
    """

    _ERROR_CODE = "ClusterQuotaForCustomerExceededFault"


class DefaultUserRequired(MemoryDBError):
    """A default user is required and must be specified."""
    _ERROR_CODE = "DefaultUserRequired"


class DuplicateUserNameFault(MemoryDBError):
    """A user with the specified name already exists."""
    _ERROR_CODE = "DuplicateUserNameFault"


class InsufficientClusterCapacityFault(MemoryDBError):
    """The cluster does not have sufficient capacity to perform the requested operation."""
    _ERROR_CODE = "InsufficientClusterCapacityFault"


class InvalidACLStateFault(MemoryDBError):
    """The ACL is not in a valid state for the requested operation."""
    _ERROR_CODE = "InvalidACLStateFault"


class InvalidARNFault(MemoryDBError):
    """The specified Amazon Resource Name (ARN) is not valid."""
    _ERROR_CODE = "InvalidARNFault"


class InvalidClusterStateFault(MemoryDBError):
    """The cluster is not in a valid state for the requested operation."""
    _ERROR_CODE = "InvalidClusterStateFault"


class InvalidCredentialsException(MemoryDBError):
    """The provided credentials are not valid."""
    _ERROR_CODE = "InvalidCredentialsException"


class InvalidKMSKeyFault(MemoryDBError):
    """The specified KMS key is not valid or accessible."""
    _ERROR_CODE = "InvalidKMSKeyFault"


class InvalidMultiRegionClusterStateFault(MemoryDBError):
    """The requested operation cannot be performed on the multi-Region cluster in its
    current state.
    """

    _ERROR_CODE = "InvalidMultiRegionClusterStateFault"


class InvalidNodeStateFault(MemoryDBError):
    """The node is not in a valid state for the requested operation."""
    _ERROR_CODE = "InvalidNodeStateFault"


class InvalidParameterCombinationException(MemoryDBError):
    """The specified parameter combination is not valid."""
    _ERROR_CODE = "InvalidParameterCombinationException"


class InvalidParameterGroupStateFault(MemoryDBError):
    """The parameter group is not in a valid state for the requested operation."""
    _ERROR_CODE = "InvalidParameterGroupStateFault"


class InvalidParameterValueException(MemoryDBError):
    """The specified parameter value is not valid."""
    _ERROR_CODE = "InvalidParameterValueException"


class InvalidSnapshotStateFault(MemoryDBError):
    """The snapshot is not in a valid state for the requested operation."""
    _ERROR_CODE = "InvalidSnapshotStateFault"


class InvalidSubnet(MemoryDBError):
    """The specified subnet is not valid."""
    _ERROR_CODE = "InvalidSubnet"


class InvalidUserStateFault(MemoryDBError):
    """The user is not in a valid state for the requested operation."""
    _ERROR_CODE = "InvalidUserStateFault"


class InvalidVPCNetworkStateFault(MemoryDBError):
    """The VPC network is not in a valid state for the requested operation."""
    _ERROR_CODE = "InvalidVPCNetworkStateFault"


class MultiRegionClusterAlreadyExistsFault(MemoryDBError):
    """A multi-Region cluster with the specified name already exists."""
    _ERROR_CODE = "MultiRegionClusterAlreadyExistsFault"


class MultiRegionClusterNotFoundFault(MemoryDBError):
    """The specified multi-Region cluster does not exist."""
    _ERROR_CODE = "MultiRegionClusterNotFoundFault"


class MultiRegionParameterGroupNotFoundFault(MemoryDBError):
    """The specified multi-Region parameter group does not exist."""
    _ERROR_CODE = "MultiRegionParameterGroupNotFoundFault"


class NoOperationFault(MemoryDBError):
    """The requested operation would result in no changes."""
    _ERROR_CODE = "NoOperationFault"


class NodeQuotaForClusterExceededFault(MemoryDBError):
    """The request cannot be processed because it would exceed the maximum number of nodes
    allowed for this cluster.
    """

    _ERROR_CODE = "NodeQuotaForClusterExceededFault"


class NodeQuotaForCustomerExceededFault(MemoryDBError):
    """The request cannot be processed because it would exceed the maximum number of nodes
    allowed for this customer.
    """

    _ERROR_CODE = "NodeQuotaForCustomerExceededFault"


class ParameterGroupAlreadyExistsFault(MemoryDBError):
    """A parameter group with the specified name already exists."""
    _ERROR_CODE = "ParameterGroupAlreadyExistsFault"


class ParameterGroupNotFoundFault(MemoryDBError):
    """The specified parameter group does not exist."""
    _ERROR_CODE = "ParameterGroupNotFoundFault"


class ParameterGroupQuotaExceededFault(MemoryDBError):
    """The request cannot be processed because it would exceed the maximum number of
    parameter groups allowed.
    """

    _ERROR_CODE = "ParameterGroupQuotaExceededFault"


class ReservedNodeAlreadyExistsFault(MemoryDBError):
    """You already have a reservation with the given identifier."""
    _ERROR_CODE = "ReservedNodeAlreadyExistsFault"


class ReservedNodeNotFoundFault(MemoryDBError):
    """The requested node does not exist."""
    _ERROR_CODE = "ReservedNodeNotFoundFault"


class ReservedNodeQuotaExceededFault(MemoryDBError):
    """The request cannot be processed because it would exceed the user's node quota."""
    _ERROR_CODE = "ReservedNodeQuotaExceededFault"


class ReservedNodesOfferingNotFoundFault(MemoryDBError):
    """The requested node offering does not exist."""
    _ERROR_CODE = "ReservedNodesOfferingNotFoundFault"


class ServiceLinkedRoleNotFoundFault(MemoryDBError):
    """The required service-linked role was not found."""
    _ERROR_CODE = "ServiceLinkedRoleNotFoundFault"


class ServiceUpdateNotFoundFault(MemoryDBError):
    """The specified service update does not exist."""
    _ERROR_CODE = "ServiceUpdateNotFoundFault"


class ShardNotFoundFault(MemoryDBError):
    """The specified shard does not exist."""
    _ERROR_CODE = "ShardNotFoundFault"


class ShardsPerClusterQuotaExceededFault(MemoryDBError):
    """The request cannot be processed because it would exceed the maximum number of shards
    allowed per cluster.
    """

    _ERROR_CODE = "ShardsPerClusterQuotaExceededFault"


class SnapshotAlreadyExistsFault(MemoryDBError):
    """A snapshot with the specified name already exists."""
    _ERROR_CODE = "SnapshotAlreadyExistsFault"


class SnapshotNotFoundFault(MemoryDBError):
    """The specified snapshot does not exist."""
    _ERROR_CODE = "SnapshotNotFoundFault"


class SnapshotQuotaExceededFault(MemoryDBError):
    """The request cannot be processed because it would exceed the maximum number of
    snapshots allowed.
    """

    _ERROR_CODE = "SnapshotQuotaExceededFault"


class SubnetGroupAlreadyExistsFault(MemoryDBError):
    """A subnet group with the specified name already exists."""
    _ERROR_CODE = "SubnetGroupAlreadyExistsFault"


class SubnetGroupInUseFault(MemoryDBError):
    """The subnet group is currently in use and cannot be deleted."""
    _ERROR_CODE = "SubnetGroupInUseFault"


class SubnetGroupNotFoundFault(MemoryDBError):
    """The specified subnet group does not exist."""
    _ERROR_CODE = "SubnetGroupNotFoundFault"


class SubnetGroupQuotaExceededFault(MemoryDBError):
    """The request cannot be processed because it would exceed the maximum number of subnet
    groups allowed.
    """

    _ERROR_CODE = "SubnetGroupQuotaExceededFault"


class SubnetInUse(MemoryDBError):
    """The subnet is currently in use and cannot be deleted."""
    _ERROR_CODE = "SubnetInUse"


class SubnetNotAllowedFault(MemoryDBError):
    """The specified subnet is not allowed for this operation."""
    _ERROR_CODE = "SubnetNotAllowedFault"


class SubnetQuotaExceededFault(MemoryDBError):
    """The request cannot be processed because it would exceed the maximum number of
    subnets allowed.
    """

    _ERROR_CODE = "SubnetQuotaExceededFault"


class TagNotFoundFault(MemoryDBError):
    """The specified tag does not exist."""
    _ERROR_CODE = "TagNotFoundFault"


class TagQuotaPerResourceExceeded(MemoryDBError):
    """The request cannot be processed because it would exceed the maximum number of tags
    allowed per resource.
    """

    _ERROR_CODE = "TagQuotaPerResourceExceeded"


class TestFailoverNotAvailableFault(MemoryDBError):
    """Test failover is not available for this cluster configuration."""
    _ERROR_CODE = "TestFailoverNotAvailableFault"


class UserAlreadyExistsFault(MemoryDBError):
    """A user with the specified name already exists."""
    _ERROR_CODE = "UserAlreadyExistsFault"


class UserNotFoundFault(MemoryDBError):
    """The specified user does not exist."""
    _ERROR_CODE = "UserNotFoundFault"


class UserQuotaExceededFault(MemoryDBError):
    """The request cannot be processed because it would exceed the maximum number of users
    allowed.
    """

    _ERROR_CODE = "UserQuotaExceededFault"


EXCEPTIONS: dict[str, type[MemoryDBError]] = {
    "ACLAlreadyExistsFault": ACLAlreadyExistsFault,
    "ACLNotFoundFault": ACLNotFoundFault,
    "ACLQuotaExceededFault": ACLQuotaExceededFault,
    "APICallRateForCustomerExceededFault": APICallRateForCustomerExceededFault,
    "ClusterAlreadyExistsFault": ClusterAlreadyExistsFault,
    "ClusterNotFoundFault": ClusterNotFoundFault,
    "ClusterQuotaForCustomerExceededFault": ClusterQuotaForCustomerExceededFault,
    "DefaultUserRequired": DefaultUserRequired,
    "DuplicateUserNameFault": DuplicateUserNameFault,
    "InsufficientClusterCapacityFault": InsufficientClusterCapacityFault,
    "InvalidACLStateFault": InvalidACLStateFault,
    "InvalidARNFault": InvalidARNFault,
    "InvalidClusterStateFault": InvalidClusterStateFault,
    "InvalidCredentialsException": InvalidCredentialsException,
    "InvalidKMSKeyFault": InvalidKMSKeyFault,
    "InvalidMultiRegionClusterStateFault": InvalidMultiRegionClusterStateFault,
    "InvalidNodeStateFault": InvalidNodeStateFault,
    "InvalidParameterCombinationException": InvalidParameterCombinationException,
    "InvalidParameterGroupStateFault": InvalidParameterGroupStateFault,
    "InvalidParameterValueException": InvalidParameterValueException,
    "InvalidSnapshotStateFault": InvalidSnapshotStateFault,
    "InvalidSubnet": InvalidSubnet,
    "InvalidUserStateFault": InvalidUserStateFault,
    "InvalidVPCNetworkStateFault": InvalidVPCNetworkStateFault,
    "MultiRegionClusterAlreadyExistsFault": MultiRegionClusterAlreadyExistsFault,
    "MultiRegionClusterNotFoundFault": MultiRegionClusterNotFoundFault,
    "MultiRegionParameterGroupNotFoundFault": MultiRegionParameterGroupNotFoundFault,
    "NoOperationFault": NoOperationFault,
    "NodeQuotaForClusterExceededFault": NodeQuotaForClusterExceededFault,
    "NodeQuotaForCustomerExceededFault": NodeQuotaForCustomerExceededFault,
    "ParameterGroupAlreadyExistsFault": ParameterGroupAlreadyExistsFault,
    "ParameterGroupNotFoundFault": ParameterGroupNotFoundFault,
    "ParameterGroupQuotaExceededFault": ParameterGroupQuotaExceededFault,
    "ReservedNodeAlreadyExistsFault": ReservedNodeAlreadyExistsFault,
    "ReservedNodeNotFoundFault": ReservedNodeNotFoundFault,
    "ReservedNodeQuotaExceededFault": ReservedNodeQuotaExceededFault,
    "ReservedNodesOfferingNotFoundFault": ReservedNodesOfferingNotFoundFault,
    "ServiceLinkedRoleNotFoundFault": ServiceLinkedRoleNotFoundFault,
    "ServiceUpdateNotFoundFault": ServiceUpdateNotFoundFault,
    "ShardNotFoundFault": ShardNotFoundFault,
    "ShardsPerClusterQuotaExceededFault": ShardsPerClusterQuotaExceededFault,
    "SnapshotAlreadyExistsFault": SnapshotAlreadyExistsFault,
    "SnapshotNotFoundFault": SnapshotNotFoundFault,
    "SnapshotQuotaExceededFault": SnapshotQuotaExceededFault,
    "SubnetGroupAlreadyExistsFault": SubnetGroupAlreadyExistsFault,
    "SubnetGroupInUseFault": SubnetGroupInUseFault,
    "SubnetGroupNotFoundFault": SubnetGroupNotFoundFault,
    "SubnetGroupQuotaExceededFault": SubnetGroupQuotaExceededFault,
    "SubnetInUse": SubnetInUse,
    "SubnetNotAllowedFault": SubnetNotAllowedFault,
    "SubnetQuotaExceededFault": SubnetQuotaExceededFault,
    "TagNotFoundFault": TagNotFoundFault,
    "TagQuotaPerResourceExceeded": TagQuotaPerResourceExceeded,
    "TestFailoverNotAvailableFault": TestFailoverNotAvailableFault,
    "UserAlreadyExistsFault": UserAlreadyExistsFault,
    "UserNotFoundFault": UserNotFoundFault,
    "UserQuotaExceededFault": UserQuotaExceededFault,
}
