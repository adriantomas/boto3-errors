# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class AbuseSignalError(Boto3Error):
    _SERVICE = "abuse-signal"


class AccessDeniedException(AbuseSignalError):
    """The caller does not have sufficient access to perform this operation. Verify that
    the caller has the specific IAM permission for the operation it is calling (for
    example, `abuse:CreateAbuseReport`, `abuse:GetAbuseReportStatus`, or
    `abuse:ListAbuseReportStatuses`). Grant only the actions each caller requires.
    """

    _ERROR_CODE = "AccessDeniedException"


class ConflictException(AbuseSignalError):
    """The request conflicts with the current state of the resource. For example, an
    idempotency token was reused with a different payload.
    """

    _ERROR_CODE = "ConflictException"


class InternalServerException(AbuseSignalError):
    """An unexpected error occurred during the processing of the request. This error is
    retryable; check the `Retry-After` header before you retry.
    """

    _ERROR_CODE = "InternalServerException"

    @property
    def retry_after_seconds(self) -> int | None:
        """The number of seconds to wait before you retry the request. The service also
        returns this value in the `Retry-After` HTTP header.
        """
        return self.response.get("retryAfterSeconds")


class ResourceNotFoundException(AbuseSignalError):
    """The specified resource was not found. Verify that the `reportId` is correct."""
    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def resource_id(self) -> str | None:
        """The identifier of the resource that was not found."""
        return self.response.get("resourceId")


class SubmissionRequirementException(AbuseSignalError):
    """The report is well-formed and satisfies the XARF schema, but it does not meet one or
    more submission requirements (for example, the submission lookback window or
    `source_identifier` restrictions). This error is distinct from `ValidationException`
    (HTTP 400), which indicates that the report is not well-formed. Retrying the same
    report will not succeed; the report content must change.
    """

    _ERROR_CODE = "SubmissionRequirementException"

    @property
    def unmet_requirements(self) -> list[Any] | None:
        """A list of the specific submission requirements that the report did not meet."""
        return self.response.get("unmetRequirements")


class ThrottlingException(AbuseSignalError):
    """The request was denied due to request throttling. This error is retryable; retry
    with exponential backoff.
    """

    _ERROR_CODE = "ThrottlingException"

    @property
    def quota_code(self) -> str | None:
        """The code for the service quota that was exceeded."""
        return self.response.get("quotaCode")

    @property
    def retry_after_seconds(self) -> int | None:
        """The number of seconds to wait before you retry the request. The service also
        returns this value in the `Retry-After` HTTP header.
        """
        return self.response.get("retryAfterSeconds")

    @property
    def service_code(self) -> str | None:
        """The code for the Amazon Web Services service that is associated with the quota
        that was exceeded.
        """
        return self.response.get("serviceCode")


class ValidationException(AbuseSignalError):
    """The input fails to satisfy the constraints specified by the service, which indicates
    that the request is not well-formed. Check `fieldList` for the specific members that
    failed validation.
    """

    _ERROR_CODE = "ValidationException"

    @property
    def field_list(self) -> list[Any] | None:
        """A list of the specific input fields that failed validation."""
        return self.response.get("fieldList")


EXCEPTIONS: dict[str, type[AbuseSignalError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "SubmissionRequirementException": SubmissionRequirementException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
