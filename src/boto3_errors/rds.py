# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class RDSError(Boto3Error):
    _SERVICE = "rds"


class AuthorizationAlreadyExistsFault(RDSError):
    """The specified CIDR IP range or Amazon EC2 security group is already authorized for
    the specified DB security group.
    """

    _ERROR_CODE = "AuthorizationAlreadyExists"


class AuthorizationNotFoundFault(RDSError):
    """The specified CIDR IP range or Amazon EC2 security group might not be authorized for
    the specified DB security group.

    Or, RDS might not be authorized to perform necessary actions using IAM on your
    behalf.
    """

    _ERROR_CODE = "AuthorizationNotFound"


class AuthorizationQuotaExceededFault(RDSError):
    """The DB security group authorization quota has been reached."""
    _ERROR_CODE = "AuthorizationQuotaExceeded"


class BackupPolicyNotFoundFault(RDSError):
    _ERROR_CODE = "BackupPolicyNotFoundFault"


class BlueGreenDeploymentAlreadyExistsFault(RDSError):
    """A blue/green deployment with the specified name already exists."""
    _ERROR_CODE = "BlueGreenDeploymentAlreadyExistsFault"


class BlueGreenDeploymentNotFoundFault(RDSError):
    """`BlueGreenDeploymentIdentifier` doesn't refer to an existing blue/green deployment."""
    _ERROR_CODE = "BlueGreenDeploymentNotFoundFault"


class CertificateNotFoundFault(RDSError):
    """`CertificateIdentifier` doesn't refer to an existing certificate."""
    _ERROR_CODE = "CertificateNotFound"


class CreateCustomDBEngineVersionFault(RDSError):
    """An error occurred while trying to create the CEV."""
    _ERROR_CODE = "CreateCustomDBEngineVersionFault"


class CustomAvailabilityZoneNotFoundFault(RDSError):
    """`CustomAvailabilityZoneId` doesn't refer to an existing custom Availability Zone
    identifier.
    """

    _ERROR_CODE = "CustomAvailabilityZoneNotFound"


class CustomDBEngineVersionAlreadyExistsFault(RDSError):
    """A CEV with the specified name already exists."""
    _ERROR_CODE = "CustomDBEngineVersionAlreadyExistsFault"


class CustomDBEngineVersionNotFoundFault(RDSError):
    """The specified CEV was not found."""
    _ERROR_CODE = "CustomDBEngineVersionNotFoundFault"


class CustomDBEngineVersionQuotaExceededFault(RDSError):
    """You have exceeded your CEV quota."""
    _ERROR_CODE = "CustomDBEngineVersionQuotaExceededFault"


class DBClusterAlreadyExistsFault(RDSError):
    """The user already has a DB cluster with the given identifier."""
    _ERROR_CODE = "DBClusterAlreadyExistsFault"


class DBClusterAutomatedBackupNotFoundFault(RDSError):
    """No automated backup for this DB cluster was found."""
    _ERROR_CODE = "DBClusterAutomatedBackupNotFoundFault"


class DBClusterAutomatedBackupQuotaExceededFault(RDSError):
    """The quota for retained automated backups was exceeded. This prevents you from
    retaining any additional automated backups. The retained automated backups quota is
    the same as your DB cluster quota.
    """

    _ERROR_CODE = "DBClusterAutomatedBackupQuotaExceededFault"


class DBClusterBacktrackNotFoundFault(RDSError):
    """`BacktrackIdentifier` doesn't refer to an existing backtrack."""
    _ERROR_CODE = "DBClusterBacktrackNotFoundFault"


class DBClusterEndpointAlreadyExistsFault(RDSError):
    """The specified custom endpoint can't be created because it already exists."""
    _ERROR_CODE = "DBClusterEndpointAlreadyExistsFault"


class DBClusterEndpointNotFoundFault(RDSError):
    """The specified custom endpoint doesn't exist."""
    _ERROR_CODE = "DBClusterEndpointNotFoundFault"


class DBClusterEndpointQuotaExceededFault(RDSError):
    """The cluster already has the maximum number of custom endpoints."""
    _ERROR_CODE = "DBClusterEndpointQuotaExceededFault"


class DBClusterNotFoundFault(RDSError):
    """`DBClusterIdentifier` doesn't refer to an existing DB cluster."""
    _ERROR_CODE = "DBClusterNotFoundFault"


class DBClusterParameterGroupNotFoundFault(RDSError):
    """`DBClusterParameterGroupName` doesn't refer to an existing DB cluster parameter
    group.
    """

    _ERROR_CODE = "DBClusterParameterGroupNotFound"


class DBClusterQuotaExceededFault(RDSError):
    """The user attempted to create a new DB cluster and the user has already reached the
    maximum allowed DB cluster quota.
    """

    _ERROR_CODE = "DBClusterQuotaExceededFault"


class DBClusterRoleAlreadyExistsFault(RDSError):
    """The specified IAM role Amazon Resource Name (ARN) is already associated with the
    specified DB cluster.
    """

    _ERROR_CODE = "DBClusterRoleAlreadyExists"


class DBClusterRoleNotFoundFault(RDSError):
    """The specified IAM role Amazon Resource Name (ARN) isn't associated with the
    specified DB cluster.
    """

    _ERROR_CODE = "DBClusterRoleNotFound"


class DBClusterRoleQuotaExceededFault(RDSError):
    """You have exceeded the maximum number of IAM roles that can be associated with the
    specified DB cluster.
    """

    _ERROR_CODE = "DBClusterRoleQuotaExceeded"


class DBClusterSnapshotAlreadyExistsFault(RDSError):
    """The user already has a DB cluster snapshot with the given identifier."""
    _ERROR_CODE = "DBClusterSnapshotAlreadyExistsFault"


class DBClusterSnapshotNotFoundFault(RDSError):
    """`DBClusterSnapshotIdentifier` doesn't refer to an existing DB cluster snapshot."""
    _ERROR_CODE = "DBClusterSnapshotNotFoundFault"


class DBInstanceAlreadyExistsFault(RDSError):
    """The user already has a DB instance with the given identifier."""
    _ERROR_CODE = "DBInstanceAlreadyExists"


class DBInstanceAutomatedBackupNotFoundFault(RDSError):
    """No automated backup for this DB instance was found."""
    _ERROR_CODE = "DBInstanceAutomatedBackupNotFound"


class DBInstanceAutomatedBackupQuotaExceededFault(RDSError):
    """The quota for retained automated backups was exceeded. This prevents you from
    retaining any additional automated backups. The retained automated backups quota is
    the same as your DB instance quota.
    """

    _ERROR_CODE = "DBInstanceAutomatedBackupQuotaExceeded"


class DBInstanceNotFoundFault(RDSError):
    """`DBInstanceIdentifier` doesn't refer to an existing DB instance."""
    _ERROR_CODE = "DBInstanceNotFound"


class DBInstanceNotReadyFault(RDSError):
    """An attempt to download or examine log files didn't succeed because an Aurora
    Serverless v2 instance was paused.
    """

    _ERROR_CODE = "DBInstanceNotReady"


class DBInstanceRoleAlreadyExistsFault(RDSError):
    """The specified `RoleArn` or `FeatureName` value is already associated with the DB
    instance.
    """

    _ERROR_CODE = "DBInstanceRoleAlreadyExists"


class DBInstanceRoleNotFoundFault(RDSError):
    """The specified `RoleArn` value doesn't match the specified feature for the DB
    instance.
    """

    _ERROR_CODE = "DBInstanceRoleNotFound"


class DBInstanceRoleQuotaExceededFault(RDSError):
    """You can't associate any more Amazon Web Services Identity and Access Management
    (IAM) roles with the DB instance because the quota has been reached.
    """

    _ERROR_CODE = "DBInstanceRoleQuotaExceeded"


class DBLogFileNotFoundFault(RDSError):
    """`LogFileName` doesn't refer to an existing DB log file."""
    _ERROR_CODE = "DBLogFileNotFoundFault"


class DBParameterGroupAlreadyExistsFault(RDSError):
    """A DB parameter group with the same name exists."""
    _ERROR_CODE = "DBParameterGroupAlreadyExists"


class DBParameterGroupNotFoundFault(RDSError):
    """`DBParameterGroupName` doesn't refer to an existing DB parameter group."""
    _ERROR_CODE = "DBParameterGroupNotFound"


class DBParameterGroupQuotaExceededFault(RDSError):
    """The request would result in the user exceeding the allowed number of DB parameter
    groups.
    """

    _ERROR_CODE = "DBParameterGroupQuotaExceeded"


class DBProxyAlreadyExistsFault(RDSError):
    """The specified proxy name must be unique for all proxies owned by your Amazon Web
    Services account in the specified Amazon Web Services Region.
    """

    _ERROR_CODE = "DBProxyAlreadyExistsFault"


class DBProxyEndpointAlreadyExistsFault(RDSError):
    """The specified DB proxy endpoint name must be unique for all DB proxy endpoints owned
    by your Amazon Web Services account in the specified Amazon Web Services Region.
    """

    _ERROR_CODE = "DBProxyEndpointAlreadyExistsFault"


class DBProxyEndpointNotFoundFault(RDSError):
    """The DB proxy endpoint doesn't exist."""
    _ERROR_CODE = "DBProxyEndpointNotFoundFault"


class DBProxyEndpointQuotaExceededFault(RDSError):
    """The DB proxy already has the maximum number of endpoints."""
    _ERROR_CODE = "DBProxyEndpointQuotaExceededFault"


class DBProxyNotFoundFault(RDSError):
    """The specified proxy name doesn't correspond to a proxy owned by your Amazon Web
    Services account in the specified Amazon Web Services Region.
    """

    _ERROR_CODE = "DBProxyNotFoundFault"


class DBProxyQuotaExceededFault(RDSError):
    """Your Amazon Web Services account already has the maximum number of proxies in the
    specified Amazon Web Services Region.
    """

    _ERROR_CODE = "DBProxyQuotaExceededFault"


class DBProxyTargetAlreadyRegisteredFault(RDSError):
    """The proxy is already associated with the specified RDS DB instance or Aurora DB
    cluster.
    """

    _ERROR_CODE = "DBProxyTargetAlreadyRegisteredFault"


class DBProxyTargetGroupNotFoundFault(RDSError):
    """The specified target group isn't available for a proxy owned by your Amazon Web
    Services account in the specified Amazon Web Services Region.
    """

    _ERROR_CODE = "DBProxyTargetGroupNotFoundFault"


class DBProxyTargetNotFoundFault(RDSError):
    """The specified RDS DB instance or Aurora DB cluster isn't available for a proxy owned
    by your Amazon Web Services account in the specified Amazon Web Services Region.
    """

    _ERROR_CODE = "DBProxyTargetNotFoundFault"


class DBSecurityGroupAlreadyExistsFault(RDSError):
    """A DB security group with the name specified in `DBSecurityGroupName` already exists."""
    _ERROR_CODE = "DBSecurityGroupAlreadyExists"


class DBSecurityGroupNotFoundFault(RDSError):
    """`DBSecurityGroupName` doesn't refer to an existing DB security group."""
    _ERROR_CODE = "DBSecurityGroupNotFound"


class DBSecurityGroupNotSupportedFault(RDSError):
    """A DB security group isn't allowed for this action."""
    _ERROR_CODE = "DBSecurityGroupNotSupported"


class DBSecurityGroupQuotaExceededFault(RDSError):
    """The request would result in the user exceeding the allowed number of DB security
    groups.
    """

    _ERROR_CODE = "QuotaExceeded.DBSecurityGroup"


class DBShardGroupAlreadyExistsFault(RDSError):
    """The specified DB shard group name must be unique in your Amazon Web Services account
    in the specified Amazon Web Services Region.
    """

    _ERROR_CODE = "DBShardGroupAlreadyExists"


class DBShardGroupNotFoundFault(RDSError):
    """The specified DB shard group name wasn't found."""
    _ERROR_CODE = "DBShardGroupNotFound"


class DBSnapshotAlreadyExistsFault(RDSError):
    """`DBSnapshotIdentifier` is already used by an existing snapshot."""
    _ERROR_CODE = "DBSnapshotAlreadyExists"


class DBSnapshotNotFoundFault(RDSError):
    """`DBSnapshotIdentifier` doesn't refer to an existing DB snapshot."""
    _ERROR_CODE = "DBSnapshotNotFound"


class DBSnapshotTenantDatabaseNotFoundFault(RDSError):
    """The specified snapshot tenant database wasn't found."""
    _ERROR_CODE = "DBSnapshotTenantDatabaseNotFoundFault"


class DBSubnetGroupAlreadyExistsFault(RDSError):
    """`DBSubnetGroupName` is already used by an existing DB subnet group."""
    _ERROR_CODE = "DBSubnetGroupAlreadyExists"


class DBSubnetGroupDoesNotCoverEnoughAZs(RDSError):
    """Subnets in the DB subnet group should cover at least two Availability Zones unless
    there is only one Availability Zone.
    """

    _ERROR_CODE = "DBSubnetGroupDoesNotCoverEnoughAZs"


class DBSubnetGroupNotAllowedFault(RDSError):
    """The DBSubnetGroup shouldn't be specified while creating read replicas that lie in
    the same region as the source instance.
    """

    _ERROR_CODE = "DBSubnetGroupNotAllowedFault"


class DBSubnetGroupNotFoundFault(RDSError):
    """`DBSubnetGroupName` doesn't refer to an existing DB subnet group."""
    _ERROR_CODE = "DBSubnetGroupNotFoundFault"


class DBSubnetGroupQuotaExceededFault(RDSError):
    """The request would result in the user exceeding the allowed number of DB subnet
    groups.
    """

    _ERROR_CODE = "DBSubnetGroupQuotaExceeded"


class DBSubnetQuotaExceededFault(RDSError):
    """The request would result in the user exceeding the allowed number of subnets in a DB
    subnet groups.
    """

    _ERROR_CODE = "DBSubnetQuotaExceededFault"


class DBUpgradeDependencyFailureFault(RDSError):
    """The DB upgrade failed because a resource the DB depends on can't be modified."""
    _ERROR_CODE = "DBUpgradeDependencyFailure"


class DomainNotFoundFault(RDSError):
    """`Domain` doesn't refer to an existing Active Directory domain."""
    _ERROR_CODE = "DomainNotFoundFault"


class Ec2ImagePropertiesNotSupportedFault(RDSError):
    """The AMI configuration prerequisite has not been met."""
    _ERROR_CODE = "Ec2ImagePropertiesNotSupportedFault"


class EventSubscriptionQuotaExceededFault(RDSError):
    """You have reached the maximum number of event subscriptions."""
    _ERROR_CODE = "EventSubscriptionQuotaExceeded"


class ExportTaskAlreadyExistsFault(RDSError):
    """You can't start an export task that's already running."""
    _ERROR_CODE = "ExportTaskAlreadyExists"


class ExportTaskNotFoundFault(RDSError):
    """The export task doesn't exist."""
    _ERROR_CODE = "ExportTaskNotFound"


class GlobalClusterAlreadyExistsFault(RDSError):
    """The `GlobalClusterIdentifier` already exists. Specify a new global database
    identifier (unique name) to create a new global database cluster or to rename an
    existing one.
    """

    _ERROR_CODE = "GlobalClusterAlreadyExistsFault"


class GlobalClusterNotFoundFault(RDSError):
    """The `GlobalClusterIdentifier` doesn't refer to an existing global database cluster."""
    _ERROR_CODE = "GlobalClusterNotFoundFault"


class GlobalClusterQuotaExceededFault(RDSError):
    """The number of global database clusters for this account is already at the maximum
    allowed.
    """

    _ERROR_CODE = "GlobalClusterQuotaExceededFault"


class IamRoleMissingPermissionsFault(RDSError):
    """The IAM role requires additional permissions to export to an Amazon S3 bucket."""
    _ERROR_CODE = "IamRoleMissingPermissions"


class IamRoleNotFoundFault(RDSError):
    """The IAM role is missing for exporting to an Amazon S3 bucket."""
    _ERROR_CODE = "IamRoleNotFound"


class InstanceQuotaExceededFault(RDSError):
    """The request would result in the user exceeding the allowed number of DB instances."""
    _ERROR_CODE = "InstanceQuotaExceeded"


class InsufficientAvailableIPsInSubnetFault(RDSError):
    """The requested operation can't be performed because there aren't enough available IP
    addresses in the proxy's subnets. Add more CIDR blocks to the VPC or remove IP
    address that aren't required from the subnets.
    """

    _ERROR_CODE = "InsufficientAvailableIPsInSubnetFault"


class InsufficientDBClusterCapacityFault(RDSError):
    """The DB cluster doesn't have enough capacity for the current operation."""
    _ERROR_CODE = "InsufficientDBClusterCapacityFault"


class InsufficientDBInstanceCapacityFault(RDSError):
    """The specified DB instance class isn't available in the specified Availability Zone."""
    _ERROR_CODE = "InsufficientDBInstanceCapacity"


class InsufficientStorageClusterCapacityFault(RDSError):
    """There is insufficient storage available for the current action. You might be able to
    resolve this error by updating your subnet group to use different Availability Zones
    that have more storage available.
    """

    _ERROR_CODE = "InsufficientStorageClusterCapacity"


class IntegrationAlreadyExistsFault(RDSError):
    """The integration you are trying to create already exists."""
    _ERROR_CODE = "IntegrationAlreadyExistsFault"


class IntegrationConflictOperationFault(RDSError):
    """A conflicting conditional operation is currently in progress against this resource.
    Typically occurs when there are multiple requests being made to the same resource at
    the same time, and these requests conflict with each other.
    """

    _ERROR_CODE = "IntegrationConflictOperationFault"


class IntegrationNotFoundFault(RDSError):
    """The specified integration could not be found."""
    _ERROR_CODE = "IntegrationNotFoundFault"


class IntegrationQuotaExceededFault(RDSError):
    """You can't crate any more zero-ETL integrations because the quota has been reached."""
    _ERROR_CODE = "IntegrationQuotaExceededFault"


class InvalidBlueGreenDeploymentStateFault(RDSError):
    """The blue/green deployment can't be switched over or deleted because there is an
    invalid configuration in the green environment.
    """

    _ERROR_CODE = "InvalidBlueGreenDeploymentStateFault"


class InvalidCustomDBEngineVersionStateFault(RDSError):
    """You can't delete the CEV."""
    _ERROR_CODE = "InvalidCustomDBEngineVersionStateFault"


class InvalidDBClusterAutomatedBackupStateFault(RDSError):
    """The automated backup is in an invalid state. For example, this automated backup is
    associated with an active cluster.
    """

    _ERROR_CODE = "InvalidDBClusterAutomatedBackupStateFault"


class InvalidDBClusterCapacityFault(RDSError):
    """`Capacity` isn't a valid Aurora Serverless DB cluster capacity. Valid capacity
    values are `2`, `4`, `8`, `16`, `32`, `64`, `128`, and `256`.
    """

    _ERROR_CODE = "InvalidDBClusterCapacityFault"


class InvalidDBClusterEndpointStateFault(RDSError):
    """The requested operation can't be performed on the endpoint while the endpoint is in
    this state.
    """

    _ERROR_CODE = "InvalidDBClusterEndpointStateFault"


class InvalidDBClusterSnapshotStateFault(RDSError):
    """The supplied value isn't a valid DB cluster snapshot state."""
    _ERROR_CODE = "InvalidDBClusterSnapshotStateFault"


class InvalidDBClusterStateFault(RDSError):
    """The requested operation can't be performed while the cluster is in this state."""
    _ERROR_CODE = "InvalidDBClusterStateFault"


class InvalidDBInstanceAutomatedBackupStateFault(RDSError):
    """The automated backup is in an invalid state. For example, this automated backup is
    associated with an active instance.
    """

    _ERROR_CODE = "InvalidDBInstanceAutomatedBackupState"


class InvalidDBInstanceStateFault(RDSError):
    """The DB instance isn't in a valid state."""
    _ERROR_CODE = "InvalidDBInstanceState"


class InvalidDBParameterGroupStateFault(RDSError):
    """The DB parameter group is in use or is in an invalid state. If you are attempting to
    delete the parameter group, you can't delete it when the parameter group is in this
    state.
    """

    _ERROR_CODE = "InvalidDBParameterGroupState"


class InvalidDBProxyEndpointStateFault(RDSError):
    """You can't perform this operation while the DB proxy endpoint is in a particular
    state.
    """

    _ERROR_CODE = "InvalidDBProxyEndpointStateFault"


class InvalidDBProxyStateFault(RDSError):
    """The requested operation can't be performed while the proxy is in this state."""
    _ERROR_CODE = "InvalidDBProxyStateFault"


class InvalidDBSecurityGroupStateFault(RDSError):
    """The state of the DB security group doesn't allow deletion."""
    _ERROR_CODE = "InvalidDBSecurityGroupState"


class InvalidDBShardGroupStateFault(RDSError):
    """The DB shard group must be in the available state."""
    _ERROR_CODE = "InvalidDBShardGroupState"


class InvalidDBSnapshotStateFault(RDSError):
    """The state of the DB snapshot doesn't allow deletion."""
    _ERROR_CODE = "InvalidDBSnapshotState"


class InvalidDBSubnetGroupFault(RDSError):
    """The DBSubnetGroup doesn't belong to the same VPC as that of an existing cross-region
    read replica of the same source instance.
    """

    _ERROR_CODE = "InvalidDBSubnetGroupFault"


class InvalidDBSubnetGroupStateFault(RDSError):
    """The DB subnet group cannot be deleted because it's in use."""
    _ERROR_CODE = "InvalidDBSubnetGroupStateFault"


class InvalidDBSubnetStateFault(RDSError):
    """The DB subnet isn't in the available state."""
    _ERROR_CODE = "InvalidDBSubnetStateFault"


class InvalidEventSubscriptionStateFault(RDSError):
    """This error can occur if someone else is modifying a subscription. You should retry
    the action.
    """

    _ERROR_CODE = "InvalidEventSubscriptionState"


class InvalidExportOnlyFault(RDSError):
    """The export is invalid for exporting to an Amazon S3 bucket."""
    _ERROR_CODE = "InvalidExportOnly"


class InvalidExportSourceStateFault(RDSError):
    """The state of the export snapshot is invalid for exporting to an Amazon S3 bucket."""
    _ERROR_CODE = "InvalidExportSourceState"


class InvalidExportTaskStateFault(RDSError):
    """You can't cancel an export task that has completed."""
    _ERROR_CODE = "InvalidExportTaskStateFault"


class InvalidGlobalClusterStateFault(RDSError):
    """The global cluster is in an invalid state and can't perform the requested operation."""
    _ERROR_CODE = "InvalidGlobalClusterStateFault"


class InvalidIntegrationStateFault(RDSError):
    """The integration is in an invalid state and can't perform the requested operation."""
    _ERROR_CODE = "InvalidIntegrationStateFault"


class InvalidOptionGroupStateFault(RDSError):
    """The option group isn't in the available state."""
    _ERROR_CODE = "InvalidOptionGroupStateFault"


class InvalidResourceStateFault(RDSError):
    """The operation can't be performed because another operation is in progress."""
    _ERROR_CODE = "InvalidResourceStateFault"


class InvalidRestoreFault(RDSError):
    """Cannot restore from VPC backup to non-VPC DB instance."""
    _ERROR_CODE = "InvalidRestoreFault"


class InvalidS3BucketFault(RDSError):
    """The specified Amazon S3 bucket name can't be found or Amazon RDS isn't authorized to
    access the specified Amazon S3 bucket. Verify the SourceS3BucketName and
    S3IngestionRoleArn values and try again.
    """

    _ERROR_CODE = "InvalidS3BucketFault"


class InvalidSubnet(RDSError):
    """The requested subnet is invalid, or multiple subnets were requested that are not all
    in a common VPC.
    """

    _ERROR_CODE = "InvalidSubnet"


class InvalidVPCNetworkStateFault(RDSError):
    """The DB subnet group doesn't cover all Availability Zones after it's created because
    of users' change.
    """

    _ERROR_CODE = "InvalidVPCNetworkStateFault"


class KMSKeyNotAccessibleFault(RDSError):
    """An error occurred accessing an Amazon Web Services KMS key."""
    _ERROR_CODE = "KMSKeyNotAccessibleFault"


class MaxDBShardGroupLimitReached(RDSError):
    """The maximum number of DB shard groups for your Amazon Web Services account in the
    specified Amazon Web Services Region has been reached.
    """

    _ERROR_CODE = "MaxDBShardGroupLimitReached"


class NetworkTypeNotSupported(RDSError):
    """The network type is invalid for the DB instance. Valid nework type values are `IPV4`
    and `DUAL`.
    """

    _ERROR_CODE = "NetworkTypeNotSupported"


class OptionGroupAlreadyExistsFault(RDSError):
    """The option group you are trying to create already exists."""
    _ERROR_CODE = "OptionGroupAlreadyExistsFault"


class OptionGroupNotFoundFault(RDSError):
    """The specified option group could not be found."""
    _ERROR_CODE = "OptionGroupNotFoundFault"


class OptionGroupQuotaExceededFault(RDSError):
    """The quota of 20 option groups was exceeded for this Amazon Web Services account."""
    _ERROR_CODE = "OptionGroupQuotaExceededFault"


class PointInTimeRestoreNotEnabledFault(RDSError):
    """`SourceDBInstanceIdentifier` refers to a DB instance with `BackupRetentionPeriod`
    equal to 0.
    """

    _ERROR_CODE = "PointInTimeRestoreNotEnabled"


class ProvisionedIopsNotAvailableInAZFault(RDSError):
    """Provisioned IOPS not available in the specified Availability Zone."""
    _ERROR_CODE = "ProvisionedIopsNotAvailableInAZFault"


class ReservedDBInstanceAlreadyExistsFault(RDSError):
    """User already has a reservation with the given identifier."""
    _ERROR_CODE = "ReservedDBInstanceAlreadyExists"


class ReservedDBInstanceNotFoundFault(RDSError):
    """The specified reserved DB Instance not found."""
    _ERROR_CODE = "ReservedDBInstanceNotFound"


class ReservedDBInstanceQuotaExceededFault(RDSError):
    """Request would exceed the user's DB Instance quota."""
    _ERROR_CODE = "ReservedDBInstanceQuotaExceeded"


class ReservedDBInstancesOfferingNotFoundFault(RDSError):
    """Specified offering does not exist."""
    _ERROR_CODE = "ReservedDBInstancesOfferingNotFound"


class ResourceNotFoundFault(RDSError):
    """The specified resource ID was not found."""
    _ERROR_CODE = "ResourceNotFoundFault"


class SNSInvalidTopicFault(RDSError):
    """SNS has responded that there is a problem with the SNS topic specified."""
    _ERROR_CODE = "SNSInvalidTopic"


class SNSNoAuthorizationFault(RDSError):
    """You do not have permission to publish to the SNS topic ARN."""
    _ERROR_CODE = "SNSNoAuthorization"


class SNSTopicArnNotFoundFault(RDSError):
    """The SNS topic ARN does not exist."""
    _ERROR_CODE = "SNSTopicArnNotFound"


class SharedSnapshotQuotaExceededFault(RDSError):
    """You have exceeded the maximum number of accounts that you can share a manual DB
    snapshot with.
    """

    _ERROR_CODE = "SharedSnapshotQuotaExceeded"


class SnapshotQuotaExceededFault(RDSError):
    """The request would result in the user exceeding the allowed number of DB snapshots."""
    _ERROR_CODE = "SnapshotQuotaExceeded"


class SourceClusterNotSupportedFault(RDSError):
    """The source DB cluster isn't supported for a blue/green deployment."""
    _ERROR_CODE = "SourceClusterNotSupportedFault"


class SourceDatabaseNotSupportedFault(RDSError):
    """The source DB instance isn't supported for a blue/green deployment."""
    _ERROR_CODE = "SourceDatabaseNotSupportedFault"


class SourceNotFoundFault(RDSError):
    """The requested source could not be found."""
    _ERROR_CODE = "SourceNotFound"


class StorageQuotaExceededFault(RDSError):
    """The request would result in the user exceeding the allowed amount of storage
    available across all DB instances.
    """

    _ERROR_CODE = "StorageQuotaExceeded"


class StorageTypeNotAvailableFault(RDSError):
    """The `aurora-iopt1` storage type isn't available, because you modified the DB cluster
    to use this storage type less than one month ago.
    """

    _ERROR_CODE = "StorageTypeNotAvailableFault"


class StorageTypeNotSupportedFault(RDSError):
    """The specified `StorageType` can't be associated with the DB instance."""
    _ERROR_CODE = "StorageTypeNotSupported"


class SubnetAlreadyInUse(RDSError):
    """The DB subnet is already in use in the Availability Zone."""
    _ERROR_CODE = "SubnetAlreadyInUse"


class SubscriptionAlreadyExistFault(RDSError):
    """The supplied subscription name already exists."""
    _ERROR_CODE = "SubscriptionAlreadyExist"


class SubscriptionCategoryNotFoundFault(RDSError):
    """The supplied category does not exist."""
    _ERROR_CODE = "SubscriptionCategoryNotFound"


class SubscriptionNotFoundFault(RDSError):
    """The subscription name does not exist."""
    _ERROR_CODE = "SubscriptionNotFound"


class TenantDatabaseAlreadyExistsFault(RDSError):
    """You attempted to either create a tenant database that already exists or modify a
    tenant database to use the name of an existing tenant database.
    """

    _ERROR_CODE = "TenantDatabaseAlreadyExists"


class TenantDatabaseNotFoundFault(RDSError):
    """The specified tenant database wasn't found in the DB instance."""
    _ERROR_CODE = "TenantDatabaseNotFound"


class TenantDatabaseQuotaExceededFault(RDSError):
    """You attempted to create more tenant databases than are permitted in your Amazon Web
    Services account.
    """

    _ERROR_CODE = "TenantDatabaseQuotaExceeded"


class UnsupportedDBEngineVersionFault(RDSError):
    """The specified DB engine version isn't supported for Aurora Limitless Database."""
    _ERROR_CODE = "UnsupportedDBEngineVersion"


class VpcEncryptionControlViolationException(RDSError):
    """The operation violates VPC encryption control settings. Make sure that your DB
    instance type supports the Nitro encryption-in-transit capability, or modify your
    VPC's encryption controls to not enforce encryption-in-transit.
    """

    _ERROR_CODE = "VpcEncryptionControlViolationException"


EXCEPTIONS: dict[str, type[RDSError]] = {
    "AuthorizationAlreadyExists": AuthorizationAlreadyExistsFault,
    "AuthorizationNotFound": AuthorizationNotFoundFault,
    "AuthorizationQuotaExceeded": AuthorizationQuotaExceededFault,
    "BackupPolicyNotFoundFault": BackupPolicyNotFoundFault,
    "BlueGreenDeploymentAlreadyExistsFault": BlueGreenDeploymentAlreadyExistsFault,
    "BlueGreenDeploymentNotFoundFault": BlueGreenDeploymentNotFoundFault,
    "CertificateNotFound": CertificateNotFoundFault,
    "CreateCustomDBEngineVersionFault": CreateCustomDBEngineVersionFault,
    "CustomAvailabilityZoneNotFound": CustomAvailabilityZoneNotFoundFault,
    "CustomDBEngineVersionAlreadyExistsFault": CustomDBEngineVersionAlreadyExistsFault,
    "CustomDBEngineVersionNotFoundFault": CustomDBEngineVersionNotFoundFault,
    "CustomDBEngineVersionQuotaExceededFault": CustomDBEngineVersionQuotaExceededFault,
    "DBClusterAlreadyExistsFault": DBClusterAlreadyExistsFault,
    "DBClusterAutomatedBackupNotFoundFault": DBClusterAutomatedBackupNotFoundFault,
    "DBClusterAutomatedBackupQuotaExceededFault": DBClusterAutomatedBackupQuotaExceededFault,
    "DBClusterBacktrackNotFoundFault": DBClusterBacktrackNotFoundFault,
    "DBClusterEndpointAlreadyExistsFault": DBClusterEndpointAlreadyExistsFault,
    "DBClusterEndpointNotFoundFault": DBClusterEndpointNotFoundFault,
    "DBClusterEndpointQuotaExceededFault": DBClusterEndpointQuotaExceededFault,
    "DBClusterNotFoundFault": DBClusterNotFoundFault,
    "DBClusterParameterGroupNotFound": DBClusterParameterGroupNotFoundFault,
    "DBClusterQuotaExceededFault": DBClusterQuotaExceededFault,
    "DBClusterRoleAlreadyExists": DBClusterRoleAlreadyExistsFault,
    "DBClusterRoleNotFound": DBClusterRoleNotFoundFault,
    "DBClusterRoleQuotaExceeded": DBClusterRoleQuotaExceededFault,
    "DBClusterSnapshotAlreadyExistsFault": DBClusterSnapshotAlreadyExistsFault,
    "DBClusterSnapshotNotFoundFault": DBClusterSnapshotNotFoundFault,
    "DBInstanceAlreadyExists": DBInstanceAlreadyExistsFault,
    "DBInstanceAutomatedBackupNotFound": DBInstanceAutomatedBackupNotFoundFault,
    "DBInstanceAutomatedBackupQuotaExceeded": DBInstanceAutomatedBackupQuotaExceededFault,
    "DBInstanceNotFound": DBInstanceNotFoundFault,
    "DBInstanceNotReady": DBInstanceNotReadyFault,
    "DBInstanceRoleAlreadyExists": DBInstanceRoleAlreadyExistsFault,
    "DBInstanceRoleNotFound": DBInstanceRoleNotFoundFault,
    "DBInstanceRoleQuotaExceeded": DBInstanceRoleQuotaExceededFault,
    "DBLogFileNotFoundFault": DBLogFileNotFoundFault,
    "DBParameterGroupAlreadyExists": DBParameterGroupAlreadyExistsFault,
    "DBParameterGroupNotFound": DBParameterGroupNotFoundFault,
    "DBParameterGroupQuotaExceeded": DBParameterGroupQuotaExceededFault,
    "DBProxyAlreadyExistsFault": DBProxyAlreadyExistsFault,
    "DBProxyEndpointAlreadyExistsFault": DBProxyEndpointAlreadyExistsFault,
    "DBProxyEndpointNotFoundFault": DBProxyEndpointNotFoundFault,
    "DBProxyEndpointQuotaExceededFault": DBProxyEndpointQuotaExceededFault,
    "DBProxyNotFoundFault": DBProxyNotFoundFault,
    "DBProxyQuotaExceededFault": DBProxyQuotaExceededFault,
    "DBProxyTargetAlreadyRegisteredFault": DBProxyTargetAlreadyRegisteredFault,
    "DBProxyTargetGroupNotFoundFault": DBProxyTargetGroupNotFoundFault,
    "DBProxyTargetNotFoundFault": DBProxyTargetNotFoundFault,
    "DBSecurityGroupAlreadyExists": DBSecurityGroupAlreadyExistsFault,
    "DBSecurityGroupNotFound": DBSecurityGroupNotFoundFault,
    "DBSecurityGroupNotSupported": DBSecurityGroupNotSupportedFault,
    "QuotaExceeded.DBSecurityGroup": DBSecurityGroupQuotaExceededFault,
    "DBShardGroupAlreadyExists": DBShardGroupAlreadyExistsFault,
    "DBShardGroupNotFound": DBShardGroupNotFoundFault,
    "DBSnapshotAlreadyExists": DBSnapshotAlreadyExistsFault,
    "DBSnapshotNotFound": DBSnapshotNotFoundFault,
    "DBSnapshotTenantDatabaseNotFoundFault": DBSnapshotTenantDatabaseNotFoundFault,
    "DBSubnetGroupAlreadyExists": DBSubnetGroupAlreadyExistsFault,
    "DBSubnetGroupDoesNotCoverEnoughAZs": DBSubnetGroupDoesNotCoverEnoughAZs,
    "DBSubnetGroupNotAllowedFault": DBSubnetGroupNotAllowedFault,
    "DBSubnetGroupNotFoundFault": DBSubnetGroupNotFoundFault,
    "DBSubnetGroupQuotaExceeded": DBSubnetGroupQuotaExceededFault,
    "DBSubnetQuotaExceededFault": DBSubnetQuotaExceededFault,
    "DBUpgradeDependencyFailure": DBUpgradeDependencyFailureFault,
    "DomainNotFoundFault": DomainNotFoundFault,
    "Ec2ImagePropertiesNotSupportedFault": Ec2ImagePropertiesNotSupportedFault,
    "EventSubscriptionQuotaExceeded": EventSubscriptionQuotaExceededFault,
    "ExportTaskAlreadyExists": ExportTaskAlreadyExistsFault,
    "ExportTaskNotFound": ExportTaskNotFoundFault,
    "GlobalClusterAlreadyExistsFault": GlobalClusterAlreadyExistsFault,
    "GlobalClusterNotFoundFault": GlobalClusterNotFoundFault,
    "GlobalClusterQuotaExceededFault": GlobalClusterQuotaExceededFault,
    "IamRoleMissingPermissions": IamRoleMissingPermissionsFault,
    "IamRoleNotFound": IamRoleNotFoundFault,
    "InstanceQuotaExceeded": InstanceQuotaExceededFault,
    "InsufficientAvailableIPsInSubnetFault": InsufficientAvailableIPsInSubnetFault,
    "InsufficientDBClusterCapacityFault": InsufficientDBClusterCapacityFault,
    "InsufficientDBInstanceCapacity": InsufficientDBInstanceCapacityFault,
    "InsufficientStorageClusterCapacity": InsufficientStorageClusterCapacityFault,
    "IntegrationAlreadyExistsFault": IntegrationAlreadyExistsFault,
    "IntegrationConflictOperationFault": IntegrationConflictOperationFault,
    "IntegrationNotFoundFault": IntegrationNotFoundFault,
    "IntegrationQuotaExceededFault": IntegrationQuotaExceededFault,
    "InvalidBlueGreenDeploymentStateFault": InvalidBlueGreenDeploymentStateFault,
    "InvalidCustomDBEngineVersionStateFault": InvalidCustomDBEngineVersionStateFault,
    "InvalidDBClusterAutomatedBackupStateFault": InvalidDBClusterAutomatedBackupStateFault,
    "InvalidDBClusterCapacityFault": InvalidDBClusterCapacityFault,
    "InvalidDBClusterEndpointStateFault": InvalidDBClusterEndpointStateFault,
    "InvalidDBClusterSnapshotStateFault": InvalidDBClusterSnapshotStateFault,
    "InvalidDBClusterStateFault": InvalidDBClusterStateFault,
    "InvalidDBInstanceAutomatedBackupState": InvalidDBInstanceAutomatedBackupStateFault,
    "InvalidDBInstanceState": InvalidDBInstanceStateFault,
    "InvalidDBParameterGroupState": InvalidDBParameterGroupStateFault,
    "InvalidDBProxyEndpointStateFault": InvalidDBProxyEndpointStateFault,
    "InvalidDBProxyStateFault": InvalidDBProxyStateFault,
    "InvalidDBSecurityGroupState": InvalidDBSecurityGroupStateFault,
    "InvalidDBShardGroupState": InvalidDBShardGroupStateFault,
    "InvalidDBSnapshotState": InvalidDBSnapshotStateFault,
    "InvalidDBSubnetGroupFault": InvalidDBSubnetGroupFault,
    "InvalidDBSubnetGroupStateFault": InvalidDBSubnetGroupStateFault,
    "InvalidDBSubnetStateFault": InvalidDBSubnetStateFault,
    "InvalidEventSubscriptionState": InvalidEventSubscriptionStateFault,
    "InvalidExportOnly": InvalidExportOnlyFault,
    "InvalidExportSourceState": InvalidExportSourceStateFault,
    "InvalidExportTaskStateFault": InvalidExportTaskStateFault,
    "InvalidGlobalClusterStateFault": InvalidGlobalClusterStateFault,
    "InvalidIntegrationStateFault": InvalidIntegrationStateFault,
    "InvalidOptionGroupStateFault": InvalidOptionGroupStateFault,
    "InvalidResourceStateFault": InvalidResourceStateFault,
    "InvalidRestoreFault": InvalidRestoreFault,
    "InvalidS3BucketFault": InvalidS3BucketFault,
    "InvalidSubnet": InvalidSubnet,
    "InvalidVPCNetworkStateFault": InvalidVPCNetworkStateFault,
    "KMSKeyNotAccessibleFault": KMSKeyNotAccessibleFault,
    "MaxDBShardGroupLimitReached": MaxDBShardGroupLimitReached,
    "NetworkTypeNotSupported": NetworkTypeNotSupported,
    "OptionGroupAlreadyExistsFault": OptionGroupAlreadyExistsFault,
    "OptionGroupNotFoundFault": OptionGroupNotFoundFault,
    "OptionGroupQuotaExceededFault": OptionGroupQuotaExceededFault,
    "PointInTimeRestoreNotEnabled": PointInTimeRestoreNotEnabledFault,
    "ProvisionedIopsNotAvailableInAZFault": ProvisionedIopsNotAvailableInAZFault,
    "ReservedDBInstanceAlreadyExists": ReservedDBInstanceAlreadyExistsFault,
    "ReservedDBInstanceNotFound": ReservedDBInstanceNotFoundFault,
    "ReservedDBInstanceQuotaExceeded": ReservedDBInstanceQuotaExceededFault,
    "ReservedDBInstancesOfferingNotFound": ReservedDBInstancesOfferingNotFoundFault,
    "ResourceNotFoundFault": ResourceNotFoundFault,
    "SNSInvalidTopic": SNSInvalidTopicFault,
    "SNSNoAuthorization": SNSNoAuthorizationFault,
    "SNSTopicArnNotFound": SNSTopicArnNotFoundFault,
    "SharedSnapshotQuotaExceeded": SharedSnapshotQuotaExceededFault,
    "SnapshotQuotaExceeded": SnapshotQuotaExceededFault,
    "SourceClusterNotSupportedFault": SourceClusterNotSupportedFault,
    "SourceDatabaseNotSupportedFault": SourceDatabaseNotSupportedFault,
    "SourceNotFound": SourceNotFoundFault,
    "StorageQuotaExceeded": StorageQuotaExceededFault,
    "StorageTypeNotAvailableFault": StorageTypeNotAvailableFault,
    "StorageTypeNotSupported": StorageTypeNotSupportedFault,
    "SubnetAlreadyInUse": SubnetAlreadyInUse,
    "SubscriptionAlreadyExist": SubscriptionAlreadyExistFault,
    "SubscriptionCategoryNotFound": SubscriptionCategoryNotFoundFault,
    "SubscriptionNotFound": SubscriptionNotFoundFault,
    "TenantDatabaseAlreadyExists": TenantDatabaseAlreadyExistsFault,
    "TenantDatabaseNotFound": TenantDatabaseNotFoundFault,
    "TenantDatabaseQuotaExceeded": TenantDatabaseQuotaExceededFault,
    "UnsupportedDBEngineVersion": UnsupportedDBEngineVersionFault,
    "VpcEncryptionControlViolationException": VpcEncryptionControlViolationException,
}
