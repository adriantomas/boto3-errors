# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class ElasticLoadBalancingError(Boto3Error):
    _SERVICE = "elb"


class AccessPointNotFoundException(ElasticLoadBalancingError):
    """The specified load balancer does not exist."""
    _ERROR_CODE = "LoadBalancerNotFound"


class CertificateNotFoundException(ElasticLoadBalancingError):
    """The specified ARN does not refer to a valid SSL certificate in AWS Identity and
    Access Management (IAM) or AWS Certificate Manager (ACM). Note that if you recently
    uploaded the certificate to IAM, this error might indicate that the certificate is
    not fully available yet.
    """

    _ERROR_CODE = "CertificateNotFound"


class DependencyThrottleException(ElasticLoadBalancingError):
    """A request made by Elastic Load Balancing to another service exceeds the maximum
    request rate permitted for your account.
    """

    _ERROR_CODE = "DependencyThrottle"


class DuplicateAccessPointNameException(ElasticLoadBalancingError):
    """The specified load balancer name already exists for this account."""
    _ERROR_CODE = "DuplicateLoadBalancerName"


class DuplicateListenerException(ElasticLoadBalancingError):
    """A listener already exists for the specified load balancer name and port, but with a
    different instance port, protocol, or SSL certificate.
    """

    _ERROR_CODE = "DuplicateListener"


class DuplicatePolicyNameException(ElasticLoadBalancingError):
    """A policy with the specified name already exists for this load balancer."""
    _ERROR_CODE = "DuplicatePolicyName"


class DuplicateTagKeysException(ElasticLoadBalancingError):
    """A tag key was specified more than once."""
    _ERROR_CODE = "DuplicateTagKeys"


class InvalidConfigurationRequestException(ElasticLoadBalancingError):
    """The requested configuration change is not valid."""
    _ERROR_CODE = "InvalidConfigurationRequest"


class InvalidEndPointException(ElasticLoadBalancingError):
    """The specified endpoint is not valid."""
    _ERROR_CODE = "InvalidInstance"


class InvalidSchemeException(ElasticLoadBalancingError):
    """The specified value for the schema is not valid. You can only specify a scheme for
    load balancers in a VPC.
    """

    _ERROR_CODE = "InvalidScheme"


class InvalidSecurityGroupException(ElasticLoadBalancingError):
    """One or more of the specified security groups do not exist."""
    _ERROR_CODE = "InvalidSecurityGroup"


class InvalidSubnetException(ElasticLoadBalancingError):
    """The specified VPC has no associated Internet gateway."""
    _ERROR_CODE = "InvalidSubnet"


class ListenerNotFoundException(ElasticLoadBalancingError):
    """The load balancer does not have a listener configured at the specified port."""
    _ERROR_CODE = "ListenerNotFound"


class LoadBalancerAttributeNotFoundException(ElasticLoadBalancingError):
    """The specified load balancer attribute does not exist."""
    _ERROR_CODE = "LoadBalancerAttributeNotFound"


class OperationNotPermittedException(ElasticLoadBalancingError):
    """This operation is not allowed."""
    _ERROR_CODE = "OperationNotPermitted"


class PolicyNotFoundException(ElasticLoadBalancingError):
    """One or more of the specified policies do not exist."""
    _ERROR_CODE = "PolicyNotFound"


class PolicyTypeNotFoundException(ElasticLoadBalancingError):
    """One or more of the specified policy types do not exist."""
    _ERROR_CODE = "PolicyTypeNotFound"


class SubnetNotFoundException(ElasticLoadBalancingError):
    """One or more of the specified subnets do not exist."""
    _ERROR_CODE = "SubnetNotFound"


class TooManyAccessPointsException(ElasticLoadBalancingError):
    """The quota for the number of load balancers has been reached."""
    _ERROR_CODE = "TooManyLoadBalancers"


class TooManyPoliciesException(ElasticLoadBalancingError):
    """The quota for the number of policies for this load balancer has been reached."""
    _ERROR_CODE = "TooManyPolicies"


class TooManyTagsException(ElasticLoadBalancingError):
    """The quota for the number of tags that can be assigned to a load balancer has been
    reached.
    """

    _ERROR_CODE = "TooManyTags"


class UnsupportedProtocolException(ElasticLoadBalancingError):
    """The specified protocol or signature version is not supported."""
    _ERROR_CODE = "UnsupportedProtocol"


EXCEPTIONS: dict[str, type[ElasticLoadBalancingError]] = {
    "LoadBalancerNotFound": AccessPointNotFoundException,
    "CertificateNotFound": CertificateNotFoundException,
    "DependencyThrottle": DependencyThrottleException,
    "DuplicateLoadBalancerName": DuplicateAccessPointNameException,
    "DuplicateListener": DuplicateListenerException,
    "DuplicatePolicyName": DuplicatePolicyNameException,
    "DuplicateTagKeys": DuplicateTagKeysException,
    "InvalidConfigurationRequest": InvalidConfigurationRequestException,
    "InvalidInstance": InvalidEndPointException,
    "InvalidScheme": InvalidSchemeException,
    "InvalidSecurityGroup": InvalidSecurityGroupException,
    "InvalidSubnet": InvalidSubnetException,
    "ListenerNotFound": ListenerNotFoundException,
    "LoadBalancerAttributeNotFound": LoadBalancerAttributeNotFoundException,
    "OperationNotPermitted": OperationNotPermittedException,
    "PolicyNotFound": PolicyNotFoundException,
    "PolicyTypeNotFound": PolicyTypeNotFoundException,
    "SubnetNotFound": SubnetNotFoundException,
    "TooManyLoadBalancers": TooManyAccessPointsException,
    "TooManyPolicies": TooManyPoliciesException,
    "TooManyTags": TooManyTagsException,
    "UnsupportedProtocol": UnsupportedProtocolException,
}
