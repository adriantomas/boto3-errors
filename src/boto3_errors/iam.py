# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class IAMError(Boto3Error):
    _SERVICE = "iam"


class ConcurrentModificationException(IAMError):
    """The request was rejected because multiple requests to change this object were
    submitted simultaneously. Wait a few minutes and submit your request again.
    """

    _ERROR_CODE = "ConcurrentModification"


class CredentialReportExpiredException(IAMError):
    """The request was rejected because the most recent credential report has expired. To
    generate a new credential report, use GenerateCredentialReport. For more information
    about credential report expiration, see Getting credential reports in the IAM User
    Guide.
    """

    _ERROR_CODE = "ReportExpired"


class CredentialReportNotPresentException(IAMError):
    """The request was rejected because the credential report does not exist. To generate a
    credential report, use GenerateCredentialReport.
    """

    _ERROR_CODE = "ReportNotPresent"


class CredentialReportNotReadyException(IAMError):
    """The request was rejected because the credential report is still being generated."""
    _ERROR_CODE = "ReportInProgress"


class DeleteConflictException(IAMError):
    """The request was rejected because it attempted to delete a resource that has attached
    subordinate entities. The error message describes these entities.
    """

    _ERROR_CODE = "DeleteConflict"


class DuplicateCertificateException(IAMError):
    """The request was rejected because the same certificate is associated with an IAM user
    in the account.
    """

    _ERROR_CODE = "DuplicateCertificate"


class DuplicateSSHPublicKeyException(IAMError):
    """The request was rejected because the SSH public key is already associated with the
    specified IAM user.
    """

    _ERROR_CODE = "DuplicateSSHPublicKey"


class EntityAlreadyExistsException(IAMError):
    """The request was rejected because it attempted to create a resource that already
    exists.
    """

    _ERROR_CODE = "EntityAlreadyExists"


class EntityTemporarilyUnmodifiableException(IAMError):
    """The request was rejected because it referenced an entity that is temporarily
    unmodifiable, such as a user name that was deleted and then recreated. The error
    indicates that the request is likely to succeed if you try again after waiting
    several minutes. The error message describes the entity.
    """

    _ERROR_CODE = "EntityTemporarilyUnmodifiable"


class InvalidAuthenticationCodeException(IAMError):
    """The request was rejected because the authentication code was not recognized. The
    error message describes the specific error.
    """

    _ERROR_CODE = "InvalidAuthenticationCode"


class InvalidCertificateException(IAMError):
    """The request was rejected because the certificate is invalid."""
    _ERROR_CODE = "InvalidCertificate"


class InvalidInputException(IAMError):
    """The request was rejected because an invalid or out-of-range value was supplied for
    an input parameter.
    """

    _ERROR_CODE = "InvalidInput"


class InvalidPublicKeyException(IAMError):
    """The request was rejected because the public key is malformed or otherwise invalid."""
    _ERROR_CODE = "InvalidPublicKey"


class InvalidUserTypeException(IAMError):
    """The request was rejected because the type of user for the transaction was incorrect."""
    _ERROR_CODE = "InvalidUserType"


class KeyPairMismatchException(IAMError):
    """The request was rejected because the public key certificate and the private key do
    not match.
    """

    _ERROR_CODE = "KeyPairMismatch"


class LimitExceededException(IAMError):
    """The request was rejected because it attempted to create resources beyond the current
    Amazon Web Services account limits. The error message describes the limit exceeded.
    """

    _ERROR_CODE = "LimitExceeded"


class MalformedCertificateException(IAMError):
    """The request was rejected because the certificate was malformed or expired. The error
    message describes the specific error.
    """

    _ERROR_CODE = "MalformedCertificate"


class MalformedPolicyDocumentException(IAMError):
    """The request was rejected because the policy document was malformed. The error
    message describes the specific error.
    """

    _ERROR_CODE = "MalformedPolicyDocument"


class NoSuchEntityException(IAMError):
    """The request was rejected because it referenced a resource entity that does not
    exist. The error message describes the resource.
    """

    _ERROR_CODE = "NoSuchEntity"


class PasswordPolicyViolationException(IAMError):
    """The request was rejected because the provided password did not meet the requirements
    imposed by the account password policy.
    """

    _ERROR_CODE = "PasswordPolicyViolation"


class PolicyEvaluationException(IAMError):
    """The request failed because a provided policy could not be successfully evaluated. An
    additional detailed message indicates the source of the failure.
    """

    _ERROR_CODE = "PolicyEvaluation"


class PolicyNotAttachableException(IAMError):
    """The request failed because Amazon Web Services service role policies can only be
    attached to the service-linked role for that service.
    """

    _ERROR_CODE = "PolicyNotAttachable"


class ReportGenerationLimitExceededException(IAMError):
    """The request failed because the maximum number of concurrent requests for this
    account are already running.
    """

    _ERROR_CODE = "ReportGenerationLimitExceeded"


class ServiceFailureException(IAMError):
    """The request processing has failed because of an unknown error, exception or failure."""
    _ERROR_CODE = "ServiceFailure"


class ServiceNotSupportedException(IAMError):
    """The specified service does not support service-specific credentials."""
    _ERROR_CODE = "NotSupportedService"


class UnmodifiableEntityException(IAMError):
    """The request was rejected because service-linked roles are protected Amazon Web
    Services resources. Only the service that depends on the service-linked role can
    modify or delete the role on your behalf. The error message includes the name of the
    service that depends on this service-linked role. You must request the change
    through that service.
    """

    _ERROR_CODE = "UnmodifiableEntity"


class UnrecognizedPublicKeyEncodingException(IAMError):
    """The request was rejected because the public key encoding format is unsupported or
    unrecognized.
    """

    _ERROR_CODE = "UnrecognizedPublicKeyEncoding"


EXCEPTIONS: dict[str, type[IAMError]] = {
    "ConcurrentModification": ConcurrentModificationException,
    "ReportExpired": CredentialReportExpiredException,
    "ReportNotPresent": CredentialReportNotPresentException,
    "ReportInProgress": CredentialReportNotReadyException,
    "DeleteConflict": DeleteConflictException,
    "DuplicateCertificate": DuplicateCertificateException,
    "DuplicateSSHPublicKey": DuplicateSSHPublicKeyException,
    "EntityAlreadyExists": EntityAlreadyExistsException,
    "EntityTemporarilyUnmodifiable": EntityTemporarilyUnmodifiableException,
    "InvalidAuthenticationCode": InvalidAuthenticationCodeException,
    "InvalidCertificate": InvalidCertificateException,
    "InvalidInput": InvalidInputException,
    "InvalidPublicKey": InvalidPublicKeyException,
    "InvalidUserType": InvalidUserTypeException,
    "KeyPairMismatch": KeyPairMismatchException,
    "LimitExceeded": LimitExceededException,
    "MalformedCertificate": MalformedCertificateException,
    "MalformedPolicyDocument": MalformedPolicyDocumentException,
    "NoSuchEntity": NoSuchEntityException,
    "PasswordPolicyViolation": PasswordPolicyViolationException,
    "PolicyEvaluation": PolicyEvaluationException,
    "PolicyNotAttachable": PolicyNotAttachableException,
    "ReportGenerationLimitExceeded": ReportGenerationLimitExceededException,
    "ServiceFailure": ServiceFailureException,
    "NotSupportedService": ServiceNotSupportedException,
    "UnmodifiableEntity": UnmodifiableEntityException,
    "UnrecognizedPublicKeyEncoding": UnrecognizedPublicKeyEncodingException,
}
