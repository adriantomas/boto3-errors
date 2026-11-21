# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class PaymentsError(Boto3Error):
    _SERVICE = "payments"


class AccessDeniedException(PaymentsError):
    """The request is denied because you don't have sufficient access to perform this
    operation. Verify that you have the required permissions and try again. This error
    is also returned, instead of `ResourceNotFoundException`, when you aren't authorized
    for the resource, so the response doesn't reveal whether the resource exists.
    """

    _ERROR_CODE = "AccessDeniedException"

    @property
    def reason(self) -> str | None:
        """The reason that access was denied. The following values are valid:

        - `NOT_AUTHORIZED` – Your IAM policies don't allow this action.
        - `INVALID_ACCOUNT_STATE` – Your Amazon Web Services account isn't in a state
          that allows this action, for example because registration isn't complete or
          the account is suspended.
        - `OTHER` – Access was denied for another reason.
        """
        return self.response.get("reason")


class InternalServerException(PaymentsError):
    """The request processing failed because of an unknown error, exception, or failure.
    Retry your request.
    """

    _ERROR_CODE = "InternalServerException"

    @property
    def retry_after_seconds(self) -> int | None:
        """The suggested number of seconds to wait before retrying the request."""
        return self.response.get("retryAfterSeconds")


class ResourceNotFoundException(PaymentsError):
    """The requested resource couldn't be found. Verify that the resource ID is correct.
    This error is returned only when you're authorized for the resource.
    """

    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def resource_id(self) -> str | None:
        """The ID of the resource that wasn't found."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of the resource that wasn't found."""
        return self.response.get("resourceType")


class ThrottlingException(PaymentsError):
    """The request was denied due to request throttling. Reduce the frequency of your
    requests and try again.
    """

    _ERROR_CODE = "ThrottlingException"

    @property
    def retry_after_seconds(self) -> int | None:
        """The suggested number of seconds to wait before retrying the request."""
        return self.response.get("retryAfterSeconds")


class ValidationException(PaymentsError):
    """The request isn't valid. Check `reason` and `fieldList` for the cause, correct the
    request, and try again.
    """

    _ERROR_CODE = "ValidationException"

    @property
    def field_list(self) -> list[Any] | None:
        """The request members that failed validation. This member is populated when
        `reason` is `FIELD_VALIDATION_FAILED`.
        """
        return self.response.get("fieldList")

    @property
    def reason(self) -> str | None:
        """The reason that validation failed. The following values are valid:

        - `CANNOT_PARSE` – The request body couldn't be parsed, or a value isn't of the
          expected type.
        - `FIELD_VALIDATION_FAILED` – One or more members failed validation. `fieldList`
          names them.
        - `INVALID_PAGINATION_TOKEN` – The `nextToken` is malformed or expired, or
          doesn't match the original request. Start again from the first page.
        - `UNSUPPORTED_ACTION` – The request is well formed, but the action isn't
          supported for your account, Region, or resource.
        - `OTHER` – The request isn't valid for another reason.
        """
        return self.response.get("reason")


EXCEPTIONS: dict[str, type[PaymentsError]] = {
    "AccessDeniedException": AccessDeniedException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
