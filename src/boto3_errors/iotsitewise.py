# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class IoTSiteWiseError(Boto3Error):
    _SERVICE = "iotsitewise"


class AccessDeniedException(IoTSiteWiseError):
    """Access is denied."""
    _ERROR_CODE = "AccessDeniedException"


class ConflictingOperationException(IoTSiteWiseError):
    """Your request has conflicting operations. This can occur if you're trying to perform
    more than one operation on the same resource at the same time.
    """

    _ERROR_CODE = "ConflictingOperationException"

    @property
    def resource_id(self) -> str | None:
        """The ID of the resource that conflicts with this operation."""
        return self.response.get("resourceId")

    @property
    def resource_arn(self) -> str | None:
        """The ARN of the resource that conflicts with this operation."""
        return self.response.get("resourceArn")


class InternalFailureException(IoTSiteWiseError):
    """IoT SiteWise can't process your request right now. Try again later."""
    _ERROR_CODE = "InternalFailureException"


class InvalidRequestException(IoTSiteWiseError):
    """The request isn't valid. This can occur if your request contains malformed JSON or
    unsupported characters. Check your request and try again.
    """

    _ERROR_CODE = "InvalidRequestException"


class LimitExceededException(IoTSiteWiseError):
    """You've reached the quota for a resource. For example, this can occur if you're
    trying to associate more than the allowed number of child assets or attempting to
    create more than the allowed number of properties for an asset model.

    For more information, see Quotas in the IoT SiteWise User Guide.
    """

    _ERROR_CODE = "LimitExceededException"


class PreconditionFailedException(IoTSiteWiseError):
    """The precondition in one or more of the request-header fields evaluated to `FALSE`."""
    _ERROR_CODE = "PreconditionFailedException"

    @property
    def resource_id(self) -> str | None:
        """The ID of the resource on which precondition failed with this operation."""
        return self.response.get("resourceId")

    @property
    def resource_arn(self) -> str | None:
        """The ARN of the resource on which precondition failed with this operation."""
        return self.response.get("resourceArn")


class QueryTimeoutException(IoTSiteWiseError):
    """The query timed out."""
    _ERROR_CODE = "QueryTimeoutException"


class ResourceAlreadyExistsException(IoTSiteWiseError):
    """The resource already exists."""
    _ERROR_CODE = "ResourceAlreadyExistsException"

    @property
    def resource_id(self) -> str | None:
        """The ID of the resource that already exists."""
        return self.response.get("resourceId")

    @property
    def resource_arn(self) -> str | None:
        """The ARN of the resource that already exists."""
        return self.response.get("resourceArn")


class ResourceNotFoundException(IoTSiteWiseError):
    """The requested resource can't be found."""
    _ERROR_CODE = "ResourceNotFoundException"


class ServiceUnavailableException(IoTSiteWiseError):
    """The requested service is unavailable."""
    _ERROR_CODE = "ServiceUnavailableException"


class ThrottlingException(IoTSiteWiseError):
    """Your request exceeded a rate limit. For example, you might have exceeded the number
    of IoT SiteWise assets that can be created per second, the allowed number of
    messages per second, and so on.

    For more information, see Quotas in the IoT SiteWise User Guide.
    """

    _ERROR_CODE = "ThrottlingException"


class TooManyTagsException(IoTSiteWiseError):
    """You've reached the quota for the number of tags allowed for a resource. For more
    information, see Tag naming limits and requirements in the Amazon Web Services
    General Reference.
    """

    _ERROR_CODE = "TooManyTagsException"

    @property
    def resource_name(self) -> str | None:
        """The name of the resource with too many tags."""
        return self.response.get("resourceName")


class UnauthorizedException(IoTSiteWiseError):
    """You are not authorized."""
    _ERROR_CODE = "UnauthorizedException"


class ValidationException(IoTSiteWiseError):
    """The validation failed for this query."""
    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[IoTSiteWiseError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictingOperationException": ConflictingOperationException,
    "InternalFailureException": InternalFailureException,
    "InvalidRequestException": InvalidRequestException,
    "LimitExceededException": LimitExceededException,
    "PreconditionFailedException": PreconditionFailedException,
    "QueryTimeoutException": QueryTimeoutException,
    "ResourceAlreadyExistsException": ResourceAlreadyExistsException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceUnavailableException": ServiceUnavailableException,
    "ThrottlingException": ThrottlingException,
    "TooManyTagsException": TooManyTagsException,
    "UnauthorizedException": UnauthorizedException,
    "ValidationException": ValidationException,
}
