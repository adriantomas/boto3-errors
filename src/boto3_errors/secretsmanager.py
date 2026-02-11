# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class SecretsManagerError(Boto3Error):
    _SERVICE = "secretsmanager"


class DecryptionFailure(SecretsManagerError):
    """Secrets Manager can't decrypt the protected secret text using the provided KMS key."""
    _ERROR_CODE = "DecryptionFailure"


class EncryptionFailure(SecretsManagerError):
    """Secrets Manager can't encrypt the protected secret text using the provided KMS key.
    Check that the KMS key is available, enabled, and not in an invalid state. For more
    information, see Key state: Effect on your KMS key.
    """

    _ERROR_CODE = "EncryptionFailure"


class InternalServiceError(SecretsManagerError):
    """An error occurred on the server side."""
    _ERROR_CODE = "InternalServiceError"


class InvalidNextTokenException(SecretsManagerError):
    """The `NextToken` value is invalid."""
    _ERROR_CODE = "InvalidNextTokenException"


class InvalidParameterException(SecretsManagerError):
    """The parameter name or value is invalid."""
    _ERROR_CODE = "InvalidParameterException"


class InvalidRequestException(SecretsManagerError):
    """A parameter value is not valid for the current state of the resource.

    Possible causes:

    - The secret is scheduled for deletion.
    - You tried to enable rotation on a secret that doesn't already have a Lambda
      function ARN configured and you didn't include such an ARN as a parameter in this
      call.
    - The secret is managed by another service, and you must use that service to update
      it. For more information, see Secrets managed by other Amazon Web Services
      services.
    """

    _ERROR_CODE = "InvalidRequestException"


class LimitExceededException(SecretsManagerError):
    """The request failed because it would exceed one of the Secrets Manager quotas."""
    _ERROR_CODE = "LimitExceededException"


class MalformedPolicyDocumentException(SecretsManagerError):
    """The resource policy has syntax errors."""
    _ERROR_CODE = "MalformedPolicyDocumentException"


class PreconditionNotMetException(SecretsManagerError):
    """The request failed because you did not complete all the prerequisite steps."""
    _ERROR_CODE = "PreconditionNotMetException"


class PublicPolicyException(SecretsManagerError):
    """The `BlockPublicPolicy` parameter is set to true, and the resource policy did not
    prevent broad access to the secret.
    """

    _ERROR_CODE = "PublicPolicyException"


class ResourceExistsException(SecretsManagerError):
    """A resource with the ID you requested already exists."""
    _ERROR_CODE = "ResourceExistsException"


class ResourceNotFoundException(SecretsManagerError):
    """Secrets Manager can't find the resource that you asked for."""
    _ERROR_CODE = "ResourceNotFoundException"


EXCEPTIONS: dict[str, type[SecretsManagerError]] = {
    "DecryptionFailure": DecryptionFailure,
    "EncryptionFailure": EncryptionFailure,
    "InternalServiceError": InternalServiceError,
    "InvalidNextTokenException": InvalidNextTokenException,
    "InvalidParameterException": InvalidParameterException,
    "InvalidRequestException": InvalidRequestException,
    "LimitExceededException": LimitExceededException,
    "MalformedPolicyDocumentException": MalformedPolicyDocumentException,
    "PreconditionNotMetException": PreconditionNotMetException,
    "PublicPolicyException": PublicPolicyException,
    "ResourceExistsException": ResourceExistsException,
    "ResourceNotFoundException": ResourceNotFoundException,
}
