# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class WorkMailError(Boto3Error):
    _SERVICE = "workmail"


class DirectoryInUseException(WorkMailError):
    """The directory is already in use by another WorkMail organization in the same account
    and Region.
    """

    _ERROR_CODE = "DirectoryInUseException"


class DirectoryServiceAuthenticationFailedException(WorkMailError):
    """The directory service doesn't recognize the credentials supplied by WorkMail."""
    _ERROR_CODE = "DirectoryServiceAuthenticationFailedException"


class DirectoryUnavailableException(WorkMailError):
    """The directory is unavailable. It might be located in another Region or deleted."""
    _ERROR_CODE = "DirectoryUnavailableException"


class EmailAddressInUseException(WorkMailError):
    """The email address that you're trying to assign is already created for a different
    user, group, or resource.
    """

    _ERROR_CODE = "EmailAddressInUseException"


class EntityAlreadyRegisteredException(WorkMailError):
    """The user, group, or resource that you're trying to register is already registered."""
    _ERROR_CODE = "EntityAlreadyRegisteredException"


class EntityNotFoundException(WorkMailError):
    """The identifier supplied for the user, group, or resource does not exist in your
    organization.
    """

    _ERROR_CODE = "EntityNotFoundException"


class EntityStateException(WorkMailError):
    """You are performing an operation on a user, group, or resource that isn't in the
    expected state, such as trying to delete an active user.
    """

    _ERROR_CODE = "EntityStateException"


class InvalidConfigurationException(WorkMailError):
    """The configuration for a resource isn't valid. A resource must either be able to
    auto-respond to requests or have at least one delegate associated that can do so on
    its behalf.
    """

    _ERROR_CODE = "InvalidConfigurationException"


class InvalidCustomSesConfigurationException(WorkMailError):
    """You SES configuration has customizations that WorkMail cannot save. The error
    message lists the invalid setting. For examples of invalid settings, refer to
    CreateReceiptRule.
    """

    _ERROR_CODE = "InvalidCustomSesConfigurationException"


class InvalidParameterException(WorkMailError):
    """One or more of the input parameters don't match the service's restrictions."""
    _ERROR_CODE = "InvalidParameterException"


class InvalidPasswordException(WorkMailError):
    """The supplied password doesn't match the minimum security constraints, such as length
    or use of special characters.
    """

    _ERROR_CODE = "InvalidPasswordException"


class LimitExceededException(WorkMailError):
    """The request exceeds the limit of the resource."""
    _ERROR_CODE = "LimitExceededException"


class MailDomainInUseException(WorkMailError):
    """The domain you're trying to change is in use by another user or organization in your
    account. See the error message for details.
    """

    _ERROR_CODE = "MailDomainInUseException"


class MailDomainNotFoundException(WorkMailError):
    """The domain specified is not found in your organization."""
    _ERROR_CODE = "MailDomainNotFoundException"


class MailDomainStateException(WorkMailError):
    """After a domain has been added to the organization, it must be verified. The domain
    is not yet verified.
    """

    _ERROR_CODE = "MailDomainStateException"


class NameAvailabilityException(WorkMailError):
    """The user, group, or resource name isn't unique in WorkMail."""
    _ERROR_CODE = "NameAvailabilityException"


class OrganizationNotFoundException(WorkMailError):
    """An operation received a valid organization identifier that either doesn't belong or
    exist in the system.
    """

    _ERROR_CODE = "OrganizationNotFoundException"


class OrganizationStateException(WorkMailError):
    """The organization must have a valid state to perform certain operations on the
    organization or its members.
    """

    _ERROR_CODE = "OrganizationStateException"


class ReservedNameException(WorkMailError):
    """This user, group, or resource name is not allowed in WorkMail."""
    _ERROR_CODE = "ReservedNameException"


class ResourceNotFoundException(WorkMailError):
    """The resource cannot be found."""
    _ERROR_CODE = "ResourceNotFoundException"


class TooManyTagsException(WorkMailError):
    """The resource can have up to 50 user-applied tags."""
    _ERROR_CODE = "TooManyTagsException"


class UnsupportedOperationException(WorkMailError):
    """You can't perform a write operation against a read-only directory."""
    _ERROR_CODE = "UnsupportedOperationException"


EXCEPTIONS: dict[str, type[WorkMailError]] = {
    "DirectoryInUseException": DirectoryInUseException,
    "DirectoryServiceAuthenticationFailedException": DirectoryServiceAuthenticationFailedException,
    "DirectoryUnavailableException": DirectoryUnavailableException,
    "EmailAddressInUseException": EmailAddressInUseException,
    "EntityAlreadyRegisteredException": EntityAlreadyRegisteredException,
    "EntityNotFoundException": EntityNotFoundException,
    "EntityStateException": EntityStateException,
    "InvalidConfigurationException": InvalidConfigurationException,
    "InvalidCustomSesConfigurationException": InvalidCustomSesConfigurationException,
    "InvalidParameterException": InvalidParameterException,
    "InvalidPasswordException": InvalidPasswordException,
    "LimitExceededException": LimitExceededException,
    "MailDomainInUseException": MailDomainInUseException,
    "MailDomainNotFoundException": MailDomainNotFoundException,
    "MailDomainStateException": MailDomainStateException,
    "NameAvailabilityException": NameAvailabilityException,
    "OrganizationNotFoundException": OrganizationNotFoundException,
    "OrganizationStateException": OrganizationStateException,
    "ReservedNameException": ReservedNameException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "TooManyTagsException": TooManyTagsException,
    "UnsupportedOperationException": UnsupportedOperationException,
}
