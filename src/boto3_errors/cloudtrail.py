# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class CloudTrailError(Boto3Error):
    _SERVICE = "cloudtrail"


class AccessDeniedException(CloudTrailError):
    """You do not have sufficient access to perform this action."""
    _ERROR_CODE = "AccessDeniedException"


class AccountHasOngoingImportException(CloudTrailError):
    """This exception is thrown when you start a new import and a previous import is still
    in progress.
    """

    _ERROR_CODE = "AccountHasOngoingImportException"


class AccountNotFoundException(CloudTrailError):
    """This exception is thrown when the specified account is not found or not part of an
    organization.
    """

    _ERROR_CODE = "AccountNotFoundException"


class AccountNotRegisteredException(CloudTrailError):
    """This exception is thrown when the specified account is not registered as the
    CloudTrail delegated administrator.
    """

    _ERROR_CODE = "AccountNotRegisteredException"


class AccountRegisteredException(CloudTrailError):
    """This exception is thrown when the account is already registered as the CloudTrail
    delegated administrator.
    """

    _ERROR_CODE = "AccountRegisteredException"


class CannotDelegateManagementAccountException(CloudTrailError):
    """This exception is thrown when the management account of an organization is
    registered as the CloudTrail delegated administrator.
    """

    _ERROR_CODE = "CannotDelegateManagementAccountException"


class ChannelARNInvalidException(CloudTrailError):
    """This exception is thrown when the specified value of `ChannelARN` is not valid."""
    _ERROR_CODE = "ChannelARNInvalidException"


class ChannelAlreadyExistsException(CloudTrailError):
    """This exception is thrown when the provided channel already exists."""
    _ERROR_CODE = "ChannelAlreadyExistsException"


class ChannelExistsForEDSException(CloudTrailError):
    """This exception is thrown when the specified event data store cannot yet be deleted
    because it is in use by a channel.
    """

    _ERROR_CODE = "ChannelExistsForEDSException"


class ChannelMaxLimitExceededException(CloudTrailError):
    """This exception is thrown when the maximum number of channels limit is exceeded."""
    _ERROR_CODE = "ChannelMaxLimitExceededException"


class ChannelNotFoundException(CloudTrailError):
    """This exception is thrown when CloudTrail cannot find the specified channel."""
    _ERROR_CODE = "ChannelNotFoundException"


class CloudTrailARNInvalidException(CloudTrailError):
    """This exception is thrown when an operation is called with an ARN that is not valid.

    The following is the format of a trail ARN: `arn:aws:cloudtrail:us-
    east-2:123456789012:trail/MyTrail`

    The following is the format of an event data store ARN: `arn:aws:cloudtrail:us-
    east-2:123456789012:eventdatastore/EXAMPLE-f852-4e8f-8bd1-bcf6cEXAMPLE`

    The following is the format of a dashboard ARN: `arn:aws:cloudtrail:us-
    east-1:123456789012:dashboard/exampleDash`

    The following is the format of a channel ARN: `arn:aws:cloudtrail:us-
    east-2:123456789012:channel/01234567890`
    """

    _ERROR_CODE = "CloudTrailARNInvalidException"


class CloudTrailAccessNotEnabledException(CloudTrailError):
    """This exception is thrown when trusted access has not been enabled between CloudTrail
    and Organizations. For more information, see How to enable or disable trusted access
    in the Organizations User Guide and Prepare For Creating a Trail For Your
    Organization in the CloudTrail User Guide.
    """

    _ERROR_CODE = "CloudTrailAccessNotEnabledException"


class CloudTrailInvalidClientTokenIdException(CloudTrailError):
    """This exception is thrown when a call results in the `InvalidClientTokenId` error
    code. This can occur when you are creating or updating a trail to send notifications
    to an Amazon SNS topic that is in a suspended Amazon Web Services account.
    """

    _ERROR_CODE = "CloudTrailInvalidClientTokenIdException"


class CloudWatchLogsDeliveryUnavailableException(CloudTrailError):
    """Cannot set a CloudWatch Logs delivery for this Region."""
    _ERROR_CODE = "CloudWatchLogsDeliveryUnavailableException"


class ConcurrentModificationException(CloudTrailError):
    """You are trying to update a resource when another request is in progress. Allow
    sufficient wait time for the previous request to complete, then retry your request.
    """

    _ERROR_CODE = "ConcurrentModificationException"


class ConflictException(CloudTrailError):
    """This exception is thrown when the specified resource is not ready for an operation.
    This can occur when you try to run an operation on a resource before CloudTrail has
    time to fully load the resource, or because another operation is modifying the
    resource. If this exception occurs, wait a few minutes, and then try the operation
    again.
    """

    _ERROR_CODE = "ConflictException"


class DelegatedAdminAccountLimitExceededException(CloudTrailError):
    """This exception is thrown when the maximum number of CloudTrail delegated
    administrators is reached.
    """

    _ERROR_CODE = "DelegatedAdminAccountLimitExceededException"


class EventDataStoreARNInvalidException(CloudTrailError):
    """The specified event data store ARN is not valid or does not map to an event data
    store in your account.
    """

    _ERROR_CODE = "EventDataStoreARNInvalidException"


class EventDataStoreAlreadyExistsException(CloudTrailError):
    """An event data store with that name already exists."""
    _ERROR_CODE = "EventDataStoreAlreadyExistsException"


class EventDataStoreFederationEnabledException(CloudTrailError):
    """You cannot delete the event data store because Lake query federation is enabled. To
    delete the event data store, run the `DisableFederation` operation to disable Lake
    query federation on the event data store.
    """

    _ERROR_CODE = "EventDataStoreFederationEnabledException"


class EventDataStoreHasOngoingImportException(CloudTrailError):
    """This exception is thrown when you try to update or delete an event data store that
    currently has an import in progress.
    """

    _ERROR_CODE = "EventDataStoreHasOngoingImportException"


class EventDataStoreMaxLimitExceededException(CloudTrailError):
    """Your account has used the maximum number of event data stores."""
    _ERROR_CODE = "EventDataStoreMaxLimitExceededException"


class EventDataStoreNotFoundException(CloudTrailError):
    """The specified event data store was not found."""
    _ERROR_CODE = "EventDataStoreNotFoundException"


class EventDataStoreTerminationProtectedException(CloudTrailError):
    """The event data store cannot be deleted because termination protection is enabled for
    it.
    """

    _ERROR_CODE = "EventDataStoreTerminationProtectedException"


class GenerateResponseException(CloudTrailError):
    """This exception is thrown when a valid query could not be generated for the provided
    prompt.
    """

    _ERROR_CODE = "GenerateResponseException"


class ImportNotFoundException(CloudTrailError):
    """The specified import was not found."""
    _ERROR_CODE = "ImportNotFoundException"


class InactiveEventDataStoreException(CloudTrailError):
    """The event data store is inactive."""
    _ERROR_CODE = "InactiveEventDataStoreException"


class InactiveQueryException(CloudTrailError):
    """The specified query cannot be canceled because it is in the `FINISHED`, `FAILED`,
    `TIMED_OUT`, or `CANCELLED` state.
    """

    _ERROR_CODE = "InactiveQueryException"


class InsightNotEnabledException(CloudTrailError):
    """If you run `GetInsightSelectors` on a trail or event data store that does not have
    Insights events enabled, the operation throws the exception
    `InsightNotEnabledException`.
    """

    _ERROR_CODE = "InsightNotEnabledException"


class InsufficientDependencyServiceAccessPermissionException(CloudTrailError):
    """This exception is thrown when the IAM identity that is used to create the
    organization resource lacks one or more required permissions for creating an
    organization resource in a required service.
    """

    _ERROR_CODE = "InsufficientDependencyServiceAccessPermissionException"


class InsufficientEncryptionPolicyException(CloudTrailError):
    """For the `CreateTrail` `PutInsightSelectors`, `UpdateTrail`, `StartQuery`, and
    `StartImport` operations, this exception is thrown when the policy on the S3 bucket
    or KMS key does not have sufficient permissions for the operation.

    For all other operations, this exception is thrown when the policy for the KMS key
    does not have sufficient permissions for the operation.
    """

    _ERROR_CODE = "InsufficientEncryptionPolicyException"


class InsufficientIAMAccessPermissionException(CloudTrailError):
    """The task can't be completed because you are signed in with an account that lacks
    permissions to view or create a service-linked role. Sign in with an account that
    has the required permissions and then try again.
    """

    _ERROR_CODE = "InsufficientIAMAccessPermissionException"


class InsufficientS3BucketPolicyException(CloudTrailError):
    """This exception is thrown when the policy on the S3 bucket is not sufficient."""
    _ERROR_CODE = "InsufficientS3BucketPolicyException"


class InsufficientSnsTopicPolicyException(CloudTrailError):
    """This exception is thrown when the policy on the Amazon SNS topic is not sufficient."""
    _ERROR_CODE = "InsufficientSnsTopicPolicyException"


class InvalidCloudWatchLogsLogGroupArnException(CloudTrailError):
    """This exception is thrown when the provided CloudWatch Logs log group is not valid."""
    _ERROR_CODE = "InvalidCloudWatchLogsLogGroupArnException"


class InvalidCloudWatchLogsRoleArnException(CloudTrailError):
    """This exception is thrown when the provided role is not valid."""
    _ERROR_CODE = "InvalidCloudWatchLogsRoleArnException"


class InvalidDateRangeException(CloudTrailError):
    """A date range for the query was specified that is not valid. Be sure that the start
    time is chronologically before the end time. For more information about writing a
    query, see Create or edit a query in the CloudTrail User Guide.
    """

    _ERROR_CODE = "InvalidDateRangeException"


class InvalidEventCategoryException(CloudTrailError):
    """Occurs if an event category that is not valid is specified as a value of
    `EventCategory`.
    """

    _ERROR_CODE = "InvalidEventCategoryException"


class InvalidEventDataStoreCategoryException(CloudTrailError):
    """This exception is thrown when event categories of specified event data stores are
    not valid.
    """

    _ERROR_CODE = "InvalidEventDataStoreCategoryException"


class InvalidEventDataStoreStatusException(CloudTrailError):
    """The event data store is not in a status that supports the operation."""
    _ERROR_CODE = "InvalidEventDataStoreStatusException"


class InvalidEventSelectorsException(CloudTrailError):
    """This exception is thrown when the `PutEventSelectors` operation is called with a
    number of event selectors, advanced event selectors, or data resources that is not
    valid. The combination of event selectors or advanced event selectors and data
    resources is not valid. A trail can have up to 5 event selectors. If a trail uses
    advanced event selectors, a maximum of 500 total values for all conditions in all
    advanced event selectors is allowed. A trail is limited to 250 data resources. These
    data resources can be distributed across event selectors, but the overall total
    cannot exceed 250.

    You can:

    - Specify a valid number of event selectors (1 to 5) for a trail.
    - Specify a valid number of data resources (1 to 250) for an event selector. The
      limit of number of resources on an individual event selector is configurable up to
      250. However, this upper limit is allowed only if the total number of data
      resources does not exceed 250 across all event selectors for a trail.
    - Specify up to 500 values for all conditions in all advanced event selectors for a
      trail.
    - Specify a valid value for a parameter. For example, specifying the `ReadWriteType`
      parameter with a value of `read-only` is not valid.
    """

    _ERROR_CODE = "InvalidEventSelectorsException"


class InvalidHomeRegionException(CloudTrailError):
    """This exception is thrown when an operation is called on a trail from a Region other
    than the Region in which the trail was created.
    """

    _ERROR_CODE = "InvalidHomeRegionException"


class InvalidImportSourceException(CloudTrailError):
    """This exception is thrown when the provided source S3 bucket is not valid for import."""
    _ERROR_CODE = "InvalidImportSourceException"


class InvalidInsightSelectorsException(CloudTrailError):
    """For `PutInsightSelectors`, this exception is thrown when the formatting or syntax of
    the `InsightSelectors` JSON statement is not valid, or the specified `InsightType`
    in the `InsightSelectors` statement is not valid. Valid values for `InsightType` are
    `ApiCallRateInsight` and `ApiErrorRateInsight`. To enable Insights on an event data
    store, the destination event data store specified by the `InsightsDestination`
    parameter must log Insights events and the source event data store specified by the
    `EventDataStore` parameter must log management events.

    For `UpdateEventDataStore`, this exception is thrown if Insights are enabled on the
    event data store and the updated advanced event selectors are not compatible with
    the configured `InsightSelectors`. If the `InsightSelectors` includes an
    `InsightType` of `ApiCallRateInsight`, the source event data store must log `write`
    management events. If the `InsightSelectors` includes an `InsightType` of
    `ApiErrorRateInsight`, the source event data store must log management events.
    """

    _ERROR_CODE = "InvalidInsightSelectorsException"


class InvalidKmsKeyIdException(CloudTrailError):
    """This exception is thrown when the KMS key ARN is not valid."""
    _ERROR_CODE = "InvalidKmsKeyIdException"


class InvalidLookupAttributesException(CloudTrailError):
    """Occurs when a lookup attribute is specified that is not valid."""
    _ERROR_CODE = "InvalidLookupAttributesException"


class InvalidMaxResultsException(CloudTrailError):
    """This exception is thrown if the limit specified is not valid."""
    _ERROR_CODE = "InvalidMaxResultsException"


class InvalidNextTokenException(CloudTrailError):
    """A token that is not valid, or a token that was previously used in a request with
    different parameters. This exception is thrown if the token is not valid.
    """

    _ERROR_CODE = "InvalidNextTokenException"


class InvalidParameterCombinationException(CloudTrailError):
    """This exception is thrown when the combination of parameters provided is not valid."""
    _ERROR_CODE = "InvalidParameterCombinationException"


class InvalidParameterException(CloudTrailError):
    """The request includes a parameter that is not valid."""
    _ERROR_CODE = "InvalidParameterException"


class InvalidQueryStatementException(CloudTrailError):
    """The query that was submitted has validation errors, or uses incorrect syntax or
    unsupported keywords. For more information about writing a query, see Create or edit
    a query in the CloudTrail User Guide.
    """

    _ERROR_CODE = "InvalidQueryStatementException"


class InvalidQueryStatusException(CloudTrailError):
    """The query status is not valid for the operation."""
    _ERROR_CODE = "InvalidQueryStatusException"


class InvalidS3BucketNameException(CloudTrailError):
    """This exception is thrown when the provided S3 bucket name is not valid."""
    _ERROR_CODE = "InvalidS3BucketNameException"


class InvalidS3PrefixException(CloudTrailError):
    """This exception is thrown when the provided S3 prefix is not valid."""
    _ERROR_CODE = "InvalidS3PrefixException"


class InvalidSnsTopicNameException(CloudTrailError):
    """This exception is thrown when the provided SNS topic name is not valid."""
    _ERROR_CODE = "InvalidSnsTopicNameException"


class InvalidSourceException(CloudTrailError):
    """This exception is thrown when the specified value of `Source` is not valid."""
    _ERROR_CODE = "InvalidSourceException"


class InvalidTagParameterException(CloudTrailError):
    """This exception is thrown when the specified tag key or values are not valid. It can
    also occur if there are duplicate tags or too many tags on the resource.
    """

    _ERROR_CODE = "InvalidTagParameterException"


class InvalidTimeRangeException(CloudTrailError):
    """Occurs if the timestamp values are not valid. Either the start time occurs after the
    end time, or the time range is outside the range of possible values.
    """

    _ERROR_CODE = "InvalidTimeRangeException"


class InvalidTokenException(CloudTrailError):
    """Reserved for future use."""
    _ERROR_CODE = "InvalidTokenException"


class InvalidTrailNameException(CloudTrailError):
    """This exception is thrown when the provided trail name is not valid. Trail names must
    meet the following requirements:

    - Contain only ASCII letters (a-z, A-Z), numbers (0-9), periods (.), underscores
      (_), or dashes (-)
    - Start with a letter or number, and end with a letter or number
    - Be between 3 and 128 characters
    - Have no adjacent periods, underscores or dashes. Names like `my-_namespace` and
      `my--namespace` are not valid.
    - Not be in IP address format (for example, 192.168.5.4)
    """

    _ERROR_CODE = "InvalidTrailNameException"


class KmsException(CloudTrailError):
    """This exception is thrown when there is an issue with the specified KMS key and the
    trail or event data store can't be updated.
    """

    _ERROR_CODE = "KmsException"


class KmsKeyDisabledException(CloudTrailError):
    """This exception is no longer in use."""
    _ERROR_CODE = "KmsKeyDisabledException"


class KmsKeyNotFoundException(CloudTrailError):
    """This exception is thrown when the KMS key does not exist, when the S3 bucket and the
    KMS key are not in the same Region, or when the KMS key associated with the Amazon
    SNS topic either does not exist or is not in the same Region.
    """

    _ERROR_CODE = "KmsKeyNotFoundException"


class MaxConcurrentQueriesException(CloudTrailError):
    """You are already running the maximum number of concurrent queries. The maximum number
    of concurrent queries is 10. Wait a minute for some queries to finish, and then run
    the query again.
    """

    _ERROR_CODE = "MaxConcurrentQueriesException"


class MaximumNumberOfTrailsExceededException(CloudTrailError):
    """This exception is thrown when the maximum number of trails is reached."""
    _ERROR_CODE = "MaximumNumberOfTrailsExceededException"


class NoManagementAccountSLRExistsException(CloudTrailError):
    """This exception is thrown when the management account does not have a service-linked
    role.
    """

    _ERROR_CODE = "NoManagementAccountSLRExistsException"


class NotOrganizationManagementAccountException(CloudTrailError):
    """This exception is thrown when the account making the request is not the
    organization's management account.
    """

    _ERROR_CODE = "NotOrganizationManagementAccountException"


class NotOrganizationMasterAccountException(CloudTrailError):
    """This exception is thrown when the Amazon Web Services account making the request to
    create or update an organization trail or event data store is not the management
    account for an organization in Organizations. For more information, see Prepare For
    Creating a Trail For Your Organization or Organization event data stores.
    """

    _ERROR_CODE = "NotOrganizationMasterAccountException"


class OperationNotPermittedException(CloudTrailError):
    """This exception is thrown when the requested operation is not permitted."""
    _ERROR_CODE = "OperationNotPermittedException"


class OrganizationNotInAllFeaturesModeException(CloudTrailError):
    """This exception is thrown when Organizations is not configured to support all
    features. All features must be enabled in Organizations to support creating an
    organization trail or event data store.
    """

    _ERROR_CODE = "OrganizationNotInAllFeaturesModeException"


class OrganizationsNotInUseException(CloudTrailError):
    """This exception is thrown when the request is made from an Amazon Web Services
    account that is not a member of an organization. To make this request, sign in using
    the credentials of an account that belongs to an organization.
    """

    _ERROR_CODE = "OrganizationsNotInUseException"


class QueryIdNotFoundException(CloudTrailError):
    """The query ID does not exist or does not map to a query."""
    _ERROR_CODE = "QueryIdNotFoundException"


class ResourceARNNotValidException(CloudTrailError):
    """This exception is thrown when the provided resource does not exist, or the ARN
    format of the resource is not valid.

    The following is the format of an event data store ARN: `arn:aws:cloudtrail:us-
    east-2:123456789012:eventdatastore/EXAMPLE-f852-4e8f-8bd1-bcf6cEXAMPLE`

    The following is the format of a dashboard ARN: `arn:aws:cloudtrail:us-
    east-1:123456789012:dashboard/exampleDash`

    The following is the format of a channel ARN: `arn:aws:cloudtrail:us-
    east-2:123456789012:channel/01234567890`
    """

    _ERROR_CODE = "ResourceARNNotValidException"


class ResourceNotFoundException(CloudTrailError):
    """This exception is thrown when the specified resource is not found."""
    _ERROR_CODE = "ResourceNotFoundException"


class ResourcePolicyNotFoundException(CloudTrailError):
    """This exception is thrown when the specified resource policy is not found."""
    _ERROR_CODE = "ResourcePolicyNotFoundException"


class ResourcePolicyNotValidException(CloudTrailError):
    """This exception is thrown when the resouce-based policy has syntax errors, or
    contains a principal that is not valid.
    """

    _ERROR_CODE = "ResourcePolicyNotValidException"


class ResourceTypeNotSupportedException(CloudTrailError):
    """This exception is thrown when the specified resource type is not supported by
    CloudTrail.
    """

    _ERROR_CODE = "ResourceTypeNotSupportedException"


class S3BucketDoesNotExistException(CloudTrailError):
    """This exception is thrown when the specified S3 bucket does not exist."""
    _ERROR_CODE = "S3BucketDoesNotExistException"


class ServiceQuotaExceededException(CloudTrailError):
    """This exception is thrown when the quota is exceeded. For information about
    CloudTrail quotas, see Service quotas in the Amazon Web Services General Reference.
    """

    _ERROR_CODE = "ServiceQuotaExceededException"


class TagsLimitExceededException(CloudTrailError):
    """The number of tags per trail, event data store, dashboard, or channel has exceeded
    the permitted amount. Currently, the limit is 50.
    """

    _ERROR_CODE = "TagsLimitExceededException"


class ThrottlingException(CloudTrailError):
    """This exception is thrown when the request rate exceeds the limit."""
    _ERROR_CODE = "ThrottlingException"


class TrailAlreadyExistsException(CloudTrailError):
    """This exception is thrown when the specified trail already exists."""
    _ERROR_CODE = "TrailAlreadyExistsException"


class TrailNotFoundException(CloudTrailError):
    """This exception is thrown when the trail with the given name is not found."""
    _ERROR_CODE = "TrailNotFoundException"


class TrailNotProvidedException(CloudTrailError):
    """This exception is no longer in use."""
    _ERROR_CODE = "TrailNotProvidedException"


class UnsupportedOperationException(CloudTrailError):
    """This exception is thrown when the requested operation is not supported."""
    _ERROR_CODE = "UnsupportedOperationException"


EXCEPTIONS: dict[str, type[CloudTrailError]] = {
    "AccessDeniedException": AccessDeniedException,
    "AccountHasOngoingImportException": AccountHasOngoingImportException,
    "AccountNotFoundException": AccountNotFoundException,
    "AccountNotRegisteredException": AccountNotRegisteredException,
    "AccountRegisteredException": AccountRegisteredException,
    "CannotDelegateManagementAccountException": CannotDelegateManagementAccountException,
    "ChannelARNInvalidException": ChannelARNInvalidException,
    "ChannelAlreadyExistsException": ChannelAlreadyExistsException,
    "ChannelExistsForEDSException": ChannelExistsForEDSException,
    "ChannelMaxLimitExceededException": ChannelMaxLimitExceededException,
    "ChannelNotFoundException": ChannelNotFoundException,
    "CloudTrailARNInvalidException": CloudTrailARNInvalidException,
    "CloudTrailAccessNotEnabledException": CloudTrailAccessNotEnabledException,
    "CloudTrailInvalidClientTokenIdException": CloudTrailInvalidClientTokenIdException,
    "CloudWatchLogsDeliveryUnavailableException": CloudWatchLogsDeliveryUnavailableException,
    "ConcurrentModificationException": ConcurrentModificationException,
    "ConflictException": ConflictException,
    "DelegatedAdminAccountLimitExceededException": DelegatedAdminAccountLimitExceededException,
    "EventDataStoreARNInvalidException": EventDataStoreARNInvalidException,
    "EventDataStoreAlreadyExistsException": EventDataStoreAlreadyExistsException,
    "EventDataStoreFederationEnabledException": EventDataStoreFederationEnabledException,
    "EventDataStoreHasOngoingImportException": EventDataStoreHasOngoingImportException,
    "EventDataStoreMaxLimitExceededException": EventDataStoreMaxLimitExceededException,
    "EventDataStoreNotFoundException": EventDataStoreNotFoundException,
    "EventDataStoreTerminationProtectedException": EventDataStoreTerminationProtectedException,
    "GenerateResponseException": GenerateResponseException,
    "ImportNotFoundException": ImportNotFoundException,
    "InactiveEventDataStoreException": InactiveEventDataStoreException,
    "InactiveQueryException": InactiveQueryException,
    "InsightNotEnabledException": InsightNotEnabledException,
    "InsufficientDependencyServiceAccessPermissionException": InsufficientDependencyServiceAccessPermissionException,
    "InsufficientEncryptionPolicyException": InsufficientEncryptionPolicyException,
    "InsufficientIAMAccessPermissionException": InsufficientIAMAccessPermissionException,
    "InsufficientS3BucketPolicyException": InsufficientS3BucketPolicyException,
    "InsufficientSnsTopicPolicyException": InsufficientSnsTopicPolicyException,
    "InvalidCloudWatchLogsLogGroupArnException": InvalidCloudWatchLogsLogGroupArnException,
    "InvalidCloudWatchLogsRoleArnException": InvalidCloudWatchLogsRoleArnException,
    "InvalidDateRangeException": InvalidDateRangeException,
    "InvalidEventCategoryException": InvalidEventCategoryException,
    "InvalidEventDataStoreCategoryException": InvalidEventDataStoreCategoryException,
    "InvalidEventDataStoreStatusException": InvalidEventDataStoreStatusException,
    "InvalidEventSelectorsException": InvalidEventSelectorsException,
    "InvalidHomeRegionException": InvalidHomeRegionException,
    "InvalidImportSourceException": InvalidImportSourceException,
    "InvalidInsightSelectorsException": InvalidInsightSelectorsException,
    "InvalidKmsKeyIdException": InvalidKmsKeyIdException,
    "InvalidLookupAttributesException": InvalidLookupAttributesException,
    "InvalidMaxResultsException": InvalidMaxResultsException,
    "InvalidNextTokenException": InvalidNextTokenException,
    "InvalidParameterCombinationException": InvalidParameterCombinationException,
    "InvalidParameterException": InvalidParameterException,
    "InvalidQueryStatementException": InvalidQueryStatementException,
    "InvalidQueryStatusException": InvalidQueryStatusException,
    "InvalidS3BucketNameException": InvalidS3BucketNameException,
    "InvalidS3PrefixException": InvalidS3PrefixException,
    "InvalidSnsTopicNameException": InvalidSnsTopicNameException,
    "InvalidSourceException": InvalidSourceException,
    "InvalidTagParameterException": InvalidTagParameterException,
    "InvalidTimeRangeException": InvalidTimeRangeException,
    "InvalidTokenException": InvalidTokenException,
    "InvalidTrailNameException": InvalidTrailNameException,
    "KmsException": KmsException,
    "KmsKeyDisabledException": KmsKeyDisabledException,
    "KmsKeyNotFoundException": KmsKeyNotFoundException,
    "MaxConcurrentQueriesException": MaxConcurrentQueriesException,
    "MaximumNumberOfTrailsExceededException": MaximumNumberOfTrailsExceededException,
    "NoManagementAccountSLRExistsException": NoManagementAccountSLRExistsException,
    "NotOrganizationManagementAccountException": NotOrganizationManagementAccountException,
    "NotOrganizationMasterAccountException": NotOrganizationMasterAccountException,
    "OperationNotPermittedException": OperationNotPermittedException,
    "OrganizationNotInAllFeaturesModeException": OrganizationNotInAllFeaturesModeException,
    "OrganizationsNotInUseException": OrganizationsNotInUseException,
    "QueryIdNotFoundException": QueryIdNotFoundException,
    "ResourceARNNotValidException": ResourceARNNotValidException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ResourcePolicyNotFoundException": ResourcePolicyNotFoundException,
    "ResourcePolicyNotValidException": ResourcePolicyNotValidException,
    "ResourceTypeNotSupportedException": ResourceTypeNotSupportedException,
    "S3BucketDoesNotExistException": S3BucketDoesNotExistException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "TagsLimitExceededException": TagsLimitExceededException,
    "ThrottlingException": ThrottlingException,
    "TrailAlreadyExistsException": TrailAlreadyExistsException,
    "TrailNotFoundException": TrailNotFoundException,
    "TrailNotProvidedException": TrailNotProvidedException,
    "UnsupportedOperationException": UnsupportedOperationException,
}
