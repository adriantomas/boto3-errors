# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class ServiceDiscoveryError(Boto3Error):
    _SERVICE = "servicediscovery"


class CustomHealthNotFound(ServiceDiscoveryError):
    """The health check for the instance that's specified by `ServiceId` and `InstanceId`
    isn't a custom health check.
    """

    _ERROR_CODE = "CustomHealthNotFound"


class DuplicateRequest(ServiceDiscoveryError):
    """The operation is already in progress."""
    _ERROR_CODE = "DuplicateRequest"

    @property
    def duplicate_operation_id(self) -> str | None:
        """The ID of the operation that's already in progress."""
        return self.response.get("DuplicateOperationId")


class InstanceNotFound(ServiceDiscoveryError):
    """No instance exists with the specified ID, or the instance was recently registered,
    and information about the instance hasn't propagated yet.
    """

    _ERROR_CODE = "InstanceNotFound"


class InvalidInput(ServiceDiscoveryError):
    """One or more specified values aren't valid. For example, a required value might be
    missing, a numeric value might be outside the allowed range, or a string value might
    exceed length constraints.
    """

    _ERROR_CODE = "InvalidInput"


class NamespaceAlreadyExists(ServiceDiscoveryError):
    """The namespace that you're trying to create already exists."""
    _ERROR_CODE = "NamespaceAlreadyExists"

    @property
    def creator_request_id(self) -> str | None:
        """The `CreatorRequestId` that was used to create the namespace."""
        return self.response.get("CreatorRequestId")

    @property
    def namespace_id(self) -> str | None:
        """The ID of the existing namespace."""
        return self.response.get("NamespaceId")


class NamespaceNotFound(ServiceDiscoveryError):
    """No namespace exists with the specified ID."""
    _ERROR_CODE = "NamespaceNotFound"


class OperationNotFound(ServiceDiscoveryError):
    """No operation exists with the specified ID."""
    _ERROR_CODE = "OperationNotFound"


class RequestLimitExceeded(ServiceDiscoveryError):
    """The operation can't be completed because you've reached the quota for the number of
    requests. For more information, see Cloud Map API request throttling quota in the
    Cloud Map Developer Guide.
    """

    _ERROR_CODE = "RequestLimitExceeded"


class ResourceInUse(ServiceDiscoveryError):
    """The specified resource can't be deleted because it contains other resources. For
    example, you can't delete a service that contains any instances.
    """

    _ERROR_CODE = "ResourceInUse"


class ResourceLimitExceeded(ServiceDiscoveryError):
    """The resource can't be created because you've reached the quota on the number of
    resources.
    """

    _ERROR_CODE = "ResourceLimitExceeded"


class ResourceNotFoundException(ServiceDiscoveryError):
    """The operation can't be completed because the resource was not found."""
    _ERROR_CODE = "ResourceNotFoundException"


class ServiceAlreadyExists(ServiceDiscoveryError):
    """The service can't be created because a service with the same name already exists."""
    _ERROR_CODE = "ServiceAlreadyExists"

    @property
    def creator_request_id(self) -> str | None:
        """The `CreatorRequestId` that was used to create the service."""
        return self.response.get("CreatorRequestId")

    @property
    def service_arn(self) -> str | None:
        """The ARN of the existing service."""
        return self.response.get("ServiceArn")

    @property
    def service_id(self) -> str | None:
        """The ID of the existing service."""
        return self.response.get("ServiceId")


class ServiceAttributesLimitExceededException(ServiceDiscoveryError):
    """The attribute can't be added to the service because you've exceeded the quota for
    the number of attributes you can add to a service.
    """

    _ERROR_CODE = "ServiceAttributesLimitExceededException"


class ServiceNotFound(ServiceDiscoveryError):
    """No service exists with the specified ID."""
    _ERROR_CODE = "ServiceNotFound"


class TooManyTagsException(ServiceDiscoveryError):
    """The list of tags on the resource is over the quota. The maximum number of tags that
    can be applied to a resource is 50.
    """

    _ERROR_CODE = "TooManyTagsException"

    @property
    def resource_name(self) -> str | None:
        """The name of the resource."""
        return self.response.get("ResourceName")


EXCEPTIONS: dict[str, type[ServiceDiscoveryError]] = {
    "CustomHealthNotFound": CustomHealthNotFound,
    "DuplicateRequest": DuplicateRequest,
    "InstanceNotFound": InstanceNotFound,
    "InvalidInput": InvalidInput,
    "NamespaceAlreadyExists": NamespaceAlreadyExists,
    "NamespaceNotFound": NamespaceNotFound,
    "OperationNotFound": OperationNotFound,
    "RequestLimitExceeded": RequestLimitExceeded,
    "ResourceInUse": ResourceInUse,
    "ResourceLimitExceeded": ResourceLimitExceeded,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceAlreadyExists": ServiceAlreadyExists,
    "ServiceAttributesLimitExceededException": ServiceAttributesLimitExceededException,
    "ServiceNotFound": ServiceNotFound,
    "TooManyTagsException": TooManyTagsException,
}
