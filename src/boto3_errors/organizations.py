# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class OrganizationsError(Boto3Error):
    _SERVICE = "organizations"


class AWSOrganizationsNotInUseException(OrganizationsError):
    """Your account isn't a member of an organization. To make this request, you must use
    the credentials of an account that belongs to an organization.
    """

    _ERROR_CODE = "AWSOrganizationsNotInUseException"


class AccessDeniedException(OrganizationsError):
    """You don't have permissions to perform the requested operation. The user or role that
    is making the request must have at least one IAM permissions policy attached that
    grants the required permissions. For more information, see Access Management in the
    IAM User Guide.
    """

    _ERROR_CODE = "AccessDeniedException"


class AccessDeniedForDependencyException(OrganizationsError):
    """The operation that you attempted requires you to have the
    `iam:CreateServiceLinkedRole` for `organizations.amazonaws.com` permission so that
    Organizations can create the required service-linked role. You don't have that
    permission.
    """

    _ERROR_CODE = "AccessDeniedForDependencyException"

    @property
    def reason(self) -> str | None:
        return self.response.get("Reason")


class AccountAlreadyClosedException(OrganizationsError):
    """You attempted to close an account that is already closed."""
    _ERROR_CODE = "AccountAlreadyClosedException"


class AccountAlreadyRegisteredException(OrganizationsError):
    """The specified account is already a delegated administrator for this Amazon Web
    Services service.
    """

    _ERROR_CODE = "AccountAlreadyRegisteredException"


class AccountNotFoundException(OrganizationsError):
    """We can't find an Amazon Web Services account with the `AccountId` that you
    specified, or the account whose credentials you used to make this request isn't a
    member of an organization.
    """

    _ERROR_CODE = "AccountNotFoundException"


class AccountNotRegisteredException(OrganizationsError):
    """The specified account is not a delegated administrator for this Amazon Web Services
    service.
    """

    _ERROR_CODE = "AccountNotRegisteredException"


class AccountOwnerNotVerifiedException(OrganizationsError):
    """You can't invite an existing account to your organization until you verify that you
    own the email address associated with the management account. For more information,
    see Email address verification in the Organizations User Guide.
    """

    _ERROR_CODE = "AccountOwnerNotVerifiedException"


class AlreadyInOrganizationException(OrganizationsError):
    """This account is already a member of an organization. An account can belong to only
    one organization at a time.
    """

    _ERROR_CODE = "AlreadyInOrganizationException"


class ChildNotFoundException(OrganizationsError):
    """We can't find an organizational unit (OU) or Amazon Web Services account with the
    `ChildId` that you specified.
    """

    _ERROR_CODE = "ChildNotFoundException"


class ConcurrentModificationException(OrganizationsError):
    """The target of the operation is currently being modified by a different request. Try
    again later.
    """

    _ERROR_CODE = "ConcurrentModificationException"


class ConflictException(OrganizationsError):
    """The request failed because it conflicts with the current state of the specified
    resource.
    """

    _ERROR_CODE = "ConflictException"


class ConstraintViolationException(OrganizationsError):
    """Performing this operation violates a minimum or maximum value limit. For example,
    attempting to remove the last service control policy (SCP) from an OU or root,
    inviting or creating too many accounts to the organization, or attaching too many
    policies to an account, OU, or root. This exception includes a reason that contains
    additional information about the violated limit:

    Note:

    Some of the reasons in the following list might not be applicable to this specific
    API or operation.

    - ACCOUNT_CANNOT_LEAVE_ORGANIZATION: You attempted to remove the management account
      from the organization. You can't remove the management account. Instead, after you
      remove all member accounts, delete the organization itself.
    - ACCOUNT_CANNOT_LEAVE_WITHOUT_PHONE_VERIFICATION: You attempted to remove an
      account from the organization that doesn't yet have enough information to exist as
      a standalone account. This account requires you to first complete phone
      verification. Follow the steps at Removing a member account from your organization
      in the Organizations User Guide.
    - ACCOUNT_CREATION_RATE_LIMIT_EXCEEDED: You attempted to exceed the number of
      accounts that you can create in one day.
    - ACCOUNT_CREATION_NOT_COMPLETE: Your account setup isn't complete or your account
      isn't fully active. You must complete the account setup before you create an
      organization.
    - ACCOUNT_NUMBER_LIMIT_EXCEEDED: You attempted to exceed the limit on the number of
      accounts in an organization. If you need more accounts, contact Amazon Web
      Services Support to request an increase in your limit. Or the number of
      invitations that you tried to send would cause you to exceed the limit of accounts
      in your organization. Send fewer invitations or contact Amazon Web Services
      Support to request an increase in the number of accounts.

    Note: Deleted and closed accounts still count toward your limit.

      If you get this exception when running a command immediately after creating the
    organization, wait one hour and try again. After an hour, if the command continues
    to fail with this error, contact Amazon Web Services Support.
    - CANNOT_REGISTER_SUSPENDED_ACCOUNT_AS_DELEGATED_ADMINISTRATOR: You cannot register
      a suspended account as a delegated administrator.
    - CANNOT_REGISTER_MASTER_AS_DELEGATED_ADMINISTRATOR: You attempted to register the
      management account of the organization as a delegated administrator for an Amazon
      Web Services service integrated with Organizations. You can designate only a
      member account as a delegated administrator.
    - CANNOT_CLOSE_MANAGEMENT_ACCOUNT: You attempted to close the management account. To
      close the management account for the organization, you must first either remove or
      close all member accounts in the organization. Follow standard account closure
      process using root credentials.​
    - CANNOT_REMOVE_DELEGATED_ADMINISTRATOR_FROM_ORG: You attempted to remove an account
      that is registered as a delegated administrator for a service integrated with your
      organization. To complete this operation, you must first deregister this account
      as a delegated administrator.
    - CLOSE_ACCOUNT_QUOTA_EXCEEDED: You have exceeded close account quota for the past
      30 days.
    - CLOSE_ACCOUNT_REQUESTS_LIMIT_EXCEEDED: You attempted to exceed the number of
      accounts that you can close at a time. ​
    - CREATE_ORGANIZATION_IN_BILLING_MODE_UNSUPPORTED_REGION: To create an organization
      in the specified region, you must enable all features mode.
    - DELEGATED_ADMINISTRATOR_EXISTS_FOR_THIS_SERVICE: You attempted to register an
      Amazon Web Services account as a delegated administrator for an Amazon Web
      Services service that already has a delegated administrator. To complete this
      operation, you must first deregister any existing delegated administrators for
      this service.
    - EMAIL_VERIFICATION_CODE_EXPIRED: The email verification code is only valid for a
      limited period of time. You must resubmit the request and generate a new
      verfication code.
    - HANDSHAKE_RATE_LIMIT_EXCEEDED: You attempted to exceed the number of handshakes
      that you can send in one day.
    - INVALID_PAYMENT_INSTRUMENT: You cannot remove an account because no supported
      payment method is associated with the account. Amazon Web Services does not
      support cards issued by financial institutions in Russia or Belarus. For more
      information, see Managing your Amazon Web Services payments.
    - MASTER_ACCOUNT_ADDRESS_DOES_NOT_MATCH_MARKETPLACE: To create an account in this
      organization, you first must migrate the organization's management account to the
      marketplace that corresponds to the management account's address. For example,
      accounts with India addresses must be associated with the AISPL marketplace. All
      accounts in an organization must be associated with the same marketplace.
    - MASTER_ACCOUNT_MISSING_BUSINESS_LICENSE: Applies only to the Amazon Web Services
      Regions in China. To create an organization, the master must have a valid business
      license. For more information, contact customer support.
    - MASTER_ACCOUNT_MISSING_CONTACT_INFO: To complete this operation, you must first
      provide a valid contact address and phone number for the management account. Then
      try the operation again.
    - MASTER_ACCOUNT_NOT_GOVCLOUD_ENABLED: To complete this operation, the management
      account must have an associated account in the Amazon Web Services GovCloud (US-
      West) Region. For more information, see Organizations in the Amazon Web Services
      GovCloud User Guide.
    - MASTER_ACCOUNT_PAYMENT_INSTRUMENT_REQUIRED: To create an organization with this
      management account, you first must associate a valid payment instrument, such as a
      credit card, with the account. For more information, see Considerations before
      removing an account from an organization in the Organizations User Guide.
    - MAX_DELEGATED_ADMINISTRATORS_FOR_SERVICE_LIMIT_EXCEEDED: You attempted to register
      more delegated administrators than allowed for the service principal.
    - MAX_POLICY_TYPE_ATTACHMENT_LIMIT_EXCEEDED: You attempted to exceed the number of
      policies of a certain type that can be attached to an entity at one time.
    - MAX_TAG_LIMIT_EXCEEDED: You have exceeded the number of tags allowed on this
      resource.
    - MEMBER_ACCOUNT_PAYMENT_INSTRUMENT_REQUIRED: To complete this operation with this
      member account, you first must associate a valid payment instrument, such as a
      credit card, with the account. For more information, see Considerations before
      removing an account from an organization in the Organizations User Guide.
    - MIN_POLICY_TYPE_ATTACHMENT_LIMIT_EXCEEDED: You attempted to detach a policy from
      an entity that would cause the entity to have fewer than the minimum number of
      policies of a certain type required.
    - ORGANIZATION_NOT_IN_ALL_FEATURES_MODE: You attempted to perform an operation that
      requires the organization to be configured to support all features. An
      organization that supports only consolidated billing features can't perform this
      operation.
    - OU_DEPTH_LIMIT_EXCEEDED: You attempted to create an OU tree that is too many
      levels deep.
    - OU_NUMBER_LIMIT_EXCEEDED: You attempted to exceed the number of OUs that you can
      have in an organization.
    - POLICY_CONTENT_LIMIT_EXCEEDED: You attempted to create a policy that is larger
      than the maximum size.
    - POLICY_NUMBER_LIMIT_EXCEEDED: You attempted to exceed the number of policies that
      you can have in an organization.
    - SERVICE_ACCESS_NOT_ENABLED: You attempted to register a delegated administrator
      before you enabled service access. Call the `EnableAWSServiceAccess` API first.
    - TAG_POLICY_VIOLATION: You attempted to create or update a resource with tags that
      are not compliant with the tag policy requirements for this account.
    - WAIT_PERIOD_ACTIVE: After you create an Amazon Web Services account, there is a
      waiting period before you can remove it from the organization. If you get an error
      that indicates that a wait period is required, try again in a few days.
    """

    _ERROR_CODE = "ConstraintViolationException"

    @property
    def reason(self) -> str | None:
        return self.response.get("Reason")


class CreateAccountStatusNotFoundException(OrganizationsError):
    """We can't find an create account request with the `CreateAccountRequestId` that you
    specified.
    """

    _ERROR_CODE = "CreateAccountStatusNotFoundException"


class DestinationParentNotFoundException(OrganizationsError):
    """We can't find the destination container (a root or OU) with the `ParentId` that you
    specified.
    """

    _ERROR_CODE = "DestinationParentNotFoundException"


class DuplicateAccountException(OrganizationsError):
    """That account is already present in the specified destination."""
    _ERROR_CODE = "DuplicateAccountException"


class DuplicateHandshakeException(OrganizationsError):
    """A handshake with the same action and target already exists. For example, if you
    invited an account to join your organization, the invited account might already have
    a pending invitation from this organization. If you intend to resend an invitation
    to an account, ensure that existing handshakes that might be considered duplicates
    are canceled or declined.
    """

    _ERROR_CODE = "DuplicateHandshakeException"


class DuplicateOrganizationalUnitException(OrganizationsError):
    """An OU with the same name already exists."""
    _ERROR_CODE = "DuplicateOrganizationalUnitException"


class DuplicatePolicyAttachmentException(OrganizationsError):
    """The selected policy is already attached to the specified target."""
    _ERROR_CODE = "DuplicatePolicyAttachmentException"


class DuplicatePolicyException(OrganizationsError):
    """A policy with the same name already exists."""
    _ERROR_CODE = "DuplicatePolicyException"


class EffectivePolicyNotFoundException(OrganizationsError):
    """If you ran this action on the management account, this policy type is not enabled.
    If you ran the action on a member account, the account doesn't have an effective
    policy of this type. Contact the administrator of your organization about attaching
    a policy of this type to the account.
    """

    _ERROR_CODE = "EffectivePolicyNotFoundException"


class FinalizingOrganizationException(OrganizationsError):
    """Organizations couldn't perform the operation because your organization hasn't
    finished initializing. This can take up to an hour. Try again later. If after one
    hour you continue to receive this error, contact Amazon Web Services Support.
    """

    _ERROR_CODE = "FinalizingOrganizationException"


class HandshakeAlreadyInStateException(OrganizationsError):
    """The specified handshake is already in the requested state. For example, you can't
    accept a handshake that was already accepted.
    """

    _ERROR_CODE = "HandshakeAlreadyInStateException"


class HandshakeConstraintViolationException(OrganizationsError):
    """The requested operation would violate the constraint identified in the reason code.

    Note:

    Some of the reasons in the following list might not be applicable to this specific
    API or operation:

    - ACCOUNT_NUMBER_LIMIT_EXCEEDED: You attempted to exceed the limit on the number of
      accounts in an organization. Note that deleted and closed accounts still count
      toward your limit. If you get this exception immediately after creating the
      organization, wait one hour and try again. If after an hour it continues to fail
      with this error, contact Amazon Web Services Support.
    - ALREADY_IN_AN_ORGANIZATION: The handshake request is invalid because the invited
      account is already a member of an organization.
    - HANDSHAKE_RATE_LIMIT_EXCEEDED: You attempted to exceed the number of handshakes
      that you can send in one day.
    - INVITE_DISABLED_DURING_ENABLE_ALL_FEATURES: You can't issue new invitations to
      join an organization while it's in the process of enabling all features. You can
      resume inviting accounts after you finalize the process when all accounts have
      agreed to the change.
    - ORGANIZATION_ALREADY_HAS_ALL_FEATURES: The handshake request is invalid because
      the organization has already enabled all features.
    - ORGANIZATION_IS_ALREADY_PENDING_ALL_FEATURES_MIGRATION: The handshake request is
      invalid because the organization has already started the process to enable all
      features.
    - ORGANIZATION_FROM_DIFFERENT_SELLER_OF_RECORD: The request failed because the
      account is from a different marketplace than the accounts in the organization. For
      example, accounts with India addresses must be associated with the AISPL
      marketplace. All accounts in an organization must be from the same marketplace.
    - ORGANIZATION_MEMBERSHIP_CHANGE_RATE_LIMIT_EXCEEDED: You attempted to change the
      membership of an account too quickly after its previous change.
    - PAYMENT_INSTRUMENT_REQUIRED: You can't complete the operation with an account that
      doesn't have a payment instrument, such as a credit card, associated with it.
    """

    _ERROR_CODE = "HandshakeConstraintViolationException"

    @property
    def reason(self) -> str | None:
        return self.response.get("Reason")


class HandshakeNotFoundException(OrganizationsError):
    """We can't find a handshake with the `HandshakeId` that you specified."""
    _ERROR_CODE = "HandshakeNotFoundException"


class InvalidHandshakeTransitionException(OrganizationsError):
    """You can't perform the operation on the handshake in its current state. For example,
    you can't cancel a handshake that was already accepted or accept a handshake that
    was already declined.
    """

    _ERROR_CODE = "InvalidHandshakeTransitionException"


class InvalidInputException(OrganizationsError):
    """The requested operation failed because you provided invalid values for one or more
    of the request parameters. This exception includes a reason that contains additional
    information about the violated limit:

    Note:

    Some of the reasons in the following list might not be applicable to this specific
    API or operation.

    - DUPLICATE_TAG_KEY: Tag keys must be unique among the tags attached to the same
      entity.
    - IMMUTABLE_POLICY: You specified a policy that is managed by Amazon Web Services
      and can't be modified.
    - INPUT_REQUIRED: You must include a value for all required parameters.
    - INVALID_EMAIL_ADDRESS_TARGET: You specified an invalid email address for the
      invited account owner.
    - INVALID_ENUM: You specified an invalid value.
    - INVALID_ENUM_POLICY_TYPE: You specified an invalid policy type string.
    - INVALID_FULL_NAME_TARGET: You specified a full name that contains invalid
      characters.
    - INVALID_LIST_MEMBER: You provided a list to a parameter that contains at least one
      invalid value.
    - INVALID_PAGINATION_TOKEN: Get the value for the `NextToken` parameter from the
      response to a previous call of the operation.
    - INVALID_PARTY_TYPE_TARGET: You specified the wrong type of entity (account,
      organization, or email) as a party.
    - INVALID_PATTERN: You provided a value that doesn't match the required pattern.
    - INVALID_PATTERN_TARGET_ID: You specified a policy target ID that doesn't match the
      required pattern.
    - INVALID_ROLE_NAME: You provided a role name that isn't valid. A role name can't
      begin with the reserved prefix `AWSServiceRoleFor`.
    - INVALID_SYNTAX_ORGANIZATION_ARN: You specified an invalid Amazon Resource Name
      (ARN) for the organization.
    - INVALID_SYNTAX_POLICY_ID: You specified an invalid policy ID.
    - INVALID_SYSTEM_TAGS_PARAMETER: You specified a tag key that is a system tag. You
      can’t add, edit, or delete system tag keys because they're reserved for Amazon Web
      Services use. System tags don’t count against your tags per resource limit.
    - MAX_FILTER_LIMIT_EXCEEDED: You can specify only one filter parameter for the
      operation.
    - MAX_LENGTH_EXCEEDED: You provided a string parameter that is longer than allowed.
    - MAX_VALUE_EXCEEDED: You provided a numeric parameter that has a larger value than
      allowed.
    - MIN_LENGTH_EXCEEDED: You provided a string parameter that is shorter than allowed.
    - MIN_VALUE_EXCEEDED: You provided a numeric parameter that has a smaller value than
      allowed.
    - MOVING_ACCOUNT_BETWEEN_DIFFERENT_ROOTS: You can move an account only between
      entities in the same root.
    - TARGET_NOT_SUPPORTED: You can't perform the specified operation on that target
      entity.
    - UNRECOGNIZED_SERVICE_PRINCIPAL: You specified a service principal that isn't
      recognized.
    """

    _ERROR_CODE = "InvalidInputException"

    @property
    def reason(self) -> str | None:
        return self.response.get("Reason")


class MalformedPolicyDocumentException(OrganizationsError):
    """The provided policy document doesn't meet the requirements of the specified policy
    type. For example, the syntax might be incorrect. For details about service control
    policy syntax, see SCP syntax in the Organizations User Guide.
    """

    _ERROR_CODE = "MalformedPolicyDocumentException"


class MasterCannotLeaveOrganizationException(OrganizationsError):
    """You can't remove a management account from an organization. If you want the
    management account to become a member account in another organization, you must
    first delete the current organization of the management account.
    """

    _ERROR_CODE = "MasterCannotLeaveOrganizationException"


class OrganizationNotEmptyException(OrganizationsError):
    """The organization isn't empty. To delete an organization, you must first remove all
    accounts except the management account.
    """

    _ERROR_CODE = "OrganizationNotEmptyException"


class OrganizationalUnitNotEmptyException(OrganizationsError):
    """The specified OU is not empty. Move all accounts to another root or to other OUs,
    remove all child OUs, and try the operation again.
    """

    _ERROR_CODE = "OrganizationalUnitNotEmptyException"


class OrganizationalUnitNotFoundException(OrganizationsError):
    """We can't find an OU with the `OrganizationalUnitId` that you specified."""
    _ERROR_CODE = "OrganizationalUnitNotFoundException"


class ParentNotFoundException(OrganizationsError):
    """We can't find a root or OU with the `ParentId` that you specified."""
    _ERROR_CODE = "ParentNotFoundException"


class PolicyChangesInProgressException(OrganizationsError):
    """Changes to the effective policy are in progress, and its contents can't be returned.
    Try the operation again later.
    """

    _ERROR_CODE = "PolicyChangesInProgressException"


class PolicyInUseException(OrganizationsError):
    """The policy is attached to one or more entities. You must detach it from all roots,
    OUs, and accounts before performing this operation.
    """

    _ERROR_CODE = "PolicyInUseException"


class PolicyNotAttachedException(OrganizationsError):
    """The policy isn't attached to the specified target in the specified root."""
    _ERROR_CODE = "PolicyNotAttachedException"


class PolicyNotFoundException(OrganizationsError):
    """We can't find a policy with the `PolicyId` that you specified."""
    _ERROR_CODE = "PolicyNotFoundException"


class PolicyTypeAlreadyEnabledException(OrganizationsError):
    """The specified policy type is already enabled in the specified root."""
    _ERROR_CODE = "PolicyTypeAlreadyEnabledException"


class PolicyTypeNotAvailableForOrganizationException(OrganizationsError):
    """You can't use the specified policy type with the feature set currently enabled for
    this organization. For example, you can enable SCPs only after you enable all
    features in the organization. For more information, see Managing Organizations
    policiesin the Organizations User Guide.
    """

    _ERROR_CODE = "PolicyTypeNotAvailableForOrganizationException"


class PolicyTypeNotEnabledException(OrganizationsError):
    """The specified policy type isn't currently enabled in this root. You can't attach
    policies of the specified type to entities in a root until you enable that type in
    the root. For more information, see Enabling all features in your organization in
    the Organizations User Guide.
    """

    _ERROR_CODE = "PolicyTypeNotEnabledException"


class ResourcePolicyNotFoundException(OrganizationsError):
    """We can't find a resource policy request with the parameter that you specified."""
    _ERROR_CODE = "ResourcePolicyNotFoundException"


class RootNotFoundException(OrganizationsError):
    """We can't find a root with the `RootId` that you specified."""
    _ERROR_CODE = "RootNotFoundException"


class ServiceException(OrganizationsError):
    """Organizations can't complete your request because of an internal service error. Try
    again later.
    """

    _ERROR_CODE = "ServiceException"


class SourceParentNotFoundException(OrganizationsError):
    """We can't find a source root or OU with the `ParentId` that you specified."""
    _ERROR_CODE = "SourceParentNotFoundException"


class TargetNotFoundException(OrganizationsError):
    """We can't find a root, OU, account, or policy with the `TargetId` that you specified."""
    _ERROR_CODE = "TargetNotFoundException"


class TooManyRequestsException(OrganizationsError):
    """You have sent too many requests in too short a period of time. The quota helps
    protect against denial-of-service attacks. Try again later.

    For information about quotas that affect Organizations, see Quotas for Organizations
    in the Organizations User Guide.
    """

    _ERROR_CODE = "TooManyRequestsException"

    @property
    def type(self) -> str | None:
        return self.response.get("Type")


class UnsupportedAPIEndpointException(OrganizationsError):
    """This action isn't available in the current Amazon Web Services Region."""
    _ERROR_CODE = "UnsupportedAPIEndpointException"


EXCEPTIONS: dict[str, type[OrganizationsError]] = {
    "AWSOrganizationsNotInUseException": AWSOrganizationsNotInUseException,
    "AccessDeniedException": AccessDeniedException,
    "AccessDeniedForDependencyException": AccessDeniedForDependencyException,
    "AccountAlreadyClosedException": AccountAlreadyClosedException,
    "AccountAlreadyRegisteredException": AccountAlreadyRegisteredException,
    "AccountNotFoundException": AccountNotFoundException,
    "AccountNotRegisteredException": AccountNotRegisteredException,
    "AccountOwnerNotVerifiedException": AccountOwnerNotVerifiedException,
    "AlreadyInOrganizationException": AlreadyInOrganizationException,
    "ChildNotFoundException": ChildNotFoundException,
    "ConcurrentModificationException": ConcurrentModificationException,
    "ConflictException": ConflictException,
    "ConstraintViolationException": ConstraintViolationException,
    "CreateAccountStatusNotFoundException": CreateAccountStatusNotFoundException,
    "DestinationParentNotFoundException": DestinationParentNotFoundException,
    "DuplicateAccountException": DuplicateAccountException,
    "DuplicateHandshakeException": DuplicateHandshakeException,
    "DuplicateOrganizationalUnitException": DuplicateOrganizationalUnitException,
    "DuplicatePolicyAttachmentException": DuplicatePolicyAttachmentException,
    "DuplicatePolicyException": DuplicatePolicyException,
    "EffectivePolicyNotFoundException": EffectivePolicyNotFoundException,
    "FinalizingOrganizationException": FinalizingOrganizationException,
    "HandshakeAlreadyInStateException": HandshakeAlreadyInStateException,
    "HandshakeConstraintViolationException": HandshakeConstraintViolationException,
    "HandshakeNotFoundException": HandshakeNotFoundException,
    "InvalidHandshakeTransitionException": InvalidHandshakeTransitionException,
    "InvalidInputException": InvalidInputException,
    "MalformedPolicyDocumentException": MalformedPolicyDocumentException,
    "MasterCannotLeaveOrganizationException": MasterCannotLeaveOrganizationException,
    "OrganizationNotEmptyException": OrganizationNotEmptyException,
    "OrganizationalUnitNotEmptyException": OrganizationalUnitNotEmptyException,
    "OrganizationalUnitNotFoundException": OrganizationalUnitNotFoundException,
    "ParentNotFoundException": ParentNotFoundException,
    "PolicyChangesInProgressException": PolicyChangesInProgressException,
    "PolicyInUseException": PolicyInUseException,
    "PolicyNotAttachedException": PolicyNotAttachedException,
    "PolicyNotFoundException": PolicyNotFoundException,
    "PolicyTypeAlreadyEnabledException": PolicyTypeAlreadyEnabledException,
    "PolicyTypeNotAvailableForOrganizationException": PolicyTypeNotAvailableForOrganizationException,
    "PolicyTypeNotEnabledException": PolicyTypeNotEnabledException,
    "ResourcePolicyNotFoundException": ResourcePolicyNotFoundException,
    "RootNotFoundException": RootNotFoundException,
    "ServiceException": ServiceException,
    "SourceParentNotFoundException": SourceParentNotFoundException,
    "TargetNotFoundException": TargetNotFoundException,
    "TooManyRequestsException": TooManyRequestsException,
    "UnsupportedAPIEndpointException": UnsupportedAPIEndpointException,
}
