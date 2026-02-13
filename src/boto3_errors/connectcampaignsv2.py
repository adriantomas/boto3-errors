# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class ConnectCampaignsV2Error(Boto3Error):
    _SERVICE = "connectcampaignsv2"


class AccessDeniedException(ConnectCampaignsV2Error):
    """You do not have sufficient access to perform this action."""
    _ERROR_CODE = "AccessDeniedException"

    @property
    def x_amz_error_type(self) -> str | None:
        return self.response.get("xAmzErrorType")


class ConflictException(ConnectCampaignsV2Error):
    """The request could not be processed because of conflict in the current state of the
    resource.
    """

    _ERROR_CODE = "ConflictException"

    @property
    def x_amz_error_type(self) -> str | None:
        return self.response.get("xAmzErrorType")


class InternalServerException(ConnectCampaignsV2Error):
    """Request processing failed because of an error or failure with the service."""
    _ERROR_CODE = "InternalServerException"

    @property
    def x_amz_error_type(self) -> str | None:
        return self.response.get("xAmzErrorType")


class InvalidCampaignStateException(ConnectCampaignsV2Error):
    """The request could not be processed because of conflict in the current state of the
    campaign.
    """

    _ERROR_CODE = "InvalidCampaignStateException"

    @property
    def state(self) -> str | None:
        return self.response.get("state")

    @property
    def x_amz_error_type(self) -> str | None:
        return self.response.get("xAmzErrorType")


class InvalidStateException(ConnectCampaignsV2Error):
    """The request could not be processed because of conflict in the current state."""
    _ERROR_CODE = "InvalidStateException"

    @property
    def x_amz_error_type(self) -> str | None:
        return self.response.get("xAmzErrorType")


class ResourceNotFoundException(ConnectCampaignsV2Error):
    """The specified resource was not found."""
    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def x_amz_error_type(self) -> str | None:
        return self.response.get("xAmzErrorType")


class ServiceQuotaExceededException(ConnectCampaignsV2Error):
    """Request would cause a service quota to be exceeded."""
    _ERROR_CODE = "ServiceQuotaExceededException"

    @property
    def x_amz_error_type(self) -> str | None:
        return self.response.get("xAmzErrorType")


class ThrottlingException(ConnectCampaignsV2Error):
    """The request was denied due to request throttling."""
    _ERROR_CODE = "ThrottlingException"

    @property
    def x_amz_error_type(self) -> str | None:
        return self.response.get("xAmzErrorType")


class ValidationException(ConnectCampaignsV2Error):
    """The input fails to satisfy the constraints specified by an AWS service."""
    _ERROR_CODE = "ValidationException"

    @property
    def x_amz_error_type(self) -> str | None:
        return self.response.get("xAmzErrorType")


EXCEPTIONS: dict[str, type[ConnectCampaignsV2Error]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "InvalidCampaignStateException": InvalidCampaignStateException,
    "InvalidStateException": InvalidStateException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
