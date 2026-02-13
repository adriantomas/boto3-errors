# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class SagemakerEdgeError(Boto3Error):
    _SERVICE = "sagemaker-edge"


class InternalServiceException(SagemakerEdgeError):
    """An internal failure occurred. Try your request again. If the problem persists,
    contact Amazon Web Services customer support.
    """

    _ERROR_CODE = "InternalServiceException"


EXCEPTIONS: dict[str, type[SagemakerEdgeError]] = {
    "InternalServiceException": InternalServiceException,
}
