# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class chatbotError(Boto3Error):
    _SERVICE = "chatbot"


class ConflictException(chatbotError):
    """There was an issue processing your request."""
    _ERROR_CODE = "ConflictException"


class CreateChimeWebhookConfigurationException(chatbotError):
    """We can’t process your request right now because of a server issue. Try again later."""
    _ERROR_CODE = "CreateChimeWebhookConfigurationException"


class CreateSlackChannelConfigurationException(chatbotError):
    """We can’t process your request right now because of a server issue. Try again later."""
    _ERROR_CODE = "CreateSlackChannelConfigurationException"


class CreateTeamsChannelConfigurationException(chatbotError):
    """We can’t process your request right now because of a server issue. Try again later."""
    _ERROR_CODE = "CreateTeamsChannelConfigurationException"


class DeleteChimeWebhookConfigurationException(chatbotError):
    """We can’t process your request right now because of a server issue. Try again later."""
    _ERROR_CODE = "DeleteChimeWebhookConfigurationException"


class DeleteMicrosoftTeamsUserIdentityException(chatbotError):
    """We can’t process your request right now because of a server issue. Try again later."""
    _ERROR_CODE = "DeleteMicrosoftTeamsUserIdentityException"


class DeleteSlackChannelConfigurationException(chatbotError):
    """We can’t process your request right now because of a server issue. Try again later."""
    _ERROR_CODE = "DeleteSlackChannelConfigurationException"


class DeleteSlackUserIdentityException(chatbotError):
    """We can’t process your request right now because of a server issue. Try again later."""
    _ERROR_CODE = "DeleteSlackUserIdentityException"


class DeleteSlackWorkspaceAuthorizationFault(chatbotError):
    """There was an issue deleting your Slack workspace."""
    _ERROR_CODE = "DeleteSlackWorkspaceAuthorizationFault"


class DeleteTeamsChannelConfigurationException(chatbotError):
    """We can’t process your request right now because of a server issue. Try again later."""
    _ERROR_CODE = "DeleteTeamsChannelConfigurationException"


class DeleteTeamsConfiguredTeamException(chatbotError):
    """We can’t process your request right now because of a server issue. Try again later."""
    _ERROR_CODE = "DeleteTeamsConfiguredTeamException"


class DescribeChimeWebhookConfigurationsException(chatbotError):
    """We can’t process your request right now because of a server issue. Try again later."""
    _ERROR_CODE = "DescribeChimeWebhookConfigurationsException"


class DescribeSlackChannelConfigurationsException(chatbotError):
    """We can’t process your request right now because of a server issue. Try again later."""
    _ERROR_CODE = "DescribeSlackChannelConfigurationsException"


class DescribeSlackUserIdentitiesException(chatbotError):
    """We can’t process your request right now because of a server issue. Try again later."""
    _ERROR_CODE = "DescribeSlackUserIdentitiesException"


class DescribeSlackWorkspacesException(chatbotError):
    """We can’t process your request right now because of a server issue. Try again later."""
    _ERROR_CODE = "DescribeSlackWorkspacesException"


class GetAccountPreferencesException(chatbotError):
    """We can’t process your request right now because of a server issue. Try again later."""
    _ERROR_CODE = "GetAccountPreferencesException"


class GetTeamsChannelConfigurationException(chatbotError):
    """We can’t process your request right now because of a server issue. Try again later."""
    _ERROR_CODE = "GetTeamsChannelConfigurationException"


class InternalServiceError(chatbotError):
    """Unexpected error during processing of request."""
    _ERROR_CODE = "InternalServiceError"


class InvalidParameterException(chatbotError):
    """Your request input doesn't meet the constraints required by AWS Chatbot."""
    _ERROR_CODE = "InvalidParameterException"


class InvalidRequestException(chatbotError):
    """Your request input doesn't meet the constraints required by AWS Chatbot."""
    _ERROR_CODE = "InvalidRequestException"


class LimitExceededException(chatbotError):
    """You have exceeded a service limit for AWS Chatbot."""
    _ERROR_CODE = "LimitExceededException"


class ListMicrosoftTeamsConfiguredTeamsException(chatbotError):
    """We can’t process your request right now because of a server issue. Try again later."""
    _ERROR_CODE = "ListMicrosoftTeamsConfiguredTeamsException"


class ListMicrosoftTeamsUserIdentitiesException(chatbotError):
    """We can’t process your request right now because of a server issue. Try again later."""
    _ERROR_CODE = "ListMicrosoftTeamsUserIdentitiesException"


class ListTeamsChannelConfigurationsException(chatbotError):
    """We can’t process your request right now because of a server issue. Try again later."""
    _ERROR_CODE = "ListTeamsChannelConfigurationsException"


class ResourceNotFoundException(chatbotError):
    """We were unable to find the resource for your request"""
    _ERROR_CODE = "ResourceNotFoundException"


class ServiceUnavailableException(chatbotError):
    """We can’t process your request right now because of a server issue. Try again later."""
    _ERROR_CODE = "ServiceUnavailableException"


class TooManyTagsException(chatbotError):
    """The supplied list of tags contains too many tags."""
    _ERROR_CODE = "TooManyTagsException"


class UnauthorizedException(chatbotError):
    """The request was rejected because it doesn't have valid credentials for the target
    resource.
    """

    _ERROR_CODE = "UnauthorizedException"


class UpdateAccountPreferencesException(chatbotError):
    """We can’t process your request right now because of a server issue. Try again later."""
    _ERROR_CODE = "UpdateAccountPreferencesException"


class UpdateChimeWebhookConfigurationException(chatbotError):
    """We can’t process your request right now because of a server issue. Try again later."""
    _ERROR_CODE = "UpdateChimeWebhookConfigurationException"


class UpdateSlackChannelConfigurationException(chatbotError):
    """We can’t process your request right now because of a server issue. Try again later."""
    _ERROR_CODE = "UpdateSlackChannelConfigurationException"


class UpdateTeamsChannelConfigurationException(chatbotError):
    """We can’t process your request right now because of a server issue. Try again later."""
    _ERROR_CODE = "UpdateTeamsChannelConfigurationException"


EXCEPTIONS: dict[str, type[chatbotError]] = {
    "ConflictException": ConflictException,
    "CreateChimeWebhookConfigurationException": CreateChimeWebhookConfigurationException,
    "CreateSlackChannelConfigurationException": CreateSlackChannelConfigurationException,
    "CreateTeamsChannelConfigurationException": CreateTeamsChannelConfigurationException,
    "DeleteChimeWebhookConfigurationException": DeleteChimeWebhookConfigurationException,
    "DeleteMicrosoftTeamsUserIdentityException": DeleteMicrosoftTeamsUserIdentityException,
    "DeleteSlackChannelConfigurationException": DeleteSlackChannelConfigurationException,
    "DeleteSlackUserIdentityException": DeleteSlackUserIdentityException,
    "DeleteSlackWorkspaceAuthorizationFault": DeleteSlackWorkspaceAuthorizationFault,
    "DeleteTeamsChannelConfigurationException": DeleteTeamsChannelConfigurationException,
    "DeleteTeamsConfiguredTeamException": DeleteTeamsConfiguredTeamException,
    "DescribeChimeWebhookConfigurationsException": DescribeChimeWebhookConfigurationsException,
    "DescribeSlackChannelConfigurationsException": DescribeSlackChannelConfigurationsException,
    "DescribeSlackUserIdentitiesException": DescribeSlackUserIdentitiesException,
    "DescribeSlackWorkspacesException": DescribeSlackWorkspacesException,
    "GetAccountPreferencesException": GetAccountPreferencesException,
    "GetTeamsChannelConfigurationException": GetTeamsChannelConfigurationException,
    "InternalServiceError": InternalServiceError,
    "InvalidParameterException": InvalidParameterException,
    "InvalidRequestException": InvalidRequestException,
    "LimitExceededException": LimitExceededException,
    "ListMicrosoftTeamsConfiguredTeamsException": ListMicrosoftTeamsConfiguredTeamsException,
    "ListMicrosoftTeamsUserIdentitiesException": ListMicrosoftTeamsUserIdentitiesException,
    "ListTeamsChannelConfigurationsException": ListTeamsChannelConfigurationsException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceUnavailableException": ServiceUnavailableException,
    "TooManyTagsException": TooManyTagsException,
    "UnauthorizedException": UnauthorizedException,
    "UpdateAccountPreferencesException": UpdateAccountPreferencesException,
    "UpdateChimeWebhookConfigurationException": UpdateChimeWebhookConfigurationException,
    "UpdateSlackChannelConfigurationException": UpdateSlackChannelConfigurationException,
    "UpdateTeamsChannelConfigurationException": UpdateTeamsChannelConfigurationException,
}
