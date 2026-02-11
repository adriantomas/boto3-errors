# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class GameLiftError(Boto3Error):
    _SERVICE = "gamelift"


class ConflictException(GameLiftError):
    """The requested operation would cause a conflict with the current state of a service
    resource associated with the request. Resolve the conflict before retrying this
    request.
    """

    _ERROR_CODE = "ConflictException"


class FleetCapacityExceededException(GameLiftError):
    """The specified fleet has no available instances to fulfill a `CreateGameSession`
    request. Clients can retry such requests immediately or after a waiting period.
    """

    _ERROR_CODE = "FleetCapacityExceededException"


class GameSessionFullException(GameLiftError):
    """The game instance is currently full and cannot allow the requested player(s) to
    join. Clients can retry such requests immediately or after a waiting period.
    """

    _ERROR_CODE = "GameSessionFullException"


class IdempotentParameterMismatchException(GameLiftError):
    """A game session with this custom ID string already exists in this fleet. Resolve this
    conflict before retrying this request.
    """

    _ERROR_CODE = "IdempotentParameterMismatchException"


class InternalServiceException(GameLiftError):
    """The service encountered an unrecoverable internal failure while processing the
    request. Clients can retry such requests immediately or after a waiting period.
    """

    _ERROR_CODE = "InternalServiceException"


class InvalidFleetStatusException(GameLiftError):
    """The requested operation would cause a conflict with the current state of a resource
    associated with the request and/or the fleet. Resolve the conflict before retrying.
    """

    _ERROR_CODE = "InvalidFleetStatusException"


class InvalidGameSessionStatusException(GameLiftError):
    """The requested operation would cause a conflict with the current state of a resource
    associated with the request and/or the game instance. Resolve the conflict before
    retrying.
    """

    _ERROR_CODE = "InvalidGameSessionStatusException"


class InvalidRequestException(GameLiftError):
    """One or more parameter values in the request are invalid. Correct the invalid
    parameter values before retrying.
    """

    _ERROR_CODE = "InvalidRequestException"


class LimitExceededException(GameLiftError):
    """The requested operation would cause the resource to exceed the allowed service
    limit. Resolve the issue before retrying.
    """

    _ERROR_CODE = "LimitExceededException"


class NotFoundException(GameLiftError):
    """The requested resources was not found. The resource was either not created yet or
    deleted.
    """

    _ERROR_CODE = "NotFoundException"


class NotReadyException(GameLiftError):
    """The operation failed because Amazon GameLift Servers has not yet finished validating
    this compute. We recommend attempting 8 to 10 retries over 3 to 5 minutes with
    exponential backoffs and jitter.
    """

    _ERROR_CODE = "NotReadyException"


class OutOfCapacityException(GameLiftError):
    """The specified game server group has no available game servers to fulfill a
    `ClaimGameServer` request. Clients can retry such requests immediately or after a
    waiting period.
    """

    _ERROR_CODE = "OutOfCapacityException"


class TaggingFailedException(GameLiftError):
    """The requested tagging operation did not succeed. This may be due to invalid tag
    format or the maximum tag limit may have been exceeded. Resolve the issue before
    retrying.
    """

    _ERROR_CODE = "TaggingFailedException"


class TerminalRoutingStrategyException(GameLiftError):
    """The service is unable to resolve the routing for a particular alias because it has a
    terminal `RoutingStrategy` associated with it. The message returned in this
    exception is the message defined in the routing strategy itself. Such requests
    should only be retried if the routing strategy for the specified alias is modified.
    """

    _ERROR_CODE = "TerminalRoutingStrategyException"


class UnauthorizedException(GameLiftError):
    """The client failed authentication. Clients should not retry such requests."""
    _ERROR_CODE = "UnauthorizedException"


class UnsupportedRegionException(GameLiftError):
    """The requested operation is not supported in the Region specified."""
    _ERROR_CODE = "UnsupportedRegionException"


EXCEPTIONS: dict[str, type[GameLiftError]] = {
    "ConflictException": ConflictException,
    "FleetCapacityExceededException": FleetCapacityExceededException,
    "GameSessionFullException": GameSessionFullException,
    "IdempotentParameterMismatchException": IdempotentParameterMismatchException,
    "InternalServiceException": InternalServiceException,
    "InvalidFleetStatusException": InvalidFleetStatusException,
    "InvalidGameSessionStatusException": InvalidGameSessionStatusException,
    "InvalidRequestException": InvalidRequestException,
    "LimitExceededException": LimitExceededException,
    "NotFoundException": NotFoundException,
    "NotReadyException": NotReadyException,
    "OutOfCapacityException": OutOfCapacityException,
    "TaggingFailedException": TaggingFailedException,
    "TerminalRoutingStrategyException": TerminalRoutingStrategyException,
    "UnauthorizedException": UnauthorizedException,
    "UnsupportedRegionException": UnsupportedRegionException,
}
