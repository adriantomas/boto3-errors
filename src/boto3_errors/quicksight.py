# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class QuickSightError(Boto3Error):
    _SERVICE = "quicksight"


class AccessDeniedException(QuickSightError):
    """You don't have access to this item. The provided credentials couldn't be validated.
    You might not be authorized to carry out the request. Make sure that your account is
    authorized to use the Amazon Quick Sight service, that your policies have the
    correct permissions, and that you are using the correct credentials.
    """

    _ERROR_CODE = "AccessDeniedException"

    @property
    def request_id(self) -> str | None:
        """The Amazon Web Services request ID for this request."""
        return self.response.get("RequestId")


class ConcurrentUpdatingException(QuickSightError):
    """A resource is already in a state that indicates an operation is happening that must
    complete before a new update can be applied.
    """

    _ERROR_CODE = "ConcurrentUpdatingException"

    @property
    def request_id(self) -> str | None:
        return self.response.get("RequestId")


class ConflictException(QuickSightError):
    """Updating or deleting a resource can cause an inconsistent state."""
    _ERROR_CODE = "ConflictException"

    @property
    def request_id(self) -> str | None:
        """The Amazon Web Services request ID for this request."""
        return self.response.get("RequestId")


class CustomerManagedKeyUnavailableException(QuickSightError):
    """The customer managed key that is registered to your Amazon Quick Sight account is
    unavailable.
    """

    _ERROR_CODE = "CustomerManagedKeyUnavailableException"

    @property
    def request_id(self) -> str | None:
        """The Amazon Web Services request ID for this operation."""
        return self.response.get("RequestId")


class DomainNotWhitelistedException(QuickSightError):
    """The domain specified isn't on the allow list. All domains for embedded dashboards
    must be added to the approved list by an Amazon Quick Suite admin.
    """

    _ERROR_CODE = "DomainNotWhitelistedException"

    @property
    def request_id(self) -> str | None:
        """The Amazon Web Services request ID for this request."""
        return self.response.get("RequestId")


class IdentityTypeNotSupportedException(QuickSightError):
    """The identity type specified isn't supported. Supported identity types include `IAM`
    and `QUICKSIGHT`.
    """

    _ERROR_CODE = "IdentityTypeNotSupportedException"

    @property
    def request_id(self) -> str | None:
        """The Amazon Web Services request ID for this request."""
        return self.response.get("RequestId")


class InternalFailureException(QuickSightError):
    """An internal failure occurred."""
    _ERROR_CODE = "InternalFailureException"

    @property
    def request_id(self) -> str | None:
        """The Amazon Web Services request ID for this request."""
        return self.response.get("RequestId")


class InternalServerException(QuickSightError):
    """An internal service exception."""
    _ERROR_CODE = "InternalServerException"


class InvalidDataSetParameterValueException(QuickSightError):
    """An exception thrown when an invalid parameter value is provided for dataset
    operations.
    """

    _ERROR_CODE = "InvalidDataSetParameterValueException"

    @property
    def request_id(self) -> str | None:
        """The Amazon Web Services request ID for this request."""
        return self.response.get("RequestId")


class InvalidNextTokenException(QuickSightError):
    """The `NextToken` value isn't valid."""
    _ERROR_CODE = "InvalidNextTokenException"

    @property
    def request_id(self) -> str | None:
        """The Amazon Web Services request ID for this request."""
        return self.response.get("RequestId")


class InvalidParameterException(QuickSightError):
    """One or more parameter has a value that isn't valid."""
    _ERROR_CODE = "InvalidParameterException"

    @property
    def request_id(self) -> str | None:
        """The Amazon Web Services request ID for this request."""
        return self.response.get("RequestId")


class InvalidParameterValueException(QuickSightError):
    """One or more parameters has a value that isn't valid."""
    _ERROR_CODE = "InvalidParameterValueException"

    @property
    def request_id(self) -> str | None:
        """The Amazon Web Services request ID for this request."""
        return self.response.get("RequestId")


class InvalidRequestException(QuickSightError):
    """You don't have this feature activated for your account. To fix this issue, contact
    Amazon Web Services support.
    """

    _ERROR_CODE = "InvalidRequestException"

    @property
    def request_id(self) -> str | None:
        """The Amazon Web Services request ID for this request."""
        return self.response.get("RequestId")


class LimitExceededException(QuickSightError):
    """A limit is exceeded."""
    _ERROR_CODE = "LimitExceededException"

    @property
    def request_id(self) -> str | None:
        """The Amazon Web Services request ID for this request."""
        return self.response.get("RequestId")

    @property
    def resource_type(self) -> str | None:
        """Limit exceeded."""
        return self.response.get("ResourceType")


class PreconditionNotMetException(QuickSightError):
    """One or more preconditions aren't met."""
    _ERROR_CODE = "PreconditionNotMetException"

    @property
    def request_id(self) -> str | None:
        """The Amazon Web Services request ID for this request."""
        return self.response.get("RequestId")


class QuickSightUserNotFoundException(QuickSightError):
    """The user with the provided name isn't found. This error can happen in any operation
    that requires finding a user based on a provided user name, such as `DeleteUser`,
    `DescribeUser`, and so on.
    """

    _ERROR_CODE = "QuickSightUserNotFoundException"

    @property
    def request_id(self) -> str | None:
        """The Amazon Web Services request ID for this request."""
        return self.response.get("RequestId")


class ResourceExistsException(QuickSightError):
    """The resource specified already exists."""
    _ERROR_CODE = "ResourceExistsException"

    @property
    def request_id(self) -> str | None:
        """The Amazon Web Services request ID for this request."""
        return self.response.get("RequestId")

    @property
    def resource_type(self) -> str | None:
        """The resource type for this request."""
        return self.response.get("ResourceType")


class ResourceNotFoundException(QuickSightError):
    """One or more resources can't be found."""
    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def request_id(self) -> str | None:
        """The Amazon Web Services request ID for this request."""
        return self.response.get("RequestId")

    @property
    def resource_type(self) -> str | None:
        """The resource type for this request."""
        return self.response.get("ResourceType")


class ResourceUnavailableException(QuickSightError):
    """This resource is currently unavailable."""
    _ERROR_CODE = "ResourceUnavailableException"

    @property
    def request_id(self) -> str | None:
        """The Amazon Web Services request ID for this request."""
        return self.response.get("RequestId")

    @property
    def resource_type(self) -> str | None:
        """The resource type for this request."""
        return self.response.get("ResourceType")


class SessionLifetimeInMinutesInvalidException(QuickSightError):
    """The number of minutes specified for the lifetime of a session isn't valid. The
    session lifetime must be 15-600 minutes.
    """

    _ERROR_CODE = "SessionLifetimeInMinutesInvalidException"

    @property
    def request_id(self) -> str | None:
        """The Amazon Web Services request ID for this request."""
        return self.response.get("RequestId")


class ThrottlingException(QuickSightError):
    """Access is throttled."""
    _ERROR_CODE = "ThrottlingException"

    @property
    def request_id(self) -> str | None:
        """The Amazon Web Services request ID for this request."""
        return self.response.get("RequestId")


class UnsupportedPricingPlanException(QuickSightError):
    """This error indicates that you are calling an embedding operation in Amazon Quick
    Sight without the required pricing plan on your Amazon Web Services account. Before
    you can use embedding for anonymous users, a Quick Suite administrator needs to add
    capacity pricing to Quick Sight. You can do this on the Manage Quick Suite page.

    After capacity pricing is added, you can use the ` GetDashboardEmbedUrl ` API
    operation with the `--identity-type ANONYMOUS` option.
    """

    _ERROR_CODE = "UnsupportedPricingPlanException"

    @property
    def request_id(self) -> str | None:
        """The Amazon Web Services request ID for this request."""
        return self.response.get("RequestId")


class UnsupportedUserEditionException(QuickSightError):
    """This error indicates that you are calling an operation on an Amazon Quick Suite
    subscription where the edition doesn't include support for that operation. Amazon
    Quick Suite currently has Standard Edition and Enterprise Edition. Not every
    operation and capability is available in every edition.
    """

    _ERROR_CODE = "UnsupportedUserEditionException"

    @property
    def request_id(self) -> str | None:
        """The Amazon Web Services request ID for this request."""
        return self.response.get("RequestId")


EXCEPTIONS: dict[str, type[QuickSightError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConcurrentUpdatingException": ConcurrentUpdatingException,
    "ConflictException": ConflictException,
    "CustomerManagedKeyUnavailableException": CustomerManagedKeyUnavailableException,
    "DomainNotWhitelistedException": DomainNotWhitelistedException,
    "IdentityTypeNotSupportedException": IdentityTypeNotSupportedException,
    "InternalFailureException": InternalFailureException,
    "InternalServerException": InternalServerException,
    "InvalidDataSetParameterValueException": InvalidDataSetParameterValueException,
    "InvalidNextTokenException": InvalidNextTokenException,
    "InvalidParameterException": InvalidParameterException,
    "InvalidParameterValueException": InvalidParameterValueException,
    "InvalidRequestException": InvalidRequestException,
    "LimitExceededException": LimitExceededException,
    "PreconditionNotMetException": PreconditionNotMetException,
    "QuickSightUserNotFoundException": QuickSightUserNotFoundException,
    "ResourceExistsException": ResourceExistsException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ResourceUnavailableException": ResourceUnavailableException,
    "SessionLifetimeInMinutesInvalidException": SessionLifetimeInMinutesInvalidException,
    "ThrottlingException": ThrottlingException,
    "UnsupportedPricingPlanException": UnsupportedPricingPlanException,
    "UnsupportedUserEditionException": UnsupportedUserEditionException,
}
