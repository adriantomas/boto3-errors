# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class ConnectError(Boto3Error):
    _SERVICE = "connect"


class AccessDeniedException(ConnectError):
    """You do not have sufficient permissions to perform this action."""
    _ERROR_CODE = "AccessDeniedException"


class ConditionalOperationFailedException(ConnectError):
    """Request processing failed because dependent condition failed."""
    _ERROR_CODE = "ConditionalOperationFailedException"


class ConflictException(ConnectError):
    """Operation cannot be performed at this time as there is a conflict with another
    operation or contact state.
    """

    _ERROR_CODE = "ConflictException"


class ContactFlowNotPublishedException(ConnectError):
    """The flow has not been published."""
    _ERROR_CODE = "ContactFlowNotPublishedException"


class ContactNotFoundException(ConnectError):
    """The contact with the specified ID does not exist."""
    _ERROR_CODE = "ContactNotFoundException"


class DestinationNotAllowedException(ConnectError):
    """Outbound calls to the destination number are not allowed."""
    _ERROR_CODE = "DestinationNotAllowedException"


class DuplicateResourceException(ConnectError):
    """A resource with the specified name already exists."""
    _ERROR_CODE = "DuplicateResourceException"


class IdempotencyException(ConnectError):
    """An entity with the same name already exists."""
    _ERROR_CODE = "IdempotencyException"


class InternalServiceException(ConnectError):
    """Request processing failed because of an error or failure with the service."""
    _ERROR_CODE = "InternalServiceException"


class InvalidActiveRegionException(ConnectError):
    """This exception occurs when an API request is made to a non-active region in an
    Amazon Connect instance configured with Amazon Connect Global Resiliency. For
    example, if the active region is US West (Oregon) and a request is made to US East
    (N. Virginia), the exception will be returned.
    """

    _ERROR_CODE = "InvalidActiveRegionException"


class InvalidContactFlowException(ConnectError):
    """The flow is not valid."""
    _ERROR_CODE = "InvalidContactFlowException"

    @property
    def problems(self) -> list[Any] | None:
        """The problems with the flow. Please fix before trying again."""
        return self.response.get("problems")


class InvalidContactFlowModuleException(ConnectError):
    """The problems with the module. Please fix before trying again."""
    _ERROR_CODE = "InvalidContactFlowModuleException"

    @property
    def problems(self) -> list[Any] | None:
        return self.response.get("Problems")


class InvalidParameterException(ConnectError):
    """One or more of the specified parameters are not valid."""
    _ERROR_CODE = "InvalidParameterException"


class InvalidRequestException(ConnectError):
    """The request is not valid."""
    _ERROR_CODE = "InvalidRequestException"

    @property
    def reason(self) -> dict[str, Any] | None:
        return self.response.get("Reason")


class InvalidTestCaseException(ConnectError):
    """The test is not valid."""
    _ERROR_CODE = "InvalidTestCaseException"

    @property
    def problems(self) -> list[Any] | None:
        """The problems with the test. Please fix before trying again."""
        return self.response.get("Problems")


class LimitExceededException(ConnectError):
    """The allowed limit for the resource has been exceeded."""
    _ERROR_CODE = "LimitExceededException"


class MaximumResultReturnedException(ConnectError):
    """Maximum number (1000) of tags have been returned with current request. Consider
    changing request parameters to get more tags.
    """

    _ERROR_CODE = "MaximumResultReturnedException"


class OutboundContactNotPermittedException(ConnectError):
    """The contact is not permitted."""
    _ERROR_CODE = "OutboundContactNotPermittedException"


class OutputTypeNotFoundException(ConnectError):
    """Thrown for analyzed content when requested OutputType was not enabled for a given
    contact. For example, if an OutputType.Raw was requested for a contact that had
    `RedactedOnly` Redaction policy set in the flow.
    """

    _ERROR_CODE = "OutputTypeNotFoundException"


class PropertyValidationException(ConnectError):
    """The property is not valid."""
    _ERROR_CODE = "PropertyValidationException"

    @property
    def property_list(self) -> list[Any] | None:
        return self.response.get("PropertyList")


class ResourceConflictException(ConnectError):
    """A resource already has that name."""
    _ERROR_CODE = "ResourceConflictException"


class ResourceInUseException(ConnectError):
    """That resource is already in use (for example, you're trying to add a record with the
    same name as an existing record). If you are trying to delete a resource (for
    example, DeleteHoursOfOperation or DeletePredefinedAttribute), remove its reference
    from related resources and then try again.
    """

    _ERROR_CODE = "ResourceInUseException"

    @property
    def resource_id(self) -> str | None:
        """The identifier for the resource."""
        return self.response.get("ResourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of resource."""
        return self.response.get("ResourceType")


class ResourceNotFoundException(ConnectError):
    """The specified resource was not found."""
    _ERROR_CODE = "ResourceNotFoundException"


class ResourceNotReadyException(ConnectError):
    """The resource is not ready."""
    _ERROR_CODE = "ResourceNotReadyException"


class ServiceQuotaExceededException(ConnectError):
    """The service quota has been exceeded."""
    _ERROR_CODE = "ServiceQuotaExceededException"

    @property
    def reason(self) -> dict[str, Any] | None:
        return self.response.get("Reason")


class ThrottlingException(ConnectError):
    """The throttling limit has been exceeded."""
    _ERROR_CODE = "ThrottlingException"


class TooManyRequestsException(ConnectError):
    """Displayed when rate-related API limits are exceeded."""
    _ERROR_CODE = "TooManyRequestsException"


class UserNotFoundException(ConnectError):
    """No user with the specified credentials was found in the Amazon Connect instance."""
    _ERROR_CODE = "UserNotFoundException"


EXCEPTIONS: dict[str, type[ConnectError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConditionalOperationFailedException": ConditionalOperationFailedException,
    "ConflictException": ConflictException,
    "ContactFlowNotPublishedException": ContactFlowNotPublishedException,
    "ContactNotFoundException": ContactNotFoundException,
    "DestinationNotAllowedException": DestinationNotAllowedException,
    "DuplicateResourceException": DuplicateResourceException,
    "IdempotencyException": IdempotencyException,
    "InternalServiceException": InternalServiceException,
    "InvalidActiveRegionException": InvalidActiveRegionException,
    "InvalidContactFlowException": InvalidContactFlowException,
    "InvalidContactFlowModuleException": InvalidContactFlowModuleException,
    "InvalidParameterException": InvalidParameterException,
    "InvalidRequestException": InvalidRequestException,
    "InvalidTestCaseException": InvalidTestCaseException,
    "LimitExceededException": LimitExceededException,
    "MaximumResultReturnedException": MaximumResultReturnedException,
    "OutboundContactNotPermittedException": OutboundContactNotPermittedException,
    "OutputTypeNotFoundException": OutputTypeNotFoundException,
    "PropertyValidationException": PropertyValidationException,
    "ResourceConflictException": ResourceConflictException,
    "ResourceInUseException": ResourceInUseException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ResourceNotReadyException": ResourceNotReadyException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "TooManyRequestsException": TooManyRequestsException,
    "UserNotFoundException": UserNotFoundException,
}
