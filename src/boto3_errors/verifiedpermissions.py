# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class VerifiedPermissionsError(Boto3Error):
    _SERVICE = "verifiedpermissions"


class AccessDeniedException(VerifiedPermissionsError):
    """You don't have sufficient access to perform this action."""
    _ERROR_CODE = "AccessDeniedException"


class ConflictException(VerifiedPermissionsError):
    """The request failed because another request to modify a resource occurred at the
    same.
    """

    _ERROR_CODE = "ConflictException"

    @property
    def resources(self) -> list[Any] | None:
        """The list of resources referenced with this failed request."""
        return self.response.get("resources")


class InternalServerException(VerifiedPermissionsError):
    """The request failed because of an internal error. Try your request again later"""
    _ERROR_CODE = "InternalServerException"


class ResourceNotFoundException(VerifiedPermissionsError):
    """The request failed because it references a resource that doesn't exist."""
    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def resource_id(self) -> str | None:
        """The unique ID of the resource referenced in the failed request."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """The resource type of the resource referenced in the failed request."""
        return self.response.get("resourceType")


class ServiceQuotaExceededException(VerifiedPermissionsError):
    """The request failed because it would cause a service quota to be exceeded."""
    _ERROR_CODE = "ServiceQuotaExceededException"

    @property
    def quota_code(self) -> str | None:
        """The quota code recognized by the Amazon Web Services Service Quotas service."""
        return self.response.get("quotaCode")

    @property
    def resource_id(self) -> str | None:
        """The unique ID of the resource referenced in the failed request."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """The resource type of the resource referenced in the failed request."""
        return self.response.get("resourceType")

    @property
    def service_code(self) -> str | None:
        """The code for the Amazon Web Service that owns the quota."""
        return self.response.get("serviceCode")


class ThrottlingException(VerifiedPermissionsError):
    """The request failed because it exceeded a throttling quota."""
    _ERROR_CODE = "ThrottlingException"

    @property
    def quota_code(self) -> str | None:
        """The quota code recognized by the Amazon Web Services Service Quotas service."""
        return self.response.get("quotaCode")

    @property
    def service_code(self) -> str | None:
        """The code for the Amazon Web Service that owns the quota."""
        return self.response.get("serviceCode")


class ValidationException(VerifiedPermissionsError):
    """The request failed because one or more input parameters don't satisfy their
    constraint requirements. The output is provided as a list of fields and a reason for
    each field that isn't valid.

    The possible reasons include the following:

    - UnrecognizedEntityType The policy includes an entity type that isn't found in the
      schema.
    - UnrecognizedActionId The policy includes an action id that isn't found in the
      schema.
    - InvalidActionApplication The policy includes an action that, according to the
      schema, doesn't support the specified principal and resource.
    - UnexpectedType The policy included an operand that isn't a valid type for the
      specified operation.
    - IncompatibleTypes The types of elements included in a `set`, or the types of
      expressions used in an `if...then...else` clause aren't compatible in this
      context.
    - MissingAttribute The policy attempts to access a record or entity attribute that
      isn't specified in the schema. Test for the existence of the attribute first
      before attempting to access its value. For more information, see the has (presence
      of attribute test) operator in the Cedar Policy Language Guide.
    - UnsafeOptionalAttributeAccess The policy attempts to access a record or entity
      attribute that is optional and isn't guaranteed to be present. Test for the
      existence of the attribute first before attempting to access its value. For more
      information, see the has (presence of attribute test) operator in the Cedar Policy
      Language Guide.
    - ImpossiblePolicy Cedar has determined that a policy condition always evaluates to
      false. If the policy is always false, it can never apply to any query, and so it
      can never affect an authorization decision.
    - WrongNumberArguments The policy references an extension type with the wrong number
      of arguments.
    - FunctionArgumentValidationError Cedar couldn't parse the argument passed to an
      extension type. For example, a string that is to be parsed as an IPv4 address can
      contain only digits and the period character.
    """

    _ERROR_CODE = "ValidationException"

    @property
    def field_list(self) -> list[Any] | None:
        """The list of fields that aren't valid."""
        return self.response.get("fieldList")


EXCEPTIONS: dict[str, type[VerifiedPermissionsError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
