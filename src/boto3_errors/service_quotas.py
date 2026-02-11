# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class ServiceQuotasError(Boto3Error):
    _SERVICE = "service-quotas"


class AWSServiceAccessNotEnabledException(ServiceQuotasError):
    """The action you attempted is not allowed unless Service Access with Service Quotas is
    enabled in your organization.
    """

    _ERROR_CODE = "AWSServiceAccessNotEnabledException"


class AccessDeniedException(ServiceQuotasError):
    """You do not have sufficient permission to perform this action."""
    _ERROR_CODE = "AccessDeniedException"


class DependencyAccessDeniedException(ServiceQuotasError):
    """You can't perform this action because a dependency does not have access."""
    _ERROR_CODE = "DependencyAccessDeniedException"


class IllegalArgumentException(ServiceQuotasError):
    """Invalid input was provided."""
    _ERROR_CODE = "IllegalArgumentException"


class InvalidPaginationTokenException(ServiceQuotasError):
    """Invalid input was provided."""
    _ERROR_CODE = "InvalidPaginationTokenException"


class InvalidResourceStateException(ServiceQuotasError):
    """The resource is in an invalid state."""
    _ERROR_CODE = "InvalidResourceStateException"


class NoAvailableOrganizationException(ServiceQuotasError):
    """The Amazon Web Services account making this call is not a member of an organization."""
    _ERROR_CODE = "NoAvailableOrganizationException"


class NoSuchResourceException(ServiceQuotasError):
    """The specified resource does not exist."""
    _ERROR_CODE = "NoSuchResourceException"


class OrganizationNotInAllFeaturesModeException(ServiceQuotasError):
    """The organization that your Amazon Web Services account belongs to is not in All
    Features mode.
    """

    _ERROR_CODE = "OrganizationNotInAllFeaturesModeException"


class QuotaExceededException(ServiceQuotasError):
    """You have exceeded your service quota. To perform the requested action, remove some
    of the relevant resources, or use Service Quotas to request a service quota
    increase.
    """

    _ERROR_CODE = "QuotaExceededException"


class ResourceAlreadyExistsException(ServiceQuotasError):
    """The specified resource already exists."""
    _ERROR_CODE = "ResourceAlreadyExistsException"


class ServiceException(ServiceQuotasError):
    """Something went wrong."""
    _ERROR_CODE = "ServiceException"


class ServiceQuotaTemplateNotInUseException(ServiceQuotasError):
    """The quota request template is not associated with your organization."""
    _ERROR_CODE = "ServiceQuotaTemplateNotInUseException"


class TagPolicyViolationException(ServiceQuotasError):
    """The specified tag is a reserved word and cannot be used."""
    _ERROR_CODE = "TagPolicyViolationException"


class TemplatesNotAvailableInRegionException(ServiceQuotasError):
    """The Service Quotas template is not available in this Amazon Web Services Region."""
    _ERROR_CODE = "TemplatesNotAvailableInRegionException"


class TooManyRequestsException(ServiceQuotasError):
    """Due to throttling, the request was denied. Slow down the rate of request calls, or
    request an increase for this quota.
    """

    _ERROR_CODE = "TooManyRequestsException"


class TooManyTagsException(ServiceQuotasError):
    """You've exceeded the number of tags allowed for a resource. For more information, see
    Tag restrictions in the Service Quotas User Guide.
    """

    _ERROR_CODE = "TooManyTagsException"


EXCEPTIONS: dict[str, type[ServiceQuotasError]] = {
    "AWSServiceAccessNotEnabledException": AWSServiceAccessNotEnabledException,
    "AccessDeniedException": AccessDeniedException,
    "DependencyAccessDeniedException": DependencyAccessDeniedException,
    "IllegalArgumentException": IllegalArgumentException,
    "InvalidPaginationTokenException": InvalidPaginationTokenException,
    "InvalidResourceStateException": InvalidResourceStateException,
    "NoAvailableOrganizationException": NoAvailableOrganizationException,
    "NoSuchResourceException": NoSuchResourceException,
    "OrganizationNotInAllFeaturesModeException": OrganizationNotInAllFeaturesModeException,
    "QuotaExceededException": QuotaExceededException,
    "ResourceAlreadyExistsException": ResourceAlreadyExistsException,
    "ServiceException": ServiceException,
    "ServiceQuotaTemplateNotInUseException": ServiceQuotaTemplateNotInUseException,
    "TagPolicyViolationException": TagPolicyViolationException,
    "TemplatesNotAvailableInRegionException": TemplatesNotAvailableInRegionException,
    "TooManyRequestsException": TooManyRequestsException,
    "TooManyTagsException": TooManyTagsException,
}
