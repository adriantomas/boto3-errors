# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class SupportAppError(Boto3Error):
    _SERVICE = "support-app"


class AccessDeniedException(SupportAppError):
    """You don't have sufficient permission to perform this action."""
    _ERROR_CODE = "AccessDeniedException"


class ConflictException(SupportAppError):
    """Your request has a conflict. For example, you might receive this error if you try
    the following:

    - Add, update, or delete a Slack channel configuration before you add a Slack
      workspace to your Amazon Web Services account.
    - Add a Slack channel configuration that already exists in your Amazon Web Services
      account.
    - Delete a Slack channel configuration for a live chat channel.
    - Delete a Slack workspace from your Amazon Web Services account that has an active
      live chat channel.
    - Call the `RegisterSlackWorkspaceForOrganization` API from an Amazon Web Services
      account that doesn't belong to an organization.
    - Call the `RegisterSlackWorkspaceForOrganization` API from a member account, but
      the management account hasn't registered that workspace yet for the organization.
    """

    _ERROR_CODE = "ConflictException"


class InternalServerException(SupportAppError):
    """We can’t process your request right now because of a server issue. Try again later."""
    _ERROR_CODE = "InternalServerException"


class ResourceNotFoundException(SupportAppError):
    """The specified resource is missing or doesn't exist, such as an account alias, Slack
    channel configuration, or Slack workspace configuration.
    """

    _ERROR_CODE = "ResourceNotFoundException"


class ServiceQuotaExceededException(SupportAppError):
    """Your Service Quotas request exceeds the quota for the service. For example, your
    Service Quotas request to Amazon Web Services Support App might exceed the maximum
    number of workspaces or channels per account, or the maximum number of accounts per
    Slack channel.
    """

    _ERROR_CODE = "ServiceQuotaExceededException"


class ValidationException(SupportAppError):
    """Your request input doesn't meet the constraints that the Amazon Web Services Support
    App specifies.
    """

    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[SupportAppError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ValidationException": ValidationException,
}
