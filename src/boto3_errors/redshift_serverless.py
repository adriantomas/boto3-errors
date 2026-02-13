# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class RedshiftServerlessError(Boto3Error):
    _SERVICE = "redshift-serverless"


class AccessDeniedException(RedshiftServerlessError):
    """You do not have sufficient access to perform this action."""
    _ERROR_CODE = "AccessDeniedException"

    @property
    def code(self) -> str | None:
        return self.response.get("code")


class ConflictException(RedshiftServerlessError):
    """The submitted action has conflicts."""
    _ERROR_CODE = "ConflictException"


class DryRunException(RedshiftServerlessError):
    """This exception is thrown when the request was successful, but dry run was enabled so
    no action was taken.
    """

    _ERROR_CODE = "DryRunException"


class InsufficientCapacityException(RedshiftServerlessError):
    """There is an insufficient capacity to perform the action."""
    _ERROR_CODE = "InsufficientCapacityException"


class InternalServerException(RedshiftServerlessError):
    """The request processing has failed because of an unknown error, exception or failure."""
    _ERROR_CODE = "InternalServerException"


class InvalidPaginationException(RedshiftServerlessError):
    """The provided pagination token is invalid."""
    _ERROR_CODE = "InvalidPaginationException"


class Ipv6CidrBlockNotFoundException(RedshiftServerlessError):
    """There are no subnets in your VPC with associated IPv6 CIDR blocks. To use dual-stack
    mode, associate an IPv6 CIDR block with each subnet in your VPC.
    """

    _ERROR_CODE = "Ipv6CidrBlockNotFoundException"


class ResourceNotFoundException(RedshiftServerlessError):
    """The resource could not be found."""
    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def resource_name(self) -> str | None:
        """The name of the resource that could not be found."""
        return self.response.get("resourceName")


class ServiceQuotaExceededException(RedshiftServerlessError):
    """The service limit was exceeded."""
    _ERROR_CODE = "ServiceQuotaExceededException"


class ThrottlingException(RedshiftServerlessError):
    """The request was denied due to request throttling."""
    _ERROR_CODE = "ThrottlingException"

    @property
    def code(self) -> str | None:
        return self.response.get("code")


class TooManyTagsException(RedshiftServerlessError):
    """The request exceeded the number of tags allowed for a resource."""
    _ERROR_CODE = "TooManyTagsException"

    @property
    def resource_name(self) -> str | None:
        """The name of the resource that exceeded the number of tags allowed for a
        resource.
        """
        return self.response.get("resourceName")


class ValidationException(RedshiftServerlessError):
    """The input failed to satisfy the constraints specified by an Amazon Web Services
    service.
    """

    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[RedshiftServerlessError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "DryRunException": DryRunException,
    "InsufficientCapacityException": InsufficientCapacityException,
    "InternalServerException": InternalServerException,
    "InvalidPaginationException": InvalidPaginationException,
    "Ipv6CidrBlockNotFoundException": Ipv6CidrBlockNotFoundException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "TooManyTagsException": TooManyTagsException,
    "ValidationException": ValidationException,
}
