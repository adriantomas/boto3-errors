# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class XRayError(Boto3Error):
    _SERVICE = "xray"


class InvalidPolicyRevisionIdException(XRayError):
    """A policy revision id was provided which does not match the latest policy revision.
    This exception is also if a policy revision id of 0 is provided via
    `PutResourcePolicy` and a policy with the same name already exists.
    """

    _ERROR_CODE = "InvalidPolicyRevisionIdException"


class InvalidRequestException(XRayError):
    """The request is missing required parameters or has invalid parameters."""
    _ERROR_CODE = "InvalidRequestException"


class LockoutPreventionException(XRayError):
    """The provided resource policy would prevent the caller of this request from calling
    PutResourcePolicy in the future.
    """

    _ERROR_CODE = "LockoutPreventionException"


class MalformedPolicyDocumentException(XRayError):
    """Invalid policy document provided in request."""
    _ERROR_CODE = "MalformedPolicyDocumentException"


class PolicyCountLimitExceededException(XRayError):
    """Exceeded the maximum number of resource policies for a target Amazon Web Services
    account.
    """

    _ERROR_CODE = "PolicyCountLimitExceededException"


class PolicySizeLimitExceededException(XRayError):
    """Exceeded the maximum size for a resource policy."""
    _ERROR_CODE = "PolicySizeLimitExceededException"


class ResourceNotFoundException(XRayError):
    """The resource was not found. Verify that the name or Amazon Resource Name (ARN) of
    the resource is correct.
    """

    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def resource_name(self) -> str | None:
        return self.response.get("ResourceName")


class RuleLimitExceededException(XRayError):
    """You have reached the maximum number of sampling rules."""
    _ERROR_CODE = "RuleLimitExceededException"


class ThrottledException(XRayError):
    """The request exceeds the maximum number of requests per second."""
    _ERROR_CODE = "ThrottledException"


class TooManyTagsException(XRayError):
    """You have exceeded the maximum number of tags you can apply to this resource."""
    _ERROR_CODE = "TooManyTagsException"

    @property
    def resource_name(self) -> str | None:
        return self.response.get("ResourceName")


EXCEPTIONS: dict[str, type[XRayError]] = {
    "InvalidPolicyRevisionIdException": InvalidPolicyRevisionIdException,
    "InvalidRequestException": InvalidRequestException,
    "LockoutPreventionException": LockoutPreventionException,
    "MalformedPolicyDocumentException": MalformedPolicyDocumentException,
    "PolicyCountLimitExceededException": PolicyCountLimitExceededException,
    "PolicySizeLimitExceededException": PolicySizeLimitExceededException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "RuleLimitExceededException": RuleLimitExceededException,
    "ThrottledException": ThrottledException,
    "TooManyTagsException": TooManyTagsException,
}
