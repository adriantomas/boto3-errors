# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class RedshiftError(Boto3Error):
    _SERVICE = "redshift"


class AccessToClusterDeniedFault(RedshiftError):
    """You are not authorized to access the cluster."""
    _ERROR_CODE = "AccessToClusterDenied"


class AccessToSnapshotDeniedFault(RedshiftError):
    """The owner of the specified snapshot has not authorized your account to access the
    snapshot.
    """

    _ERROR_CODE = "AccessToSnapshotDenied"


class AuthenticationProfileAlreadyExistsFault(RedshiftError):
    """The authentication profile already exists."""
    _ERROR_CODE = "AuthenticationProfileAlreadyExistsFault"


class AuthenticationProfileNotFoundFault(RedshiftError):
    """The authentication profile can't be found."""
    _ERROR_CODE = "AuthenticationProfileNotFoundFault"


class AuthenticationProfileQuotaExceededFault(RedshiftError):
    """The size or number of authentication profiles has exceeded the quota. The maximum
    length of the JSON string and maximum number of authentication profiles is
    determined by a quota for your account.
    """

    _ERROR_CODE = "AuthenticationProfileQuotaExceededFault"


class AuthorizationAlreadyExistsFault(RedshiftError):
    """The specified CIDR block or EC2 security group is already authorized for the
    specified cluster security group.
    """

    _ERROR_CODE = "AuthorizationAlreadyExists"


class AuthorizationNotFoundFault(RedshiftError):
    """The specified CIDR IP range or EC2 security group is not authorized for the
    specified cluster security group.
    """

    _ERROR_CODE = "AuthorizationNotFound"


class AuthorizationQuotaExceededFault(RedshiftError):
    """The authorization quota for the cluster security group has been reached."""
    _ERROR_CODE = "AuthorizationQuotaExceeded"


class BatchDeleteRequestSizeExceededFault(RedshiftError):
    """The maximum number for a batch delete of snapshots has been reached. The limit is
    100.
    """

    _ERROR_CODE = "BatchDeleteRequestSizeExceeded"


class BatchModifyClusterSnapshotsLimitExceededFault(RedshiftError):
    """The maximum number for snapshot identifiers has been reached. The limit is 100."""
    _ERROR_CODE = "BatchModifyClusterSnapshotsLimitExceededFault"


class BucketNotFoundFault(RedshiftError):
    """Could not find the specified S3 bucket."""
    _ERROR_CODE = "BucketNotFoundFault"


class ClusterAlreadyExistsFault(RedshiftError):
    """The account already has a cluster with the given identifier."""
    _ERROR_CODE = "ClusterAlreadyExists"


class ClusterNotFoundFault(RedshiftError):
    """The `ClusterIdentifier` parameter does not refer to an existing cluster."""
    _ERROR_CODE = "ClusterNotFound"


class ClusterOnLatestRevisionFault(RedshiftError):
    """Cluster is already on the latest database revision."""
    _ERROR_CODE = "ClusterOnLatestRevision"


class ClusterParameterGroupAlreadyExistsFault(RedshiftError):
    """A cluster parameter group with the same name already exists."""
    _ERROR_CODE = "ClusterParameterGroupAlreadyExists"


class ClusterParameterGroupNotFoundFault(RedshiftError):
    """The parameter group name does not refer to an existing parameter group."""
    _ERROR_CODE = "ClusterParameterGroupNotFound"


class ClusterParameterGroupQuotaExceededFault(RedshiftError):
    """The request would result in the user exceeding the allowed number of cluster
    parameter groups. For information about increasing your quota, go to Limits in
    Amazon Redshift in the Amazon Redshift Cluster Management Guide.
    """

    _ERROR_CODE = "ClusterParameterGroupQuotaExceeded"


class ClusterQuotaExceededFault(RedshiftError):
    """The request would exceed the allowed number of cluster instances for this account.
    For information about increasing your quota, go to Limits in Amazon Redshift in the
    Amazon Redshift Cluster Management Guide.
    """

    _ERROR_CODE = "ClusterQuotaExceeded"


class ClusterSecurityGroupAlreadyExistsFault(RedshiftError):
    """A cluster security group with the same name already exists."""
    _ERROR_CODE = "ClusterSecurityGroupAlreadyExists"


class ClusterSecurityGroupNotFoundFault(RedshiftError):
    """The cluster security group name does not refer to an existing cluster security
    group.
    """

    _ERROR_CODE = "ClusterSecurityGroupNotFound"


class ClusterSecurityGroupQuotaExceededFault(RedshiftError):
    """The request would result in the user exceeding the allowed number of cluster
    security groups. For information about increasing your quota, go to Limits in Amazon
    Redshift in the Amazon Redshift Cluster Management Guide.
    """

    _ERROR_CODE = "QuotaExceeded.ClusterSecurityGroup"


class ClusterSnapshotAlreadyExistsFault(RedshiftError):
    """The value specified as a snapshot identifier is already used by an existing
    snapshot.
    """

    _ERROR_CODE = "ClusterSnapshotAlreadyExists"


class ClusterSnapshotNotFoundFault(RedshiftError):
    """The snapshot identifier does not refer to an existing cluster snapshot."""
    _ERROR_CODE = "ClusterSnapshotNotFound"


class ClusterSnapshotQuotaExceededFault(RedshiftError):
    """The request would result in the user exceeding the allowed number of cluster
    snapshots.
    """

    _ERROR_CODE = "ClusterSnapshotQuotaExceeded"


class ClusterSubnetGroupAlreadyExistsFault(RedshiftError):
    """A ClusterSubnetGroupName is already used by an existing cluster subnet group."""
    _ERROR_CODE = "ClusterSubnetGroupAlreadyExists"


class ClusterSubnetGroupNotFoundFault(RedshiftError):
    """The cluster subnet group name does not refer to an existing cluster subnet group."""
    _ERROR_CODE = "ClusterSubnetGroupNotFoundFault"


class ClusterSubnetGroupQuotaExceededFault(RedshiftError):
    """The request would result in user exceeding the allowed number of cluster subnet
    groups. For information about increasing your quota, go to Limits in Amazon Redshift
    in the Amazon Redshift Cluster Management Guide.
    """

    _ERROR_CODE = "ClusterSubnetGroupQuotaExceeded"


class ClusterSubnetQuotaExceededFault(RedshiftError):
    """The request would result in user exceeding the allowed number of subnets in a
    cluster subnet groups. For information about increasing your quota, go to Limits in
    Amazon Redshift in the Amazon Redshift Cluster Management Guide.
    """

    _ERROR_CODE = "ClusterSubnetQuotaExceededFault"


class ConflictPolicyUpdateFault(RedshiftError):
    """There is a conflict while updating the resource policy."""
    _ERROR_CODE = "ConflictPolicyUpdateFault"


class CopyToRegionDisabledFault(RedshiftError):
    """Cross-region snapshot copy was temporarily disabled. Try your request again."""
    _ERROR_CODE = "CopyToRegionDisabledFault"


class CustomCnameAssociationFault(RedshiftError):
    """An error occurred when an attempt was made to change the custom domain association."""
    _ERROR_CODE = "CustomCnameAssociationFault"


class CustomDomainAssociationNotFoundFault(RedshiftError):
    """An error occurred. The custom domain name couldn't be found."""
    _ERROR_CODE = "CustomDomainAssociationNotFoundFault"


class DependentServiceAccessDeniedFault(RedshiftError):
    """A dependent service denied access for the integration."""
    _ERROR_CODE = "DependentServiceAccessDenied"


class DependentServiceRequestThrottlingFault(RedshiftError):
    """The request cannot be completed because a dependent service is throttling requests
    made by Amazon Redshift on your behalf. Wait and retry the request.
    """

    _ERROR_CODE = "DependentServiceRequestThrottlingFault"


class DependentServiceUnavailableFault(RedshiftError):
    """Your request cannot be completed because a dependent internal service is temporarily
    unavailable. Wait 30 to 60 seconds and try again.
    """

    _ERROR_CODE = "DependentServiceUnavailableFault"


class EndpointAlreadyExistsFault(RedshiftError):
    """The account already has a Redshift-managed VPC endpoint with the given identifier."""
    _ERROR_CODE = "EndpointAlreadyExists"


class EndpointAuthorizationAlreadyExistsFault(RedshiftError):
    """The authorization already exists for this endpoint."""
    _ERROR_CODE = "EndpointAuthorizationAlreadyExists"


class EndpointAuthorizationNotFoundFault(RedshiftError):
    """The authorization for this endpoint can't be found."""
    _ERROR_CODE = "EndpointAuthorizationNotFound"


class EndpointAuthorizationsPerClusterLimitExceededFault(RedshiftError):
    """The number of endpoint authorizations per cluster has exceeded its limit."""
    _ERROR_CODE = "EndpointAuthorizationsPerClusterLimitExceeded"


class EndpointNotFoundFault(RedshiftError):
    """The endpoint name doesn't refer to an existing endpoint."""
    _ERROR_CODE = "EndpointNotFound"


class EndpointsPerAuthorizationLimitExceededFault(RedshiftError):
    """The number of Redshift-managed VPC endpoints per authorization has exceeded its
    limit.
    """

    _ERROR_CODE = "EndpointsPerAuthorizationLimitExceeded"


class EndpointsPerClusterLimitExceededFault(RedshiftError):
    """The number of Redshift-managed VPC endpoints per cluster has exceeded its limit."""
    _ERROR_CODE = "EndpointsPerClusterLimitExceeded"


class EventSubscriptionQuotaExceededFault(RedshiftError):
    """The request would exceed the allowed number of event subscriptions for this account.
    For information about increasing your quota, go to Limits in Amazon Redshift in the
    Amazon Redshift Cluster Management Guide.
    """

    _ERROR_CODE = "EventSubscriptionQuotaExceeded"


class HsmClientCertificateAlreadyExistsFault(RedshiftError):
    """There is already an existing Amazon Redshift HSM client certificate with the
    specified identifier.
    """

    _ERROR_CODE = "HsmClientCertificateAlreadyExistsFault"


class HsmClientCertificateNotFoundFault(RedshiftError):
    """There is no Amazon Redshift HSM client certificate with the specified identifier."""
    _ERROR_CODE = "HsmClientCertificateNotFoundFault"


class HsmClientCertificateQuotaExceededFault(RedshiftError):
    """The quota for HSM client certificates has been reached. For information about
    increasing your quota, go to Limits in Amazon Redshift in the Amazon Redshift
    Cluster Management Guide.
    """

    _ERROR_CODE = "HsmClientCertificateQuotaExceededFault"


class HsmConfigurationAlreadyExistsFault(RedshiftError):
    """There is already an existing Amazon Redshift HSM configuration with the specified
    identifier.
    """

    _ERROR_CODE = "HsmConfigurationAlreadyExistsFault"


class HsmConfigurationNotFoundFault(RedshiftError):
    """There is no Amazon Redshift HSM configuration with the specified identifier."""
    _ERROR_CODE = "HsmConfigurationNotFoundFault"


class HsmConfigurationQuotaExceededFault(RedshiftError):
    """The quota for HSM configurations has been reached. For information about increasing
    your quota, go to Limits in Amazon Redshift in the Amazon Redshift Cluster
    Management Guide.
    """

    _ERROR_CODE = "HsmConfigurationQuotaExceededFault"


class InProgressTableRestoreQuotaExceededFault(RedshiftError):
    """You have exceeded the allowed number of table restore requests. Wait for your
    current table restore requests to complete before making a new request.
    """

    _ERROR_CODE = "InProgressTableRestoreQuotaExceededFault"


class IncompatibleOrderableOptions(RedshiftError):
    """The specified options are incompatible."""
    _ERROR_CODE = "IncompatibleOrderableOptions"


class InsufficientClusterCapacityFault(RedshiftError):
    """The number of nodes specified exceeds the allotted capacity of the cluster."""
    _ERROR_CODE = "InsufficientClusterCapacity"


class InsufficientS3BucketPolicyFault(RedshiftError):
    """The cluster does not have read bucket or put object permissions on the S3 bucket
    specified when enabling logging.
    """

    _ERROR_CODE = "InsufficientS3BucketPolicyFault"


class IntegrationAlreadyExistsFault(RedshiftError):
    """The integration you are trying to create already exists."""
    _ERROR_CODE = "IntegrationAlreadyExistsFault"


class IntegrationConflictOperationFault(RedshiftError):
    """A conflicting conditional operation is currently in progress against this resource.
    This typically occurs when there are multiple requests being made to the same
    resource at the same time, and these requests conflict with each other.
    """

    _ERROR_CODE = "IntegrationConflictOperationFault"


class IntegrationConflictStateFault(RedshiftError):
    """The integration is in an invalid state and can't perform the requested operation."""
    _ERROR_CODE = "IntegrationConflictStateFault"


class IntegrationNotFoundFault(RedshiftError):
    """The integration can't be found."""
    _ERROR_CODE = "IntegrationNotFoundFault"


class IntegrationQuotaExceededFault(RedshiftError):
    """You can't create any more zero-ETL or S3 event integrations because the quota has
    been reached.
    """

    _ERROR_CODE = "IntegrationQuotaExceededFault"


class IntegrationSourceNotFoundFault(RedshiftError):
    """The specified integration source can't be found."""
    _ERROR_CODE = "IntegrationSourceNotFoundFault"


class IntegrationTargetNotFoundFault(RedshiftError):
    """The specified integration target can't be found."""
    _ERROR_CODE = "IntegrationTargetNotFoundFault"


class InvalidAuthenticationProfileRequestFault(RedshiftError):
    """The authentication profile request is not valid. The profile name can't be null or
    empty. The authentication profile API operation must be available in the Amazon Web
    Services Region.
    """

    _ERROR_CODE = "InvalidAuthenticationProfileRequestFault"


class InvalidAuthorizationStateFault(RedshiftError):
    """The status of the authorization is not valid."""
    _ERROR_CODE = "InvalidAuthorizationState"


class InvalidClusterParameterGroupStateFault(RedshiftError):
    """The cluster parameter group action can not be completed because another task is in
    progress that involves the parameter group. Wait a few moments and try the operation
    again.
    """

    _ERROR_CODE = "InvalidClusterParameterGroupState"


class InvalidClusterSecurityGroupStateFault(RedshiftError):
    """The state of the cluster security group is not `available`."""
    _ERROR_CODE = "InvalidClusterSecurityGroupState"


class InvalidClusterSnapshotScheduleStateFault(RedshiftError):
    """The cluster snapshot schedule state is not valid."""
    _ERROR_CODE = "InvalidClusterSnapshotScheduleState"


class InvalidClusterSnapshotStateFault(RedshiftError):
    """The specified cluster snapshot is not in the `available` state, or other accounts
    are authorized to access the snapshot.
    """

    _ERROR_CODE = "InvalidClusterSnapshotState"


class InvalidClusterStateFault(RedshiftError):
    """The specified cluster is not in the `available` state."""
    _ERROR_CODE = "InvalidClusterState"


class InvalidClusterSubnetGroupStateFault(RedshiftError):
    """The cluster subnet group cannot be deleted because it is in use."""
    _ERROR_CODE = "InvalidClusterSubnetGroupStateFault"


class InvalidClusterSubnetStateFault(RedshiftError):
    """The state of the subnet is invalid."""
    _ERROR_CODE = "InvalidClusterSubnetStateFault"


class InvalidClusterTrackFault(RedshiftError):
    """The provided cluster track name is not valid."""
    _ERROR_CODE = "InvalidClusterTrack"


class InvalidDataShareFault(RedshiftError):
    """There is an error with the datashare."""
    _ERROR_CODE = "InvalidDataShareFault"


class InvalidElasticIpFault(RedshiftError):
    """The Elastic IP (EIP) is invalid or cannot be found."""
    _ERROR_CODE = "InvalidElasticIpFault"


class InvalidEndpointStateFault(RedshiftError):
    """The status of the endpoint is not valid."""
    _ERROR_CODE = "InvalidEndpointState"


class InvalidHsmClientCertificateStateFault(RedshiftError):
    """The specified HSM client certificate is not in the `available` state, or it is still
    in use by one or more Amazon Redshift clusters.
    """

    _ERROR_CODE = "InvalidHsmClientCertificateStateFault"


class InvalidHsmConfigurationStateFault(RedshiftError):
    """The specified HSM configuration is not in the `available` state, or it is still in
    use by one or more Amazon Redshift clusters.
    """

    _ERROR_CODE = "InvalidHsmConfigurationStateFault"


class InvalidNamespaceFault(RedshiftError):
    """The namespace isn't valid because the namespace doesn't exist. Provide a valid
    namespace.
    """

    _ERROR_CODE = "InvalidNamespaceFault"


class InvalidPolicyFault(RedshiftError):
    """The resource policy isn't valid."""
    _ERROR_CODE = "InvalidPolicyFault"


class InvalidReservedNodeStateFault(RedshiftError):
    """Indicates that the Reserved Node being exchanged is not in an active state."""
    _ERROR_CODE = "InvalidReservedNodeState"


class InvalidRestoreFault(RedshiftError):
    """The restore is invalid."""
    _ERROR_CODE = "InvalidRestore"


class InvalidRetentionPeriodFault(RedshiftError):
    """The retention period specified is either in the past or is not a valid value.

    The value must be either -1 or an integer between 1 and 3,653.
    """

    _ERROR_CODE = "InvalidRetentionPeriodFault"


class InvalidS3BucketNameFault(RedshiftError):
    """The S3 bucket name is invalid. For more information about naming rules, go to Bucket
    Restrictions and Limitations in the Amazon Simple Storage Service (S3) Developer
    Guide.
    """

    _ERROR_CODE = "InvalidS3BucketNameFault"


class InvalidS3KeyPrefixFault(RedshiftError):
    """The string specified for the logging S3 key prefix does not comply with the
    documented constraints.
    """

    _ERROR_CODE = "InvalidS3KeyPrefixFault"


class InvalidScheduleFault(RedshiftError):
    """The schedule you submitted isn't valid."""
    _ERROR_CODE = "InvalidSchedule"


class InvalidScheduledActionFault(RedshiftError):
    """The scheduled action is not valid."""
    _ERROR_CODE = "InvalidScheduledAction"


class InvalidSnapshotCopyGrantStateFault(RedshiftError):
    """The snapshot copy grant can't be deleted because it is used by one or more clusters."""
    _ERROR_CODE = "InvalidSnapshotCopyGrantStateFault"


class InvalidSubnet(RedshiftError):
    """The requested subnet is not valid, or not all of the subnets are in the same VPC."""
    _ERROR_CODE = "InvalidSubnet"


class InvalidSubscriptionStateFault(RedshiftError):
    """The subscription request is invalid because it is a duplicate request. This
    subscription request is already in progress.
    """

    _ERROR_CODE = "InvalidSubscriptionStateFault"


class InvalidTableRestoreArgumentFault(RedshiftError):
    """The value specified for the `sourceDatabaseName`, `sourceSchemaName`, or
    `sourceTableName` parameter, or a combination of these, doesn't exist in the
    snapshot.
    """

    _ERROR_CODE = "InvalidTableRestoreArgument"


class InvalidTagFault(RedshiftError):
    """The tag is invalid."""
    _ERROR_CODE = "InvalidTagFault"


class InvalidUsageLimitFault(RedshiftError):
    """The usage limit is not valid."""
    _ERROR_CODE = "InvalidUsageLimit"


class InvalidVPCNetworkStateFault(RedshiftError):
    """The cluster subnet group does not cover all Availability Zones."""
    _ERROR_CODE = "InvalidVPCNetworkStateFault"


class Ipv6CidrBlockNotFoundFault(RedshiftError):
    """There are no subnets in your VPC with associated IPv6 CIDR blocks. To use dual-stack
    mode, associate an IPv6 CIDR block with each subnet in your VPC.
    """

    _ERROR_CODE = "Ipv6CidrBlockNotFoundFault"


class LimitExceededFault(RedshiftError):
    """The encryption key has exceeded its grant limit in Amazon Web Services KMS."""
    _ERROR_CODE = "LimitExceededFault"


class NumberOfNodesPerClusterLimitExceededFault(RedshiftError):
    """The operation would exceed the number of nodes allowed for a cluster."""
    _ERROR_CODE = "NumberOfNodesPerClusterLimitExceeded"


class NumberOfNodesQuotaExceededFault(RedshiftError):
    """The operation would exceed the number of nodes allotted to the account. For
    information about increasing your quota, go to Limits in Amazon Redshift in the
    Amazon Redshift Cluster Management Guide.
    """

    _ERROR_CODE = "NumberOfNodesQuotaExceeded"


class PartnerNotFoundFault(RedshiftError):
    """The name of the partner was not found."""
    _ERROR_CODE = "PartnerNotFound"


class RedshiftIdcApplicationAlreadyExistsFault(RedshiftError):
    """The application you attempted to add already exists."""
    _ERROR_CODE = "RedshiftIdcApplicationAlreadyExists"


class RedshiftIdcApplicationNotExistsFault(RedshiftError):
    """The application you attempted to find doesn't exist."""
    _ERROR_CODE = "RedshiftIdcApplicationNotExists"


class RedshiftIdcApplicationQuotaExceededFault(RedshiftError):
    """The maximum number of Redshift IAM Identity Center applications was exceeded."""
    _ERROR_CODE = "RedshiftIdcApplicationQuotaExceeded"


class RedshiftInvalidParameterFault(RedshiftError):
    """The request contains one or more invalid parameters. This error occurs when required
    parameters are missing, parameter values are outside acceptable ranges, or parameter
    formats are incorrect.
    """

    _ERROR_CODE = "RedshiftInvalidParameter"


class ReservedNodeAlreadyExistsFault(RedshiftError):
    """User already has a reservation with the given identifier."""
    _ERROR_CODE = "ReservedNodeAlreadyExists"


class ReservedNodeAlreadyMigratedFault(RedshiftError):
    """Indicates that the reserved node has already been exchanged."""
    _ERROR_CODE = "ReservedNodeAlreadyMigrated"


class ReservedNodeExchangeNotFoundFault(RedshiftError):
    """The reserved-node exchange status wasn't found."""
    _ERROR_CODE = "ReservedNodeExchangeNotFond"


class ReservedNodeNotFoundFault(RedshiftError):
    """The specified reserved compute node not found."""
    _ERROR_CODE = "ReservedNodeNotFound"


class ReservedNodeOfferingNotFoundFault(RedshiftError):
    """Specified offering does not exist."""
    _ERROR_CODE = "ReservedNodeOfferingNotFound"


class ReservedNodeQuotaExceededFault(RedshiftError):
    """Request would exceed the user's compute node quota. For information about increasing
    your quota, go to Limits in Amazon Redshift in the Amazon Redshift Cluster
    Management Guide.
    """

    _ERROR_CODE = "ReservedNodeQuotaExceeded"


class ResizeNotFoundFault(RedshiftError):
    """A resize operation for the specified cluster is not found."""
    _ERROR_CODE = "ResizeNotFound"


class ResourceNotFoundFault(RedshiftError):
    """The resource could not be found."""
    _ERROR_CODE = "ResourceNotFoundFault"


class SNSInvalidTopicFault(RedshiftError):
    """Amazon SNS has responded that there is a problem with the specified Amazon SNS
    topic.
    """

    _ERROR_CODE = "SNSInvalidTopic"


class SNSNoAuthorizationFault(RedshiftError):
    """You do not have permission to publish to the specified Amazon SNS topic."""
    _ERROR_CODE = "SNSNoAuthorization"


class SNSTopicArnNotFoundFault(RedshiftError):
    """An Amazon SNS topic with the specified Amazon Resource Name (ARN) does not exist."""
    _ERROR_CODE = "SNSTopicArnNotFound"


class ScheduleDefinitionTypeUnsupportedFault(RedshiftError):
    """The definition you submitted is not supported."""
    _ERROR_CODE = "ScheduleDefinitionTypeUnsupported"


class ScheduledActionAlreadyExistsFault(RedshiftError):
    """The scheduled action already exists."""
    _ERROR_CODE = "ScheduledActionAlreadyExists"


class ScheduledActionNotFoundFault(RedshiftError):
    """The scheduled action cannot be found."""
    _ERROR_CODE = "ScheduledActionNotFound"


class ScheduledActionQuotaExceededFault(RedshiftError):
    """The quota for scheduled actions exceeded."""
    _ERROR_CODE = "ScheduledActionQuotaExceeded"


class ScheduledActionTypeUnsupportedFault(RedshiftError):
    """The action type specified for a scheduled action is not supported."""
    _ERROR_CODE = "ScheduledActionTypeUnsupported"


class SnapshotCopyAlreadyDisabledFault(RedshiftError):
    """The cluster already has cross-region snapshot copy disabled."""
    _ERROR_CODE = "SnapshotCopyAlreadyDisabledFault"


class SnapshotCopyAlreadyEnabledFault(RedshiftError):
    """The cluster already has cross-region snapshot copy enabled."""
    _ERROR_CODE = "SnapshotCopyAlreadyEnabledFault"


class SnapshotCopyDisabledFault(RedshiftError):
    """Cross-region snapshot copy was temporarily disabled. Try your request again."""
    _ERROR_CODE = "SnapshotCopyDisabledFault"


class SnapshotCopyGrantAlreadyExistsFault(RedshiftError):
    """The snapshot copy grant can't be created because a grant with the same name already
    exists.
    """

    _ERROR_CODE = "SnapshotCopyGrantAlreadyExistsFault"


class SnapshotCopyGrantNotFoundFault(RedshiftError):
    """The specified snapshot copy grant can't be found. Make sure that the name is typed
    correctly and that the grant exists in the destination region.
    """

    _ERROR_CODE = "SnapshotCopyGrantNotFoundFault"


class SnapshotCopyGrantQuotaExceededFault(RedshiftError):
    """The Amazon Web Services account has exceeded the maximum number of snapshot copy
    grants in this region.
    """

    _ERROR_CODE = "SnapshotCopyGrantQuotaExceededFault"


class SnapshotScheduleAlreadyExistsFault(RedshiftError):
    """The specified snapshot schedule already exists."""
    _ERROR_CODE = "SnapshotScheduleAlreadyExists"


class SnapshotScheduleNotFoundFault(RedshiftError):
    """We could not find the specified snapshot schedule."""
    _ERROR_CODE = "SnapshotScheduleNotFound"


class SnapshotScheduleQuotaExceededFault(RedshiftError):
    """You have exceeded the quota of snapshot schedules."""
    _ERROR_CODE = "SnapshotScheduleQuotaExceeded"


class SnapshotScheduleUpdateInProgressFault(RedshiftError):
    """The specified snapshot schedule is already being updated."""
    _ERROR_CODE = "SnapshotScheduleUpdateInProgress"


class SourceNotFoundFault(RedshiftError):
    """The specified Amazon Redshift event source could not be found."""
    _ERROR_CODE = "SourceNotFound"


class SubnetAlreadyInUse(RedshiftError):
    """A specified subnet is already in use by another cluster."""
    _ERROR_CODE = "SubnetAlreadyInUse"


class SubscriptionAlreadyExistFault(RedshiftError):
    """There is already an existing event notification subscription with the specified
    name.
    """

    _ERROR_CODE = "SubscriptionAlreadyExist"


class SubscriptionCategoryNotFoundFault(RedshiftError):
    """The value specified for the event category was not one of the allowed values, or it
    specified a category that does not apply to the specified source type. The allowed
    values are Configuration, Management, Monitoring, and Security.
    """

    _ERROR_CODE = "SubscriptionCategoryNotFound"


class SubscriptionEventIdNotFoundFault(RedshiftError):
    """An Amazon Redshift event with the specified event ID does not exist."""
    _ERROR_CODE = "SubscriptionEventIdNotFound"


class SubscriptionNotFoundFault(RedshiftError):
    """An Amazon Redshift event notification subscription with the specified name does not
    exist.
    """

    _ERROR_CODE = "SubscriptionNotFound"


class SubscriptionSeverityNotFoundFault(RedshiftError):
    """The value specified for the event severity was not one of the allowed values, or it
    specified a severity that does not apply to the specified source type. The allowed
    values are ERROR and INFO.
    """

    _ERROR_CODE = "SubscriptionSeverityNotFound"


class TableLimitExceededFault(RedshiftError):
    """The number of tables in the cluster exceeds the limit for the requested new cluster
    node type.
    """

    _ERROR_CODE = "TableLimitExceeded"


class TableRestoreNotFoundFault(RedshiftError):
    """The specified `TableRestoreRequestId` value was not found."""
    _ERROR_CODE = "TableRestoreNotFoundFault"


class TagLimitExceededFault(RedshiftError):
    """You have exceeded the number of tags allowed."""
    _ERROR_CODE = "TagLimitExceededFault"


class UnauthorizedOperation(RedshiftError):
    """Your account is not authorized to perform the requested operation."""
    _ERROR_CODE = "UnauthorizedOperation"


class UnauthorizedPartnerIntegrationFault(RedshiftError):
    """The partner integration is not authorized."""
    _ERROR_CODE = "UnauthorizedPartnerIntegration"


class UnknownSnapshotCopyRegionFault(RedshiftError):
    """The specified region is incorrect or does not exist."""
    _ERROR_CODE = "UnknownSnapshotCopyRegionFault"


class UnsupportedOperationFault(RedshiftError):
    """The requested operation isn't supported."""
    _ERROR_CODE = "UnsupportedOperation"


class UnsupportedOptionFault(RedshiftError):
    """A request option was specified that is not supported."""
    _ERROR_CODE = "UnsupportedOptionFault"


class UsageLimitAlreadyExistsFault(RedshiftError):
    """The usage limit already exists."""
    _ERROR_CODE = "UsageLimitAlreadyExists"


class UsageLimitNotFoundFault(RedshiftError):
    """The usage limit identifier can't be found."""
    _ERROR_CODE = "UsageLimitNotFound"


EXCEPTIONS: dict[str, type[RedshiftError]] = {
    "AccessToClusterDenied": AccessToClusterDeniedFault,
    "AccessToSnapshotDenied": AccessToSnapshotDeniedFault,
    "AuthenticationProfileAlreadyExistsFault": AuthenticationProfileAlreadyExistsFault,
    "AuthenticationProfileNotFoundFault": AuthenticationProfileNotFoundFault,
    "AuthenticationProfileQuotaExceededFault": AuthenticationProfileQuotaExceededFault,
    "AuthorizationAlreadyExists": AuthorizationAlreadyExistsFault,
    "AuthorizationNotFound": AuthorizationNotFoundFault,
    "AuthorizationQuotaExceeded": AuthorizationQuotaExceededFault,
    "BatchDeleteRequestSizeExceeded": BatchDeleteRequestSizeExceededFault,
    "BatchModifyClusterSnapshotsLimitExceededFault": BatchModifyClusterSnapshotsLimitExceededFault,
    "BucketNotFoundFault": BucketNotFoundFault,
    "ClusterAlreadyExists": ClusterAlreadyExistsFault,
    "ClusterNotFound": ClusterNotFoundFault,
    "ClusterOnLatestRevision": ClusterOnLatestRevisionFault,
    "ClusterParameterGroupAlreadyExists": ClusterParameterGroupAlreadyExistsFault,
    "ClusterParameterGroupNotFound": ClusterParameterGroupNotFoundFault,
    "ClusterParameterGroupQuotaExceeded": ClusterParameterGroupQuotaExceededFault,
    "ClusterQuotaExceeded": ClusterQuotaExceededFault,
    "ClusterSecurityGroupAlreadyExists": ClusterSecurityGroupAlreadyExistsFault,
    "ClusterSecurityGroupNotFound": ClusterSecurityGroupNotFoundFault,
    "QuotaExceeded.ClusterSecurityGroup": ClusterSecurityGroupQuotaExceededFault,
    "ClusterSnapshotAlreadyExists": ClusterSnapshotAlreadyExistsFault,
    "ClusterSnapshotNotFound": ClusterSnapshotNotFoundFault,
    "ClusterSnapshotQuotaExceeded": ClusterSnapshotQuotaExceededFault,
    "ClusterSubnetGroupAlreadyExists": ClusterSubnetGroupAlreadyExistsFault,
    "ClusterSubnetGroupNotFoundFault": ClusterSubnetGroupNotFoundFault,
    "ClusterSubnetGroupQuotaExceeded": ClusterSubnetGroupQuotaExceededFault,
    "ClusterSubnetQuotaExceededFault": ClusterSubnetQuotaExceededFault,
    "ConflictPolicyUpdateFault": ConflictPolicyUpdateFault,
    "CopyToRegionDisabledFault": CopyToRegionDisabledFault,
    "CustomCnameAssociationFault": CustomCnameAssociationFault,
    "CustomDomainAssociationNotFoundFault": CustomDomainAssociationNotFoundFault,
    "DependentServiceAccessDenied": DependentServiceAccessDeniedFault,
    "DependentServiceRequestThrottlingFault": DependentServiceRequestThrottlingFault,
    "DependentServiceUnavailableFault": DependentServiceUnavailableFault,
    "EndpointAlreadyExists": EndpointAlreadyExistsFault,
    "EndpointAuthorizationAlreadyExists": EndpointAuthorizationAlreadyExistsFault,
    "EndpointAuthorizationNotFound": EndpointAuthorizationNotFoundFault,
    "EndpointAuthorizationsPerClusterLimitExceeded": EndpointAuthorizationsPerClusterLimitExceededFault,
    "EndpointNotFound": EndpointNotFoundFault,
    "EndpointsPerAuthorizationLimitExceeded": EndpointsPerAuthorizationLimitExceededFault,
    "EndpointsPerClusterLimitExceeded": EndpointsPerClusterLimitExceededFault,
    "EventSubscriptionQuotaExceeded": EventSubscriptionQuotaExceededFault,
    "HsmClientCertificateAlreadyExistsFault": HsmClientCertificateAlreadyExistsFault,
    "HsmClientCertificateNotFoundFault": HsmClientCertificateNotFoundFault,
    "HsmClientCertificateQuotaExceededFault": HsmClientCertificateQuotaExceededFault,
    "HsmConfigurationAlreadyExistsFault": HsmConfigurationAlreadyExistsFault,
    "HsmConfigurationNotFoundFault": HsmConfigurationNotFoundFault,
    "HsmConfigurationQuotaExceededFault": HsmConfigurationQuotaExceededFault,
    "InProgressTableRestoreQuotaExceededFault": InProgressTableRestoreQuotaExceededFault,
    "IncompatibleOrderableOptions": IncompatibleOrderableOptions,
    "InsufficientClusterCapacity": InsufficientClusterCapacityFault,
    "InsufficientS3BucketPolicyFault": InsufficientS3BucketPolicyFault,
    "IntegrationAlreadyExistsFault": IntegrationAlreadyExistsFault,
    "IntegrationConflictOperationFault": IntegrationConflictOperationFault,
    "IntegrationConflictStateFault": IntegrationConflictStateFault,
    "IntegrationNotFoundFault": IntegrationNotFoundFault,
    "IntegrationQuotaExceededFault": IntegrationQuotaExceededFault,
    "IntegrationSourceNotFoundFault": IntegrationSourceNotFoundFault,
    "IntegrationTargetNotFoundFault": IntegrationTargetNotFoundFault,
    "InvalidAuthenticationProfileRequestFault": InvalidAuthenticationProfileRequestFault,
    "InvalidAuthorizationState": InvalidAuthorizationStateFault,
    "InvalidClusterParameterGroupState": InvalidClusterParameterGroupStateFault,
    "InvalidClusterSecurityGroupState": InvalidClusterSecurityGroupStateFault,
    "InvalidClusterSnapshotScheduleState": InvalidClusterSnapshotScheduleStateFault,
    "InvalidClusterSnapshotState": InvalidClusterSnapshotStateFault,
    "InvalidClusterState": InvalidClusterStateFault,
    "InvalidClusterSubnetGroupStateFault": InvalidClusterSubnetGroupStateFault,
    "InvalidClusterSubnetStateFault": InvalidClusterSubnetStateFault,
    "InvalidClusterTrack": InvalidClusterTrackFault,
    "InvalidDataShareFault": InvalidDataShareFault,
    "InvalidElasticIpFault": InvalidElasticIpFault,
    "InvalidEndpointState": InvalidEndpointStateFault,
    "InvalidHsmClientCertificateStateFault": InvalidHsmClientCertificateStateFault,
    "InvalidHsmConfigurationStateFault": InvalidHsmConfigurationStateFault,
    "InvalidNamespaceFault": InvalidNamespaceFault,
    "InvalidPolicyFault": InvalidPolicyFault,
    "InvalidReservedNodeState": InvalidReservedNodeStateFault,
    "InvalidRestore": InvalidRestoreFault,
    "InvalidRetentionPeriodFault": InvalidRetentionPeriodFault,
    "InvalidS3BucketNameFault": InvalidS3BucketNameFault,
    "InvalidS3KeyPrefixFault": InvalidS3KeyPrefixFault,
    "InvalidSchedule": InvalidScheduleFault,
    "InvalidScheduledAction": InvalidScheduledActionFault,
    "InvalidSnapshotCopyGrantStateFault": InvalidSnapshotCopyGrantStateFault,
    "InvalidSubnet": InvalidSubnet,
    "InvalidSubscriptionStateFault": InvalidSubscriptionStateFault,
    "InvalidTableRestoreArgument": InvalidTableRestoreArgumentFault,
    "InvalidTagFault": InvalidTagFault,
    "InvalidUsageLimit": InvalidUsageLimitFault,
    "InvalidVPCNetworkStateFault": InvalidVPCNetworkStateFault,
    "Ipv6CidrBlockNotFoundFault": Ipv6CidrBlockNotFoundFault,
    "LimitExceededFault": LimitExceededFault,
    "NumberOfNodesPerClusterLimitExceeded": NumberOfNodesPerClusterLimitExceededFault,
    "NumberOfNodesQuotaExceeded": NumberOfNodesQuotaExceededFault,
    "PartnerNotFound": PartnerNotFoundFault,
    "RedshiftIdcApplicationAlreadyExists": RedshiftIdcApplicationAlreadyExistsFault,
    "RedshiftIdcApplicationNotExists": RedshiftIdcApplicationNotExistsFault,
    "RedshiftIdcApplicationQuotaExceeded": RedshiftIdcApplicationQuotaExceededFault,
    "RedshiftInvalidParameter": RedshiftInvalidParameterFault,
    "ReservedNodeAlreadyExists": ReservedNodeAlreadyExistsFault,
    "ReservedNodeAlreadyMigrated": ReservedNodeAlreadyMigratedFault,
    "ReservedNodeExchangeNotFond": ReservedNodeExchangeNotFoundFault,
    "ReservedNodeNotFound": ReservedNodeNotFoundFault,
    "ReservedNodeOfferingNotFound": ReservedNodeOfferingNotFoundFault,
    "ReservedNodeQuotaExceeded": ReservedNodeQuotaExceededFault,
    "ResizeNotFound": ResizeNotFoundFault,
    "ResourceNotFoundFault": ResourceNotFoundFault,
    "SNSInvalidTopic": SNSInvalidTopicFault,
    "SNSNoAuthorization": SNSNoAuthorizationFault,
    "SNSTopicArnNotFound": SNSTopicArnNotFoundFault,
    "ScheduleDefinitionTypeUnsupported": ScheduleDefinitionTypeUnsupportedFault,
    "ScheduledActionAlreadyExists": ScheduledActionAlreadyExistsFault,
    "ScheduledActionNotFound": ScheduledActionNotFoundFault,
    "ScheduledActionQuotaExceeded": ScheduledActionQuotaExceededFault,
    "ScheduledActionTypeUnsupported": ScheduledActionTypeUnsupportedFault,
    "SnapshotCopyAlreadyDisabledFault": SnapshotCopyAlreadyDisabledFault,
    "SnapshotCopyAlreadyEnabledFault": SnapshotCopyAlreadyEnabledFault,
    "SnapshotCopyDisabledFault": SnapshotCopyDisabledFault,
    "SnapshotCopyGrantAlreadyExistsFault": SnapshotCopyGrantAlreadyExistsFault,
    "SnapshotCopyGrantNotFoundFault": SnapshotCopyGrantNotFoundFault,
    "SnapshotCopyGrantQuotaExceededFault": SnapshotCopyGrantQuotaExceededFault,
    "SnapshotScheduleAlreadyExists": SnapshotScheduleAlreadyExistsFault,
    "SnapshotScheduleNotFound": SnapshotScheduleNotFoundFault,
    "SnapshotScheduleQuotaExceeded": SnapshotScheduleQuotaExceededFault,
    "SnapshotScheduleUpdateInProgress": SnapshotScheduleUpdateInProgressFault,
    "SourceNotFound": SourceNotFoundFault,
    "SubnetAlreadyInUse": SubnetAlreadyInUse,
    "SubscriptionAlreadyExist": SubscriptionAlreadyExistFault,
    "SubscriptionCategoryNotFound": SubscriptionCategoryNotFoundFault,
    "SubscriptionEventIdNotFound": SubscriptionEventIdNotFoundFault,
    "SubscriptionNotFound": SubscriptionNotFoundFault,
    "SubscriptionSeverityNotFound": SubscriptionSeverityNotFoundFault,
    "TableLimitExceeded": TableLimitExceededFault,
    "TableRestoreNotFoundFault": TableRestoreNotFoundFault,
    "TagLimitExceededFault": TagLimitExceededFault,
    "UnauthorizedOperation": UnauthorizedOperation,
    "UnauthorizedPartnerIntegration": UnauthorizedPartnerIntegrationFault,
    "UnknownSnapshotCopyRegionFault": UnknownSnapshotCopyRegionFault,
    "UnsupportedOperation": UnsupportedOperationFault,
    "UnsupportedOptionFault": UnsupportedOptionFault,
    "UsageLimitAlreadyExists": UsageLimitAlreadyExistsFault,
    "UsageLimitNotFound": UsageLimitNotFoundFault,
}
