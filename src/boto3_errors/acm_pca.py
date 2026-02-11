# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class ACMPCAError(Boto3Error):
    _SERVICE = "acm-pca"


class CertificateMismatchException(ACMPCAError):
    """The certificate authority certificate you are importing does not comply with
    conditions specified in the certificate that signed it.
    """

    _ERROR_CODE = "CertificateMismatchException"


class ConcurrentModificationException(ACMPCAError):
    """A previous update to your private CA is still ongoing."""
    _ERROR_CODE = "ConcurrentModificationException"


class InvalidArgsException(ACMPCAError):
    """One or more of the specified arguments was not valid."""
    _ERROR_CODE = "InvalidArgsException"


class InvalidArnException(ACMPCAError):
    """The requested Amazon Resource Name (ARN) does not refer to an existing resource."""
    _ERROR_CODE = "InvalidArnException"


class InvalidNextTokenException(ACMPCAError):
    """The token specified in the `NextToken` argument is not valid. Use the token returned
    from your previous call to ListCertificateAuthorities.
    """

    _ERROR_CODE = "InvalidNextTokenException"


class InvalidPolicyException(ACMPCAError):
    """The resource policy is invalid or is missing a required statement. For general
    information about IAM policy and statement structure, see Overview of JSON Policies.
    """

    _ERROR_CODE = "InvalidPolicyException"


class InvalidRequestException(ACMPCAError):
    """The request action cannot be performed or is prohibited."""
    _ERROR_CODE = "InvalidRequestException"


class InvalidStateException(ACMPCAError):
    """The state of the private CA does not allow this action to occur."""
    _ERROR_CODE = "InvalidStateException"


class InvalidTagException(ACMPCAError):
    """The tag associated with the CA is not valid. The invalid argument is contained in
    the message field.
    """

    _ERROR_CODE = "InvalidTagException"


class LimitExceededException(ACMPCAError):
    """An Amazon Web Services Private CA quota has been exceeded. See the exception message
    returned to determine the quota that was exceeded.
    """

    _ERROR_CODE = "LimitExceededException"


class LockoutPreventedException(ACMPCAError):
    """The current action was prevented because it would lock the caller out from
    performing subsequent actions. Verify that the specified parameters would not result
    in the caller being denied access to the resource.
    """

    _ERROR_CODE = "LockoutPreventedException"


class MalformedCSRException(ACMPCAError):
    """The certificate signing request is invalid."""
    _ERROR_CODE = "MalformedCSRException"


class MalformedCertificateException(ACMPCAError):
    """One or more fields in the certificate are invalid."""
    _ERROR_CODE = "MalformedCertificateException"


class PermissionAlreadyExistsException(ACMPCAError):
    """The designated permission has already been given to the user."""
    _ERROR_CODE = "PermissionAlreadyExistsException"


class RequestAlreadyProcessedException(ACMPCAError):
    """Your request has already been completed."""
    _ERROR_CODE = "RequestAlreadyProcessedException"


class RequestFailedException(ACMPCAError):
    """The request has failed for an unspecified reason."""
    _ERROR_CODE = "RequestFailedException"


class RequestInProgressException(ACMPCAError):
    """Your request is already in progress."""
    _ERROR_CODE = "RequestInProgressException"


class ResourceNotFoundException(ACMPCAError):
    """A resource such as a private CA, S3 bucket, certificate, audit report, or policy
    cannot be found.
    """

    _ERROR_CODE = "ResourceNotFoundException"


class TooManyTagsException(ACMPCAError):
    """You can associate up to 50 tags with a private CA. Exception information is
    contained in the exception message field.
    """

    _ERROR_CODE = "TooManyTagsException"


EXCEPTIONS: dict[str, type[ACMPCAError]] = {
    "CertificateMismatchException": CertificateMismatchException,
    "ConcurrentModificationException": ConcurrentModificationException,
    "InvalidArgsException": InvalidArgsException,
    "InvalidArnException": InvalidArnException,
    "InvalidNextTokenException": InvalidNextTokenException,
    "InvalidPolicyException": InvalidPolicyException,
    "InvalidRequestException": InvalidRequestException,
    "InvalidStateException": InvalidStateException,
    "InvalidTagException": InvalidTagException,
    "LimitExceededException": LimitExceededException,
    "LockoutPreventedException": LockoutPreventedException,
    "MalformedCSRException": MalformedCSRException,
    "MalformedCertificateException": MalformedCertificateException,
    "PermissionAlreadyExistsException": PermissionAlreadyExistsException,
    "RequestAlreadyProcessedException": RequestAlreadyProcessedException,
    "RequestFailedException": RequestFailedException,
    "RequestInProgressException": RequestInProgressException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "TooManyTagsException": TooManyTagsException,
}
