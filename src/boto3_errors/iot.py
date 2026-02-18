# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class IoTError(Boto3Error):
    _SERVICE = "iot"


class CertificateConflictException(IoTError):
    """Unable to verify the CA certificate used to sign the device certificate you are
    attempting to register. This is happens when you have registered more than one CA
    certificate that has the same subject field and public key.
    """

    _ERROR_CODE = "CertificateConflictException"


class CertificateStateException(IoTError):
    """The certificate operation is not allowed."""
    _ERROR_CODE = "CertificateStateException"


class CertificateValidationException(IoTError):
    """The certificate is invalid."""
    _ERROR_CODE = "CertificateValidationException"


class ConflictException(IoTError):
    """A resource with the same name already exists."""
    _ERROR_CODE = "ConflictException"

    @property
    def resource_id(self) -> str | None:
        """A resource with the same name already exists."""
        return self.response.get("resourceId")


class ConflictingResourceUpdateException(IoTError):
    """A conflicting resource update exception. This exception is thrown when two pending
    updates cause a conflict.
    """

    _ERROR_CODE = "ConflictingResourceUpdateException"


class DeleteConflictException(IoTError):
    """You can't delete the resource because it is attached to one or more resources."""
    _ERROR_CODE = "DeleteConflictException"


class IndexNotReadyException(IoTError):
    """The index is not ready."""
    _ERROR_CODE = "IndexNotReadyException"


class InternalException(IoTError):
    """An unexpected error has occurred."""
    _ERROR_CODE = "InternalException"


class InternalFailureException(IoTError):
    """An unexpected error has occurred."""
    _ERROR_CODE = "InternalFailureException"


class InternalServerException(IoTError):
    """Internal error from the service that indicates an unexpected error or that the
    service is unavailable.
    """

    _ERROR_CODE = "InternalServerException"


class InvalidAggregationException(IoTError):
    """The aggregation is invalid."""
    _ERROR_CODE = "InvalidAggregationException"


class InvalidQueryException(IoTError):
    """The query is invalid."""
    _ERROR_CODE = "InvalidQueryException"


class InvalidRequestException(IoTError):
    """The request is not valid."""
    _ERROR_CODE = "InvalidRequestException"


class InvalidResponseException(IoTError):
    """The response is invalid."""
    _ERROR_CODE = "InvalidResponseException"


class InvalidStateTransitionException(IoTError):
    """An attempt was made to change to an invalid state, for example by deleting a job or
    a job execution which is "IN_PROGRESS" without setting the `force` parameter.
    """

    _ERROR_CODE = "InvalidStateTransitionException"


class LimitExceededException(IoTError):
    """A limit has been exceeded."""
    _ERROR_CODE = "LimitExceededException"


class MalformedPolicyException(IoTError):
    """The policy documentation is not valid."""
    _ERROR_CODE = "MalformedPolicyException"


class NotConfiguredException(IoTError):
    """The resource is not configured."""
    _ERROR_CODE = "NotConfiguredException"


class RegistrationCodeValidationException(IoTError):
    """The registration code is invalid."""
    _ERROR_CODE = "RegistrationCodeValidationException"


class ResourceAlreadyExistsException(IoTError):
    """The resource already exists."""
    _ERROR_CODE = "ResourceAlreadyExistsException"

    @property
    def resource_arn(self) -> str | None:
        """The ARN of the resource that caused the exception."""
        return self.response.get("resourceArn")

    @property
    def resource_id(self) -> str | None:
        """The ID of the resource that caused the exception."""
        return self.response.get("resourceId")


class ResourceNotFoundException(IoTError):
    """The specified resource does not exist."""
    _ERROR_CODE = "ResourceNotFoundException"


class ResourceRegistrationFailureException(IoTError):
    """The resource registration failed."""
    _ERROR_CODE = "ResourceRegistrationFailureException"


class ServiceQuotaExceededException(IoTError):
    """A limit has been exceeded."""
    _ERROR_CODE = "ServiceQuotaExceededException"


class ServiceUnavailableException(IoTError):
    """The service is temporarily unavailable."""
    _ERROR_CODE = "ServiceUnavailableException"


class SqlParseException(IoTError):
    """The Rule-SQL expression can't be parsed correctly."""
    _ERROR_CODE = "SqlParseException"


class TaskAlreadyExistsException(IoTError):
    """This exception occurs if you attempt to start a task with the same task-id as an
    existing task but with a different clientRequestToken.
    """

    _ERROR_CODE = "TaskAlreadyExistsException"


class ThrottlingException(IoTError):
    """The rate exceeds the limit."""
    _ERROR_CODE = "ThrottlingException"


class TransferAlreadyCompletedException(IoTError):
    """You can't revert the certificate transfer because the transfer is already complete."""
    _ERROR_CODE = "TransferAlreadyCompletedException"


class TransferConflictException(IoTError):
    """You can't transfer the certificate because authorization policies are still
    attached.
    """

    _ERROR_CODE = "TransferConflictException"


class UnauthorizedException(IoTError):
    """You are not authorized to perform this operation."""
    _ERROR_CODE = "UnauthorizedException"


class ValidationException(IoTError):
    """The request is not valid."""
    _ERROR_CODE = "ValidationException"


class VersionConflictException(IoTError):
    """An exception thrown when the version of an entity specified with the
    `expectedVersion` parameter does not match the latest version in the system.
    """

    _ERROR_CODE = "VersionConflictException"


class VersionsLimitExceededException(IoTError):
    """The number of policy versions exceeds the limit."""
    _ERROR_CODE = "VersionsLimitExceededException"


EXCEPTIONS: dict[str, type[IoTError]] = {
    "CertificateConflictException": CertificateConflictException,
    "CertificateStateException": CertificateStateException,
    "CertificateValidationException": CertificateValidationException,
    "ConflictException": ConflictException,
    "ConflictingResourceUpdateException": ConflictingResourceUpdateException,
    "DeleteConflictException": DeleteConflictException,
    "IndexNotReadyException": IndexNotReadyException,
    "InternalException": InternalException,
    "InternalFailureException": InternalFailureException,
    "InternalServerException": InternalServerException,
    "InvalidAggregationException": InvalidAggregationException,
    "InvalidQueryException": InvalidQueryException,
    "InvalidRequestException": InvalidRequestException,
    "InvalidResponseException": InvalidResponseException,
    "InvalidStateTransitionException": InvalidStateTransitionException,
    "LimitExceededException": LimitExceededException,
    "MalformedPolicyException": MalformedPolicyException,
    "NotConfiguredException": NotConfiguredException,
    "RegistrationCodeValidationException": RegistrationCodeValidationException,
    "ResourceAlreadyExistsException": ResourceAlreadyExistsException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ResourceRegistrationFailureException": ResourceRegistrationFailureException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ServiceUnavailableException": ServiceUnavailableException,
    "SqlParseException": SqlParseException,
    "TaskAlreadyExistsException": TaskAlreadyExistsException,
    "ThrottlingException": ThrottlingException,
    "TransferAlreadyCompletedException": TransferAlreadyCompletedException,
    "TransferConflictException": TransferConflictException,
    "UnauthorizedException": UnauthorizedException,
    "ValidationException": ValidationException,
    "VersionConflictException": VersionConflictException,
    "VersionsLimitExceededException": VersionsLimitExceededException,
}
