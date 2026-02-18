# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class AlexaForBusinessError(Boto3Error):
    _SERVICE = "alexaforbusiness"


class AlreadyExistsException(AlexaForBusinessError):
    """The resource being created already exists."""
    _ERROR_CODE = "AlreadyExistsException"


class ConcurrentModificationException(AlexaForBusinessError):
    """There is a concurrent modification of resources."""
    _ERROR_CODE = "ConcurrentModificationException"


class DeviceNotRegisteredException(AlexaForBusinessError):
    """The request failed because this device is no longer registered and therefore no
    longer managed by this account.
    """

    _ERROR_CODE = "DeviceNotRegisteredException"


class InvalidCertificateAuthorityException(AlexaForBusinessError):
    """The Certificate Authority can't issue or revoke a certificate."""
    _ERROR_CODE = "InvalidCertificateAuthorityException"


class InvalidDeviceException(AlexaForBusinessError):
    """The device is in an invalid state."""
    _ERROR_CODE = "InvalidDeviceException"


class InvalidSecretsManagerResourceException(AlexaForBusinessError):
    """A password in SecretsManager is in an invalid state."""
    _ERROR_CODE = "InvalidSecretsManagerResourceException"


class InvalidServiceLinkedRoleStateException(AlexaForBusinessError):
    """The service linked role is locked for deletion."""
    _ERROR_CODE = "InvalidServiceLinkedRoleStateException"


class InvalidUserStatusException(AlexaForBusinessError):
    """The attempt to update a user is invalid due to the user's current status."""
    _ERROR_CODE = "InvalidUserStatusException"


class LimitExceededException(AlexaForBusinessError):
    """You are performing an action that would put you beyond your account's limits."""
    _ERROR_CODE = "LimitExceededException"


class NameInUseException(AlexaForBusinessError):
    """The name sent in the request is already in use."""
    _ERROR_CODE = "NameInUseException"


class NotFoundException(AlexaForBusinessError):
    """The resource is not found."""
    _ERROR_CODE = "NotFoundException"


class ResourceAssociatedException(AlexaForBusinessError):
    """Another resource is associated with the resource in the request."""
    _ERROR_CODE = "ResourceAssociatedException"


class ResourceInUseException(AlexaForBusinessError):
    """The resource in the request is already in use."""
    _ERROR_CODE = "ResourceInUseException"

    @property
    def client_request_token(self) -> str | None:
        return self.response.get("ClientRequestToken")


class SkillNotLinkedException(AlexaForBusinessError):
    """The skill must be linked to a third-party account."""
    _ERROR_CODE = "SkillNotLinkedException"


class UnauthorizedException(AlexaForBusinessError):
    """The caller has no permissions to operate on the resource involved in the API call."""
    _ERROR_CODE = "UnauthorizedException"


EXCEPTIONS: dict[str, type[AlexaForBusinessError]] = {
    "AlreadyExistsException": AlreadyExistsException,
    "ConcurrentModificationException": ConcurrentModificationException,
    "DeviceNotRegisteredException": DeviceNotRegisteredException,
    "InvalidCertificateAuthorityException": InvalidCertificateAuthorityException,
    "InvalidDeviceException": InvalidDeviceException,
    "InvalidSecretsManagerResourceException": InvalidSecretsManagerResourceException,
    "InvalidServiceLinkedRoleStateException": InvalidServiceLinkedRoleStateException,
    "InvalidUserStatusException": InvalidUserStatusException,
    "LimitExceededException": LimitExceededException,
    "NameInUseException": NameInUseException,
    "NotFoundException": NotFoundException,
    "ResourceAssociatedException": ResourceAssociatedException,
    "ResourceInUseException": ResourceInUseException,
    "SkillNotLinkedException": SkillNotLinkedException,
    "UnauthorizedException": UnauthorizedException,
}
