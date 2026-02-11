# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class LightsailError(Boto3Error):
    _SERVICE = "lightsail"


class AccessDeniedException(LightsailError):
    """Lightsail throws this exception when the user cannot be authenticated or uses
    invalid credentials to access a resource.
    """

    _ERROR_CODE = "AccessDeniedException"

    @property
    def code(self) -> str | None:
        return self.response.get("code")

    @property
    def docs(self) -> str | None:
        return self.response.get("docs")

    @property
    def tip(self) -> str | None:
        return self.response.get("tip")


class AccountSetupInProgressException(LightsailError):
    """Lightsail throws this exception when an account is still in the setup in progress
    state.
    """

    _ERROR_CODE = "AccountSetupInProgressException"

    @property
    def code(self) -> str | None:
        return self.response.get("code")

    @property
    def docs(self) -> str | None:
        return self.response.get("docs")

    @property
    def tip(self) -> str | None:
        return self.response.get("tip")


class InvalidInputException(LightsailError):
    """Lightsail throws this exception when user input does not conform to the validation
    rules of an input field.

    Note:

    Domain and distribution APIs are only available in the N. Virginia (`us-east-1`)
    Amazon Web Services Region. Please set your Amazon Web Services Region configuration
    to `us-east-1` to create, view, or edit these resources.
    """

    _ERROR_CODE = "InvalidInputException"

    @property
    def code(self) -> str | None:
        return self.response.get("code")

    @property
    def docs(self) -> str | None:
        return self.response.get("docs")

    @property
    def tip(self) -> str | None:
        return self.response.get("tip")


class NotFoundException(LightsailError):
    """Lightsail throws this exception when it cannot find a resource."""
    _ERROR_CODE = "NotFoundException"

    @property
    def code(self) -> str | None:
        return self.response.get("code")

    @property
    def docs(self) -> str | None:
        return self.response.get("docs")

    @property
    def tip(self) -> str | None:
        return self.response.get("tip")


class OperationFailureException(LightsailError):
    """Lightsail throws this exception when an operation fails to execute."""
    _ERROR_CODE = "OperationFailureException"

    @property
    def code(self) -> str | None:
        return self.response.get("code")

    @property
    def docs(self) -> str | None:
        return self.response.get("docs")

    @property
    def tip(self) -> str | None:
        return self.response.get("tip")


class RegionSetupInProgressException(LightsailError):
    """Lightsail throws this exception when an operation is performed on resources in an
    opt-in Region that is currently being set up.
    """

    _ERROR_CODE = "RegionSetupInProgressException"

    @property
    def code(self) -> str | None:
        return self.response.get("code")

    @property
    def docs(self) -> str | None:
        """Regions and Availability Zones for Lightsail"""
        return self.response.get("docs")

    @property
    def tip(self) -> str | None:
        """Opt-in Regions typically take a few minutes to finish setting up before you can
        work with them. Wait a few minutes and try again.
        """
        return self.response.get("tip")


class ServiceException(LightsailError):
    """A general service exception."""
    _ERROR_CODE = "ServiceException"

    @property
    def code(self) -> str | None:
        return self.response.get("code")

    @property
    def docs(self) -> str | None:
        return self.response.get("docs")

    @property
    def tip(self) -> str | None:
        return self.response.get("tip")


class UnauthenticatedException(LightsailError):
    """Lightsail throws this exception when the user has not been authenticated."""
    _ERROR_CODE = "UnauthenticatedException"

    @property
    def code(self) -> str | None:
        return self.response.get("code")

    @property
    def docs(self) -> str | None:
        return self.response.get("docs")

    @property
    def tip(self) -> str | None:
        return self.response.get("tip")


EXCEPTIONS: dict[str, type[LightsailError]] = {
    "AccessDeniedException": AccessDeniedException,
    "AccountSetupInProgressException": AccountSetupInProgressException,
    "InvalidInputException": InvalidInputException,
    "NotFoundException": NotFoundException,
    "OperationFailureException": OperationFailureException,
    "RegionSetupInProgressException": RegionSetupInProgressException,
    "ServiceException": ServiceException,
    "UnauthenticatedException": UnauthenticatedException,
}
