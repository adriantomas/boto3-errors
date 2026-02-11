# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class CodeDeployError(Boto3Error):
    _SERVICE = "codedeploy"


class AlarmsLimitExceededException(CodeDeployError):
    """The maximum number of alarms for a deployment group (10) was exceeded."""
    _ERROR_CODE = "AlarmsLimitExceededException"


class ApplicationAlreadyExistsException(CodeDeployError):
    """An application with the specified name with the user or Amazon Web Services account
    already exists.
    """

    _ERROR_CODE = "ApplicationAlreadyExistsException"


class ApplicationDoesNotExistException(CodeDeployError):
    """The application does not exist with the user or Amazon Web Services account."""
    _ERROR_CODE = "ApplicationDoesNotExistException"


class ApplicationLimitExceededException(CodeDeployError):
    """More applications were attempted to be created than are allowed."""
    _ERROR_CODE = "ApplicationLimitExceededException"


class ApplicationNameRequiredException(CodeDeployError):
    """The minimum number of required application names was not specified."""
    _ERROR_CODE = "ApplicationNameRequiredException"


class ArnNotSupportedException(CodeDeployError):
    """The specified ARN is not supported. For example, it might be an ARN for a resource
    that is not expected.
    """

    _ERROR_CODE = "ArnNotSupportedException"


class BatchLimitExceededException(CodeDeployError):
    """The maximum number of names or IDs allowed for this request (100) was exceeded."""
    _ERROR_CODE = "BatchLimitExceededException"


class BucketNameFilterRequiredException(CodeDeployError):
    """A bucket name is required, but was not provided."""
    _ERROR_CODE = "BucketNameFilterRequiredException"


class DeploymentAlreadyCompletedException(CodeDeployError):
    """The deployment is already complete."""
    _ERROR_CODE = "DeploymentAlreadyCompletedException"


class DeploymentAlreadyStartedException(CodeDeployError):
    """A deployment to a target was attempted while another deployment was in progress."""
    _ERROR_CODE = "DeploymentAlreadyStartedException"


class DeploymentConfigAlreadyExistsException(CodeDeployError):
    """A deployment configuration with the specified name with the user or Amazon Web
    Services account already exists.
    """

    _ERROR_CODE = "DeploymentConfigAlreadyExistsException"


class DeploymentConfigDoesNotExistException(CodeDeployError):
    """The deployment configuration does not exist with the user or Amazon Web Services
    account.
    """

    _ERROR_CODE = "DeploymentConfigDoesNotExistException"


class DeploymentConfigInUseException(CodeDeployError):
    """The deployment configuration is still in use."""
    _ERROR_CODE = "DeploymentConfigInUseException"


class DeploymentConfigLimitExceededException(CodeDeployError):
    """The deployment configurations limit was exceeded."""
    _ERROR_CODE = "DeploymentConfigLimitExceededException"


class DeploymentConfigNameRequiredException(CodeDeployError):
    """The deployment configuration name was not specified."""
    _ERROR_CODE = "DeploymentConfigNameRequiredException"


class DeploymentDoesNotExistException(CodeDeployError):
    """The deployment with the user or Amazon Web Services account does not exist."""
    _ERROR_CODE = "DeploymentDoesNotExistException"


class DeploymentGroupAlreadyExistsException(CodeDeployError):
    """A deployment group with the specified name with the user or Amazon Web Services
    account already exists.
    """

    _ERROR_CODE = "DeploymentGroupAlreadyExistsException"


class DeploymentGroupDoesNotExistException(CodeDeployError):
    """The named deployment group with the user or Amazon Web Services account does not
    exist.
    """

    _ERROR_CODE = "DeploymentGroupDoesNotExistException"


class DeploymentGroupLimitExceededException(CodeDeployError):
    """The deployment groups limit was exceeded."""
    _ERROR_CODE = "DeploymentGroupLimitExceededException"


class DeploymentGroupNameRequiredException(CodeDeployError):
    """The deployment group name was not specified."""
    _ERROR_CODE = "DeploymentGroupNameRequiredException"


class DeploymentIdRequiredException(CodeDeployError):
    """At least one deployment ID must be specified."""
    _ERROR_CODE = "DeploymentIdRequiredException"


class DeploymentIsNotInReadyStateException(CodeDeployError):
    """The deployment does not have a status of Ready and can't continue yet."""
    _ERROR_CODE = "DeploymentIsNotInReadyStateException"


class DeploymentLimitExceededException(CodeDeployError):
    """The number of allowed deployments was exceeded."""
    _ERROR_CODE = "DeploymentLimitExceededException"


class DeploymentNotStartedException(CodeDeployError):
    """The specified deployment has not started."""
    _ERROR_CODE = "DeploymentNotStartedException"


class DeploymentTargetDoesNotExistException(CodeDeployError):
    """The provided target ID does not belong to the attempted deployment."""
    _ERROR_CODE = "DeploymentTargetDoesNotExistException"


class DeploymentTargetIdRequiredException(CodeDeployError):
    """A deployment target ID was not provided."""
    _ERROR_CODE = "DeploymentTargetIdRequiredException"


class DeploymentTargetListSizeExceededException(CodeDeployError):
    """The maximum number of targets that can be associated with an Amazon ECS or Lambda
    deployment was exceeded. The target list of both types of deployments must have
    exactly one item. This exception does not apply to EC2/On-premises deployments.
    """

    _ERROR_CODE = "DeploymentTargetListSizeExceededException"


class DescriptionTooLongException(CodeDeployError):
    """The description is too long."""
    _ERROR_CODE = "DescriptionTooLongException"


class ECSServiceMappingLimitExceededException(CodeDeployError):
    """The Amazon ECS service is associated with more than one deployment groups. An Amazon
    ECS service can be associated with only one deployment group.
    """

    _ERROR_CODE = "ECSServiceMappingLimitExceededException"


class GitHubAccountTokenDoesNotExistException(CodeDeployError):
    """No GitHub account connection exists with the named specified in the call."""
    _ERROR_CODE = "GitHubAccountTokenDoesNotExistException"


class GitHubAccountTokenNameRequiredException(CodeDeployError):
    """The call is missing a required GitHub account connection name."""
    _ERROR_CODE = "GitHubAccountTokenNameRequiredException"


class IamArnRequiredException(CodeDeployError):
    """No IAM ARN was included in the request. You must use an IAM session ARN or user ARN
    in the request.
    """

    _ERROR_CODE = "IamArnRequiredException"


class IamSessionArnAlreadyRegisteredException(CodeDeployError):
    """The request included an IAM session ARN that has already been used to register a
    different instance.
    """

    _ERROR_CODE = "IamSessionArnAlreadyRegisteredException"


class IamUserArnAlreadyRegisteredException(CodeDeployError):
    """The specified user ARN is already registered with an on-premises instance."""
    _ERROR_CODE = "IamUserArnAlreadyRegisteredException"


class IamUserArnRequiredException(CodeDeployError):
    """An user ARN was not specified."""
    _ERROR_CODE = "IamUserArnRequiredException"


class InstanceDoesNotExistException(CodeDeployError):
    """The specified instance does not exist in the deployment group."""
    _ERROR_CODE = "InstanceDoesNotExistException"


class InstanceIdRequiredException(CodeDeployError):
    """The instance ID was not specified."""
    _ERROR_CODE = "InstanceIdRequiredException"


class InstanceLimitExceededException(CodeDeployError):
    """The maximum number of allowed on-premises instances in a single call was exceeded."""
    _ERROR_CODE = "InstanceLimitExceededException"


class InstanceNameAlreadyRegisteredException(CodeDeployError):
    """The specified on-premises instance name is already registered."""
    _ERROR_CODE = "InstanceNameAlreadyRegisteredException"


class InstanceNameRequiredException(CodeDeployError):
    """An on-premises instance name was not specified."""
    _ERROR_CODE = "InstanceNameRequiredException"


class InstanceNotRegisteredException(CodeDeployError):
    """The specified on-premises instance is not registered."""
    _ERROR_CODE = "InstanceNotRegisteredException"


class InvalidAlarmConfigException(CodeDeployError):
    """The format of the alarm configuration is invalid. Possible causes include:

    - The alarm list is null.
    - The alarm object is null.
    - The alarm name is empty or null or exceeds the limit of 255 characters.
    - Two alarms with the same name have been specified.
    - The alarm configuration is enabled, but the alarm list is empty.
    """

    _ERROR_CODE = "InvalidAlarmConfigException"


class InvalidApplicationNameException(CodeDeployError):
    """The application name was specified in an invalid format."""
    _ERROR_CODE = "InvalidApplicationNameException"


class InvalidArnException(CodeDeployError):
    """The specified ARN is not in a valid format."""
    _ERROR_CODE = "InvalidArnException"


class InvalidAutoRollbackConfigException(CodeDeployError):
    """The automatic rollback configuration was specified in an invalid format. For
    example, automatic rollback is enabled, but an invalid triggering event type or no
    event types were listed.
    """

    _ERROR_CODE = "InvalidAutoRollbackConfigException"


class InvalidAutoScalingGroupException(CodeDeployError):
    """The Auto Scaling group was specified in an invalid format or does not exist."""
    _ERROR_CODE = "InvalidAutoScalingGroupException"


class InvalidBlueGreenDeploymentConfigurationException(CodeDeployError):
    """The configuration for the blue/green deployment group was provided in an invalid
    format. For information about deployment configuration format, see
    CreateDeploymentConfig.
    """

    _ERROR_CODE = "InvalidBlueGreenDeploymentConfigurationException"


class InvalidBucketNameFilterException(CodeDeployError):
    """The bucket name either doesn't exist or was specified in an invalid format."""
    _ERROR_CODE = "InvalidBucketNameFilterException"


class InvalidComputePlatformException(CodeDeployError):
    """The computePlatform is invalid. The computePlatform should be `Lambda`, `Server`, or
    `ECS`.
    """

    _ERROR_CODE = "InvalidComputePlatformException"


class InvalidDeployedStateFilterException(CodeDeployError):
    """The deployed state filter was specified in an invalid format."""
    _ERROR_CODE = "InvalidDeployedStateFilterException"


class InvalidDeploymentConfigNameException(CodeDeployError):
    """The deployment configuration name was specified in an invalid format."""
    _ERROR_CODE = "InvalidDeploymentConfigNameException"


class InvalidDeploymentGroupNameException(CodeDeployError):
    """The deployment group name was specified in an invalid format."""
    _ERROR_CODE = "InvalidDeploymentGroupNameException"


class InvalidDeploymentIdException(CodeDeployError):
    """At least one of the deployment IDs was specified in an invalid format."""
    _ERROR_CODE = "InvalidDeploymentIdException"


class InvalidDeploymentInstanceTypeException(CodeDeployError):
    """An instance type was specified for an in-place deployment. Instance types are
    supported for blue/green deployments only.
    """

    _ERROR_CODE = "InvalidDeploymentInstanceTypeException"


class InvalidDeploymentStatusException(CodeDeployError):
    """The specified deployment status doesn't exist or cannot be determined."""
    _ERROR_CODE = "InvalidDeploymentStatusException"


class InvalidDeploymentStyleException(CodeDeployError):
    """An invalid deployment style was specified. Valid deployment types include "IN_PLACE"
    and "BLUE_GREEN." Valid deployment options include "WITH_TRAFFIC_CONTROL" and
    "WITHOUT_TRAFFIC_CONTROL."
    """

    _ERROR_CODE = "InvalidDeploymentStyleException"


class InvalidDeploymentTargetIdException(CodeDeployError):
    """The target ID provided was not valid."""
    _ERROR_CODE = "InvalidDeploymentTargetIdException"


class InvalidDeploymentWaitTypeException(CodeDeployError):
    """The wait type is invalid."""
    _ERROR_CODE = "InvalidDeploymentWaitTypeException"


class InvalidEC2TagCombinationException(CodeDeployError):
    """A call was submitted that specified both Ec2TagFilters and Ec2TagSet, but only one
    of these data types can be used in a single call.
    """

    _ERROR_CODE = "InvalidEC2TagCombinationException"


class InvalidEC2TagException(CodeDeployError):
    """The tag was specified in an invalid format."""
    _ERROR_CODE = "InvalidEC2TagException"


class InvalidECSServiceException(CodeDeployError):
    """The Amazon ECS service identifier is not valid."""
    _ERROR_CODE = "InvalidECSServiceException"


class InvalidExternalIdException(CodeDeployError):
    """The external ID was specified in an invalid format."""
    _ERROR_CODE = "InvalidExternalIdException"


class InvalidFileExistsBehaviorException(CodeDeployError):
    """An invalid fileExistsBehavior option was specified to determine how CodeDeploy
    handles files or directories that already exist in a deployment target location, but
    weren't part of the previous successful deployment. Valid values include "DISALLOW,"
    "OVERWRITE," and "RETAIN."
    """

    _ERROR_CODE = "InvalidFileExistsBehaviorException"


class InvalidGitHubAccountTokenException(CodeDeployError):
    """The GitHub token is not valid."""
    _ERROR_CODE = "InvalidGitHubAccountTokenException"


class InvalidGitHubAccountTokenNameException(CodeDeployError):
    """The format of the specified GitHub account connection name is invalid."""
    _ERROR_CODE = "InvalidGitHubAccountTokenNameException"


class InvalidIamSessionArnException(CodeDeployError):
    """The IAM session ARN was specified in an invalid format."""
    _ERROR_CODE = "InvalidIamSessionArnException"


class InvalidIamUserArnException(CodeDeployError):
    """The user ARN was specified in an invalid format."""
    _ERROR_CODE = "InvalidIamUserArnException"


class InvalidIgnoreApplicationStopFailuresValueException(CodeDeployError):
    """The IgnoreApplicationStopFailures value is invalid. For Lambda deployments, `false`
    is expected. For EC2/On-premises deployments, `true` or `false` is expected.
    """

    _ERROR_CODE = "InvalidIgnoreApplicationStopFailuresValueException"


class InvalidInputException(CodeDeployError):
    """The input was specified in an invalid format."""
    _ERROR_CODE = "InvalidInputException"


class InvalidInstanceIdException(CodeDeployError):
    _ERROR_CODE = "InvalidInstanceIdException"


class InvalidInstanceNameException(CodeDeployError):
    """The on-premises instance name was specified in an invalid format."""
    _ERROR_CODE = "InvalidInstanceNameException"


class InvalidInstanceStatusException(CodeDeployError):
    """The specified instance status does not exist."""
    _ERROR_CODE = "InvalidInstanceStatusException"


class InvalidInstanceTypeException(CodeDeployError):
    """An invalid instance type was specified for instances in a blue/green deployment.
    Valid values include "Blue" for an original environment and "Green" for a
    replacement environment.
    """

    _ERROR_CODE = "InvalidInstanceTypeException"


class InvalidKeyPrefixFilterException(CodeDeployError):
    """The specified key prefix filter was specified in an invalid format."""
    _ERROR_CODE = "InvalidKeyPrefixFilterException"


class InvalidLifecycleEventHookExecutionIdException(CodeDeployError):
    """A lifecycle event hook is invalid. Review the `hooks` section in your AppSpec file
    to ensure the lifecycle events and `hooks` functions are valid.
    """

    _ERROR_CODE = "InvalidLifecycleEventHookExecutionIdException"


class InvalidLifecycleEventHookExecutionStatusException(CodeDeployError):
    """The result of a Lambda validation function that verifies a lifecycle event is
    invalid. It should return `Succeeded` or `Failed`.
    """

    _ERROR_CODE = "InvalidLifecycleEventHookExecutionStatusException"


class InvalidLoadBalancerInfoException(CodeDeployError):
    """An invalid load balancer name, or no load balancer name, was specified."""
    _ERROR_CODE = "InvalidLoadBalancerInfoException"


class InvalidMinimumHealthyHostValueException(CodeDeployError):
    """The minimum healthy instance value was specified in an invalid format."""
    _ERROR_CODE = "InvalidMinimumHealthyHostValueException"


class InvalidNextTokenException(CodeDeployError):
    """The next token was specified in an invalid format."""
    _ERROR_CODE = "InvalidNextTokenException"


class InvalidOnPremisesTagCombinationException(CodeDeployError):
    """A call was submitted that specified both OnPremisesTagFilters and OnPremisesTagSet,
    but only one of these data types can be used in a single call.
    """

    _ERROR_CODE = "InvalidOnPremisesTagCombinationException"


class InvalidOperationException(CodeDeployError):
    """An invalid operation was detected."""
    _ERROR_CODE = "InvalidOperationException"


class InvalidRegistrationStatusException(CodeDeployError):
    """The registration status was specified in an invalid format."""
    _ERROR_CODE = "InvalidRegistrationStatusException"


class InvalidRevisionException(CodeDeployError):
    """The revision was specified in an invalid format."""
    _ERROR_CODE = "InvalidRevisionException"


class InvalidRoleException(CodeDeployError):
    """The service role ARN was specified in an invalid format. Or, if an Auto Scaling
    group was specified, the specified service role does not grant the appropriate
    permissions to Amazon EC2 Auto Scaling.
    """

    _ERROR_CODE = "InvalidRoleException"


class InvalidSortByException(CodeDeployError):
    """The column name to sort by is either not present or was specified in an invalid
    format.
    """

    _ERROR_CODE = "InvalidSortByException"


class InvalidSortOrderException(CodeDeployError):
    """The sort order was specified in an invalid format."""
    _ERROR_CODE = "InvalidSortOrderException"


class InvalidTagException(CodeDeployError):
    """The tag was specified in an invalid format."""
    _ERROR_CODE = "InvalidTagException"


class InvalidTagFilterException(CodeDeployError):
    """The tag filter was specified in an invalid format."""
    _ERROR_CODE = "InvalidTagFilterException"


class InvalidTagsToAddException(CodeDeployError):
    """The specified tags are not valid."""
    _ERROR_CODE = "InvalidTagsToAddException"


class InvalidTargetException(CodeDeployError):
    """A target is not valid."""
    _ERROR_CODE = "InvalidTargetException"


class InvalidTargetFilterNameException(CodeDeployError):
    """The target filter name is invalid."""
    _ERROR_CODE = "InvalidTargetFilterNameException"


class InvalidTargetGroupPairException(CodeDeployError):
    """A target group pair associated with this deployment is not valid."""
    _ERROR_CODE = "InvalidTargetGroupPairException"


class InvalidTargetInstancesException(CodeDeployError):
    """The target instance configuration is invalid. Possible causes include:

    - Configuration data for target instances was entered for an in-place deployment.
    - The limit of 10 tags for a tag type was exceeded.
    - The combined length of the tag names exceeded the limit.
    - A specified tag is not currently applied to any instances.
    """

    _ERROR_CODE = "InvalidTargetInstancesException"


class InvalidTimeRangeException(CodeDeployError):
    """The specified time range was specified in an invalid format."""
    _ERROR_CODE = "InvalidTimeRangeException"


class InvalidTrafficRoutingConfigurationException(CodeDeployError):
    """The configuration that specifies how traffic is routed during a deployment is
    invalid.
    """

    _ERROR_CODE = "InvalidTrafficRoutingConfigurationException"


class InvalidTriggerConfigException(CodeDeployError):
    """The trigger was specified in an invalid format."""
    _ERROR_CODE = "InvalidTriggerConfigException"


class InvalidUpdateOutdatedInstancesOnlyValueException(CodeDeployError):
    """The UpdateOutdatedInstancesOnly value is invalid. For Lambda deployments, `false` is
    expected. For EC2/On-premises deployments, `true` or `false` is expected.
    """

    _ERROR_CODE = "InvalidUpdateOutdatedInstancesOnlyValueException"


class InvalidZonalDeploymentConfigurationException(CodeDeployError):
    """The `ZonalConfig` object is not valid."""
    _ERROR_CODE = "InvalidZonalDeploymentConfigurationException"


class LifecycleEventAlreadyCompletedException(CodeDeployError):
    """An attempt to return the status of an already completed lifecycle event occurred."""
    _ERROR_CODE = "LifecycleEventAlreadyCompletedException"


class LifecycleHookLimitExceededException(CodeDeployError):
    """The limit for lifecycle hooks was exceeded."""
    _ERROR_CODE = "LifecycleHookLimitExceededException"


class MultipleIamArnsProvidedException(CodeDeployError):
    """Both an user ARN and an IAM session ARN were included in the request. Use only one
    ARN type.
    """

    _ERROR_CODE = "MultipleIamArnsProvidedException"


class OperationNotSupportedException(CodeDeployError):
    """The API used does not support the deployment."""
    _ERROR_CODE = "OperationNotSupportedException"


class ResourceArnRequiredException(CodeDeployError):
    """The ARN of a resource is required, but was not found."""
    _ERROR_CODE = "ResourceArnRequiredException"


class ResourceValidationException(CodeDeployError):
    """The specified resource could not be validated."""
    _ERROR_CODE = "ResourceValidationException"


class RevisionDoesNotExistException(CodeDeployError):
    """The named revision does not exist with the user or Amazon Web Services account."""
    _ERROR_CODE = "RevisionDoesNotExistException"


class RevisionRequiredException(CodeDeployError):
    """The revision ID was not specified."""
    _ERROR_CODE = "RevisionRequiredException"


class RoleRequiredException(CodeDeployError):
    """The role ID was not specified."""
    _ERROR_CODE = "RoleRequiredException"


class TagLimitExceededException(CodeDeployError):
    """The maximum allowed number of tags was exceeded."""
    _ERROR_CODE = "TagLimitExceededException"


class TagRequiredException(CodeDeployError):
    """A tag was not specified."""
    _ERROR_CODE = "TagRequiredException"


class TagSetListLimitExceededException(CodeDeployError):
    """The number of tag groups included in the tag set list exceeded the maximum allowed
    limit of 3.
    """

    _ERROR_CODE = "TagSetListLimitExceededException"


class ThrottlingException(CodeDeployError):
    """An API function was called too frequently."""
    _ERROR_CODE = "ThrottlingException"


class TriggerTargetsLimitExceededException(CodeDeployError):
    """The maximum allowed number of triggers was exceeded."""
    _ERROR_CODE = "TriggerTargetsLimitExceededException"


class UnsupportedActionForDeploymentTypeException(CodeDeployError):
    """A call was submitted that is not supported for the specified deployment type."""
    _ERROR_CODE = "UnsupportedActionForDeploymentTypeException"


EXCEPTIONS: dict[str, type[CodeDeployError]] = {
    "AlarmsLimitExceededException": AlarmsLimitExceededException,
    "ApplicationAlreadyExistsException": ApplicationAlreadyExistsException,
    "ApplicationDoesNotExistException": ApplicationDoesNotExistException,
    "ApplicationLimitExceededException": ApplicationLimitExceededException,
    "ApplicationNameRequiredException": ApplicationNameRequiredException,
    "ArnNotSupportedException": ArnNotSupportedException,
    "BatchLimitExceededException": BatchLimitExceededException,
    "BucketNameFilterRequiredException": BucketNameFilterRequiredException,
    "DeploymentAlreadyCompletedException": DeploymentAlreadyCompletedException,
    "DeploymentAlreadyStartedException": DeploymentAlreadyStartedException,
    "DeploymentConfigAlreadyExistsException": DeploymentConfigAlreadyExistsException,
    "DeploymentConfigDoesNotExistException": DeploymentConfigDoesNotExistException,
    "DeploymentConfigInUseException": DeploymentConfigInUseException,
    "DeploymentConfigLimitExceededException": DeploymentConfigLimitExceededException,
    "DeploymentConfigNameRequiredException": DeploymentConfigNameRequiredException,
    "DeploymentDoesNotExistException": DeploymentDoesNotExistException,
    "DeploymentGroupAlreadyExistsException": DeploymentGroupAlreadyExistsException,
    "DeploymentGroupDoesNotExistException": DeploymentGroupDoesNotExistException,
    "DeploymentGroupLimitExceededException": DeploymentGroupLimitExceededException,
    "DeploymentGroupNameRequiredException": DeploymentGroupNameRequiredException,
    "DeploymentIdRequiredException": DeploymentIdRequiredException,
    "DeploymentIsNotInReadyStateException": DeploymentIsNotInReadyStateException,
    "DeploymentLimitExceededException": DeploymentLimitExceededException,
    "DeploymentNotStartedException": DeploymentNotStartedException,
    "DeploymentTargetDoesNotExistException": DeploymentTargetDoesNotExistException,
    "DeploymentTargetIdRequiredException": DeploymentTargetIdRequiredException,
    "DeploymentTargetListSizeExceededException": DeploymentTargetListSizeExceededException,
    "DescriptionTooLongException": DescriptionTooLongException,
    "ECSServiceMappingLimitExceededException": ECSServiceMappingLimitExceededException,
    "GitHubAccountTokenDoesNotExistException": GitHubAccountTokenDoesNotExistException,
    "GitHubAccountTokenNameRequiredException": GitHubAccountTokenNameRequiredException,
    "IamArnRequiredException": IamArnRequiredException,
    "IamSessionArnAlreadyRegisteredException": IamSessionArnAlreadyRegisteredException,
    "IamUserArnAlreadyRegisteredException": IamUserArnAlreadyRegisteredException,
    "IamUserArnRequiredException": IamUserArnRequiredException,
    "InstanceDoesNotExistException": InstanceDoesNotExistException,
    "InstanceIdRequiredException": InstanceIdRequiredException,
    "InstanceLimitExceededException": InstanceLimitExceededException,
    "InstanceNameAlreadyRegisteredException": InstanceNameAlreadyRegisteredException,
    "InstanceNameRequiredException": InstanceNameRequiredException,
    "InstanceNotRegisteredException": InstanceNotRegisteredException,
    "InvalidAlarmConfigException": InvalidAlarmConfigException,
    "InvalidApplicationNameException": InvalidApplicationNameException,
    "InvalidArnException": InvalidArnException,
    "InvalidAutoRollbackConfigException": InvalidAutoRollbackConfigException,
    "InvalidAutoScalingGroupException": InvalidAutoScalingGroupException,
    "InvalidBlueGreenDeploymentConfigurationException": InvalidBlueGreenDeploymentConfigurationException,
    "InvalidBucketNameFilterException": InvalidBucketNameFilterException,
    "InvalidComputePlatformException": InvalidComputePlatformException,
    "InvalidDeployedStateFilterException": InvalidDeployedStateFilterException,
    "InvalidDeploymentConfigNameException": InvalidDeploymentConfigNameException,
    "InvalidDeploymentGroupNameException": InvalidDeploymentGroupNameException,
    "InvalidDeploymentIdException": InvalidDeploymentIdException,
    "InvalidDeploymentInstanceTypeException": InvalidDeploymentInstanceTypeException,
    "InvalidDeploymentStatusException": InvalidDeploymentStatusException,
    "InvalidDeploymentStyleException": InvalidDeploymentStyleException,
    "InvalidDeploymentTargetIdException": InvalidDeploymentTargetIdException,
    "InvalidDeploymentWaitTypeException": InvalidDeploymentWaitTypeException,
    "InvalidEC2TagCombinationException": InvalidEC2TagCombinationException,
    "InvalidEC2TagException": InvalidEC2TagException,
    "InvalidECSServiceException": InvalidECSServiceException,
    "InvalidExternalIdException": InvalidExternalIdException,
    "InvalidFileExistsBehaviorException": InvalidFileExistsBehaviorException,
    "InvalidGitHubAccountTokenException": InvalidGitHubAccountTokenException,
    "InvalidGitHubAccountTokenNameException": InvalidGitHubAccountTokenNameException,
    "InvalidIamSessionArnException": InvalidIamSessionArnException,
    "InvalidIamUserArnException": InvalidIamUserArnException,
    "InvalidIgnoreApplicationStopFailuresValueException": InvalidIgnoreApplicationStopFailuresValueException,
    "InvalidInputException": InvalidInputException,
    "InvalidInstanceIdException": InvalidInstanceIdException,
    "InvalidInstanceNameException": InvalidInstanceNameException,
    "InvalidInstanceStatusException": InvalidInstanceStatusException,
    "InvalidInstanceTypeException": InvalidInstanceTypeException,
    "InvalidKeyPrefixFilterException": InvalidKeyPrefixFilterException,
    "InvalidLifecycleEventHookExecutionIdException": InvalidLifecycleEventHookExecutionIdException,
    "InvalidLifecycleEventHookExecutionStatusException": InvalidLifecycleEventHookExecutionStatusException,
    "InvalidLoadBalancerInfoException": InvalidLoadBalancerInfoException,
    "InvalidMinimumHealthyHostValueException": InvalidMinimumHealthyHostValueException,
    "InvalidNextTokenException": InvalidNextTokenException,
    "InvalidOnPremisesTagCombinationException": InvalidOnPremisesTagCombinationException,
    "InvalidOperationException": InvalidOperationException,
    "InvalidRegistrationStatusException": InvalidRegistrationStatusException,
    "InvalidRevisionException": InvalidRevisionException,
    "InvalidRoleException": InvalidRoleException,
    "InvalidSortByException": InvalidSortByException,
    "InvalidSortOrderException": InvalidSortOrderException,
    "InvalidTagException": InvalidTagException,
    "InvalidTagFilterException": InvalidTagFilterException,
    "InvalidTagsToAddException": InvalidTagsToAddException,
    "InvalidTargetException": InvalidTargetException,
    "InvalidTargetFilterNameException": InvalidTargetFilterNameException,
    "InvalidTargetGroupPairException": InvalidTargetGroupPairException,
    "InvalidTargetInstancesException": InvalidTargetInstancesException,
    "InvalidTimeRangeException": InvalidTimeRangeException,
    "InvalidTrafficRoutingConfigurationException": InvalidTrafficRoutingConfigurationException,
    "InvalidTriggerConfigException": InvalidTriggerConfigException,
    "InvalidUpdateOutdatedInstancesOnlyValueException": InvalidUpdateOutdatedInstancesOnlyValueException,
    "InvalidZonalDeploymentConfigurationException": InvalidZonalDeploymentConfigurationException,
    "LifecycleEventAlreadyCompletedException": LifecycleEventAlreadyCompletedException,
    "LifecycleHookLimitExceededException": LifecycleHookLimitExceededException,
    "MultipleIamArnsProvidedException": MultipleIamArnsProvidedException,
    "OperationNotSupportedException": OperationNotSupportedException,
    "ResourceArnRequiredException": ResourceArnRequiredException,
    "ResourceValidationException": ResourceValidationException,
    "RevisionDoesNotExistException": RevisionDoesNotExistException,
    "RevisionRequiredException": RevisionRequiredException,
    "RoleRequiredException": RoleRequiredException,
    "TagLimitExceededException": TagLimitExceededException,
    "TagRequiredException": TagRequiredException,
    "TagSetListLimitExceededException": TagSetListLimitExceededException,
    "ThrottlingException": ThrottlingException,
    "TriggerTargetsLimitExceededException": TriggerTargetsLimitExceededException,
    "UnsupportedActionForDeploymentTypeException": UnsupportedActionForDeploymentTypeException,
}
