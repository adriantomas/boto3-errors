# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class ECSError(Boto3Error):
    _SERVICE = "ecs"


class AccessDeniedException(ECSError):
    """You don't have authorization to perform the requested action."""
    _ERROR_CODE = "AccessDeniedException"


class AttributeLimitExceededException(ECSError):
    """You can apply up to 10 custom attributes for each resource. You can view the
    attributes of a resource with ListAttributes. You can remove existing attributes on
    a resource with DeleteAttributes.
    """

    _ERROR_CODE = "AttributeLimitExceededException"


class BlockedException(ECSError):
    """Your Amazon Web Services account was blocked. For more information, contact Amazon
    Web Services Support.
    """

    _ERROR_CODE = "BlockedException"


class ClientException(ECSError):
    """These errors are usually caused by a client action. This client action might be
    using an action or resource on behalf of a user that doesn't have permissions to use
    the action or resource. Or, it might be specifying an identifier that isn't valid.
    """

    _ERROR_CODE = "ClientException"


class ClusterContainsCapacityProviderException(ECSError):
    """The cluster contains one or more capacity providers that prevent the requested
    operation. This exception occurs when you try to delete a cluster that still has
    active capacity providers, including Amazon ECS Managed Instances capacity
    providers. You must first delete all capacity providers from the cluster before you
    can delete the cluster itself.
    """

    _ERROR_CODE = "ClusterContainsCapacityProviderException"


class ClusterContainsContainerInstancesException(ECSError):
    """You can't delete a cluster that has registered container instances. First,
    deregister the container instances before you can delete the cluster. For more
    information, see DeregisterContainerInstance.
    """

    _ERROR_CODE = "ClusterContainsContainerInstancesException"


class ClusterContainsServicesException(ECSError):
    """You can't delete a cluster that contains services. First, update the service to
    reduce its desired task count to 0, and then delete the service. For more
    information, see UpdateService and DeleteService.
    """

    _ERROR_CODE = "ClusterContainsServicesException"


class ClusterContainsTasksException(ECSError):
    """You can't delete a cluster that has active tasks."""
    _ERROR_CODE = "ClusterContainsTasksException"


class ClusterNotFoundException(ECSError):
    """The specified cluster wasn't found. You can view your available clusters with
    ListClusters. Amazon ECS clusters are Region specific.
    """

    _ERROR_CODE = "ClusterNotFoundException"


class ConflictException(ECSError):
    """The request could not be processed because of conflict in the current state of the
    resource.
    """

    _ERROR_CODE = "ConflictException"

    @property
    def resource_ids(self) -> list[Any] | None:
        """The existing task ARNs which are already associated with the `clientToken`."""
        return self.response.get("resourceIds")


class InvalidParameterException(ECSError):
    """The specified parameter isn't valid. Review the available parameters for the API
    request.

    For more information about service event errors, see Amazon ECS service event
    messages.
    """

    _ERROR_CODE = "InvalidParameterException"


class LimitExceededException(ECSError):
    """The limit for the resource was exceeded."""
    _ERROR_CODE = "LimitExceededException"


class MissingVersionException(ECSError):
    """Amazon ECS can't determine the current version of the Amazon ECS container agent on
    the container instance and doesn't have enough information to proceed with an
    update. This could be because the agent running on the container instance is a
    previous or custom version that doesn't use our version information.
    """

    _ERROR_CODE = "MissingVersionException"


class NamespaceNotFoundException(ECSError):
    """The specified namespace wasn't found."""
    _ERROR_CODE = "NamespaceNotFoundException"


class NoUpdateAvailableException(ECSError):
    """There's no update available for this Amazon ECS container agent. This might be
    because the agent is already running the latest version or because it's so old that
    there's no update path to the current version.
    """

    _ERROR_CODE = "NoUpdateAvailableException"


class PlatformTaskDefinitionIncompatibilityException(ECSError):
    """The specified platform version doesn't satisfy the required capabilities of the task
    definition.
    """

    _ERROR_CODE = "PlatformTaskDefinitionIncompatibilityException"


class PlatformUnknownException(ECSError):
    """The specified platform version doesn't exist."""
    _ERROR_CODE = "PlatformUnknownException"


class ResourceInUseException(ECSError):
    """The specified resource is in-use and can't be removed."""
    _ERROR_CODE = "ResourceInUseException"


class ResourceNotFoundException(ECSError):
    """The specified resource wasn't found."""
    _ERROR_CODE = "ResourceNotFoundException"


class ServerException(ECSError):
    """These errors are usually caused by a server issue."""
    _ERROR_CODE = "ServerException"


class ServiceDeploymentNotFoundException(ECSError):
    """The service deploy ARN that you specified in the `StopServiceDeployment` doesn't
    exist. You can use `ListServiceDeployments` to retrieve the service deployment ARNs.
    """

    _ERROR_CODE = "ServiceDeploymentNotFoundException"


class ServiceNotActiveException(ECSError):
    """The specified service isn't active. You can't update a service that's inactive. If
    you have previously deleted a service, you can re-create it with CreateService.
    """

    _ERROR_CODE = "ServiceNotActiveException"


class ServiceNotFoundException(ECSError):
    """The specified service wasn't found. You can view your available services with
    ListServices. Amazon ECS services are cluster specific and Region specific.
    """

    _ERROR_CODE = "ServiceNotFoundException"


class TargetNotConnectedException(ECSError):
    """The execute command cannot run. This error can be caused by any of the following
    configuration issues:

    - Incorrect IAM permissions
    - The SSM agent is not installed or is not running
    - There is an interface Amazon VPC endpoint for Amazon ECS, but there is not one for
      Systems Manager Session Manager

    For information about how to troubleshoot the issues, see Troubleshooting issues
    with ECS Exec in the Amazon Elastic Container Service Developer Guide.
    """

    _ERROR_CODE = "TargetNotConnectedException"


class TargetNotFoundException(ECSError):
    """The specified target wasn't found. You can view your available container instances
    with ListContainerInstances. Amazon ECS container instances are cluster-specific and
    Region-specific.
    """

    _ERROR_CODE = "TargetNotFoundException"


class TaskSetNotFoundException(ECSError):
    """The specified task set wasn't found. You can view your available task sets with
    DescribeTaskSets. Task sets are specific to each cluster, service and Region.
    """

    _ERROR_CODE = "TaskSetNotFoundException"


class UnsupportedFeatureException(ECSError):
    """The specified task isn't supported in this Region."""
    _ERROR_CODE = "UnsupportedFeatureException"


class UpdateInProgressException(ECSError):
    """There's already a current Amazon ECS container agent update in progress on the
    container instance that's specified. If the container agent becomes disconnected
    while it's in a transitional stage, such as `PENDING` or `STAGING`, the update
    process can get stuck in that state. However, when the agent reconnects, it resumes
    where it stopped previously.
    """

    _ERROR_CODE = "UpdateInProgressException"


EXCEPTIONS: dict[str, type[ECSError]] = {
    "AccessDeniedException": AccessDeniedException,
    "AttributeLimitExceededException": AttributeLimitExceededException,
    "BlockedException": BlockedException,
    "ClientException": ClientException,
    "ClusterContainsCapacityProviderException": ClusterContainsCapacityProviderException,
    "ClusterContainsContainerInstancesException": ClusterContainsContainerInstancesException,
    "ClusterContainsServicesException": ClusterContainsServicesException,
    "ClusterContainsTasksException": ClusterContainsTasksException,
    "ClusterNotFoundException": ClusterNotFoundException,
    "ConflictException": ConflictException,
    "InvalidParameterException": InvalidParameterException,
    "LimitExceededException": LimitExceededException,
    "MissingVersionException": MissingVersionException,
    "NamespaceNotFoundException": NamespaceNotFoundException,
    "NoUpdateAvailableException": NoUpdateAvailableException,
    "PlatformTaskDefinitionIncompatibilityException": PlatformTaskDefinitionIncompatibilityException,
    "PlatformUnknownException": PlatformUnknownException,
    "ResourceInUseException": ResourceInUseException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServerException": ServerException,
    "ServiceDeploymentNotFoundException": ServiceDeploymentNotFoundException,
    "ServiceNotActiveException": ServiceNotActiveException,
    "ServiceNotFoundException": ServiceNotFoundException,
    "TargetNotConnectedException": TargetNotConnectedException,
    "TargetNotFoundException": TargetNotFoundException,
    "TaskSetNotFoundException": TaskSetNotFoundException,
    "UnsupportedFeatureException": UnsupportedFeatureException,
    "UpdateInProgressException": UpdateInProgressException,
}
