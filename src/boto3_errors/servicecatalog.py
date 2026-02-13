# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class ServiceCatalogError(Boto3Error):
    _SERVICE = "servicecatalog"


class DuplicateResourceException(ServiceCatalogError):
    """The specified resource is a duplicate."""
    _ERROR_CODE = "DuplicateResourceException"


class InvalidParametersException(ServiceCatalogError):
    """One or more parameters provided to the operation are not valid."""
    _ERROR_CODE = "InvalidParametersException"


class InvalidStateException(ServiceCatalogError):
    """An attempt was made to modify a resource that is in a state that is not valid. Check
    your resources to ensure that they are in valid states before retrying the
    operation.
    """

    _ERROR_CODE = "InvalidStateException"


class LimitExceededException(ServiceCatalogError):
    """The current limits of the service would have been exceeded by this operation.
    Decrease your resource use or increase your service limits and retry the operation.
    """

    _ERROR_CODE = "LimitExceededException"


class OperationNotSupportedException(ServiceCatalogError):
    """The operation is not supported."""
    _ERROR_CODE = "OperationNotSupportedException"


class ResourceInUseException(ServiceCatalogError):
    """A resource that is currently in use. Ensure that the resource is not in use and
    retry the operation.
    """

    _ERROR_CODE = "ResourceInUseException"


class ResourceNotFoundException(ServiceCatalogError):
    """The specified resource was not found."""
    _ERROR_CODE = "ResourceNotFoundException"


class TagOptionNotMigratedException(ServiceCatalogError):
    """An operation requiring TagOptions failed because the TagOptions migration process
    has not been performed for this account. Use the Amazon Web Services Management
    Console to perform the migration process before retrying the operation.
    """

    _ERROR_CODE = "TagOptionNotMigratedException"


EXCEPTIONS: dict[str, type[ServiceCatalogError]] = {
    "DuplicateResourceException": DuplicateResourceException,
    "InvalidParametersException": InvalidParametersException,
    "InvalidStateException": InvalidStateException,
    "LimitExceededException": LimitExceededException,
    "OperationNotSupportedException": OperationNotSupportedException,
    "ResourceInUseException": ResourceInUseException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "TagOptionNotMigratedException": TagOptionNotMigratedException,
}
