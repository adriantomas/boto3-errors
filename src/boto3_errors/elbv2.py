# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class ElasticLoadBalancingv2Error(Boto3Error):
    _SERVICE = "elbv2"


class ALPNPolicyNotSupportedException(ElasticLoadBalancingv2Error):
    """The specified ALPN policy is not supported."""
    _ERROR_CODE = "ALPNPolicyNotFound"


class AllocationIdNotFoundException(ElasticLoadBalancingv2Error):
    """The specified allocation ID does not exist."""
    _ERROR_CODE = "AllocationIdNotFound"


class AvailabilityZoneNotSupportedException(ElasticLoadBalancingv2Error):
    """The specified Availability Zone is not supported."""
    _ERROR_CODE = "AvailabilityZoneNotSupported"


class CaCertificatesBundleNotFoundException(ElasticLoadBalancingv2Error):
    """The specified ca certificate bundle does not exist."""
    _ERROR_CODE = "CaCertificatesBundleNotFound"


class CertificateNotFoundException(ElasticLoadBalancingv2Error):
    """The specified certificate does not exist."""
    _ERROR_CODE = "CertificateNotFound"


class DuplicateListenerException(ElasticLoadBalancingv2Error):
    """A listener with the specified port already exists."""
    _ERROR_CODE = "DuplicateListener"


class DuplicateLoadBalancerNameException(ElasticLoadBalancingv2Error):
    """A load balancer with the specified name already exists."""
    _ERROR_CODE = "DuplicateLoadBalancerName"


class DuplicateTagKeysException(ElasticLoadBalancingv2Error):
    """A tag key was specified more than once."""
    _ERROR_CODE = "DuplicateTagKeys"


class DuplicateTargetGroupNameException(ElasticLoadBalancingv2Error):
    """A target group with the specified name already exists."""
    _ERROR_CODE = "DuplicateTargetGroupName"


class DuplicateTrustStoreNameException(ElasticLoadBalancingv2Error):
    """A trust store with the specified name already exists."""
    _ERROR_CODE = "DuplicateTrustStoreName"


class HealthUnavailableException(ElasticLoadBalancingv2Error):
    """The health of the specified targets could not be retrieved due to an internal error."""
    _ERROR_CODE = "HealthUnavailable"


class IncompatibleProtocolsException(ElasticLoadBalancingv2Error):
    """The specified configuration is not valid with this protocol."""
    _ERROR_CODE = "IncompatibleProtocols"


class InvalidCaCertificatesBundleException(ElasticLoadBalancingv2Error):
    """The specified ca certificate bundle is in an invalid format, or corrupt."""
    _ERROR_CODE = "InvalidCaCertificatesBundle"


class InvalidConfigurationRequestException(ElasticLoadBalancingv2Error):
    """The requested configuration is not valid."""
    _ERROR_CODE = "InvalidConfigurationRequest"


class InvalidLoadBalancerActionException(ElasticLoadBalancingv2Error):
    """The requested action is not valid."""
    _ERROR_CODE = "InvalidLoadBalancerAction"


class InvalidRevocationContentException(ElasticLoadBalancingv2Error):
    """The provided revocation file is an invalid format, or uses an incorrect algorithm."""
    _ERROR_CODE = "InvalidRevocationContent"


class InvalidSchemeException(ElasticLoadBalancingv2Error):
    """The requested scheme is not valid."""
    _ERROR_CODE = "InvalidScheme"


class InvalidSecurityGroupException(ElasticLoadBalancingv2Error):
    """The specified security group does not exist."""
    _ERROR_CODE = "InvalidSecurityGroup"


class InvalidSubnetException(ElasticLoadBalancingv2Error):
    """The specified subnet is out of available addresses."""
    _ERROR_CODE = "InvalidSubnet"


class InvalidTargetException(ElasticLoadBalancingv2Error):
    """The specified target does not exist, is not in the same VPC as the target group, or
    has an unsupported instance type.
    """

    _ERROR_CODE = "InvalidTarget"


class ListenerNotFoundException(ElasticLoadBalancingv2Error):
    """The specified listener does not exist."""
    _ERROR_CODE = "ListenerNotFound"


class LoadBalancerNotFoundException(ElasticLoadBalancingv2Error):
    """The specified load balancer does not exist."""
    _ERROR_CODE = "LoadBalancerNotFound"


class OperationNotPermittedException(ElasticLoadBalancingv2Error):
    """This operation is not allowed."""
    _ERROR_CODE = "OperationNotPermitted"


class PriorityInUseException(ElasticLoadBalancingv2Error):
    """The specified priority is in use."""
    _ERROR_CODE = "PriorityInUse"


class ResourceInUseException(ElasticLoadBalancingv2Error):
    """A specified resource is in use."""
    _ERROR_CODE = "ResourceInUse"


class RevocationContentNotFoundException(ElasticLoadBalancingv2Error):
    """The specified revocation file does not exist."""
    _ERROR_CODE = "RevocationContentNotFound"


class RevocationIdNotFoundException(ElasticLoadBalancingv2Error):
    """The specified revocation ID does not exist."""
    _ERROR_CODE = "RevocationIdNotFound"


class RuleNotFoundException(ElasticLoadBalancingv2Error):
    """The specified rule does not exist."""
    _ERROR_CODE = "RuleNotFound"


class SSLPolicyNotFoundException(ElasticLoadBalancingv2Error):
    """The specified SSL policy does not exist."""
    _ERROR_CODE = "SSLPolicyNotFound"


class SubnetNotFoundException(ElasticLoadBalancingv2Error):
    """The specified subnet does not exist."""
    _ERROR_CODE = "SubnetNotFound"


class TargetGroupAssociationLimitException(ElasticLoadBalancingv2Error):
    """You've reached the limit on the number of load balancers per target group."""
    _ERROR_CODE = "TargetGroupAssociationLimit"


class TargetGroupNotFoundException(ElasticLoadBalancingv2Error):
    """The specified target group does not exist."""
    _ERROR_CODE = "TargetGroupNotFound"


class TooManyActionsException(ElasticLoadBalancingv2Error):
    """You've reached the limit on the number of actions per rule."""
    _ERROR_CODE = "TooManyActions"


class TooManyCertificatesException(ElasticLoadBalancingv2Error):
    """You've reached the limit on the number of certificates per load balancer."""
    _ERROR_CODE = "TooManyCertificates"


class TooManyListenersException(ElasticLoadBalancingv2Error):
    """You've reached the limit on the number of listeners per load balancer."""
    _ERROR_CODE = "TooManyListeners"


class TooManyLoadBalancersException(ElasticLoadBalancingv2Error):
    """You've reached the limit on the number of load balancers for your Amazon Web
    Services account.
    """

    _ERROR_CODE = "TooManyLoadBalancers"


class TooManyRegistrationsForTargetIdException(ElasticLoadBalancingv2Error):
    """You've reached the limit on the number of times a target can be registered with a
    load balancer.
    """

    _ERROR_CODE = "TooManyRegistrationsForTargetId"


class TooManyRulesException(ElasticLoadBalancingv2Error):
    """You've reached the limit on the number of rules per load balancer."""
    _ERROR_CODE = "TooManyRules"


class TooManyTagsException(ElasticLoadBalancingv2Error):
    """You've reached the limit on the number of tags for this resource."""
    _ERROR_CODE = "TooManyTags"


class TooManyTargetGroupsException(ElasticLoadBalancingv2Error):
    """You've reached the limit on the number of target groups for your Amazon Web Services
    account.
    """

    _ERROR_CODE = "TooManyTargetGroups"


class TooManyTargetsException(ElasticLoadBalancingv2Error):
    """You've reached the limit on the number of targets."""
    _ERROR_CODE = "TooManyTargets"


class TooManyTrustStoreRevocationEntriesException(ElasticLoadBalancingv2Error):
    """The specified trust store has too many revocation entries."""
    _ERROR_CODE = "TooManyTrustStoreRevocationEntries"


class TooManyTrustStoresException(ElasticLoadBalancingv2Error):
    """You've reached the limit on the number of trust stores for your Amazon Web Services
    account.
    """

    _ERROR_CODE = "TooManyTrustStores"


class TooManyUniqueTargetGroupsPerLoadBalancerException(ElasticLoadBalancingv2Error):
    """You've reached the limit on the number of unique target groups per load balancer
    across all listeners. If a target group is used by multiple actions for a load
    balancer, it is counted as only one use.
    """

    _ERROR_CODE = "TooManyUniqueTargetGroupsPerLoadBalancer"


class TrustStoreInUseException(ElasticLoadBalancingv2Error):
    """The specified trust store is currently in use."""
    _ERROR_CODE = "TrustStoreInUse"


class TrustStoreNotFoundException(ElasticLoadBalancingv2Error):
    """The specified trust store does not exist."""
    _ERROR_CODE = "TrustStoreNotFound"


class TrustStoreNotReadyException(ElasticLoadBalancingv2Error):
    """The specified trust store is not active."""
    _ERROR_CODE = "TrustStoreNotReady"


class UnsupportedProtocolException(ElasticLoadBalancingv2Error):
    """The specified protocol is not supported."""
    _ERROR_CODE = "UnsupportedProtocol"


EXCEPTIONS: dict[str, type[ElasticLoadBalancingv2Error]] = {
    "ALPNPolicyNotFound": ALPNPolicyNotSupportedException,
    "AllocationIdNotFound": AllocationIdNotFoundException,
    "AvailabilityZoneNotSupported": AvailabilityZoneNotSupportedException,
    "CaCertificatesBundleNotFound": CaCertificatesBundleNotFoundException,
    "CertificateNotFound": CertificateNotFoundException,
    "DuplicateListener": DuplicateListenerException,
    "DuplicateLoadBalancerName": DuplicateLoadBalancerNameException,
    "DuplicateTagKeys": DuplicateTagKeysException,
    "DuplicateTargetGroupName": DuplicateTargetGroupNameException,
    "DuplicateTrustStoreName": DuplicateTrustStoreNameException,
    "HealthUnavailable": HealthUnavailableException,
    "IncompatibleProtocols": IncompatibleProtocolsException,
    "InvalidCaCertificatesBundle": InvalidCaCertificatesBundleException,
    "InvalidConfigurationRequest": InvalidConfigurationRequestException,
    "InvalidLoadBalancerAction": InvalidLoadBalancerActionException,
    "InvalidRevocationContent": InvalidRevocationContentException,
    "InvalidScheme": InvalidSchemeException,
    "InvalidSecurityGroup": InvalidSecurityGroupException,
    "InvalidSubnet": InvalidSubnetException,
    "InvalidTarget": InvalidTargetException,
    "ListenerNotFound": ListenerNotFoundException,
    "LoadBalancerNotFound": LoadBalancerNotFoundException,
    "OperationNotPermitted": OperationNotPermittedException,
    "PriorityInUse": PriorityInUseException,
    "ResourceInUse": ResourceInUseException,
    "RevocationContentNotFound": RevocationContentNotFoundException,
    "RevocationIdNotFound": RevocationIdNotFoundException,
    "RuleNotFound": RuleNotFoundException,
    "SSLPolicyNotFound": SSLPolicyNotFoundException,
    "SubnetNotFound": SubnetNotFoundException,
    "TargetGroupAssociationLimit": TargetGroupAssociationLimitException,
    "TargetGroupNotFound": TargetGroupNotFoundException,
    "TooManyActions": TooManyActionsException,
    "TooManyCertificates": TooManyCertificatesException,
    "TooManyListeners": TooManyListenersException,
    "TooManyLoadBalancers": TooManyLoadBalancersException,
    "TooManyRegistrationsForTargetId": TooManyRegistrationsForTargetIdException,
    "TooManyRules": TooManyRulesException,
    "TooManyTags": TooManyTagsException,
    "TooManyTargetGroups": TooManyTargetGroupsException,
    "TooManyTargets": TooManyTargetsException,
    "TooManyTrustStoreRevocationEntries": TooManyTrustStoreRevocationEntriesException,
    "TooManyTrustStores": TooManyTrustStoresException,
    "TooManyUniqueTargetGroupsPerLoadBalancer": TooManyUniqueTargetGroupsPerLoadBalancerException,
    "TrustStoreInUse": TrustStoreInUseException,
    "TrustStoreNotFound": TrustStoreNotFoundException,
    "TrustStoreNotReady": TrustStoreNotReadyException,
    "UnsupportedProtocol": UnsupportedProtocolException,
}
