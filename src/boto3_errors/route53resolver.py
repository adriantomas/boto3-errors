# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class Route53ResolverError(Boto3Error):
    _SERVICE = "route53resolver"


class AccessDeniedException(Route53ResolverError):
    """The current account doesn't have the IAM permissions required to perform the
    specified Resolver operation.
    """

    _ERROR_CODE = "AccessDeniedException"


class ConflictException(Route53ResolverError):
    """The requested state transition isn't valid. For example, you can't delete a firewall
    domain list if it is in the process of being deleted, or you can't import domains
    into a domain list that is in the process of being deleted.
    """

    _ERROR_CODE = "ConflictException"


class InternalServiceErrorException(Route53ResolverError):
    """We encountered an unknown error. Try again in a few minutes."""
    _ERROR_CODE = "InternalServiceErrorException"


class InvalidNextTokenException(Route53ResolverError):
    """The value that you specified for `NextToken` in a `List` request isn't valid."""
    _ERROR_CODE = "InvalidNextTokenException"


class InvalidParameterException(Route53ResolverError):
    """One or more parameters in this request are not valid."""
    _ERROR_CODE = "InvalidParameterException"

    @property
    def field_name(self) -> str | None:
        """For an `InvalidParameterException` error, the name of the parameter that's
        invalid.
        """
        return self.response.get("FieldName")


class InvalidPolicyDocument(Route53ResolverError):
    """The specified Resolver rule policy is invalid."""
    _ERROR_CODE = "InvalidPolicyDocument"


class InvalidRequestException(Route53ResolverError):
    """The request is invalid."""
    _ERROR_CODE = "InvalidRequestException"


class InvalidTagException(Route53ResolverError):
    """The specified tag is invalid."""
    _ERROR_CODE = "InvalidTagException"


class LimitExceededException(Route53ResolverError):
    """The request caused one or more limits to be exceeded."""
    _ERROR_CODE = "LimitExceededException"

    @property
    def resource_type(self) -> str | None:
        """For a `LimitExceededException` error, the type of resource that exceeded the
        current limit.
        """
        return self.response.get("ResourceType")


class ResourceExistsException(Route53ResolverError):
    """The resource that you tried to create already exists."""
    _ERROR_CODE = "ResourceExistsException"

    @property
    def resource_type(self) -> str | None:
        """For a `ResourceExistsException` error, the type of resource that the error
        applies to.
        """
        return self.response.get("ResourceType")


class ResourceInUseException(Route53ResolverError):
    """The resource that you tried to update or delete is currently in use."""
    _ERROR_CODE = "ResourceInUseException"

    @property
    def resource_type(self) -> str | None:
        """For a `ResourceInUseException` error, the type of resource that is currently in
        use.
        """
        return self.response.get("ResourceType")


class ResourceNotFoundException(Route53ResolverError):
    """The specified resource doesn't exist."""
    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def resource_type(self) -> str | None:
        """For a `ResourceNotFoundException` error, the type of resource that doesn't
        exist.
        """
        return self.response.get("ResourceType")


class ResourceUnavailableException(Route53ResolverError):
    """The specified resource isn't available."""
    _ERROR_CODE = "ResourceUnavailableException"

    @property
    def resource_type(self) -> str | None:
        """For a `ResourceUnavailableException` error, the type of resource that isn't
        available.
        """
        return self.response.get("ResourceType")


class ServiceQuotaExceededException(Route53ResolverError):
    """Fulfilling the request would cause one or more quotas to be exceeded."""
    _ERROR_CODE = "ServiceQuotaExceededException"


class ThrottlingException(Route53ResolverError):
    """The request was throttled. Try again in a few minutes."""
    _ERROR_CODE = "ThrottlingException"


class UnknownResourceException(Route53ResolverError):
    """The specified resource doesn't exist."""
    _ERROR_CODE = "UnknownResourceException"


class ValidationException(Route53ResolverError):
    """You have provided an invalid command. If you ran the `UpdateFirewallDomains`
    request. supported values are `ADD`, `REMOVE`, or `REPLACE` a domain.
    """

    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[Route53ResolverError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServiceErrorException": InternalServiceErrorException,
    "InvalidNextTokenException": InvalidNextTokenException,
    "InvalidParameterException": InvalidParameterException,
    "InvalidPolicyDocument": InvalidPolicyDocument,
    "InvalidRequestException": InvalidRequestException,
    "InvalidTagException": InvalidTagException,
    "LimitExceededException": LimitExceededException,
    "ResourceExistsException": ResourceExistsException,
    "ResourceInUseException": ResourceInUseException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ResourceUnavailableException": ResourceUnavailableException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "UnknownResourceException": UnknownResourceException,
    "ValidationException": ValidationException,
}
