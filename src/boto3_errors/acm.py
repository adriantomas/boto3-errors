# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class ACMError(Boto3Error):
    _SERVICE = "acm"


class AccessDeniedException(ACMError):
    """You do not have access required to perform this action."""
    _ERROR_CODE = "AccessDeniedException"


class ConflictException(ACMError):
    """You are trying to update a resource or configuration that is already being created
    or updated. Wait for the previous operation to finish and try again.
    """

    _ERROR_CODE = "ConflictException"


class InvalidArgsException(ACMError):
    """One or more of request parameters specified is not valid."""
    _ERROR_CODE = "InvalidArgsException"


class InvalidArnException(ACMError):
    """The requested Amazon Resource Name (ARN) does not refer to an existing resource."""
    _ERROR_CODE = "InvalidArnException"


class InvalidDomainValidationOptionsException(ACMError):
    """One or more values in the DomainValidationOption structure is incorrect."""
    _ERROR_CODE = "InvalidDomainValidationOptionsException"


class InvalidParameterException(ACMError):
    """An input parameter was invalid."""
    _ERROR_CODE = "InvalidParameterException"


class InvalidStateException(ACMError):
    """Processing has reached an invalid state."""
    _ERROR_CODE = "InvalidStateException"


class InvalidTagException(ACMError):
    """One or both of the values that make up the key-value pair is not valid. For example,
    you cannot specify a tag value that begins with `aws:`.
    """

    _ERROR_CODE = "InvalidTagException"


class LimitExceededException(ACMError):
    """An ACM quota has been exceeded."""
    _ERROR_CODE = "LimitExceededException"


class RequestInProgressException(ACMError):
    """The certificate request is in process and the certificate in your account has not
    yet been issued.
    """

    _ERROR_CODE = "RequestInProgressException"


class ResourceInUseException(ACMError):
    """The certificate is in use by another Amazon Web Services service in the caller's
    account. Remove the association and try again.
    """

    _ERROR_CODE = "ResourceInUseException"


class ResourceNotFoundException(ACMError):
    """The specified certificate cannot be found in the caller's account or the caller's
    account cannot be found.
    """

    _ERROR_CODE = "ResourceNotFoundException"


class TagPolicyException(ACMError):
    """A specified tag did not comply with an existing tag policy and was rejected."""
    _ERROR_CODE = "TagPolicyException"


class ThrottlingException(ACMError):
    """The request was denied because it exceeded a quota."""
    _ERROR_CODE = "ThrottlingException"


class TooManyTagsException(ACMError):
    """The request contains too many tags. Try the request again with fewer tags."""
    _ERROR_CODE = "TooManyTagsException"


class ValidationException(ACMError):
    """The supplied input failed to satisfy constraints of an Amazon Web Services service."""
    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[ACMError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InvalidArgsException": InvalidArgsException,
    "InvalidArnException": InvalidArnException,
    "InvalidDomainValidationOptionsException": InvalidDomainValidationOptionsException,
    "InvalidParameterException": InvalidParameterException,
    "InvalidStateException": InvalidStateException,
    "InvalidTagException": InvalidTagException,
    "LimitExceededException": LimitExceededException,
    "RequestInProgressException": RequestInProgressException,
    "ResourceInUseException": ResourceInUseException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "TagPolicyException": TagPolicyException,
    "ThrottlingException": ThrottlingException,
    "TooManyTagsException": TooManyTagsException,
    "ValidationException": ValidationException,
}
