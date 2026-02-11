# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class MachineLearningError(Boto3Error):
    _SERVICE = "machinelearning"


class IdempotentParameterMismatchException(MachineLearningError):
    """A second request to use or change an object was not allowed. This can result from
    retrying a request using a parameter that was not present in the original request.
    """

    _ERROR_CODE = "IdempotentParameterMismatchException"

    @property
    def code(self) -> int | None:
        return self.response.get("code")


class InternalServerException(MachineLearningError):
    """An error on the server occurred when trying to process a request."""
    _ERROR_CODE = "InternalServerException"

    @property
    def code(self) -> int | None:
        return self.response.get("code")


class InvalidInputException(MachineLearningError):
    """An error on the client occurred. Typically, the cause is an invalid input value."""
    _ERROR_CODE = "InvalidInputException"

    @property
    def code(self) -> int | None:
        return self.response.get("code")


class InvalidTagException(MachineLearningError):
    _ERROR_CODE = "InvalidTagException"


class LimitExceededException(MachineLearningError):
    """The subscriber exceeded the maximum number of operations. This exception can occur
    when listing objects such as `DataSource`.
    """

    _ERROR_CODE = "LimitExceededException"

    @property
    def code(self) -> int | None:
        return self.response.get("code")


class PredictorNotMountedException(MachineLearningError):
    """The exception is thrown when a predict request is made to an unmounted `MLModel`."""
    _ERROR_CODE = "PredictorNotMountedException"


class ResourceNotFoundException(MachineLearningError):
    """A specified resource cannot be located."""
    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def code(self) -> int | None:
        return self.response.get("code")


class TagLimitExceededException(MachineLearningError):
    _ERROR_CODE = "TagLimitExceededException"


EXCEPTIONS: dict[str, type[MachineLearningError]] = {
    "IdempotentParameterMismatchException": IdempotentParameterMismatchException,
    "InternalServerException": InternalServerException,
    "InvalidInputException": InvalidInputException,
    "InvalidTagException": InvalidTagException,
    "LimitExceededException": LimitExceededException,
    "PredictorNotMountedException": PredictorNotMountedException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "TagLimitExceededException": TagLimitExceededException,
}
