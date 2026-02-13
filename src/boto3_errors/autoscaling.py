# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class AutoScalingError(Boto3Error):
    _SERVICE = "autoscaling"


class ActiveInstanceRefreshNotFoundFault(AutoScalingError):
    """The request failed because an active instance refresh or rollback for the specified
    Auto Scaling group was not found.
    """

    _ERROR_CODE = "ActiveInstanceRefreshNotFound"


class AlreadyExistsFault(AutoScalingError):
    """You already have an Auto Scaling group or launch configuration with this name."""
    _ERROR_CODE = "AlreadyExists"


class IdempotentParameterMismatchError(AutoScalingError):
    """Indicates that the parameters in the current request do not match the parameters
    from a previous request with the same client token within the idempotency window.
    """

    _ERROR_CODE = "IdempotentParameterMismatch"


class InstanceRefreshInProgressFault(AutoScalingError):
    """The request failed because an active instance refresh already exists for the
    specified Auto Scaling group.
    """

    _ERROR_CODE = "InstanceRefreshInProgress"


class InvalidNextToken(AutoScalingError):
    """The `NextToken` value is not valid."""
    _ERROR_CODE = "InvalidNextToken"


class IrreversibleInstanceRefreshFault(AutoScalingError):
    """The request failed because a desired configuration was not found or an incompatible
    launch template (uses a Systems Manager parameter instead of an AMI ID) or launch
    template version (`$Latest` or `$Default`) is present on the Auto Scaling group.
    """

    _ERROR_CODE = "IrreversibleInstanceRefresh"


class LimitExceededFault(AutoScalingError):
    """You have already reached a limit for your Amazon EC2 Auto Scaling resources (for
    example, Auto Scaling groups, launch configurations, or lifecycle hooks). For more
    information, see DescribeAccountLimits in the Amazon EC2 Auto Scaling API Reference.
    """

    _ERROR_CODE = "LimitExceeded"


class ResourceContentionFault(AutoScalingError):
    """You already have a pending update to an Amazon EC2 Auto Scaling resource (for
    example, an Auto Scaling group, instance, or load balancer).
    """

    _ERROR_CODE = "ResourceContention"


class ResourceInUseFault(AutoScalingError):
    """The operation can't be performed because the resource is in use."""
    _ERROR_CODE = "ResourceInUse"


class ScalingActivityInProgressFault(AutoScalingError):
    """The operation can't be performed because there are scaling activities in progress."""
    _ERROR_CODE = "ScalingActivityInProgress"


class ServiceLinkedRoleFailure(AutoScalingError):
    """The service-linked role is not yet ready for use."""
    _ERROR_CODE = "ServiceLinkedRoleFailure"


EXCEPTIONS: dict[str, type[AutoScalingError]] = {
    "ActiveInstanceRefreshNotFound": ActiveInstanceRefreshNotFoundFault,
    "AlreadyExists": AlreadyExistsFault,
    "IdempotentParameterMismatch": IdempotentParameterMismatchError,
    "InstanceRefreshInProgress": InstanceRefreshInProgressFault,
    "InvalidNextToken": InvalidNextToken,
    "IrreversibleInstanceRefresh": IrreversibleInstanceRefreshFault,
    "LimitExceeded": LimitExceededFault,
    "ResourceContention": ResourceContentionFault,
    "ResourceInUse": ResourceInUseFault,
    "ScalingActivityInProgress": ScalingActivityInProgressFault,
    "ServiceLinkedRoleFailure": ServiceLinkedRoleFailure,
}
