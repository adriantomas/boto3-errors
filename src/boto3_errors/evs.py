# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class evsError(Boto3Error):
    _SERVICE = "evs"


class InternalServerException(evsError):
    """An internal server error occurred. Retry your request."""
    _ERROR_CODE = "InternalServerException"


class ResourceNotFoundException(evsError):
    """A service resource associated with the request could not be found. The resource
    might not be specified correctly, or it may have a `state` of `DELETED`.
    """

    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def resource_id(self) -> str | None:
        """The ID of the resource that could not be found."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of the resource that is associated with the error."""
        return self.response.get("resourceType")


class ServiceQuotaExceededException(evsError):
    """The number of one or more Amazon EVS resources exceeds the maximum allowed. For a
    list of Amazon EVS quotas, see Amazon EVS endpoints and quotas in the Amazon EVS
    User Guide. Delete some resources or request an increase in your service quota. To
    request an increase, see Amazon Web Services Service Quotas in the Amazon Web
    Services General Reference Guide.
    """

    _ERROR_CODE = "ServiceQuotaExceededException"


class TagPolicyException(evsError):
    """Note:

     `TagPolicyException` is deprecated. See `ValidationException` instead.

    The request doesn't comply with IAM tag policy. Correct your request and then retry
    it.
    """

    _ERROR_CODE = "TagPolicyException"


class ThrottlingException(evsError):
    """The operation could not be performed because the service is throttling requests.
    This exception is thrown when the service endpoint receives too many concurrent
    requests.
    """

    _ERROR_CODE = "ThrottlingException"

    @property
    def retry_after_seconds(self) -> int | None:
        """The seconds to wait to retry."""
        return self.response.get("retryAfterSeconds")


class TooManyTagsException(evsError):
    """Note:

     `TooManyTagsException` is deprecated. See `ServiceQuotaExceededException` instead.

    A service resource associated with the request has more than 200 tags.
    """

    _ERROR_CODE = "TooManyTagsException"


class ValidationException(evsError):
    """The input fails to satisfy the specified constraints. You will see this exception if
    invalid inputs are provided for any of the Amazon EVS environment operations, or if
    a list operation is performed on an environment resource that is still initializing.
    """

    _ERROR_CODE = "ValidationException"

    @property
    def reason(self) -> str | None:
        """The reason for the exception."""
        return self.response.get("reason")

    @property
    def field_list(self) -> list[Any] | None:
        """A list of fields that didn't validate."""
        return self.response.get("fieldList")


EXCEPTIONS: dict[str, type[evsError]] = {
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "TagPolicyException": TagPolicyException,
    "ThrottlingException": ThrottlingException,
    "TooManyTagsException": TooManyTagsException,
    "ValidationException": ValidationException,
}
