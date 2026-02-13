# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class CloudHSMV2Error(Boto3Error):
    _SERVICE = "cloudhsmv2"


class CloudHsmAccessDeniedException(CloudHSMV2Error):
    """The request was rejected because the requester does not have permission to perform
    the requested operation.
    """

    _ERROR_CODE = "CloudHsmAccessDeniedException"


class CloudHsmInternalFailureException(CloudHSMV2Error):
    """The request was rejected because of an CloudHSM internal failure. The request can be
    retried.
    """

    _ERROR_CODE = "CloudHsmInternalFailureException"


class CloudHsmInvalidRequestException(CloudHSMV2Error):
    """The request was rejected because it is not a valid request."""
    _ERROR_CODE = "CloudHsmInvalidRequestException"


class CloudHsmResourceLimitExceededException(CloudHSMV2Error):
    """The request was rejected because it exceeds an CloudHSM limit."""
    _ERROR_CODE = "CloudHsmResourceLimitExceededException"


class CloudHsmResourceNotFoundException(CloudHSMV2Error):
    """The request was rejected because it refers to a resource that cannot be found."""
    _ERROR_CODE = "CloudHsmResourceNotFoundException"


class CloudHsmServiceException(CloudHSMV2Error):
    """The request was rejected because an error occurred."""
    _ERROR_CODE = "CloudHsmServiceException"


class CloudHsmTagException(CloudHSMV2Error):
    """The request was rejected because of a tagging failure. Verify the tag conditions in
    all applicable policies, and then retry the request.
    """

    _ERROR_CODE = "CloudHsmTagException"


EXCEPTIONS: dict[str, type[CloudHSMV2Error]] = {
    "CloudHsmAccessDeniedException": CloudHsmAccessDeniedException,
    "CloudHsmInternalFailureException": CloudHsmInternalFailureException,
    "CloudHsmInvalidRequestException": CloudHsmInvalidRequestException,
    "CloudHsmResourceLimitExceededException": CloudHsmResourceLimitExceededException,
    "CloudHsmResourceNotFoundException": CloudHsmResourceNotFoundException,
    "CloudHsmServiceException": CloudHsmServiceException,
    "CloudHsmTagException": CloudHsmTagException,
}
