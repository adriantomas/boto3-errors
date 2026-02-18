# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class MemoryDBError(Boto3Error):
    _SERVICE = "memorydb"


class ACLAlreadyExistsFault(MemoryDBError):
    _ERROR_CODE = "ACLAlreadyExistsFault"


class ACLNotFoundFault(MemoryDBError):
    _ERROR_CODE = "ACLNotFoundFault"


class ACLQuotaExceededFault(MemoryDBError):
    _ERROR_CODE = "ACLQuotaExceededFault"


class APICallRateForCustomerExceededFault(MemoryDBError):
    _ERROR_CODE = "APICallRateForCustomerExceededFault"


class ClusterAlreadyExistsFault(MemoryDBError):
    _ERROR_CODE = "ClusterAlreadyExistsFault"


class ClusterNotFoundFault(MemoryDBError):
    _ERROR_CODE = "ClusterNotFoundFault"


class ClusterQuotaForCustomerExceededFault(MemoryDBError):
    _ERROR_CODE = "ClusterQuotaForCustomerExceededFault"


class DefaultUserRequired(MemoryDBError):
    _ERROR_CODE = "DefaultUserRequired"


class DuplicateUserNameFault(MemoryDBError):
    _ERROR_CODE = "DuplicateUserNameFault"


class InsufficientClusterCapacityFault(MemoryDBError):
    _ERROR_CODE = "InsufficientClusterCapacityFault"


class InvalidACLStateFault(MemoryDBError):
    _ERROR_CODE = "InvalidACLStateFault"


class InvalidARNFault(MemoryDBError):
    _ERROR_CODE = "InvalidARNFault"


class InvalidClusterStateFault(MemoryDBError):
    _ERROR_CODE = "InvalidClusterStateFault"


class InvalidCredentialsException(MemoryDBError):
    _ERROR_CODE = "InvalidCredentialsException"


class InvalidKMSKeyFault(MemoryDBError):
    _ERROR_CODE = "InvalidKMSKeyFault"


class InvalidNodeStateFault(MemoryDBError):
    _ERROR_CODE = "InvalidNodeStateFault"


class InvalidParameterCombinationException(MemoryDBError):
    _ERROR_CODE = "InvalidParameterCombinationException"


class InvalidParameterGroupStateFault(MemoryDBError):
    _ERROR_CODE = "InvalidParameterGroupStateFault"


class InvalidParameterValueException(MemoryDBError):
    _ERROR_CODE = "InvalidParameterValueException"


class InvalidSnapshotStateFault(MemoryDBError):
    _ERROR_CODE = "InvalidSnapshotStateFault"


class InvalidSubnet(MemoryDBError):
    _ERROR_CODE = "InvalidSubnet"


class InvalidUserStateFault(MemoryDBError):
    _ERROR_CODE = "InvalidUserStateFault"


class InvalidVPCNetworkStateFault(MemoryDBError):
    _ERROR_CODE = "InvalidVPCNetworkStateFault"


class NoOperationFault(MemoryDBError):
    _ERROR_CODE = "NoOperationFault"


class NodeQuotaForClusterExceededFault(MemoryDBError):
    _ERROR_CODE = "NodeQuotaForClusterExceededFault"


class NodeQuotaForCustomerExceededFault(MemoryDBError):
    _ERROR_CODE = "NodeQuotaForCustomerExceededFault"


class ParameterGroupAlreadyExistsFault(MemoryDBError):
    _ERROR_CODE = "ParameterGroupAlreadyExistsFault"


class ParameterGroupNotFoundFault(MemoryDBError):
    _ERROR_CODE = "ParameterGroupNotFoundFault"


class ParameterGroupQuotaExceededFault(MemoryDBError):
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
    _ERROR_CODE = "ServiceLinkedRoleNotFoundFault"


class ServiceUpdateNotFoundFault(MemoryDBError):
    _ERROR_CODE = "ServiceUpdateNotFoundFault"


class ShardNotFoundFault(MemoryDBError):
    _ERROR_CODE = "ShardNotFoundFault"


class ShardsPerClusterQuotaExceededFault(MemoryDBError):
    _ERROR_CODE = "ShardsPerClusterQuotaExceededFault"


class SnapshotAlreadyExistsFault(MemoryDBError):
    _ERROR_CODE = "SnapshotAlreadyExistsFault"


class SnapshotNotFoundFault(MemoryDBError):
    _ERROR_CODE = "SnapshotNotFoundFault"


class SnapshotQuotaExceededFault(MemoryDBError):
    _ERROR_CODE = "SnapshotQuotaExceededFault"


class SubnetGroupAlreadyExistsFault(MemoryDBError):
    _ERROR_CODE = "SubnetGroupAlreadyExistsFault"


class SubnetGroupInUseFault(MemoryDBError):
    _ERROR_CODE = "SubnetGroupInUseFault"


class SubnetGroupNotFoundFault(MemoryDBError):
    _ERROR_CODE = "SubnetGroupNotFoundFault"


class SubnetGroupQuotaExceededFault(MemoryDBError):
    _ERROR_CODE = "SubnetGroupQuotaExceededFault"


class SubnetInUse(MemoryDBError):
    _ERROR_CODE = "SubnetInUse"


class SubnetNotAllowedFault(MemoryDBError):
    _ERROR_CODE = "SubnetNotAllowedFault"


class SubnetQuotaExceededFault(MemoryDBError):
    _ERROR_CODE = "SubnetQuotaExceededFault"


class TagNotFoundFault(MemoryDBError):
    _ERROR_CODE = "TagNotFoundFault"


class TagQuotaPerResourceExceeded(MemoryDBError):
    _ERROR_CODE = "TagQuotaPerResourceExceeded"


class TestFailoverNotAvailableFault(MemoryDBError):
    _ERROR_CODE = "TestFailoverNotAvailableFault"


class UserAlreadyExistsFault(MemoryDBError):
    _ERROR_CODE = "UserAlreadyExistsFault"


class UserNotFoundFault(MemoryDBError):
    _ERROR_CODE = "UserNotFoundFault"


class UserQuotaExceededFault(MemoryDBError):
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
    "InvalidNodeStateFault": InvalidNodeStateFault,
    "InvalidParameterCombinationException": InvalidParameterCombinationException,
    "InvalidParameterGroupStateFault": InvalidParameterGroupStateFault,
    "InvalidParameterValueException": InvalidParameterValueException,
    "InvalidSnapshotStateFault": InvalidSnapshotStateFault,
    "InvalidSubnet": InvalidSubnet,
    "InvalidUserStateFault": InvalidUserStateFault,
    "InvalidVPCNetworkStateFault": InvalidVPCNetworkStateFault,
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
