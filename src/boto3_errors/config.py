# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class ConfigServiceError(Boto3Error):
    _SERVICE = "config"


class ConformancePackTemplateValidationException(ConfigServiceError):
    """You have specified a template that is not valid or supported."""
    _ERROR_CODE = "ConformancePackTemplateValidationException"


class IdempotentParameterMismatch(ConfigServiceError):
    """Using the same client token with one or more different parameters. Specify a new
    client token with the parameter changes and try again.
    """

    _ERROR_CODE = "IdempotentParameterMismatch"


class InsufficientDeliveryPolicyException(ConfigServiceError):
    """Your Amazon S3 bucket policy does not permit Config to write to it."""
    _ERROR_CODE = "InsufficientDeliveryPolicyException"


class InsufficientPermissionsException(ConfigServiceError):
    """Indicates one of the following errors:

    - For PutConfigRule, the rule cannot be created because the IAM role assigned to
      Config lacks permissions to perform the config:Put* action.
    - For PutConfigRule, the Lambda function cannot be invoked. Check the function ARN,
      and check the function's permissions.
    - For PutOrganizationConfigRule, organization Config rule cannot be created because
      you do not have permissions to call IAM `GetRole` action or create a service-
      linked role.
    - For PutConformancePack and PutOrganizationConformancePack, a conformance pack
      cannot be created because you do not have the following permissions:

      - You do not have permission to call IAM `GetRole` action or create a service-
        linked role.
      - You do not have permission to read Amazon S3 bucket or call SSM:GetDocument.
    """

    _ERROR_CODE = "InsufficientPermissionsException"


class InvalidConfigurationRecorderNameException(ConfigServiceError):
    """You have provided a name for the configuration recorder that is not valid."""
    _ERROR_CODE = "InvalidConfigurationRecorderNameException"


class InvalidDeliveryChannelNameException(ConfigServiceError):
    """The specified delivery channel name is not valid."""
    _ERROR_CODE = "InvalidDeliveryChannelNameException"


class InvalidExpressionException(ConfigServiceError):
    """The syntax of the query is incorrect."""
    _ERROR_CODE = "InvalidExpressionException"


class InvalidLimitException(ConfigServiceError):
    """The specified limit is outside the allowable range."""
    _ERROR_CODE = "InvalidLimitException"


class InvalidNextTokenException(ConfigServiceError):
    """The specified next token is not valid. Specify the `nextToken` string that was
    returned in the previous response to get the next page of results.
    """

    _ERROR_CODE = "InvalidNextTokenException"


class InvalidParameterValueException(ConfigServiceError):
    """One or more of the specified parameters are not valid. Verify that your parameters
    are valid and try again.
    """

    _ERROR_CODE = "InvalidParameterValueException"


class InvalidRecordingGroupException(ConfigServiceError):
    """Indicates one of the following errors:

    - You have provided a combination of parameter values that is not valid. For
      example:

      - Setting the `allSupported` field of RecordingGroup to `true`, but providing a
        non-empty list for the `resourceTypes`field of RecordingGroup.
      - Setting the `allSupported` field of RecordingGroup to `true`, but also setting
        the `useOnly` field of RecordingStrategy to `EXCLUSION_BY_RESOURCE_TYPES`.

    - Every parameter is either null, false, or empty.
    - You have reached the limit of the number of resource types you can provide for the
      recording group.
    - You have provided resource types or a recording strategy that are not valid.
    """

    _ERROR_CODE = "InvalidRecordingGroupException"


class InvalidResultTokenException(ConfigServiceError):
    """The specified `ResultToken` is not valid."""
    _ERROR_CODE = "InvalidResultTokenException"


class InvalidRoleException(ConfigServiceError):
    """You have provided a null or empty Amazon Resource Name (ARN) for the IAM role
    assumed by Config and used by the configuration recorder.
    """

    _ERROR_CODE = "InvalidRoleException"


class InvalidS3KeyPrefixException(ConfigServiceError):
    """The specified Amazon S3 key prefix is not valid."""
    _ERROR_CODE = "InvalidS3KeyPrefixException"


class InvalidS3KmsKeyArnException(ConfigServiceError):
    """The specified Amazon KMS Key ARN is not valid."""
    _ERROR_CODE = "InvalidS3KmsKeyArnException"


class InvalidSNSTopicARNException(ConfigServiceError):
    """The specified Amazon SNS topic does not exist."""
    _ERROR_CODE = "InvalidSNSTopicARNException"


class InvalidTimeRangeException(ConfigServiceError):
    """The specified time range is not valid. The earlier time is not chronologically
    before the later time.
    """

    _ERROR_CODE = "InvalidTimeRangeException"


class LastDeliveryChannelDeleteFailedException(ConfigServiceError):
    """You cannot delete the delivery channel you specified because the configuration
    recorder is running.
    """

    _ERROR_CODE = "LastDeliveryChannelDeleteFailedException"


class LimitExceededException(ConfigServiceError):
    """For `StartConfigRulesEvaluation` API, this exception is thrown if an evaluation is
    in progress or if you call the StartConfigRulesEvaluation API more than once per
    minute.

    For `PutConfigurationAggregator` API, this exception is thrown if the number of
    accounts and aggregators exceeds the limit.
    """

    _ERROR_CODE = "LimitExceededException"


class MaxActiveResourcesExceededException(ConfigServiceError):
    """You have reached the limit of active custom resource types in your account. There is
    a limit of 100,000. Delete unused resources using DeleteResourceConfig ``.
    """

    _ERROR_CODE = "MaxActiveResourcesExceededException"


class MaxNumberOfConfigRulesExceededException(ConfigServiceError):
    """Failed to add the Config rule because the account already contains the maximum
    number of 150 rules. Consider deleting any deactivated rules before you add new
    rules.
    """

    _ERROR_CODE = "MaxNumberOfConfigRulesExceededException"


class MaxNumberOfConfigurationRecordersExceededException(ConfigServiceError):
    """You have reached the limit of the number of configuration recorders you can create."""
    _ERROR_CODE = "MaxNumberOfConfigurationRecordersExceededException"


class MaxNumberOfConformancePacksExceededException(ConfigServiceError):
    """You have reached the limit of the number of conformance packs you can create in an
    account. For more information, see Service Limits in the Config Developer Guide.
    """

    _ERROR_CODE = "MaxNumberOfConformancePacksExceededException"


class MaxNumberOfDeliveryChannelsExceededException(ConfigServiceError):
    """You have reached the limit of the number of delivery channels you can create."""
    _ERROR_CODE = "MaxNumberOfDeliveryChannelsExceededException"


class MaxNumberOfOrganizationConfigRulesExceededException(ConfigServiceError):
    """You have reached the limit of the number of organization Config rules you can
    create. For more information, see see Service Limits in the Config Developer Guide.
    """

    _ERROR_CODE = "MaxNumberOfOrganizationConfigRulesExceededException"


class MaxNumberOfOrganizationConformancePacksExceededException(ConfigServiceError):
    """You have reached the limit of the number of organization conformance packs you can
    create in an account. For more information, see Service Limits in the Config
    Developer Guide.
    """

    _ERROR_CODE = "MaxNumberOfOrganizationConformancePacksExceededException"


class MaxNumberOfRetentionConfigurationsExceededException(ConfigServiceError):
    """Failed to add the retention configuration because a retention configuration with
    that name already exists.
    """

    _ERROR_CODE = "MaxNumberOfRetentionConfigurationsExceededException"


class NoAvailableConfigurationRecorderException(ConfigServiceError):
    """There are no configuration recorders available to provide the role needed to
    describe your resources. Create a configuration recorder.
    """

    _ERROR_CODE = "NoAvailableConfigurationRecorderException"


class NoAvailableDeliveryChannelException(ConfigServiceError):
    """There is no delivery channel available to record configurations."""
    _ERROR_CODE = "NoAvailableDeliveryChannelException"


class NoAvailableOrganizationException(ConfigServiceError):
    """Organization is no longer available."""
    _ERROR_CODE = "NoAvailableOrganizationException"


class NoRunningConfigurationRecorderException(ConfigServiceError):
    """There is no configuration recorder running."""
    _ERROR_CODE = "NoRunningConfigurationRecorderException"


class NoSuchBucketException(ConfigServiceError):
    """The specified Amazon S3 bucket does not exist."""
    _ERROR_CODE = "NoSuchBucketException"


class NoSuchConfigRuleException(ConfigServiceError):
    """The Config rule in the request is not valid. Verify that the rule is an Config
    Process Check rule, that the rule name is correct, and that valid Amazon Resouce
    Names (ARNs) are used before trying again.
    """

    _ERROR_CODE = "NoSuchConfigRuleException"


class NoSuchConfigRuleInConformancePackException(ConfigServiceError):
    """Config rule that you passed in the filter does not exist."""
    _ERROR_CODE = "NoSuchConfigRuleInConformancePackException"


class NoSuchConfigurationAggregatorException(ConfigServiceError):
    """You have specified a configuration aggregator that does not exist."""
    _ERROR_CODE = "NoSuchConfigurationAggregatorException"


class NoSuchConfigurationRecorderException(ConfigServiceError):
    """You have specified a configuration recorder that does not exist."""
    _ERROR_CODE = "NoSuchConfigurationRecorderException"


class NoSuchConformancePackException(ConfigServiceError):
    """You specified one or more conformance packs that do not exist."""
    _ERROR_CODE = "NoSuchConformancePackException"


class NoSuchDeliveryChannelException(ConfigServiceError):
    """You have specified a delivery channel that does not exist."""
    _ERROR_CODE = "NoSuchDeliveryChannelException"


class NoSuchOrganizationConfigRuleException(ConfigServiceError):
    """The Config rule in the request is not valid. Verify that the rule is an organization
    Config Process Check rule, that the rule name is correct, and that valid Amazon
    Resouce Names (ARNs) are used before trying again.
    """

    _ERROR_CODE = "NoSuchOrganizationConfigRuleException"


class NoSuchOrganizationConformancePackException(ConfigServiceError):
    """Config organization conformance pack that you passed in the filter does not exist.

    For DeleteOrganizationConformancePack, you tried to delete an organization
    conformance pack that does not exist.
    """

    _ERROR_CODE = "NoSuchOrganizationConformancePackException"


class NoSuchRemediationConfigurationException(ConfigServiceError):
    """You specified an Config rule without a remediation configuration."""
    _ERROR_CODE = "NoSuchRemediationConfigurationException"


class NoSuchRemediationExceptionException(ConfigServiceError):
    """You tried to delete a remediation exception that does not exist."""
    _ERROR_CODE = "NoSuchRemediationExceptionException"


class NoSuchRetentionConfigurationException(ConfigServiceError):
    """You have specified a retention configuration that does not exist."""
    _ERROR_CODE = "NoSuchRetentionConfigurationException"


class OrganizationAccessDeniedException(ConfigServiceError):
    """For `PutConfigurationAggregator` API, you can see this exception for the following
    reasons:

    - No permission to call `EnableAWSServiceAccess` API
    - The configuration aggregator cannot be updated because your Amazon Web Services
      Organization management account or the delegated administrator role changed.
      Delete this aggregator and create a new one with the current Amazon Web Services
      Organization.
    - The configuration aggregator is associated with a previous Amazon Web Services
      Organization and Config cannot aggregate data with current Amazon Web Services
      Organization. Delete this aggregator and create a new one with the current Amazon
      Web Services Organization.
    - You are not a registered delegated administrator for Config with permissions to
      call `ListDelegatedAdministrators` API. Ensure that the management account
      registers delagated administrator for Config service principle name before the
      delegated administrator creates an aggregator.

    For all `OrganizationConfigRule` and `OrganizationConformancePack` APIs, Config
    throws an exception if APIs are called from member accounts. All APIs must be called
    from organization management account.
    """

    _ERROR_CODE = "OrganizationAccessDeniedException"


class OrganizationAllFeaturesNotEnabledException(ConfigServiceError):
    """Config resource cannot be created because your organization does not have all
    features enabled.
    """

    _ERROR_CODE = "OrganizationAllFeaturesNotEnabledException"


class OrganizationConformancePackTemplateValidationException(ConfigServiceError):
    """You have specified a template that is not valid or supported."""
    _ERROR_CODE = "OrganizationConformancePackTemplateValidationException"


class OversizedConfigurationItemException(ConfigServiceError):
    """The configuration item size is outside the allowable range."""
    _ERROR_CODE = "OversizedConfigurationItemException"


class RemediationInProgressException(ConfigServiceError):
    """Remediation action is in progress. You can either cancel execution in Amazon Web
    Services Systems Manager or wait and try again later.
    """

    _ERROR_CODE = "RemediationInProgressException"


class ResourceConcurrentModificationException(ConfigServiceError):
    """Two users are trying to modify the same query at the same time. Wait for a moment
    and try again.
    """

    _ERROR_CODE = "ResourceConcurrentModificationException"


class ResourceInUseException(ConfigServiceError):
    """You see this exception in the following cases:

    - For DeleteConfigRule, Config is deleting this rule. Try your request again later.
    - For DeleteConfigRule, the rule is deleting your evaluation results. Try your
      request again later.
    - For DeleteConfigRule, a remediation action is associated with the rule and Config
      cannot delete this rule. Delete the remediation action associated with the rule
      before deleting the rule and try your request again later.
    - For PutConfigOrganizationRule, organization Config rule deletion is in progress.
      Try your request again later.
    - For DeleteOrganizationConfigRule, organization Config rule creation is in
      progress. Try your request again later.
    - For PutConformancePack and PutOrganizationConformancePack, a conformance pack
      creation, update, and deletion is in progress. Try your request again later.
    - For DeleteConformancePack, a conformance pack creation, update, and deletion is in
      progress. Try your request again later.
    """

    _ERROR_CODE = "ResourceInUseException"


class ResourceNotDiscoveredException(ConfigServiceError):
    """You have specified a resource that is either unknown or has not been discovered."""
    _ERROR_CODE = "ResourceNotDiscoveredException"


class ResourceNotFoundException(ConfigServiceError):
    """You have specified a resource that does not exist."""
    _ERROR_CODE = "ResourceNotFoundException"


class TooManyTagsException(ConfigServiceError):
    """You have reached the limit of the number of tags you can use. For more information,
    see Service Limits in the Config Developer Guide.
    """

    _ERROR_CODE = "TooManyTagsException"


class ValidationException(ConfigServiceError):
    """The requested action is not valid.

    For PutStoredQuery, you will see this exception if there are missing required fields
    or if the input value fails the validation, or if you are trying to create more than
    300 queries.

    For GetStoredQuery, ListStoredQuery, and DeleteStoredQuery you will see this
    exception if there are missing required fields or if the input value fails the
    validation.
    """

    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[ConfigServiceError]] = {
    "ConformancePackTemplateValidationException": ConformancePackTemplateValidationException,
    "IdempotentParameterMismatch": IdempotentParameterMismatch,
    "InsufficientDeliveryPolicyException": InsufficientDeliveryPolicyException,
    "InsufficientPermissionsException": InsufficientPermissionsException,
    "InvalidConfigurationRecorderNameException": InvalidConfigurationRecorderNameException,
    "InvalidDeliveryChannelNameException": InvalidDeliveryChannelNameException,
    "InvalidExpressionException": InvalidExpressionException,
    "InvalidLimitException": InvalidLimitException,
    "InvalidNextTokenException": InvalidNextTokenException,
    "InvalidParameterValueException": InvalidParameterValueException,
    "InvalidRecordingGroupException": InvalidRecordingGroupException,
    "InvalidResultTokenException": InvalidResultTokenException,
    "InvalidRoleException": InvalidRoleException,
    "InvalidS3KeyPrefixException": InvalidS3KeyPrefixException,
    "InvalidS3KmsKeyArnException": InvalidS3KmsKeyArnException,
    "InvalidSNSTopicARNException": InvalidSNSTopicARNException,
    "InvalidTimeRangeException": InvalidTimeRangeException,
    "LastDeliveryChannelDeleteFailedException": LastDeliveryChannelDeleteFailedException,
    "LimitExceededException": LimitExceededException,
    "MaxActiveResourcesExceededException": MaxActiveResourcesExceededException,
    "MaxNumberOfConfigRulesExceededException": MaxNumberOfConfigRulesExceededException,
    "MaxNumberOfConfigurationRecordersExceededException": MaxNumberOfConfigurationRecordersExceededException,
    "MaxNumberOfConformancePacksExceededException": MaxNumberOfConformancePacksExceededException,
    "MaxNumberOfDeliveryChannelsExceededException": MaxNumberOfDeliveryChannelsExceededException,
    "MaxNumberOfOrganizationConfigRulesExceededException": MaxNumberOfOrganizationConfigRulesExceededException,
    "MaxNumberOfOrganizationConformancePacksExceededException": MaxNumberOfOrganizationConformancePacksExceededException,
    "MaxNumberOfRetentionConfigurationsExceededException": MaxNumberOfRetentionConfigurationsExceededException,
    "NoAvailableConfigurationRecorderException": NoAvailableConfigurationRecorderException,
    "NoAvailableDeliveryChannelException": NoAvailableDeliveryChannelException,
    "NoAvailableOrganizationException": NoAvailableOrganizationException,
    "NoRunningConfigurationRecorderException": NoRunningConfigurationRecorderException,
    "NoSuchBucketException": NoSuchBucketException,
    "NoSuchConfigRuleException": NoSuchConfigRuleException,
    "NoSuchConfigRuleInConformancePackException": NoSuchConfigRuleInConformancePackException,
    "NoSuchConfigurationAggregatorException": NoSuchConfigurationAggregatorException,
    "NoSuchConfigurationRecorderException": NoSuchConfigurationRecorderException,
    "NoSuchConformancePackException": NoSuchConformancePackException,
    "NoSuchDeliveryChannelException": NoSuchDeliveryChannelException,
    "NoSuchOrganizationConfigRuleException": NoSuchOrganizationConfigRuleException,
    "NoSuchOrganizationConformancePackException": NoSuchOrganizationConformancePackException,
    "NoSuchRemediationConfigurationException": NoSuchRemediationConfigurationException,
    "NoSuchRemediationExceptionException": NoSuchRemediationExceptionException,
    "NoSuchRetentionConfigurationException": NoSuchRetentionConfigurationException,
    "OrganizationAccessDeniedException": OrganizationAccessDeniedException,
    "OrganizationAllFeaturesNotEnabledException": OrganizationAllFeaturesNotEnabledException,
    "OrganizationConformancePackTemplateValidationException": OrganizationConformancePackTemplateValidationException,
    "OversizedConfigurationItemException": OversizedConfigurationItemException,
    "RemediationInProgressException": RemediationInProgressException,
    "ResourceConcurrentModificationException": ResourceConcurrentModificationException,
    "ResourceInUseException": ResourceInUseException,
    "ResourceNotDiscoveredException": ResourceNotDiscoveredException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "TooManyTagsException": TooManyTagsException,
    "ValidationException": ValidationException,
}
