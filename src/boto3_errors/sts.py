# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class STSError(Boto3Error):
    _SERVICE = "sts"


class ExpiredTokenException(STSError):
    """The web identity token that was passed is expired or is not valid. Get a new
    identity token from the identity provider and then retry the request.
    """

    _ERROR_CODE = "ExpiredTokenException"


class IDPCommunicationErrorException(STSError):
    """The request could not be fulfilled because the identity provider (IDP) that was
    asked to verify the incoming identity token could not be reached. This is often a
    transient error caused by network conditions. Retry the request a limited number of
    times so that you don't exceed the request rate. If the error persists, the identity
    provider might be down or not responding.
    """

    _ERROR_CODE = "IDPCommunicationError"


class IDPRejectedClaimException(STSError):
    """The identity provider (IdP) reported that authentication failed. This might be
    because the claim is invalid.

    If this error is returned for the `AssumeRoleWithWebIdentity` operation, it can also
    mean that the claim has expired or has been explicitly revoked.
    """

    _ERROR_CODE = "IDPRejectedClaim"


class InvalidAuthorizationMessageException(STSError):
    """The error returned if the message passed to `DecodeAuthorizationMessage` was
    invalid. This can happen if the token contains invalid characters, such as
    linebreaks.
    """

    _ERROR_CODE = "InvalidAuthorizationMessageException"


class InvalidIdentityTokenException(STSError):
    """The web identity token that was passed could not be validated by Amazon Web
    Services. Get a new identity token from the identity provider and then retry the
    request.
    """

    _ERROR_CODE = "InvalidIdentityToken"


class MalformedPolicyDocumentException(STSError):
    """The request was rejected because the policy document was malformed. The error
    message describes the specific error.
    """

    _ERROR_CODE = "MalformedPolicyDocument"


class PackedPolicyTooLargeException(STSError):
    """The request was rejected because the total packed size of the session policies and
    session tags combined was too large. An Amazon Web Services conversion compresses
    the session policy document, session policy ARNs, and session tags into a packed
    binary format that has a separate limit. The error message indicates by percentage
    how close the policies and tags are to the upper size limit. For more information,
    see Passing Session Tags in STS in the IAM User Guide.

    You could receive this error even though you meet other defined session policy and
    session tag limits. For more information, see IAM and STS Entity Character Limits in
    the IAM User Guide.
    """

    _ERROR_CODE = "PackedPolicyTooLarge"


class RegionDisabledException(STSError):
    """STS is not activated in the requested region for the account that is being asked to
    generate credentials. The account administrator must use the IAM console to activate
    STS in that region. For more information, see Activating and Deactivating Amazon Web
    Services STS in an Amazon Web Services Region in the IAM User Guide.
    """

    _ERROR_CODE = "RegionDisabledException"


EXCEPTIONS: dict[str, type[STSError]] = {
    "ExpiredTokenException": ExpiredTokenException,
    "IDPCommunicationError": IDPCommunicationErrorException,
    "IDPRejectedClaim": IDPRejectedClaimException,
    "InvalidAuthorizationMessageException": InvalidAuthorizationMessageException,
    "InvalidIdentityToken": InvalidIdentityTokenException,
    "MalformedPolicyDocument": MalformedPolicyDocumentException,
    "PackedPolicyTooLarge": PackedPolicyTooLargeException,
    "RegionDisabledException": RegionDisabledException,
}
