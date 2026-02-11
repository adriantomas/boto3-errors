# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class DirectoryServiceError(Boto3Error):
    _SERVICE = "ds"


class ADAssessmentLimitExceededException(DirectoryServiceError):
    """A directory assessment is automatically created when you create a hybrid directory.
    There are two types of assessments: `CUSTOMER` and `SYSTEM`. Your Amazon Web
    Services account has a limit of 100 `CUSTOMER` directory assessments.

    If you attempt to create a hybrid directory; and you already have 100 `CUSTOMER`
    directory assessments;, you will encounter an error. Delete assessments to free up
    capacity before trying again.

    You can request an increase to your `CUSTOMER` directory assessment quota by
    contacting customer support or delete existing CUSTOMER directory assessments; to
    free up capacity.
    """

    _ERROR_CODE = "ADAssessmentLimitExceededException"

    @property
    def request_id(self) -> str | None:
        return self.response.get("RequestId")


class AccessDeniedException(DirectoryServiceError):
    """You do not have sufficient access to perform this action."""
    _ERROR_CODE = "AccessDeniedException"

    @property
    def request_id(self) -> str | None:
        return self.response.get("RequestId")


class AuthenticationFailedException(DirectoryServiceError):
    """An authentication error occurred."""
    _ERROR_CODE = "AuthenticationFailedException"

    @property
    def request_id(self) -> str | None:
        """The identifier of the request that caused the exception."""
        return self.response.get("RequestId")


class CertificateAlreadyExistsException(DirectoryServiceError):
    """The certificate has already been registered into the system."""
    _ERROR_CODE = "CertificateAlreadyExistsException"

    @property
    def request_id(self) -> str | None:
        return self.response.get("RequestId")


class CertificateDoesNotExistException(DirectoryServiceError):
    """The certificate is not present in the system for describe or deregister activities."""
    _ERROR_CODE = "CertificateDoesNotExistException"

    @property
    def request_id(self) -> str | None:
        return self.response.get("RequestId")


class CertificateInUseException(DirectoryServiceError):
    """The certificate is being used for the LDAP security connection and cannot be removed
    without disabling LDAP security.
    """

    _ERROR_CODE = "CertificateInUseException"

    @property
    def request_id(self) -> str | None:
        return self.response.get("RequestId")


class CertificateLimitExceededException(DirectoryServiceError):
    """The certificate could not be added because the certificate limit has been reached."""
    _ERROR_CODE = "CertificateLimitExceededException"

    @property
    def request_id(self) -> str | None:
        return self.response.get("RequestId")


class ClientException(DirectoryServiceError):
    """A client exception has occurred."""
    _ERROR_CODE = "ClientException"

    @property
    def request_id(self) -> str | None:
        return self.response.get("RequestId")


class DirectoryAlreadyInRegionException(DirectoryServiceError):
    """The Region you specified is the same Region where the Managed Microsoft AD directory
    was created. Specify a different Region and try again.
    """

    _ERROR_CODE = "DirectoryAlreadyInRegionException"

    @property
    def request_id(self) -> str | None:
        return self.response.get("RequestId")


class DirectoryAlreadySharedException(DirectoryServiceError):
    """The specified directory has already been shared with this Amazon Web Services
    account.
    """

    _ERROR_CODE = "DirectoryAlreadySharedException"

    @property
    def request_id(self) -> str | None:
        return self.response.get("RequestId")


class DirectoryDoesNotExistException(DirectoryServiceError):
    """The specified directory does not exist in the system."""
    _ERROR_CODE = "DirectoryDoesNotExistException"

    @property
    def request_id(self) -> str | None:
        return self.response.get("RequestId")


class DirectoryInDesiredStateException(DirectoryServiceError):
    """The directory is already updated to desired update type settings."""
    _ERROR_CODE = "DirectoryInDesiredStateException"

    @property
    def request_id(self) -> str | None:
        return self.response.get("RequestId")


class DirectoryLimitExceededException(DirectoryServiceError):
    """The maximum number of directories in the region has been reached. You can use the
    GetDirectoryLimits operation to determine your directory limits in the region.
    """

    _ERROR_CODE = "DirectoryLimitExceededException"

    @property
    def request_id(self) -> str | None:
        return self.response.get("RequestId")


class DirectoryNotSharedException(DirectoryServiceError):
    """The specified directory has not been shared with this Amazon Web Services account."""
    _ERROR_CODE = "DirectoryNotSharedException"

    @property
    def request_id(self) -> str | None:
        return self.response.get("RequestId")


class DirectoryUnavailableException(DirectoryServiceError):
    """The specified directory is unavailable."""
    _ERROR_CODE = "DirectoryUnavailableException"

    @property
    def request_id(self) -> str | None:
        return self.response.get("RequestId")


class DisableAlreadyInProgressException(DirectoryServiceError):
    """A disable operation for CA enrollment policy is already in progress for this
    directory.
    """

    _ERROR_CODE = "DisableAlreadyInProgressException"

    @property
    def request_id(self) -> str | None:
        return self.response.get("RequestId")


class DomainControllerLimitExceededException(DirectoryServiceError):
    """The maximum allowed number of domain controllers per directory was exceeded. The
    default limit per directory is 20 domain controllers.
    """

    _ERROR_CODE = "DomainControllerLimitExceededException"

    @property
    def request_id(self) -> str | None:
        return self.response.get("RequestId")


class EnableAlreadyInProgressException(DirectoryServiceError):
    """An enable operation for CA enrollment policy is already in progress for this
    directory.
    """

    _ERROR_CODE = "EnableAlreadyInProgressException"

    @property
    def request_id(self) -> str | None:
        return self.response.get("RequestId")


class EntityAlreadyExistsException(DirectoryServiceError):
    """The specified entity already exists."""
    _ERROR_CODE = "EntityAlreadyExistsException"

    @property
    def request_id(self) -> str | None:
        return self.response.get("RequestId")


class EntityDoesNotExistException(DirectoryServiceError):
    """The specified entity could not be found."""
    _ERROR_CODE = "EntityDoesNotExistException"

    @property
    def request_id(self) -> str | None:
        return self.response.get("RequestId")


class IncompatibleSettingsException(DirectoryServiceError):
    """The specified directory setting is not compatible with other settings."""
    _ERROR_CODE = "IncompatibleSettingsException"

    @property
    def request_id(self) -> str | None:
        return self.response.get("RequestId")


class InsufficientPermissionsException(DirectoryServiceError):
    """The account does not have sufficient permission to perform the operation."""
    _ERROR_CODE = "InsufficientPermissionsException"

    @property
    def request_id(self) -> str | None:
        return self.response.get("RequestId")


class InvalidCertificateException(DirectoryServiceError):
    """The certificate PEM that was provided has incorrect encoding."""
    _ERROR_CODE = "InvalidCertificateException"

    @property
    def request_id(self) -> str | None:
        return self.response.get("RequestId")


class InvalidClientAuthStatusException(DirectoryServiceError):
    """Client authentication is already enabled."""
    _ERROR_CODE = "InvalidClientAuthStatusException"

    @property
    def request_id(self) -> str | None:
        return self.response.get("RequestId")


class InvalidLDAPSStatusException(DirectoryServiceError):
    """The LDAP activities could not be performed because they are limited by the LDAPS
    status.
    """

    _ERROR_CODE = "InvalidLDAPSStatusException"

    @property
    def request_id(self) -> str | None:
        return self.response.get("RequestId")


class InvalidNextTokenException(DirectoryServiceError):
    """The `NextToken` value is not valid."""
    _ERROR_CODE = "InvalidNextTokenException"

    @property
    def request_id(self) -> str | None:
        return self.response.get("RequestId")


class InvalidParameterException(DirectoryServiceError):
    """One or more parameters are not valid."""
    _ERROR_CODE = "InvalidParameterException"

    @property
    def request_id(self) -> str | None:
        return self.response.get("RequestId")


class InvalidPasswordException(DirectoryServiceError):
    """The new password provided by the user does not meet the password complexity
    requirements defined in your directory.
    """

    _ERROR_CODE = "InvalidPasswordException"

    @property
    def request_id(self) -> str | None:
        return self.response.get("RequestId")


class InvalidTargetException(DirectoryServiceError):
    """The specified shared target is not valid."""
    _ERROR_CODE = "InvalidTargetException"

    @property
    def request_id(self) -> str | None:
        return self.response.get("RequestId")


class IpRouteLimitExceededException(DirectoryServiceError):
    """The maximum allowed number of IP addresses was exceeded. The default limit is 100 IP
    address blocks.
    """

    _ERROR_CODE = "IpRouteLimitExceededException"

    @property
    def request_id(self) -> str | None:
        return self.response.get("RequestId")


class NoAvailableCertificateException(DirectoryServiceError):
    """Client authentication setup could not be completed because at least one valid
    certificate must be registered in the system.
    """

    _ERROR_CODE = "NoAvailableCertificateException"

    @property
    def request_id(self) -> str | None:
        return self.response.get("RequestId")


class OrganizationsException(DirectoryServiceError):
    """Exception encountered while trying to access your Amazon Web Services organization."""
    _ERROR_CODE = "OrganizationsException"

    @property
    def request_id(self) -> str | None:
        return self.response.get("RequestId")


class RegionLimitExceededException(DirectoryServiceError):
    """You have reached the limit for maximum number of simultaneous Region replications
    per directory.
    """

    _ERROR_CODE = "RegionLimitExceededException"

    @property
    def request_id(self) -> str | None:
        return self.response.get("RequestId")


class ServiceException(DirectoryServiceError):
    """An exception has occurred in Directory Service."""
    _ERROR_CODE = "ServiceException"

    @property
    def request_id(self) -> str | None:
        return self.response.get("RequestId")


class ShareLimitExceededException(DirectoryServiceError):
    """The maximum number of Amazon Web Services accounts that you can share with this
    directory has been reached.
    """

    _ERROR_CODE = "ShareLimitExceededException"

    @property
    def request_id(self) -> str | None:
        return self.response.get("RequestId")


class SnapshotLimitExceededException(DirectoryServiceError):
    """The maximum number of manual snapshots for the directory has been reached. You can
    use the GetSnapshotLimits operation to determine the snapshot limits for a
    directory.
    """

    _ERROR_CODE = "SnapshotLimitExceededException"

    @property
    def request_id(self) -> str | None:
        return self.response.get("RequestId")


class TagLimitExceededException(DirectoryServiceError):
    """The maximum allowed number of tags was exceeded."""
    _ERROR_CODE = "TagLimitExceededException"

    @property
    def request_id(self) -> str | None:
        return self.response.get("RequestId")


class UnsupportedOperationException(DirectoryServiceError):
    """The operation is not supported."""
    _ERROR_CODE = "UnsupportedOperationException"

    @property
    def request_id(self) -> str | None:
        return self.response.get("RequestId")


class UnsupportedSettingsException(DirectoryServiceError):
    """The specified directory setting is not supported."""
    _ERROR_CODE = "UnsupportedSettingsException"

    @property
    def request_id(self) -> str | None:
        return self.response.get("RequestId")


class UserDoesNotExistException(DirectoryServiceError):
    """The user provided a username that does not exist in your directory."""
    _ERROR_CODE = "UserDoesNotExistException"

    @property
    def request_id(self) -> str | None:
        return self.response.get("RequestId")


EXCEPTIONS: dict[str, type[DirectoryServiceError]] = {
    "ADAssessmentLimitExceededException": ADAssessmentLimitExceededException,
    "AccessDeniedException": AccessDeniedException,
    "AuthenticationFailedException": AuthenticationFailedException,
    "CertificateAlreadyExistsException": CertificateAlreadyExistsException,
    "CertificateDoesNotExistException": CertificateDoesNotExistException,
    "CertificateInUseException": CertificateInUseException,
    "CertificateLimitExceededException": CertificateLimitExceededException,
    "ClientException": ClientException,
    "DirectoryAlreadyInRegionException": DirectoryAlreadyInRegionException,
    "DirectoryAlreadySharedException": DirectoryAlreadySharedException,
    "DirectoryDoesNotExistException": DirectoryDoesNotExistException,
    "DirectoryInDesiredStateException": DirectoryInDesiredStateException,
    "DirectoryLimitExceededException": DirectoryLimitExceededException,
    "DirectoryNotSharedException": DirectoryNotSharedException,
    "DirectoryUnavailableException": DirectoryUnavailableException,
    "DisableAlreadyInProgressException": DisableAlreadyInProgressException,
    "DomainControllerLimitExceededException": DomainControllerLimitExceededException,
    "EnableAlreadyInProgressException": EnableAlreadyInProgressException,
    "EntityAlreadyExistsException": EntityAlreadyExistsException,
    "EntityDoesNotExistException": EntityDoesNotExistException,
    "IncompatibleSettingsException": IncompatibleSettingsException,
    "InsufficientPermissionsException": InsufficientPermissionsException,
    "InvalidCertificateException": InvalidCertificateException,
    "InvalidClientAuthStatusException": InvalidClientAuthStatusException,
    "InvalidLDAPSStatusException": InvalidLDAPSStatusException,
    "InvalidNextTokenException": InvalidNextTokenException,
    "InvalidParameterException": InvalidParameterException,
    "InvalidPasswordException": InvalidPasswordException,
    "InvalidTargetException": InvalidTargetException,
    "IpRouteLimitExceededException": IpRouteLimitExceededException,
    "NoAvailableCertificateException": NoAvailableCertificateException,
    "OrganizationsException": OrganizationsException,
    "RegionLimitExceededException": RegionLimitExceededException,
    "ServiceException": ServiceException,
    "ShareLimitExceededException": ShareLimitExceededException,
    "SnapshotLimitExceededException": SnapshotLimitExceededException,
    "TagLimitExceededException": TagLimitExceededException,
    "UnsupportedOperationException": UnsupportedOperationException,
    "UnsupportedSettingsException": UnsupportedSettingsException,
    "UserDoesNotExistException": UserDoesNotExistException,
}
