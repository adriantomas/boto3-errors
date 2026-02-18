# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class WorkSpacesError(Boto3Error):
    _SERVICE = "workspaces"


class AccessDeniedException(WorkSpacesError):
    """The user is not authorized to access a resource."""
    _ERROR_CODE = "AccessDeniedException"


class ApplicationNotSupportedException(WorkSpacesError):
    """The specified application is not supported."""
    _ERROR_CODE = "ApplicationNotSupportedException"


class ComputeNotCompatibleException(WorkSpacesError):
    """The compute type of the WorkSpace is not compatible with the application."""
    _ERROR_CODE = "ComputeNotCompatibleException"


class IncompatibleApplicationsException(WorkSpacesError):
    """The specified application is not compatible with the resource."""
    _ERROR_CODE = "IncompatibleApplicationsException"


class InvalidParameterValuesException(WorkSpacesError):
    """One or more parameter values are not valid."""
    _ERROR_CODE = "InvalidParameterValuesException"


class InvalidResourceStateException(WorkSpacesError):
    """The state of the resource is not valid for this operation."""
    _ERROR_CODE = "InvalidResourceStateException"


class OperatingSystemNotCompatibleException(WorkSpacesError):
    """The operating system of the WorkSpace is not compatible with the application."""
    _ERROR_CODE = "OperatingSystemNotCompatibleException"


class OperationInProgressException(WorkSpacesError):
    """The properties of this WorkSpace are currently being modified. Try again in a
    moment.
    """

    _ERROR_CODE = "OperationInProgressException"


class OperationNotSupportedException(WorkSpacesError):
    """This operation is not supported."""
    _ERROR_CODE = "OperationNotSupportedException"

    @property
    def reason(self) -> str | None:
        """The exception error reason."""
        return self.response.get("reason")


class ResourceAlreadyExistsException(WorkSpacesError):
    """The specified resource already exists."""
    _ERROR_CODE = "ResourceAlreadyExistsException"


class ResourceAssociatedException(WorkSpacesError):
    """The resource is associated with a directory."""
    _ERROR_CODE = "ResourceAssociatedException"


class ResourceCreationFailedException(WorkSpacesError):
    """The resource could not be created."""
    _ERROR_CODE = "ResourceCreationFailedException"


class ResourceInUseException(WorkSpacesError):
    """The specified resource is currently in use."""
    _ERROR_CODE = "ResourceInUseException"

    @property
    def resource_id(self) -> str | None:
        """The ID of the resource that is in use."""
        return self.response.get("ResourceId")


class ResourceLimitExceededException(WorkSpacesError):
    """Your resource limits have been exceeded."""
    _ERROR_CODE = "ResourceLimitExceededException"


class ResourceNotFoundException(WorkSpacesError):
    """The resource could not be found."""
    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def resource_id(self) -> str | None:
        """The ID of the resource that could not be found."""
        return self.response.get("ResourceId")


class ResourceUnavailableException(WorkSpacesError):
    """The specified resource is not available."""
    _ERROR_CODE = "ResourceUnavailableException"

    @property
    def resource_id(self) -> str | None:
        """The identifier of the resource that is not available."""
        return self.response.get("ResourceId")


class UnsupportedNetworkConfigurationException(WorkSpacesError):
    """The configuration of this network is not supported for this operation, or your
    network configuration conflicts with the Amazon WorkSpaces management network IP
    range. For more information, see Configure a VPC for Amazon WorkSpaces.
    """

    _ERROR_CODE = "UnsupportedNetworkConfigurationException"


class UnsupportedWorkspaceConfigurationException(WorkSpacesError):
    """The configuration of this WorkSpace is not supported for this operation. For more
    information, see Required Configuration and Service Components for WorkSpaces .
    """

    _ERROR_CODE = "UnsupportedWorkspaceConfigurationException"


class WorkspacesDefaultRoleNotFoundException(WorkSpacesError):
    """The workspaces_DefaultRole role could not be found. If this is the first time you
    are registering a directory, you will need to create the workspaces_DefaultRole role
    before you can register a directory. For more information, see Creating the
    workspaces_DefaultRole Role.
    """

    _ERROR_CODE = "WorkspacesDefaultRoleNotFoundException"


EXCEPTIONS: dict[str, type[WorkSpacesError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ApplicationNotSupportedException": ApplicationNotSupportedException,
    "ComputeNotCompatibleException": ComputeNotCompatibleException,
    "IncompatibleApplicationsException": IncompatibleApplicationsException,
    "InvalidParameterValuesException": InvalidParameterValuesException,
    "InvalidResourceStateException": InvalidResourceStateException,
    "OperatingSystemNotCompatibleException": OperatingSystemNotCompatibleException,
    "OperationInProgressException": OperationInProgressException,
    "OperationNotSupportedException": OperationNotSupportedException,
    "ResourceAlreadyExistsException": ResourceAlreadyExistsException,
    "ResourceAssociatedException": ResourceAssociatedException,
    "ResourceCreationFailedException": ResourceCreationFailedException,
    "ResourceInUseException": ResourceInUseException,
    "ResourceLimitExceededException": ResourceLimitExceededException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ResourceUnavailableException": ResourceUnavailableException,
    "UnsupportedNetworkConfigurationException": UnsupportedNetworkConfigurationException,
    "UnsupportedWorkspaceConfigurationException": UnsupportedWorkspaceConfigurationException,
    "WorkspacesDefaultRoleNotFoundException": WorkspacesDefaultRoleNotFoundException,
}
