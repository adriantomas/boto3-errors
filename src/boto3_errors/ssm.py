# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class SSMError(Boto3Error):
    _SERVICE = "ssm"


class AccessDeniedException(SSMError):
    """The requester doesn't have permissions to perform the requested operation."""
    _ERROR_CODE = "AccessDeniedException"


class AlreadyExistsException(SSMError):
    """Error returned if an attempt is made to register a patch group with a patch baseline
    that is already registered with a different patch baseline.
    """

    _ERROR_CODE = "AlreadyExistsException"


class AssociatedInstances(SSMError):
    """You must disassociate a document from all managed nodes before you can delete it."""
    _ERROR_CODE = "AssociatedInstances"


class AssociationAlreadyExists(SSMError):
    """The specified association already exists."""
    _ERROR_CODE = "AssociationAlreadyExists"


class AssociationDoesNotExist(SSMError):
    """The specified association doesn't exist."""
    _ERROR_CODE = "AssociationDoesNotExist"


class AssociationExecutionDoesNotExist(SSMError):
    """The specified execution ID doesn't exist. Verify the ID number and try again."""
    _ERROR_CODE = "AssociationExecutionDoesNotExist"


class AssociationLimitExceeded(SSMError):
    """You can have at most 2,000 active associations."""
    _ERROR_CODE = "AssociationLimitExceeded"


class AssociationVersionLimitExceeded(SSMError):
    """You have reached the maximum number versions allowed for an association. Each
    association has a limit of 1,000 versions.
    """

    _ERROR_CODE = "AssociationVersionLimitExceeded"


class AutomationDefinitionNotApprovedException(SSMError):
    """Indicates that the Change Manager change template used in the change request was
    rejected or is still in a pending state.
    """

    _ERROR_CODE = "AutomationDefinitionNotApprovedException"


class AutomationDefinitionNotFoundException(SSMError):
    """An Automation runbook with the specified name couldn't be found."""
    _ERROR_CODE = "AutomationDefinitionNotFoundException"


class AutomationDefinitionVersionNotFoundException(SSMError):
    """An Automation runbook with the specified name and version couldn't be found."""
    _ERROR_CODE = "AutomationDefinitionVersionNotFoundException"


class AutomationExecutionLimitExceededException(SSMError):
    """The number of simultaneously running Automation executions exceeded the allowable
    limit.
    """

    _ERROR_CODE = "AutomationExecutionLimitExceededException"


class AutomationExecutionNotFoundException(SSMError):
    """There is no automation execution information for the requested automation execution
    ID.
    """

    _ERROR_CODE = "AutomationExecutionNotFoundException"


class AutomationStepNotFoundException(SSMError):
    """The specified step name and execution ID don't exist. Verify the information and try
    again.
    """

    _ERROR_CODE = "AutomationStepNotFoundException"


class ComplianceTypeCountLimitExceededException(SSMError):
    """You specified too many custom compliance types. You can specify a maximum of 10
    different types.
    """

    _ERROR_CODE = "ComplianceTypeCountLimitExceededException"


class CustomSchemaCountLimitExceededException(SSMError):
    """You have exceeded the limit for custom schemas. Delete one or more custom schemas
    and try again.
    """

    _ERROR_CODE = "CustomSchemaCountLimitExceededException"


class DocumentAlreadyExists(SSMError):
    """The specified document already exists."""
    _ERROR_CODE = "DocumentAlreadyExists"


class DocumentLimitExceeded(SSMError):
    """You can have at most 500 active SSM documents."""
    _ERROR_CODE = "DocumentLimitExceeded"


class DocumentPermissionLimit(SSMError):
    """The document can't be shared with more Amazon Web Services accounts. You can specify
    a maximum of 20 accounts per API operation to share a private document.

    By default, you can share a private document with a maximum of 1,000 accounts and
    publicly share up to five documents.

    If you need to increase the quota for privately or publicly shared Systems Manager
    documents, contact Amazon Web Services Support.
    """

    _ERROR_CODE = "DocumentPermissionLimit"


class DocumentVersionLimitExceeded(SSMError):
    """The document has too many versions. Delete one or more document versions and try
    again.
    """

    _ERROR_CODE = "DocumentVersionLimitExceeded"


class DoesNotExistException(SSMError):
    """Error returned when the ID specified for a resource, such as a maintenance window or
    patch baseline, doesn't exist.

    For information about resource quotas in Amazon Web Services Systems Manager, see
    Systems Manager service quotas in the Amazon Web Services General Reference.
    """

    _ERROR_CODE = "DoesNotExistException"


class DuplicateDocumentContent(SSMError):
    """The content of the association document matches another document. Change the content
    of the document and try again.
    """

    _ERROR_CODE = "DuplicateDocumentContent"


class DuplicateDocumentVersionName(SSMError):
    """The version name has already been used in this document. Specify a different version
    name, and then try again.
    """

    _ERROR_CODE = "DuplicateDocumentVersionName"


class DuplicateInstanceId(SSMError):
    """You can't specify a managed node ID in more than one association."""
    _ERROR_CODE = "DuplicateInstanceId"


class FeatureNotAvailableException(SSMError):
    """You attempted to register a `LAMBDA` or `STEP_FUNCTIONS` task in a region where the
    corresponding service isn't available.
    """

    _ERROR_CODE = "FeatureNotAvailableException"


class HierarchyLevelLimitExceededException(SSMError):
    """A hierarchy can have a maximum of 15 levels. For more information, see Requirements
    and constraints for parameter names in the Amazon Web Services Systems Manager User
    Guide.
    """

    _ERROR_CODE = "HierarchyLevelLimitExceededException"


class HierarchyTypeMismatchException(SSMError):
    """Parameter Store doesn't support changing a parameter type in a hierarchy. For
    example, you can't change a parameter from a `String` type to a `SecureString` type.
    You must create a new, unique parameter.
    """

    _ERROR_CODE = "HierarchyTypeMismatchException"


class IdempotentParameterMismatch(SSMError):
    """Error returned when an idempotent operation is retried and the parameters don't
    match the original call to the API with the same idempotency token.
    """

    _ERROR_CODE = "IdempotentParameterMismatch"


class IncompatiblePolicyException(SSMError):
    """There is a conflict in the policies specified for this parameter. You can't, for
    example, specify two Expiration policies for a parameter. Review your policies, and
    try again.
    """

    _ERROR_CODE = "IncompatiblePolicyException"


class InternalServerError(SSMError):
    """An error occurred on the server side."""
    _ERROR_CODE = "InternalServerError"


class InvalidActivation(SSMError):
    """The activation isn't valid. The activation might have been deleted, or the
    ActivationId and the ActivationCode don't match.
    """

    _ERROR_CODE = "InvalidActivation"


class InvalidActivationId(SSMError):
    """The activation ID isn't valid. Verify that you entered the correct ActivationId or
    ActivationCode and try again.
    """

    _ERROR_CODE = "InvalidActivationId"


class InvalidAggregatorException(SSMError):
    """The specified aggregator isn't valid for the group type. Verify that the aggregator
    you provided is supported.
    """

    _ERROR_CODE = "InvalidAggregatorException"


class InvalidAllowedPatternException(SSMError):
    """The request doesn't meet the regular expression requirement."""
    _ERROR_CODE = "InvalidAllowedPatternException"


class InvalidAssociation(SSMError):
    """The association isn't valid or doesn't exist."""
    _ERROR_CODE = "InvalidAssociation"


class InvalidAssociationVersion(SSMError):
    """The version you specified isn't valid. Use ListAssociationVersions to view all
    versions of an association according to the association ID. Or, use the `$LATEST`
    parameter to view the latest version of the association.
    """

    _ERROR_CODE = "InvalidAssociationVersion"


class InvalidAutomationExecutionParametersException(SSMError):
    """The supplied parameters for invoking the specified Automation runbook are incorrect.
    For example, they may not match the set of parameters permitted for the specified
    Automation document.
    """

    _ERROR_CODE = "InvalidAutomationExecutionParametersException"


class InvalidAutomationSignalException(SSMError):
    """The signal isn't valid for the current Automation execution."""
    _ERROR_CODE = "InvalidAutomationSignalException"


class InvalidAutomationStatusUpdateException(SSMError):
    """The specified update status operation isn't valid."""
    _ERROR_CODE = "InvalidAutomationStatusUpdateException"


class InvalidCommandId(SSMError):
    """The specified command ID isn't valid. Verify the ID and try again."""
    _ERROR_CODE = "InvalidCommandId"


class InvalidDeleteInventoryParametersException(SSMError):
    """One or more of the parameters specified for the delete operation isn't valid. Verify
    all parameters and try again.
    """

    _ERROR_CODE = "InvalidDeleteInventoryParametersException"


class InvalidDeletionIdException(SSMError):
    """The ID specified for the delete operation doesn't exist or isn't valid. Verify the
    ID and try again.
    """

    _ERROR_CODE = "InvalidDeletionIdException"


class InvalidDocument(SSMError):
    """The specified SSM document doesn't exist."""
    _ERROR_CODE = "InvalidDocument"


class InvalidDocumentContent(SSMError):
    """The content for the document isn't valid."""
    _ERROR_CODE = "InvalidDocumentContent"


class InvalidDocumentOperation(SSMError):
    """You attempted to delete a document while it is still shared. You must stop sharing
    the document before you can delete it.
    """

    _ERROR_CODE = "InvalidDocumentOperation"


class InvalidDocumentSchemaVersion(SSMError):
    """The version of the document schema isn't supported."""
    _ERROR_CODE = "InvalidDocumentSchemaVersion"


class InvalidDocumentType(SSMError):
    """The SSM document type isn't valid. Valid document types are described in the
    `DocumentType` property.
    """

    _ERROR_CODE = "InvalidDocumentType"


class InvalidDocumentVersion(SSMError):
    """The document version isn't valid or doesn't exist."""
    _ERROR_CODE = "InvalidDocumentVersion"


class InvalidFilter(SSMError):
    """The filter name isn't valid. Verify that you entered the correct name and try again."""
    _ERROR_CODE = "InvalidFilter"


class InvalidFilterKey(SSMError):
    """The specified key isn't valid."""
    _ERROR_CODE = "InvalidFilterKey"


class InvalidFilterOption(SSMError):
    """The specified filter option isn't valid. Valid options are Equals and BeginsWith.
    For Path filter, valid options are Recursive and OneLevel.
    """

    _ERROR_CODE = "InvalidFilterOption"


class InvalidFilterValue(SSMError):
    """The filter value isn't valid. Verify the value and try again."""
    _ERROR_CODE = "InvalidFilterValue"


class InvalidInstanceId(SSMError):
    """The following problems can cause this exception:

    - You don't have permission to access the managed node.
    - Amazon Web Services Systems Manager Agent (SSM Agent) isn't running. Verify that
      SSM Agent is running.
    - SSM Agent isn't registered with the SSM endpoint. Try reinstalling SSM Agent.
    - The managed node isn't in a valid state. Valid states are: `Running`, `Pending`,
      `Stopped`, and `Stopping`. Invalid states are: `Shutting-down` and `Terminated`.
    """

    _ERROR_CODE = "InvalidInstanceId"


class InvalidInstanceInformationFilterValue(SSMError):
    """The specified filter value isn't valid."""
    _ERROR_CODE = "InvalidInstanceInformationFilterValue"


class InvalidInstancePropertyFilterValue(SSMError):
    """The specified filter value isn't valid."""
    _ERROR_CODE = "InvalidInstancePropertyFilterValue"


class InvalidInventoryGroupException(SSMError):
    """The specified inventory group isn't valid."""
    _ERROR_CODE = "InvalidInventoryGroupException"


class InvalidInventoryItemContextException(SSMError):
    """You specified invalid keys or values in the `Context` attribute for `InventoryItem`.
    Verify the keys and values, and try again.
    """

    _ERROR_CODE = "InvalidInventoryItemContextException"


class InvalidInventoryRequestException(SSMError):
    """The request isn't valid."""
    _ERROR_CODE = "InvalidInventoryRequestException"


class InvalidItemContentException(SSMError):
    """One or more content items isn't valid."""
    _ERROR_CODE = "InvalidItemContentException"

    @property
    def type_name(self) -> str | None:
        return self.response.get("TypeName")


class InvalidKeyId(SSMError):
    """The query key ID isn't valid."""
    _ERROR_CODE = "InvalidKeyId"


class InvalidNextToken(SSMError):
    """The specified token isn't valid."""
    _ERROR_CODE = "InvalidNextToken"


class InvalidNotificationConfig(SSMError):
    """One or more configuration items isn't valid. Verify that a valid Amazon Resource
    Name (ARN) was provided for an Amazon Simple Notification Service topic.
    """

    _ERROR_CODE = "InvalidNotificationConfig"


class InvalidOptionException(SSMError):
    """The delete inventory option specified isn't valid. Verify the option and try again."""
    _ERROR_CODE = "InvalidOptionException"


class InvalidOutputFolder(SSMError):
    """The S3 bucket doesn't exist."""
    _ERROR_CODE = "InvalidOutputFolder"


class InvalidOutputLocation(SSMError):
    """The output location isn't valid or doesn't exist."""
    _ERROR_CODE = "InvalidOutputLocation"


class InvalidParameters(SSMError):
    """You must specify values for all required parameters in the Amazon Web Services
    Systems Manager document (SSM document). You can only supply values to parameters
    defined in the SSM document.
    """

    _ERROR_CODE = "InvalidParameters"


class InvalidPermissionType(SSMError):
    """The permission type isn't supported. Share is the only supported permission type."""
    _ERROR_CODE = "InvalidPermissionType"


class InvalidPluginName(SSMError):
    """The plugin name isn't valid."""
    _ERROR_CODE = "InvalidPluginName"


class InvalidPolicyAttributeException(SSMError):
    """A policy attribute or its value is invalid."""
    _ERROR_CODE = "InvalidPolicyAttributeException"


class InvalidPolicyTypeException(SSMError):
    """The policy type isn't supported. Parameter Store supports the following policy
    types: Expiration, ExpirationNotification, and NoChangeNotification.
    """

    _ERROR_CODE = "InvalidPolicyTypeException"


class InvalidResourceId(SSMError):
    """The resource ID isn't valid. Verify that you entered the correct ID and try again."""
    _ERROR_CODE = "InvalidResourceId"


class InvalidResourceType(SSMError):
    """The resource type isn't valid. For example, if you are attempting to tag an EC2
    instance, the instance must be a registered managed node.
    """

    _ERROR_CODE = "InvalidResourceType"


class InvalidResultAttributeException(SSMError):
    """The specified inventory item result attribute isn't valid."""
    _ERROR_CODE = "InvalidResultAttributeException"


class InvalidRole(SSMError):
    """The role name can't contain invalid characters. Also verify that you specified an
    IAM role for notifications that includes the required trust policy. For information
    about configuring the IAM role for Run Command notifications, see Monitoring Systems
    Manager status changes using Amazon SNS notifications in the Amazon Web Services
    Systems Manager User Guide.
    """

    _ERROR_CODE = "InvalidRole"


class InvalidSchedule(SSMError):
    """The schedule is invalid. Verify your cron or rate expression and try again."""
    _ERROR_CODE = "InvalidSchedule"


class InvalidTag(SSMError):
    """The specified tag key or value isn't valid."""
    _ERROR_CODE = "InvalidTag"


class InvalidTarget(SSMError):
    """The target isn't valid or doesn't exist. It might not be configured for Systems
    Manager or you might not have permission to perform the operation.
    """

    _ERROR_CODE = "InvalidTarget"


class InvalidTargetMaps(SSMError):
    """TargetMap parameter isn't valid."""
    _ERROR_CODE = "InvalidTargetMaps"


class InvalidTypeNameException(SSMError):
    """The parameter type name isn't valid."""
    _ERROR_CODE = "InvalidTypeNameException"


class InvalidUpdate(SSMError):
    """The update isn't valid."""
    _ERROR_CODE = "InvalidUpdate"


class InvocationDoesNotExist(SSMError):
    """The command ID and managed node ID you specified didn't match any invocations.
    Verify the command ID and the managed node ID and try again.
    """

    _ERROR_CODE = "InvocationDoesNotExist"


class ItemContentMismatchException(SSMError):
    """The inventory item has invalid content."""
    _ERROR_CODE = "ItemContentMismatchException"

    @property
    def type_name(self) -> str | None:
        return self.response.get("TypeName")


class ItemSizeLimitExceededException(SSMError):
    """The inventory item size has exceeded the size limit."""
    _ERROR_CODE = "ItemSizeLimitExceededException"

    @property
    def type_name(self) -> str | None:
        return self.response.get("TypeName")


class MalformedResourcePolicyDocumentException(SSMError):
    """The specified policy document is malformed or invalid, or excessive
    `PutResourcePolicy` or `DeleteResourcePolicy` calls have been made.
    """

    _ERROR_CODE = "MalformedResourcePolicyDocumentException"


class MaxDocumentSizeExceeded(SSMError):
    """The size limit of a document is 64 KB."""
    _ERROR_CODE = "MaxDocumentSizeExceeded"


class NoLongerSupportedException(SSMError):
    """The requested operation is no longer supported by Systems Manager."""
    _ERROR_CODE = "NoLongerSupportedException"


class OpsItemAccessDeniedException(SSMError):
    """You don't have permission to view OpsItems in the specified account. Verify that
    your account is configured either as a Systems Manager delegated administrator or
    that you are logged into the Organizations management account.
    """

    _ERROR_CODE = "OpsItemAccessDeniedException"


class OpsItemAlreadyExistsException(SSMError):
    """The OpsItem already exists."""
    _ERROR_CODE = "OpsItemAlreadyExistsException"

    @property
    def ops_item_id(self) -> str | None:
        return self.response.get("OpsItemId")


class OpsItemConflictException(SSMError):
    """The specified OpsItem is in the process of being deleted."""
    _ERROR_CODE = "OpsItemConflictException"


class OpsItemInvalidParameterException(SSMError):
    """A specified parameter argument isn't valid. Verify the available arguments and try
    again.
    """

    _ERROR_CODE = "OpsItemInvalidParameterException"

    @property
    def parameter_names(self) -> list[Any] | None:
        return self.response.get("ParameterNames")


class OpsItemLimitExceededException(SSMError):
    """The request caused OpsItems to exceed one or more quotas."""
    _ERROR_CODE = "OpsItemLimitExceededException"

    @property
    def limit(self) -> int | None:
        return self.response.get("Limit")

    @property
    def limit_type(self) -> str | None:
        return self.response.get("LimitType")

    @property
    def resource_types(self) -> list[Any] | None:
        return self.response.get("ResourceTypes")


class OpsItemNotFoundException(SSMError):
    """The specified OpsItem ID doesn't exist. Verify the ID and try again."""
    _ERROR_CODE = "OpsItemNotFoundException"


class OpsItemRelatedItemAlreadyExistsException(SSMError):
    """The Amazon Resource Name (ARN) is already associated with the OpsItem."""
    _ERROR_CODE = "OpsItemRelatedItemAlreadyExistsException"

    @property
    def ops_item_id(self) -> str | None:
        return self.response.get("OpsItemId")

    @property
    def resource_uri(self) -> str | None:
        return self.response.get("ResourceUri")


class OpsItemRelatedItemAssociationNotFoundException(SSMError):
    """The association wasn't found using the parameters you specified in the call. Verify
    the information and try again.
    """

    _ERROR_CODE = "OpsItemRelatedItemAssociationNotFoundException"


class OpsMetadataAlreadyExistsException(SSMError):
    """An OpsMetadata object already exists for the selected resource."""
    _ERROR_CODE = "OpsMetadataAlreadyExistsException"


class OpsMetadataInvalidArgumentException(SSMError):
    """One of the arguments passed is invalid."""
    _ERROR_CODE = "OpsMetadataInvalidArgumentException"


class OpsMetadataKeyLimitExceededException(SSMError):
    """The OpsMetadata object exceeds the maximum number of OpsMetadata keys that you can
    assign to an application in Application Manager.
    """

    _ERROR_CODE = "OpsMetadataKeyLimitExceededException"


class OpsMetadataLimitExceededException(SSMError):
    """Your account reached the maximum number of OpsMetadata objects allowed by
    Application Manager. The maximum is 200 OpsMetadata objects. Delete one or more
    OpsMetadata object and try again.
    """

    _ERROR_CODE = "OpsMetadataLimitExceededException"


class OpsMetadataNotFoundException(SSMError):
    """The OpsMetadata object doesn't exist."""
    _ERROR_CODE = "OpsMetadataNotFoundException"


class OpsMetadataTooManyUpdatesException(SSMError):
    """The system is processing too many concurrent updates. Wait a few moments and try
    again.
    """

    _ERROR_CODE = "OpsMetadataTooManyUpdatesException"


class ParameterAlreadyExists(SSMError):
    """The parameter already exists. You can't create duplicate parameters."""
    _ERROR_CODE = "ParameterAlreadyExists"


class ParameterLimitExceeded(SSMError):
    """You have exceeded the number of parameters for this Amazon Web Services account.
    Delete one or more parameters and try again.
    """

    _ERROR_CODE = "ParameterLimitExceeded"


class ParameterMaxVersionLimitExceeded(SSMError):
    """Parameter Store retains the 100 most recently created versions of a parameter. After
    this number of versions has been created, Parameter Store deletes the oldest version
    when a new one is created. However, if the oldest version has a label attached to
    it, Parameter Store won't delete the version and instead presents this error
    message:

     `An error occurred (ParameterMaxVersionLimitExceeded) when calling the PutParameter
    operation: You attempted to create a new version of parameter-name by calling the
    PutParameter API with the overwrite flag. Version version-number, the oldest
    version, can't be deleted because it has a label associated with it. Move the label
    to another version of the parameter, and try again.`

    This safeguard is to prevent parameter versions with mission critical labels
    assigned to them from being deleted. To continue creating new parameters, first move
    the label from the oldest version of the parameter to a newer one for use in your
    operations. For information about moving parameter labels, see Move a parameter
    label (console) or Move a parameter label (CLI) in the Amazon Web Services Systems
    Manager User Guide.
    """

    _ERROR_CODE = "ParameterMaxVersionLimitExceeded"


class ParameterNotFound(SSMError):
    """The parameter couldn't be found. Verify the name and try again.

    Note:

    For the `DeleteParameter` and `GetParameter` actions, if the specified parameter
    doesn't exist, the `ParameterNotFound` exception is not recorded in CloudTrail event
    logs.
    """

    _ERROR_CODE = "ParameterNotFound"


class ParameterPatternMismatchException(SSMError):
    """The parameter name isn't valid."""
    _ERROR_CODE = "ParameterPatternMismatchException"


class ParameterVersionLabelLimitExceeded(SSMError):
    """A parameter version can have a maximum of ten labels."""
    _ERROR_CODE = "ParameterVersionLabelLimitExceeded"


class ParameterVersionNotFound(SSMError):
    """The specified parameter version wasn't found. Verify the parameter name and version,
    and try again.
    """

    _ERROR_CODE = "ParameterVersionNotFound"


class PoliciesLimitExceededException(SSMError):
    """You specified more than the maximum number of allowed policies for the parameter.
    The maximum is 10.
    """

    _ERROR_CODE = "PoliciesLimitExceededException"


class ResourceDataSyncAlreadyExistsException(SSMError):
    """A sync configuration with the same name already exists."""
    _ERROR_CODE = "ResourceDataSyncAlreadyExistsException"

    @property
    def sync_name(self) -> str | None:
        return self.response.get("SyncName")


class ResourceDataSyncConflictException(SSMError):
    """Another `UpdateResourceDataSync` request is being processed. Wait a few minutes and
    try again.
    """

    _ERROR_CODE = "ResourceDataSyncConflictException"


class ResourceDataSyncCountExceededException(SSMError):
    """You have exceeded the allowed maximum sync configurations."""
    _ERROR_CODE = "ResourceDataSyncCountExceededException"


class ResourceDataSyncInvalidConfigurationException(SSMError):
    """The specified sync configuration is invalid."""
    _ERROR_CODE = "ResourceDataSyncInvalidConfigurationException"


class ResourceDataSyncNotFoundException(SSMError):
    """The specified sync name wasn't found."""
    _ERROR_CODE = "ResourceDataSyncNotFoundException"

    @property
    def sync_name(self) -> str | None:
        return self.response.get("SyncName")

    @property
    def sync_type(self) -> str | None:
        return self.response.get("SyncType")


class ResourceInUseException(SSMError):
    """Error returned if an attempt is made to delete a patch baseline that is registered
    for a patch group.
    """

    _ERROR_CODE = "ResourceInUseException"


class ResourceLimitExceededException(SSMError):
    """Error returned when the caller has exceeded the default resource quotas. For
    example, too many maintenance windows or patch baselines have been created.

    For information about resource quotas in Systems Manager, see Systems Manager
    service quotas in the Amazon Web Services General Reference.
    """

    _ERROR_CODE = "ResourceLimitExceededException"


class ResourceNotFoundException(SSMError):
    """The specified parameter to be shared could not be found."""
    _ERROR_CODE = "ResourceNotFoundException"


class ResourcePolicyConflictException(SSMError):
    """The hash provided in the call doesn't match the stored hash. This exception is
    thrown when trying to update an obsolete policy version or when multiple requests to
    update a policy are sent.
    """

    _ERROR_CODE = "ResourcePolicyConflictException"


class ResourcePolicyInvalidParameterException(SSMError):
    """One or more parameters specified for the call aren't valid. Verify the parameters
    and their values and try again.
    """

    _ERROR_CODE = "ResourcePolicyInvalidParameterException"

    @property
    def parameter_names(self) -> list[Any] | None:
        return self.response.get("ParameterNames")


class ResourcePolicyLimitExceededException(SSMError):
    """The PutResourcePolicy API action enforces two limits. A policy can't be greater than
    1024 bytes in size. And only one policy can be attached to `OpsItemGroup`. Verify
    these limits and try again.
    """

    _ERROR_CODE = "ResourcePolicyLimitExceededException"

    @property
    def limit(self) -> int | None:
        return self.response.get("Limit")

    @property
    def limit_type(self) -> str | None:
        return self.response.get("LimitType")


class ResourcePolicyNotFoundException(SSMError):
    """No policies with the specified policy ID and hash could be found."""
    _ERROR_CODE = "ResourcePolicyNotFoundException"


class ServiceQuotaExceededException(SSMError):
    """The request exceeds the service quota. Service quotas, also referred to as limits,
    are the maximum number of service resources or operations for your Amazon Web
    Services account.
    """

    _ERROR_CODE = "ServiceQuotaExceededException"

    @property
    def quota_code(self) -> str | None:
        """The quota code recognized by the Amazon Web Services Service Quotas service."""
        return self.response.get("QuotaCode")

    @property
    def resource_id(self) -> str | None:
        """The unique ID of the resource referenced in the failed request."""
        return self.response.get("ResourceId")

    @property
    def resource_type(self) -> str | None:
        """The resource type of the resource referenced in the failed request."""
        return self.response.get("ResourceType")

    @property
    def service_code(self) -> str | None:
        """The code for the Amazon Web Services service that owns the quota."""
        return self.response.get("ServiceCode")


class ServiceSettingNotFound(SSMError):
    """The specified service setting wasn't found. Either the service name or the setting
    hasn't been provisioned by the Amazon Web Services service team.
    """

    _ERROR_CODE = "ServiceSettingNotFound"


class StatusUnchanged(SSMError):
    """The updated status is the same as the current status."""
    _ERROR_CODE = "StatusUnchanged"


class SubTypeCountLimitExceededException(SSMError):
    """The sub-type count exceeded the limit for the inventory type."""
    _ERROR_CODE = "SubTypeCountLimitExceededException"


class TargetInUseException(SSMError):
    """You specified the `Safe` option for the DeregisterTargetFromMaintenanceWindow
    operation, but the target is still referenced in a task.
    """

    _ERROR_CODE = "TargetInUseException"


class TargetNotConnected(SSMError):
    """The specified target managed node for the session isn't fully configured for use
    with Session Manager. For more information, see Setting up Session Manager in the
    Amazon Web Services Systems Manager User Guide. This error is also returned if you
    attempt to start a session on a managed node that is located in a different account
    or Region
    """

    _ERROR_CODE = "TargetNotConnected"


class ThrottlingException(SSMError):
    """The request or operation couldn't be performed because the service is throttling
    requests.
    """

    _ERROR_CODE = "ThrottlingException"

    @property
    def quota_code(self) -> str | None:
        """The quota code recognized by the Amazon Web Services Service Quotas service."""
        return self.response.get("QuotaCode")

    @property
    def service_code(self) -> str | None:
        """The code for the Amazon Web Services service that owns the quota."""
        return self.response.get("ServiceCode")


class TooManyTagsError(SSMError):
    """The `Targets` parameter includes too many tags. Remove one or more tags and try the
    command again.
    """

    _ERROR_CODE = "TooManyTagsError"


class TooManyUpdates(SSMError):
    """There are concurrent updates for a resource that supports one update at a time."""
    _ERROR_CODE = "TooManyUpdates"


class TotalSizeLimitExceededException(SSMError):
    """The size of inventory data has exceeded the total size limit for the resource."""
    _ERROR_CODE = "TotalSizeLimitExceededException"


class UnsupportedCalendarException(SSMError):
    """The calendar entry contained in the specified SSM document isn't supported."""
    _ERROR_CODE = "UnsupportedCalendarException"


class UnsupportedFeatureRequiredException(SSMError):
    """Patching for applications released by Microsoft is only available on EC2 instances
    and advanced instances. To patch applications released by Microsoft on on-premises
    servers and VMs, you must enable advanced instances. For more information, see
    Turning on the advanced-instances tier in the Amazon Web Services Systems Manager
    User Guide.
    """

    _ERROR_CODE = "UnsupportedFeatureRequiredException"


class UnsupportedInventoryItemContextException(SSMError):
    """The `Context` attribute that you specified for the `InventoryItem` isn't allowed for
    this inventory type. You can only use the `Context` attribute with inventory types
    like `AWS:ComplianceItem`.
    """

    _ERROR_CODE = "UnsupportedInventoryItemContextException"

    @property
    def type_name(self) -> str | None:
        return self.response.get("TypeName")


class UnsupportedInventorySchemaVersionException(SSMError):
    """Inventory item type schema version has to match supported versions in the service.
    Check output of GetInventorySchema to see the available schema version for each
    type.
    """

    _ERROR_CODE = "UnsupportedInventorySchemaVersionException"


class UnsupportedOperatingSystem(SSMError):
    """The operating systems you specified isn't supported, or the operation isn't
    supported for the operating system.
    """

    _ERROR_CODE = "UnsupportedOperatingSystem"


class UnsupportedOperationException(SSMError):
    """This operation is not supported for the current account. You must first enable the
    Systems Manager integrated experience in your account.
    """

    _ERROR_CODE = "UnsupportedOperationException"


class UnsupportedParameterType(SSMError):
    """The parameter type isn't supported."""
    _ERROR_CODE = "UnsupportedParameterType"


class UnsupportedPlatformType(SSMError):
    """The document doesn't support the platform type of the given managed node IDs. For
    example, you sent an document for a Windows managed node to a Linux node.
    """

    _ERROR_CODE = "UnsupportedPlatformType"


class ValidationException(SSMError):
    """The request isn't valid. Verify that you entered valid contents for the command and
    try again.
    """

    _ERROR_CODE = "ValidationException"

    @property
    def reason_code(self) -> str | None:
        """The reason code for the invalid request."""
        return self.response.get("ReasonCode")


EXCEPTIONS: dict[str, type[SSMError]] = {
    "AccessDeniedException": AccessDeniedException,
    "AlreadyExistsException": AlreadyExistsException,
    "AssociatedInstances": AssociatedInstances,
    "AssociationAlreadyExists": AssociationAlreadyExists,
    "AssociationDoesNotExist": AssociationDoesNotExist,
    "AssociationExecutionDoesNotExist": AssociationExecutionDoesNotExist,
    "AssociationLimitExceeded": AssociationLimitExceeded,
    "AssociationVersionLimitExceeded": AssociationVersionLimitExceeded,
    "AutomationDefinitionNotApprovedException": AutomationDefinitionNotApprovedException,
    "AutomationDefinitionNotFoundException": AutomationDefinitionNotFoundException,
    "AutomationDefinitionVersionNotFoundException": AutomationDefinitionVersionNotFoundException,
    "AutomationExecutionLimitExceededException": AutomationExecutionLimitExceededException,
    "AutomationExecutionNotFoundException": AutomationExecutionNotFoundException,
    "AutomationStepNotFoundException": AutomationStepNotFoundException,
    "ComplianceTypeCountLimitExceededException": ComplianceTypeCountLimitExceededException,
    "CustomSchemaCountLimitExceededException": CustomSchemaCountLimitExceededException,
    "DocumentAlreadyExists": DocumentAlreadyExists,
    "DocumentLimitExceeded": DocumentLimitExceeded,
    "DocumentPermissionLimit": DocumentPermissionLimit,
    "DocumentVersionLimitExceeded": DocumentVersionLimitExceeded,
    "DoesNotExistException": DoesNotExistException,
    "DuplicateDocumentContent": DuplicateDocumentContent,
    "DuplicateDocumentVersionName": DuplicateDocumentVersionName,
    "DuplicateInstanceId": DuplicateInstanceId,
    "FeatureNotAvailableException": FeatureNotAvailableException,
    "HierarchyLevelLimitExceededException": HierarchyLevelLimitExceededException,
    "HierarchyTypeMismatchException": HierarchyTypeMismatchException,
    "IdempotentParameterMismatch": IdempotentParameterMismatch,
    "IncompatiblePolicyException": IncompatiblePolicyException,
    "InternalServerError": InternalServerError,
    "InvalidActivation": InvalidActivation,
    "InvalidActivationId": InvalidActivationId,
    "InvalidAggregatorException": InvalidAggregatorException,
    "InvalidAllowedPatternException": InvalidAllowedPatternException,
    "InvalidAssociation": InvalidAssociation,
    "InvalidAssociationVersion": InvalidAssociationVersion,
    "InvalidAutomationExecutionParametersException": InvalidAutomationExecutionParametersException,
    "InvalidAutomationSignalException": InvalidAutomationSignalException,
    "InvalidAutomationStatusUpdateException": InvalidAutomationStatusUpdateException,
    "InvalidCommandId": InvalidCommandId,
    "InvalidDeleteInventoryParametersException": InvalidDeleteInventoryParametersException,
    "InvalidDeletionIdException": InvalidDeletionIdException,
    "InvalidDocument": InvalidDocument,
    "InvalidDocumentContent": InvalidDocumentContent,
    "InvalidDocumentOperation": InvalidDocumentOperation,
    "InvalidDocumentSchemaVersion": InvalidDocumentSchemaVersion,
    "InvalidDocumentType": InvalidDocumentType,
    "InvalidDocumentVersion": InvalidDocumentVersion,
    "InvalidFilter": InvalidFilter,
    "InvalidFilterKey": InvalidFilterKey,
    "InvalidFilterOption": InvalidFilterOption,
    "InvalidFilterValue": InvalidFilterValue,
    "InvalidInstanceId": InvalidInstanceId,
    "InvalidInstanceInformationFilterValue": InvalidInstanceInformationFilterValue,
    "InvalidInstancePropertyFilterValue": InvalidInstancePropertyFilterValue,
    "InvalidInventoryGroupException": InvalidInventoryGroupException,
    "InvalidInventoryItemContextException": InvalidInventoryItemContextException,
    "InvalidInventoryRequestException": InvalidInventoryRequestException,
    "InvalidItemContentException": InvalidItemContentException,
    "InvalidKeyId": InvalidKeyId,
    "InvalidNextToken": InvalidNextToken,
    "InvalidNotificationConfig": InvalidNotificationConfig,
    "InvalidOptionException": InvalidOptionException,
    "InvalidOutputFolder": InvalidOutputFolder,
    "InvalidOutputLocation": InvalidOutputLocation,
    "InvalidParameters": InvalidParameters,
    "InvalidPermissionType": InvalidPermissionType,
    "InvalidPluginName": InvalidPluginName,
    "InvalidPolicyAttributeException": InvalidPolicyAttributeException,
    "InvalidPolicyTypeException": InvalidPolicyTypeException,
    "InvalidResourceId": InvalidResourceId,
    "InvalidResourceType": InvalidResourceType,
    "InvalidResultAttributeException": InvalidResultAttributeException,
    "InvalidRole": InvalidRole,
    "InvalidSchedule": InvalidSchedule,
    "InvalidTag": InvalidTag,
    "InvalidTarget": InvalidTarget,
    "InvalidTargetMaps": InvalidTargetMaps,
    "InvalidTypeNameException": InvalidTypeNameException,
    "InvalidUpdate": InvalidUpdate,
    "InvocationDoesNotExist": InvocationDoesNotExist,
    "ItemContentMismatchException": ItemContentMismatchException,
    "ItemSizeLimitExceededException": ItemSizeLimitExceededException,
    "MalformedResourcePolicyDocumentException": MalformedResourcePolicyDocumentException,
    "MaxDocumentSizeExceeded": MaxDocumentSizeExceeded,
    "NoLongerSupportedException": NoLongerSupportedException,
    "OpsItemAccessDeniedException": OpsItemAccessDeniedException,
    "OpsItemAlreadyExistsException": OpsItemAlreadyExistsException,
    "OpsItemConflictException": OpsItemConflictException,
    "OpsItemInvalidParameterException": OpsItemInvalidParameterException,
    "OpsItemLimitExceededException": OpsItemLimitExceededException,
    "OpsItemNotFoundException": OpsItemNotFoundException,
    "OpsItemRelatedItemAlreadyExistsException": OpsItemRelatedItemAlreadyExistsException,
    "OpsItemRelatedItemAssociationNotFoundException": OpsItemRelatedItemAssociationNotFoundException,
    "OpsMetadataAlreadyExistsException": OpsMetadataAlreadyExistsException,
    "OpsMetadataInvalidArgumentException": OpsMetadataInvalidArgumentException,
    "OpsMetadataKeyLimitExceededException": OpsMetadataKeyLimitExceededException,
    "OpsMetadataLimitExceededException": OpsMetadataLimitExceededException,
    "OpsMetadataNotFoundException": OpsMetadataNotFoundException,
    "OpsMetadataTooManyUpdatesException": OpsMetadataTooManyUpdatesException,
    "ParameterAlreadyExists": ParameterAlreadyExists,
    "ParameterLimitExceeded": ParameterLimitExceeded,
    "ParameterMaxVersionLimitExceeded": ParameterMaxVersionLimitExceeded,
    "ParameterNotFound": ParameterNotFound,
    "ParameterPatternMismatchException": ParameterPatternMismatchException,
    "ParameterVersionLabelLimitExceeded": ParameterVersionLabelLimitExceeded,
    "ParameterVersionNotFound": ParameterVersionNotFound,
    "PoliciesLimitExceededException": PoliciesLimitExceededException,
    "ResourceDataSyncAlreadyExistsException": ResourceDataSyncAlreadyExistsException,
    "ResourceDataSyncConflictException": ResourceDataSyncConflictException,
    "ResourceDataSyncCountExceededException": ResourceDataSyncCountExceededException,
    "ResourceDataSyncInvalidConfigurationException": ResourceDataSyncInvalidConfigurationException,
    "ResourceDataSyncNotFoundException": ResourceDataSyncNotFoundException,
    "ResourceInUseException": ResourceInUseException,
    "ResourceLimitExceededException": ResourceLimitExceededException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ResourcePolicyConflictException": ResourcePolicyConflictException,
    "ResourcePolicyInvalidParameterException": ResourcePolicyInvalidParameterException,
    "ResourcePolicyLimitExceededException": ResourcePolicyLimitExceededException,
    "ResourcePolicyNotFoundException": ResourcePolicyNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ServiceSettingNotFound": ServiceSettingNotFound,
    "StatusUnchanged": StatusUnchanged,
    "SubTypeCountLimitExceededException": SubTypeCountLimitExceededException,
    "TargetInUseException": TargetInUseException,
    "TargetNotConnected": TargetNotConnected,
    "ThrottlingException": ThrottlingException,
    "TooManyTagsError": TooManyTagsError,
    "TooManyUpdates": TooManyUpdates,
    "TotalSizeLimitExceededException": TotalSizeLimitExceededException,
    "UnsupportedCalendarException": UnsupportedCalendarException,
    "UnsupportedFeatureRequiredException": UnsupportedFeatureRequiredException,
    "UnsupportedInventoryItemContextException": UnsupportedInventoryItemContextException,
    "UnsupportedInventorySchemaVersionException": UnsupportedInventorySchemaVersionException,
    "UnsupportedOperatingSystem": UnsupportedOperatingSystem,
    "UnsupportedOperationException": UnsupportedOperationException,
    "UnsupportedParameterType": UnsupportedParameterType,
    "UnsupportedPlatformType": UnsupportedPlatformType,
    "ValidationException": ValidationException,
}
