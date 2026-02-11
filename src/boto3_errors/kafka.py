# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class KafkaError(Boto3Error):
    _SERVICE = "kafka"


class BadRequestException(KafkaError):
    """Returns information about an error."""
    _ERROR_CODE = "BadRequestException"

    @property
    def invalid_parameter(self) -> str | None:
        """The parameter that caused the error."""
        return self.response.get("InvalidParameter")


class ClusterConnectivityException(KafkaError):
    """Returns information about an error."""
    _ERROR_CODE = "ClusterConnectivityException"

    @property
    def invalid_parameter(self) -> str | None:
        """The parameter that caused the error."""
        return self.response.get("InvalidParameter")


class ConflictException(KafkaError):
    """Returns information about an error."""
    _ERROR_CODE = "ConflictException"

    @property
    def invalid_parameter(self) -> str | None:
        """The parameter that caused the error."""
        return self.response.get("InvalidParameter")


class ControllerMovedException(KafkaError):
    """Returns information about an error."""
    _ERROR_CODE = "ControllerMovedException"

    @property
    def invalid_parameter(self) -> str | None:
        """The parameter that caused the error."""
        return self.response.get("InvalidParameter")


class ForbiddenException(KafkaError):
    """Returns information about an error."""
    _ERROR_CODE = "ForbiddenException"

    @property
    def invalid_parameter(self) -> str | None:
        """The parameter that caused the error."""
        return self.response.get("InvalidParameter")


class GroupSubscribedToTopicException(KafkaError):
    """Returns information about an error."""
    _ERROR_CODE = "GroupSubscribedToTopicException"

    @property
    def invalid_parameter(self) -> str | None:
        """The parameter that caused the error."""
        return self.response.get("InvalidParameter")


class InternalServerErrorException(KafkaError):
    """Returns information about an error."""
    _ERROR_CODE = "InternalServerErrorException"

    @property
    def invalid_parameter(self) -> str | None:
        """The parameter that caused the error."""
        return self.response.get("InvalidParameter")


class KafkaRequestException(KafkaError):
    """Returns information about an error."""
    _ERROR_CODE = "KafkaRequestException"

    @property
    def invalid_parameter(self) -> str | None:
        """The parameter that caused the error."""
        return self.response.get("InvalidParameter")


class KafkaTimeoutException(KafkaError):
    """Returns information about an error."""
    _ERROR_CODE = "KafkaTimeoutException"

    @property
    def invalid_parameter(self) -> str | None:
        """The parameter that caused the error."""
        return self.response.get("InvalidParameter")


class NotControllerException(KafkaError):
    """Returns information about an error."""
    _ERROR_CODE = "NotControllerException"

    @property
    def invalid_parameter(self) -> str | None:
        """The parameter that caused the error."""
        return self.response.get("InvalidParameter")


class NotFoundException(KafkaError):
    """Returns information about an error."""
    _ERROR_CODE = "NotFoundException"

    @property
    def invalid_parameter(self) -> str | None:
        """The parameter that caused the error."""
        return self.response.get("InvalidParameter")


class ReassignmentInProgressException(KafkaError):
    """Returns information about an error."""
    _ERROR_CODE = "ReassignmentInProgressException"

    @property
    def invalid_parameter(self) -> str | None:
        """The parameter that caused the error."""
        return self.response.get("InvalidParameter")


class ServiceUnavailableException(KafkaError):
    """Returns information about an error."""
    _ERROR_CODE = "ServiceUnavailableException"

    @property
    def invalid_parameter(self) -> str | None:
        """The parameter that caused the error."""
        return self.response.get("InvalidParameter")


class TooManyRequestsException(KafkaError):
    """Returns information about an error."""
    _ERROR_CODE = "TooManyRequestsException"

    @property
    def invalid_parameter(self) -> str | None:
        """The parameter that caused the error."""
        return self.response.get("InvalidParameter")


class TopicExistsException(KafkaError):
    """Returns information about an error."""
    _ERROR_CODE = "TopicExistsException"

    @property
    def invalid_parameter(self) -> str | None:
        """The parameter that caused the error."""
        return self.response.get("InvalidParameter")


class UnauthorizedException(KafkaError):
    """Returns information about an error."""
    _ERROR_CODE = "UnauthorizedException"

    @property
    def invalid_parameter(self) -> str | None:
        """The parameter that caused the error."""
        return self.response.get("InvalidParameter")


class UnknownTopicOrPartitionException(KafkaError):
    """Returns information about an error."""
    _ERROR_CODE = "UnknownTopicOrPartitionException"

    @property
    def invalid_parameter(self) -> str | None:
        """The parameter that caused the error."""
        return self.response.get("InvalidParameter")


EXCEPTIONS: dict[str, type[KafkaError]] = {
    "BadRequestException": BadRequestException,
    "ClusterConnectivityException": ClusterConnectivityException,
    "ConflictException": ConflictException,
    "ControllerMovedException": ControllerMovedException,
    "ForbiddenException": ForbiddenException,
    "GroupSubscribedToTopicException": GroupSubscribedToTopicException,
    "InternalServerErrorException": InternalServerErrorException,
    "KafkaRequestException": KafkaRequestException,
    "KafkaTimeoutException": KafkaTimeoutException,
    "NotControllerException": NotControllerException,
    "NotFoundException": NotFoundException,
    "ReassignmentInProgressException": ReassignmentInProgressException,
    "ServiceUnavailableException": ServiceUnavailableException,
    "TooManyRequestsException": TooManyRequestsException,
    "TopicExistsException": TopicExistsException,
    "UnauthorizedException": UnauthorizedException,
    "UnknownTopicOrPartitionException": UnknownTopicOrPartitionException,
}
