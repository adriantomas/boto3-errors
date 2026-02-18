# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class EKSError(Boto3Error):
    _SERVICE = "eks"


class AccessDeniedException(EKSError):
    """You don't have permissions to perform the requested operation. The IAM principal
    making the request must have at least one IAM permissions policy attached that
    grants the required permissions. For more information, see Access management in the
    IAM User Guide.
    """

    _ERROR_CODE = "AccessDeniedException"


class BadRequestException(EKSError):
    """This exception is thrown if the request contains a semantic error. The precise
    meaning will depend on the API, and will be documented in the error message.
    """

    _ERROR_CODE = "BadRequestException"


class ClientException(EKSError):
    """These errors are usually caused by a client action. Actions can include using an
    action or resource on behalf of an IAM principal that doesn't have permissions to
    use the action or resource or specifying an identifier that is not valid.
    """

    _ERROR_CODE = "ClientException"

    @property
    def addon_name(self) -> str | None:
        """The Amazon EKS add-on name associated with the exception."""
        return self.response.get("addonName")

    @property
    def cluster_name(self) -> str | None:
        """The Amazon EKS cluster associated with the exception."""
        return self.response.get("clusterName")

    @property
    def nodegroup_name(self) -> str | None:
        """The Amazon EKS managed node group associated with the exception."""
        return self.response.get("nodegroupName")

    @property
    def subscription_id(self) -> str | None:
        """The Amazon EKS subscription ID with the exception."""
        return self.response.get("subscriptionId")


class InvalidParameterException(EKSError):
    """The specified parameter is invalid. Review the available parameters for the API
    request.
    """

    _ERROR_CODE = "InvalidParameterException"

    @property
    def addon_name(self) -> str | None:
        """The specified parameter for the add-on name is invalid. Review the available
        parameters for the API request
        """
        return self.response.get("addonName")

    @property
    def cluster_name(self) -> str | None:
        """The Amazon EKS cluster associated with the exception."""
        return self.response.get("clusterName")

    @property
    def fargate_profile_name(self) -> str | None:
        """The Fargate profile associated with the exception."""
        return self.response.get("fargateProfileName")

    @property
    def nodegroup_name(self) -> str | None:
        """The Amazon EKS managed node group associated with the exception."""
        return self.response.get("nodegroupName")

    @property
    def subscription_id(self) -> str | None:
        """The Amazon EKS subscription ID with the exception."""
        return self.response.get("subscriptionId")


class InvalidRequestException(EKSError):
    """The request is invalid given the state of the cluster. Check the state of the
    cluster and the associated operations.
    """

    _ERROR_CODE = "InvalidRequestException"

    @property
    def addon_name(self) -> str | None:
        """The request is invalid given the state of the add-on name. Check the state of
        the cluster and the associated operations.
        """
        return self.response.get("addonName")

    @property
    def cluster_name(self) -> str | None:
        """The Amazon EKS cluster associated with the exception."""
        return self.response.get("clusterName")

    @property
    def nodegroup_name(self) -> str | None:
        """The Amazon EKS managed node group associated with the exception."""
        return self.response.get("nodegroupName")

    @property
    def subscription_id(self) -> str | None:
        """The Amazon EKS subscription ID with the exception."""
        return self.response.get("subscriptionId")


class InvalidStateException(EKSError):
    """Amazon EKS detected upgrade readiness issues. Call the `ListInsights` API to view
    detected upgrade blocking issues. Pass the `force` flag when updating to override
    upgrade readiness errors.
    """

    _ERROR_CODE = "InvalidStateException"

    @property
    def cluster_name(self) -> str | None:
        """The Amazon EKS cluster associated with the exception."""
        return self.response.get("clusterName")


class NotFoundException(EKSError):
    """A service resource associated with the request could not be found. Clients should
    not retry such requests.
    """

    _ERROR_CODE = "NotFoundException"


class ResourceInUseException(EKSError):
    """The specified resource is in use."""
    _ERROR_CODE = "ResourceInUseException"

    @property
    def addon_name(self) -> str | None:
        """The specified add-on name is in use."""
        return self.response.get("addonName")

    @property
    def cluster_name(self) -> str | None:
        """The Amazon EKS cluster associated with the exception."""
        return self.response.get("clusterName")

    @property
    def nodegroup_name(self) -> str | None:
        """The Amazon EKS managed node group associated with the exception."""
        return self.response.get("nodegroupName")


class ResourceLimitExceededException(EKSError):
    """You have encountered a service limit on the specified resource."""
    _ERROR_CODE = "ResourceLimitExceededException"

    @property
    def cluster_name(self) -> str | None:
        """The Amazon EKS cluster associated with the exception."""
        return self.response.get("clusterName")

    @property
    def nodegroup_name(self) -> str | None:
        """The Amazon EKS managed node group associated with the exception."""
        return self.response.get("nodegroupName")

    @property
    def subscription_id(self) -> str | None:
        """The Amazon EKS subscription ID with the exception."""
        return self.response.get("subscriptionId")


class ResourceNotFoundException(EKSError):
    """The specified resource could not be found. You can view your available clusters with
    `ListClusters`. You can view your available managed node groups with
    `ListNodegroups`. Amazon EKS clusters and node groups are Amazon Web Services Region
    specific.
    """

    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def addon_name(self) -> str | None:
        """The Amazon EKS add-on name associated with the exception."""
        return self.response.get("addonName")

    @property
    def cluster_name(self) -> str | None:
        """The Amazon EKS cluster associated with the exception."""
        return self.response.get("clusterName")

    @property
    def fargate_profile_name(self) -> str | None:
        """The Fargate profile associated with the exception."""
        return self.response.get("fargateProfileName")

    @property
    def nodegroup_name(self) -> str | None:
        """The Amazon EKS managed node group associated with the exception."""
        return self.response.get("nodegroupName")

    @property
    def subscription_id(self) -> str | None:
        """The Amazon EKS subscription ID with the exception."""
        return self.response.get("subscriptionId")


class ResourcePropagationDelayException(EKSError):
    """Required resources (such as service-linked roles) were created and are still
    propagating. Retry later.
    """

    _ERROR_CODE = "ResourcePropagationDelayException"


class ServerException(EKSError):
    """These errors are usually caused by a server-side issue."""
    _ERROR_CODE = "ServerException"

    @property
    def addon_name(self) -> str | None:
        """The Amazon EKS add-on name associated with the exception."""
        return self.response.get("addonName")

    @property
    def cluster_name(self) -> str | None:
        """The Amazon EKS cluster associated with the exception."""
        return self.response.get("clusterName")

    @property
    def nodegroup_name(self) -> str | None:
        """The Amazon EKS managed node group associated with the exception."""
        return self.response.get("nodegroupName")

    @property
    def subscription_id(self) -> str | None:
        """The Amazon EKS subscription ID with the exception."""
        return self.response.get("subscriptionId")


class ServiceUnavailableException(EKSError):
    """The service is unavailable. Back off and retry the operation."""
    _ERROR_CODE = "ServiceUnavailableException"


class ThrottlingException(EKSError):
    """The request or operation couldn't be performed because a service is throttling
    requests.
    """

    _ERROR_CODE = "ThrottlingException"

    @property
    def cluster_name(self) -> str | None:
        """The Amazon EKS cluster associated with the exception."""
        return self.response.get("clusterName")


class UnsupportedAvailabilityZoneException(EKSError):
    """At least one of your specified cluster subnets is in an Availability Zone that does
    not support Amazon EKS. The exception output specifies the supported Availability
    Zones for your account, from which you can choose subnets for your cluster.
    """

    _ERROR_CODE = "UnsupportedAvailabilityZoneException"

    @property
    def cluster_name(self) -> str | None:
        """The Amazon EKS cluster associated with the exception."""
        return self.response.get("clusterName")

    @property
    def nodegroup_name(self) -> str | None:
        """The Amazon EKS managed node group associated with the exception."""
        return self.response.get("nodegroupName")

    @property
    def valid_zones(self) -> list[Any] | None:
        """The supported Availability Zones for your account. Choose subnets in these
        Availability Zones for your cluster.
        """
        return self.response.get("validZones")


EXCEPTIONS: dict[str, type[EKSError]] = {
    "AccessDeniedException": AccessDeniedException,
    "BadRequestException": BadRequestException,
    "ClientException": ClientException,
    "InvalidParameterException": InvalidParameterException,
    "InvalidRequestException": InvalidRequestException,
    "InvalidStateException": InvalidStateException,
    "NotFoundException": NotFoundException,
    "ResourceInUseException": ResourceInUseException,
    "ResourceLimitExceededException": ResourceLimitExceededException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ResourcePropagationDelayException": ResourcePropagationDelayException,
    "ServerException": ServerException,
    "ServiceUnavailableException": ServiceUnavailableException,
    "ThrottlingException": ThrottlingException,
    "UnsupportedAvailabilityZoneException": UnsupportedAvailabilityZoneException,
}
