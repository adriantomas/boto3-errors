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


class ExpiredTradeInTokenException(STSError):
    """The trade-in token provided in the request has expired and can no longer be
    exchanged for credentials. Request a new token and retry the operation.
    """

    _ERROR_CODE = "ExpiredTradeInTokenException"


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


class InsufficientSessionLifetimeException(STSError):
    """The request was rejected because the requested `DurationSeconds` is greater than the
    remaining lifetime of the calling session. `GetScopedCredentials` cannot extend a
    session beyond its original expiration. Request a duration that is less than or
    equal to the calling session's remaining lifetime, or omit `DurationSeconds` to
    inherit it.
    """

    _ERROR_CODE = "InsufficientSessionLifetime"


class InvalidAuthorizationMessageException(STSError):
    """The error returned if the message passed to `DecodeAuthorizationMessage` was
    invalid. This can happen if the token contains invalid characters, such as line
    breaks, or if the message has expired.
    """

    _ERROR_CODE = "InvalidAuthorizationMessageException"


class InvalidContextAssertionException(STSError):
    """The request was rejected because the context assertion that was provided is invalid.
    This can happen if the context assertion supplied in the `ProvidedContexts`
    parameter is malformed, has expired, or does not match a trusted context provider.
    """

    _ERROR_CODE = "InvalidContextAssertion"


class InvalidIdentityTokenException(STSError):
    """The web identity token that was passed could not be validated by Amazon Web
    Services. Get a new identity token from the identity provider and then retry the
    request.
    """

    _ERROR_CODE = "InvalidIdentityToken"


class InvalidSubjectCredentialsException(STSError):
    """The request was rejected because the session used to call `GetScopedCredentials` is
    not a valid session. The calling session's credentials could not be validated or
    resolved.
    """

    _ERROR_CODE = "InvalidSubjectCredentials"


class JWTPayloadSizeExceededException(STSError):
    """The requested token payload size exceeds the maximum allowed size. Reduce the number
    of request tags included in the `GetWebIdentityToken` API call to reduce the token
    payload size.
    """

    _ERROR_CODE = "JWTPayloadSizeExceededException"


class MalformedPolicyDocumentException(STSError):
    """The request was rejected because the policy document was malformed. The error
    message describes the specific error.
    """

    _ERROR_CODE = "MalformedPolicyDocument"


class OutboundWebIdentityFederationDisabledException(STSError):
    """The outbound web identity federation feature is not enabled for this account. To use
    this feature, you must first enable it through the Amazon Web Services Management
    Console or API.
    """

    _ERROR_CODE = "OutboundWebIdentityFederationDisabledException"


class PackedPolicyTooLargeException(STSError):
    """The request was rejected because the session token exceeded the maximum allowed
    size. The error message reports the session token size and the maximum allowed size,
    both in bytes. Session policies and session tags add to the session token size. For
    more information, see Passing Session Tags in STS in the IAM User Guide.

    You might receive this error even though you meet the individual session policy and
    session tag limits. Monitor `SessionTokenUtilization` to track how close the session
    token is to the maximum allowed size. For more information, see IAM and STS Entity
    Character Limits in the IAM User Guide.
    """

    _ERROR_CODE = "PackedPolicyTooLarge"


class RegionDisabledException(STSError):
    """STS is not activated in the requested region for the account that is being asked to
    generate credentials. The account administrator must use the IAM console to activate
    STS in that region. For more information, see Activating and Deactivating STS in an
    Amazon Web Services Region in the IAM User Guide.
    """

    _ERROR_CODE = "RegionDisabledException"


class SessionDurationEscalationException(STSError):
    """The requested token duration would extend the session beyond its original expiration
    time. You cannot use this operation to extend the lifetime of a session beyond what
    was granted when the session was originally created.
    """

    _ERROR_CODE = "SessionDurationEscalationException"


EXCEPTIONS: dict[str, type[STSError]] = {
    "ExpiredTokenException": ExpiredTokenException,
    "ExpiredTradeInTokenException": ExpiredTradeInTokenException,
    "IDPCommunicationError": IDPCommunicationErrorException,
    "IDPRejectedClaim": IDPRejectedClaimException,
    "InsufficientSessionLifetime": InsufficientSessionLifetimeException,
    "InvalidAuthorizationMessageException": InvalidAuthorizationMessageException,
    "InvalidContextAssertion": InvalidContextAssertionException,
    "InvalidIdentityToken": InvalidIdentityTokenException,
    "InvalidSubjectCredentials": InvalidSubjectCredentialsException,
    "JWTPayloadSizeExceededException": JWTPayloadSizeExceededException,
    "MalformedPolicyDocument": MalformedPolicyDocumentException,
    "OutboundWebIdentityFederationDisabledException": OutboundWebIdentityFederationDisabledException,
    "PackedPolicyTooLarge": PackedPolicyTooLargeException,
    "RegionDisabledException": RegionDisabledException,
    "SessionDurationEscalationException": SessionDurationEscalationException,
}
