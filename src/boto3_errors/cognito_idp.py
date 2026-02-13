# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class CognitoIdentityProviderError(Boto3Error):
    _SERVICE = "cognito-idp"


class AliasExistsException(CognitoIdentityProviderError):
    """This exception is thrown when a user tries to confirm the account with an email
    address or phone number that has already been supplied as an alias for a different
    user profile. This exception indicates that an account with this email address or
    phone already exists in a user pool that you've configured to use email address or
    phone number as a sign-in alias.
    """

    _ERROR_CODE = "AliasExistsException"


class CodeDeliveryFailureException(CognitoIdentityProviderError):
    """This exception is thrown when a verification code fails to deliver successfully."""
    _ERROR_CODE = "CodeDeliveryFailureException"


class CodeMismatchException(CognitoIdentityProviderError):
    """This exception is thrown if the provided code doesn't match what the server was
    expecting.
    """

    _ERROR_CODE = "CodeMismatchException"


class ConcurrentModificationException(CognitoIdentityProviderError):
    """This exception is thrown if two or more modifications are happening concurrently."""
    _ERROR_CODE = "ConcurrentModificationException"


class DeviceKeyExistsException(CognitoIdentityProviderError):
    """This exception is thrown when a user attempts to confirm a device with a device key
    that already exists.
    """

    _ERROR_CODE = "DeviceKeyExistsException"


class DuplicateProviderException(CognitoIdentityProviderError):
    """This exception is thrown when the provider is already supported by the user pool."""
    _ERROR_CODE = "DuplicateProviderException"


class EnableSoftwareTokenMFAException(CognitoIdentityProviderError):
    """This exception is thrown when there is a code mismatch and the service fails to
    configure the software token TOTP multi-factor authentication (MFA).
    """

    _ERROR_CODE = "EnableSoftwareTokenMFAException"


class ExpiredCodeException(CognitoIdentityProviderError):
    """This exception is thrown if a code has expired."""
    _ERROR_CODE = "ExpiredCodeException"


class FeatureUnavailableInTierException(CognitoIdentityProviderError):
    """This exception is thrown when a feature you attempted to configure isn't available
    in your current feature plan.
    """

    _ERROR_CODE = "FeatureUnavailableInTierException"


class ForbiddenException(CognitoIdentityProviderError):
    """This exception is thrown when WAF doesn't allow your request based on a web ACL
    that's associated with your user pool.
    """

    _ERROR_CODE = "ForbiddenException"


class GroupExistsException(CognitoIdentityProviderError):
    """This exception is thrown when Amazon Cognito encounters a group that already exists
    in the user pool.
    """

    _ERROR_CODE = "GroupExistsException"


class InternalErrorException(CognitoIdentityProviderError):
    """This exception is thrown when Amazon Cognito encounters an internal error."""
    _ERROR_CODE = "InternalErrorException"


class InvalidEmailRoleAccessPolicyException(CognitoIdentityProviderError):
    """This exception is thrown when Amazon Cognito isn't allowed to use your email
    identity. HTTP status code: 400.
    """

    _ERROR_CODE = "InvalidEmailRoleAccessPolicyException"


class InvalidLambdaResponseException(CognitoIdentityProviderError):
    """This exception is thrown when Amazon Cognito encounters an invalid Lambda response."""
    _ERROR_CODE = "InvalidLambdaResponseException"


class InvalidOAuthFlowException(CognitoIdentityProviderError):
    """This exception is thrown when the specified OAuth flow is not valid."""
    _ERROR_CODE = "InvalidOAuthFlowException"


class InvalidParameterException(CognitoIdentityProviderError):
    """This exception is thrown when the Amazon Cognito service encounters an invalid
    parameter.
    """

    _ERROR_CODE = "InvalidParameterException"

    @property
    def reason_code(self) -> str | None:
        """The reason code of the exception."""
        return self.response.get("reasonCode")


class InvalidPasswordException(CognitoIdentityProviderError):
    """This exception is thrown when Amazon Cognito encounters an invalid password."""
    _ERROR_CODE = "InvalidPasswordException"


class InvalidSmsRoleAccessPolicyException(CognitoIdentityProviderError):
    """This exception is returned when the role provided for SMS configuration doesn't have
    permission to publish using Amazon SNS.
    """

    _ERROR_CODE = "InvalidSmsRoleAccessPolicyException"


class InvalidSmsRoleTrustRelationshipException(CognitoIdentityProviderError):
    """This exception is thrown when the trust relationship is not valid for the role
    provided for SMS configuration. This can happen if you don't trust `cognito-
    idp.amazonaws.com` or the external ID provided in the role does not match what is
    provided in the SMS configuration for the user pool.
    """

    _ERROR_CODE = "InvalidSmsRoleTrustRelationshipException"


class InvalidUserPoolConfigurationException(CognitoIdentityProviderError):
    """This exception is thrown when the user pool configuration is not valid."""
    _ERROR_CODE = "InvalidUserPoolConfigurationException"


class LimitExceededException(CognitoIdentityProviderError):
    """This exception is thrown when a user exceeds the limit for a requested Amazon Web
    Services resource.
    """

    _ERROR_CODE = "LimitExceededException"


class MFAMethodNotFoundException(CognitoIdentityProviderError):
    """This exception is thrown when Amazon Cognito can't find a multi-factor
    authentication (MFA) method.
    """

    _ERROR_CODE = "MFAMethodNotFoundException"


class ManagedLoginBrandingExistsException(CognitoIdentityProviderError):
    """This exception is thrown when you attempt to apply a managed login branding style to
    an app client that already has an assigned style.
    """

    _ERROR_CODE = "ManagedLoginBrandingExistsException"


class NotAuthorizedException(CognitoIdentityProviderError):
    """This exception is thrown when a user isn't authorized."""
    _ERROR_CODE = "NotAuthorizedException"


class PasswordHistoryPolicyViolationException(CognitoIdentityProviderError):
    """The message returned when a user's new password matches a previous password and
    doesn't comply with the password-history policy.
    """

    _ERROR_CODE = "PasswordHistoryPolicyViolationException"


class PasswordResetRequiredException(CognitoIdentityProviderError):
    """This exception is thrown when a password reset is required."""
    _ERROR_CODE = "PasswordResetRequiredException"


class PreconditionNotMetException(CognitoIdentityProviderError):
    """This exception is thrown when a precondition is not met."""
    _ERROR_CODE = "PreconditionNotMetException"


class RefreshTokenReuseException(CognitoIdentityProviderError):
    """This exception is throw when your application requests token refresh with a refresh
    token that has been invalidated by refresh-token rotation.
    """

    _ERROR_CODE = "RefreshTokenReuseException"


class ResourceNotFoundException(CognitoIdentityProviderError):
    """This exception is thrown when the Amazon Cognito service can't find the requested
    resource.
    """

    _ERROR_CODE = "ResourceNotFoundException"


class ScopeDoesNotExistException(CognitoIdentityProviderError):
    """This exception is thrown when the specified scope doesn't exist."""
    _ERROR_CODE = "ScopeDoesNotExistException"


class SoftwareTokenMFANotFoundException(CognitoIdentityProviderError):
    """This exception is thrown when the software token time-based one-time password (TOTP)
    multi-factor authentication (MFA) isn't activated for the user pool.
    """

    _ERROR_CODE = "SoftwareTokenMFANotFoundException"


class TermsExistsException(CognitoIdentityProviderError):
    """Terms document names must be unique to the app client. This exception is thrown when
    you attempt to create terms documents with a duplicate `TermsName`.
    """

    _ERROR_CODE = "TermsExistsException"


class TierChangeNotAllowedException(CognitoIdentityProviderError):
    """This exception is thrown when you've attempted to change your feature plan but the
    operation isn't permitted.
    """

    _ERROR_CODE = "TierChangeNotAllowedException"


class TooManyFailedAttemptsException(CognitoIdentityProviderError):
    """This exception is thrown when the user has made too many failed attempts for a given
    action, such as sign-in.
    """

    _ERROR_CODE = "TooManyFailedAttemptsException"


class TooManyRequestsException(CognitoIdentityProviderError):
    """This exception is thrown when the user has made too many requests for a given
    operation.
    """

    _ERROR_CODE = "TooManyRequestsException"


class UnauthorizedException(CognitoIdentityProviderError):
    """Exception that is thrown when the request isn't authorized. This can happen due to
    an invalid access token in the request.
    """

    _ERROR_CODE = "UnauthorizedException"


class UnexpectedLambdaException(CognitoIdentityProviderError):
    """This exception is thrown when Amazon Cognito encounters an unexpected exception with
    Lambda.
    """

    _ERROR_CODE = "UnexpectedLambdaException"


class UnsupportedIdentityProviderException(CognitoIdentityProviderError):
    """This exception is thrown when the specified identifier isn't supported."""
    _ERROR_CODE = "UnsupportedIdentityProviderException"


class UnsupportedOperationException(CognitoIdentityProviderError):
    """Exception that is thrown when you attempt to perform an operation that isn't enabled
    for the user pool client.
    """

    _ERROR_CODE = "UnsupportedOperationException"


class UnsupportedTokenTypeException(CognitoIdentityProviderError):
    """Exception that is thrown when an unsupported token is passed to an operation."""
    _ERROR_CODE = "UnsupportedTokenTypeException"


class UnsupportedUserStateException(CognitoIdentityProviderError):
    """The request failed because the user is in an unsupported state."""
    _ERROR_CODE = "UnsupportedUserStateException"


class UserImportInProgressException(CognitoIdentityProviderError):
    """This exception is thrown when you're trying to modify a user pool while a user
    import job is in progress for that pool.
    """

    _ERROR_CODE = "UserImportInProgressException"


class UserLambdaValidationException(CognitoIdentityProviderError):
    """This exception is thrown when the Amazon Cognito service encounters a user
    validation exception with the Lambda service.
    """

    _ERROR_CODE = "UserLambdaValidationException"


class UserNotConfirmedException(CognitoIdentityProviderError):
    """This exception is thrown when a user isn't confirmed successfully."""
    _ERROR_CODE = "UserNotConfirmedException"


class UserNotFoundException(CognitoIdentityProviderError):
    """This exception is thrown when a user isn't found."""
    _ERROR_CODE = "UserNotFoundException"


class UserPoolAddOnNotEnabledException(CognitoIdentityProviderError):
    """This exception is thrown when user pool add-ons aren't enabled."""
    _ERROR_CODE = "UserPoolAddOnNotEnabledException"


class UserPoolTaggingException(CognitoIdentityProviderError):
    """This exception is thrown when a user pool tag can't be set or updated."""
    _ERROR_CODE = "UserPoolTaggingException"


class UsernameExistsException(CognitoIdentityProviderError):
    """This exception is thrown when Amazon Cognito encounters a user name that already
    exists in the user pool.
    """

    _ERROR_CODE = "UsernameExistsException"


class WebAuthnChallengeNotFoundException(CognitoIdentityProviderError):
    """This exception is thrown when the challenge from `StartWebAuthn` registration has
    expired.
    """

    _ERROR_CODE = "WebAuthnChallengeNotFoundException"


class WebAuthnClientMismatchException(CognitoIdentityProviderError):
    """This exception is thrown when the access token is for a different client than the
    one in the original `StartWebAuthnRegistration` request.
    """

    _ERROR_CODE = "WebAuthnClientMismatchException"


class WebAuthnConfigurationMissingException(CognitoIdentityProviderError):
    """This exception is thrown when a user pool doesn't have a configured relying party id
    or a user pool domain.
    """

    _ERROR_CODE = "WebAuthnConfigurationMissingException"


class WebAuthnCredentialNotSupportedException(CognitoIdentityProviderError):
    """This exception is thrown when a user presents passkey credentials from an
    unsupported device or provider.
    """

    _ERROR_CODE = "WebAuthnCredentialNotSupportedException"


class WebAuthnNotEnabledException(CognitoIdentityProviderError):
    """This exception is thrown when the passkey feature isn't enabled for the user pool."""
    _ERROR_CODE = "WebAuthnNotEnabledException"


class WebAuthnOriginNotAllowedException(CognitoIdentityProviderError):
    """This exception is thrown when the passkey credential's registration origin does not
    align with the user pool relying party id.
    """

    _ERROR_CODE = "WebAuthnOriginNotAllowedException"


class WebAuthnRelyingPartyMismatchException(CognitoIdentityProviderError):
    """This exception is thrown when the given passkey credential is associated with a
    different relying party ID than the user pool relying party ID.
    """

    _ERROR_CODE = "WebAuthnRelyingPartyMismatchException"


EXCEPTIONS: dict[str, type[CognitoIdentityProviderError]] = {
    "AliasExistsException": AliasExistsException,
    "CodeDeliveryFailureException": CodeDeliveryFailureException,
    "CodeMismatchException": CodeMismatchException,
    "ConcurrentModificationException": ConcurrentModificationException,
    "DeviceKeyExistsException": DeviceKeyExistsException,
    "DuplicateProviderException": DuplicateProviderException,
    "EnableSoftwareTokenMFAException": EnableSoftwareTokenMFAException,
    "ExpiredCodeException": ExpiredCodeException,
    "FeatureUnavailableInTierException": FeatureUnavailableInTierException,
    "ForbiddenException": ForbiddenException,
    "GroupExistsException": GroupExistsException,
    "InternalErrorException": InternalErrorException,
    "InvalidEmailRoleAccessPolicyException": InvalidEmailRoleAccessPolicyException,
    "InvalidLambdaResponseException": InvalidLambdaResponseException,
    "InvalidOAuthFlowException": InvalidOAuthFlowException,
    "InvalidParameterException": InvalidParameterException,
    "InvalidPasswordException": InvalidPasswordException,
    "InvalidSmsRoleAccessPolicyException": InvalidSmsRoleAccessPolicyException,
    "InvalidSmsRoleTrustRelationshipException": InvalidSmsRoleTrustRelationshipException,
    "InvalidUserPoolConfigurationException": InvalidUserPoolConfigurationException,
    "LimitExceededException": LimitExceededException,
    "MFAMethodNotFoundException": MFAMethodNotFoundException,
    "ManagedLoginBrandingExistsException": ManagedLoginBrandingExistsException,
    "NotAuthorizedException": NotAuthorizedException,
    "PasswordHistoryPolicyViolationException": PasswordHistoryPolicyViolationException,
    "PasswordResetRequiredException": PasswordResetRequiredException,
    "PreconditionNotMetException": PreconditionNotMetException,
    "RefreshTokenReuseException": RefreshTokenReuseException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ScopeDoesNotExistException": ScopeDoesNotExistException,
    "SoftwareTokenMFANotFoundException": SoftwareTokenMFANotFoundException,
    "TermsExistsException": TermsExistsException,
    "TierChangeNotAllowedException": TierChangeNotAllowedException,
    "TooManyFailedAttemptsException": TooManyFailedAttemptsException,
    "TooManyRequestsException": TooManyRequestsException,
    "UnauthorizedException": UnauthorizedException,
    "UnexpectedLambdaException": UnexpectedLambdaException,
    "UnsupportedIdentityProviderException": UnsupportedIdentityProviderException,
    "UnsupportedOperationException": UnsupportedOperationException,
    "UnsupportedTokenTypeException": UnsupportedTokenTypeException,
    "UnsupportedUserStateException": UnsupportedUserStateException,
    "UserImportInProgressException": UserImportInProgressException,
    "UserLambdaValidationException": UserLambdaValidationException,
    "UserNotConfirmedException": UserNotConfirmedException,
    "UserNotFoundException": UserNotFoundException,
    "UserPoolAddOnNotEnabledException": UserPoolAddOnNotEnabledException,
    "UserPoolTaggingException": UserPoolTaggingException,
    "UsernameExistsException": UsernameExistsException,
    "WebAuthnChallengeNotFoundException": WebAuthnChallengeNotFoundException,
    "WebAuthnClientMismatchException": WebAuthnClientMismatchException,
    "WebAuthnConfigurationMissingException": WebAuthnConfigurationMissingException,
    "WebAuthnCredentialNotSupportedException": WebAuthnCredentialNotSupportedException,
    "WebAuthnNotEnabledException": WebAuthnNotEnabledException,
    "WebAuthnOriginNotAllowedException": WebAuthnOriginNotAllowedException,
    "WebAuthnRelyingPartyMismatchException": WebAuthnRelyingPartyMismatchException,
}
