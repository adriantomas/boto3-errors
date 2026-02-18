# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class InspectorError(Boto3Error):
    _SERVICE = "inspector"


class AccessDeniedException(InspectorError):
    """You do not have required permissions to access the requested resource."""
    _ERROR_CODE = "AccessDeniedException"

    @property
    def can_retry(self) -> bool | None:
        """You can immediately retry your request."""
        return self.response.get("canRetry")

    @property
    def error_code(self) -> str | None:
        """Code that indicates the type of error that is generated."""
        return self.response.get("errorCode")


class AgentsAlreadyRunningAssessmentException(InspectorError):
    """You started an assessment run, but one of the instances is already participating in
    another assessment run.
    """

    _ERROR_CODE = "AgentsAlreadyRunningAssessmentException"

    @property
    def agents(self) -> list[Any] | None:
        return self.response.get("agents")

    @property
    def agents_truncated(self) -> bool | None:
        return self.response.get("agentsTruncated")

    @property
    def can_retry(self) -> bool | None:
        """You can immediately retry your request."""
        return self.response.get("canRetry")


class AssessmentRunInProgressException(InspectorError):
    """You cannot perform a specified action if an assessment run is currently in progress."""
    _ERROR_CODE = "AssessmentRunInProgressException"

    @property
    def assessment_run_arns(self) -> list[Any] | None:
        """The ARNs of the assessment runs that are currently in progress."""
        return self.response.get("assessmentRunArns")

    @property
    def assessment_run_arns_truncated(self) -> bool | None:
        """Boolean value that indicates whether the ARN list of the assessment runs is
        truncated.
        """
        return self.response.get("assessmentRunArnsTruncated")

    @property
    def can_retry(self) -> bool | None:
        """You can immediately retry your request."""
        return self.response.get("canRetry")


class InternalException(InspectorError):
    """Internal server error."""
    _ERROR_CODE = "InternalException"

    @property
    def can_retry(self) -> bool | None:
        """You can immediately retry your request."""
        return self.response.get("canRetry")


class InvalidCrossAccountRoleException(InspectorError):
    """Amazon Inspector cannot assume the cross-account role that it needs to list your EC2
    instances during the assessment run.
    """

    _ERROR_CODE = "InvalidCrossAccountRoleException"

    @property
    def can_retry(self) -> bool | None:
        """You can immediately retry your request."""
        return self.response.get("canRetry")

    @property
    def error_code(self) -> str | None:
        """Code that indicates the type of error that is generated."""
        return self.response.get("errorCode")


class InvalidInputException(InspectorError):
    """The request was rejected because an invalid or out-of-range value was supplied for
    an input parameter.
    """

    _ERROR_CODE = "InvalidInputException"

    @property
    def can_retry(self) -> bool | None:
        """You can immediately retry your request."""
        return self.response.get("canRetry")

    @property
    def error_code(self) -> str | None:
        """Code that indicates the type of error that is generated."""
        return self.response.get("errorCode")


class LimitExceededException(InspectorError):
    """The request was rejected because it attempted to create resources beyond the current
    AWS account limits. The error code describes the limit exceeded.
    """

    _ERROR_CODE = "LimitExceededException"

    @property
    def can_retry(self) -> bool | None:
        """You can immediately retry your request."""
        return self.response.get("canRetry")

    @property
    def error_code(self) -> str | None:
        """Code that indicates the type of error that is generated."""
        return self.response.get("errorCode")


class NoSuchEntityException(InspectorError):
    """The request was rejected because it referenced an entity that does not exist. The
    error code describes the entity.
    """

    _ERROR_CODE = "NoSuchEntityException"

    @property
    def can_retry(self) -> bool | None:
        """You can immediately retry your request."""
        return self.response.get("canRetry")

    @property
    def error_code(self) -> str | None:
        """Code that indicates the type of error that is generated."""
        return self.response.get("errorCode")


class PreviewGenerationInProgressException(InspectorError):
    """The request is rejected. The specified assessment template is currently generating
    an exclusions preview.
    """

    _ERROR_CODE = "PreviewGenerationInProgressException"


class ServiceTemporarilyUnavailableException(InspectorError):
    """The serice is temporary unavailable."""
    _ERROR_CODE = "ServiceTemporarilyUnavailableException"

    @property
    def can_retry(self) -> bool | None:
        """You can wait and then retry your request."""
        return self.response.get("canRetry")


class UnsupportedFeatureException(InspectorError):
    """Used by the GetAssessmentReport API. The request was rejected because you tried to
    generate a report for an assessment run that existed before reporting was supported
    in Amazon Inspector. You can only generate reports for assessment runs that took
    place or will take place after generating reports in Amazon Inspector became
    available.
    """

    _ERROR_CODE = "UnsupportedFeatureException"

    @property
    def can_retry(self) -> bool | None:
        return self.response.get("canRetry")


EXCEPTIONS: dict[str, type[InspectorError]] = {
    "AccessDeniedException": AccessDeniedException,
    "AgentsAlreadyRunningAssessmentException": AgentsAlreadyRunningAssessmentException,
    "AssessmentRunInProgressException": AssessmentRunInProgressException,
    "InternalException": InternalException,
    "InvalidCrossAccountRoleException": InvalidCrossAccountRoleException,
    "InvalidInputException": InvalidInputException,
    "LimitExceededException": LimitExceededException,
    "NoSuchEntityException": NoSuchEntityException,
    "PreviewGenerationInProgressException": PreviewGenerationInProgressException,
    "ServiceTemporarilyUnavailableException": ServiceTemporarilyUnavailableException,
    "UnsupportedFeatureException": UnsupportedFeatureException,
}
