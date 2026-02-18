# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class DAXError(Boto3Error):
    _SERVICE = "dax"


class ClusterAlreadyExistsFault(DAXError):
    """You already have a DAX cluster with the given identifier."""
    _ERROR_CODE = "ClusterAlreadyExistsFault"


class ClusterNotFoundFault(DAXError):
    """The requested cluster ID does not refer to an existing DAX cluster."""
    _ERROR_CODE = "ClusterNotFoundFault"


class ClusterQuotaForCustomerExceededFault(DAXError):
    """You have attempted to exceed the maximum number of DAX clusters for your AWS
    account.
    """

    _ERROR_CODE = "ClusterQuotaForCustomerExceededFault"


class InsufficientClusterCapacityFault(DAXError):
    """There are not enough system resources to create the cluster you requested (or to
    resize an already-existing cluster).
    """

    _ERROR_CODE = "InsufficientClusterCapacityFault"


class InvalidARNFault(DAXError):
    """The Amazon Resource Name (ARN) supplied in the request is not valid."""
    _ERROR_CODE = "InvalidARNFault"


class InvalidClusterStateFault(DAXError):
    """The requested DAX cluster is not in the available state."""
    _ERROR_CODE = "InvalidClusterStateFault"


class InvalidParameterCombinationException(DAXError):
    """Two or more incompatible parameters were specified."""
    _ERROR_CODE = "InvalidParameterCombinationException"


class InvalidParameterGroupStateFault(DAXError):
    """One or more parameters in a parameter group are in an invalid state."""
    _ERROR_CODE = "InvalidParameterGroupStateFault"


class InvalidParameterValueException(DAXError):
    """The value for a parameter is invalid."""
    _ERROR_CODE = "InvalidParameterValueException"


class InvalidSubnet(DAXError):
    """An invalid subnet identifier was specified."""
    _ERROR_CODE = "InvalidSubnet"


class InvalidVPCNetworkStateFault(DAXError):
    """The VPC network is in an invalid state."""
    _ERROR_CODE = "InvalidVPCNetworkStateFault"


class NodeNotFoundFault(DAXError):
    """None of the nodes in the cluster have the given node ID."""
    _ERROR_CODE = "NodeNotFoundFault"


class NodeQuotaForClusterExceededFault(DAXError):
    """You have attempted to exceed the maximum number of nodes for a DAX cluster."""
    _ERROR_CODE = "NodeQuotaForClusterExceededFault"


class NodeQuotaForCustomerExceededFault(DAXError):
    """You have attempted to exceed the maximum number of nodes for your AWS account."""
    _ERROR_CODE = "NodeQuotaForCustomerExceededFault"


class ParameterGroupAlreadyExistsFault(DAXError):
    """The specified parameter group already exists."""
    _ERROR_CODE = "ParameterGroupAlreadyExistsFault"


class ParameterGroupNotFoundFault(DAXError):
    """The specified parameter group does not exist."""
    _ERROR_CODE = "ParameterGroupNotFoundFault"


class ParameterGroupQuotaExceededFault(DAXError):
    """You have attempted to exceed the maximum number of parameter groups."""
    _ERROR_CODE = "ParameterGroupQuotaExceededFault"


class ServiceLinkedRoleNotFoundFault(DAXError):
    """The specified service linked role (SLR) was not found."""
    _ERROR_CODE = "ServiceLinkedRoleNotFoundFault"


class ServiceQuotaExceededException(DAXError):
    """You have reached the maximum number of x509 certificates that can be created for
    encrypted clusters in a 30 day period. Contact AWS customer support to discuss
    options for continuing to create encrypted clusters.
    """

    _ERROR_CODE = "ServiceQuotaExceededException"


class SubnetGroupAlreadyExistsFault(DAXError):
    """The specified subnet group already exists."""
    _ERROR_CODE = "SubnetGroupAlreadyExistsFault"


class SubnetGroupInUseFault(DAXError):
    """The specified subnet group is currently in use."""
    _ERROR_CODE = "SubnetGroupInUseFault"


class SubnetGroupNotFoundFault(DAXError):
    """The requested subnet group name does not refer to an existing subnet group."""
    _ERROR_CODE = "SubnetGroupNotFoundFault"


class SubnetGroupQuotaExceededFault(DAXError):
    """The request cannot be processed because it would exceed the allowed number of
    subnets in a subnet group.
    """

    _ERROR_CODE = "SubnetGroupQuotaExceededFault"


class SubnetInUse(DAXError):
    """The requested subnet is being used by another subnet group."""
    _ERROR_CODE = "SubnetInUse"


class SubnetQuotaExceededFault(DAXError):
    """The request cannot be processed because it would exceed the allowed number of
    subnets in a subnet group.
    """

    _ERROR_CODE = "SubnetQuotaExceededFault"


class TagNotFoundFault(DAXError):
    """The tag does not exist."""
    _ERROR_CODE = "TagNotFoundFault"


class TagQuotaPerResourceExceeded(DAXError):
    """You have exceeded the maximum number of tags for this DAX cluster."""
    _ERROR_CODE = "TagQuotaPerResourceExceeded"


EXCEPTIONS: dict[str, type[DAXError]] = {
    "ClusterAlreadyExistsFault": ClusterAlreadyExistsFault,
    "ClusterNotFoundFault": ClusterNotFoundFault,
    "ClusterQuotaForCustomerExceededFault": ClusterQuotaForCustomerExceededFault,
    "InsufficientClusterCapacityFault": InsufficientClusterCapacityFault,
    "InvalidARNFault": InvalidARNFault,
    "InvalidClusterStateFault": InvalidClusterStateFault,
    "InvalidParameterCombinationException": InvalidParameterCombinationException,
    "InvalidParameterGroupStateFault": InvalidParameterGroupStateFault,
    "InvalidParameterValueException": InvalidParameterValueException,
    "InvalidSubnet": InvalidSubnet,
    "InvalidVPCNetworkStateFault": InvalidVPCNetworkStateFault,
    "NodeNotFoundFault": NodeNotFoundFault,
    "NodeQuotaForClusterExceededFault": NodeQuotaForClusterExceededFault,
    "NodeQuotaForCustomerExceededFault": NodeQuotaForCustomerExceededFault,
    "ParameterGroupAlreadyExistsFault": ParameterGroupAlreadyExistsFault,
    "ParameterGroupNotFoundFault": ParameterGroupNotFoundFault,
    "ParameterGroupQuotaExceededFault": ParameterGroupQuotaExceededFault,
    "ServiceLinkedRoleNotFoundFault": ServiceLinkedRoleNotFoundFault,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "SubnetGroupAlreadyExistsFault": SubnetGroupAlreadyExistsFault,
    "SubnetGroupInUseFault": SubnetGroupInUseFault,
    "SubnetGroupNotFoundFault": SubnetGroupNotFoundFault,
    "SubnetGroupQuotaExceededFault": SubnetGroupQuotaExceededFault,
    "SubnetInUse": SubnetInUse,
    "SubnetQuotaExceededFault": SubnetQuotaExceededFault,
    "TagNotFoundFault": TagNotFoundFault,
    "TagQuotaPerResourceExceeded": TagQuotaPerResourceExceeded,
}
