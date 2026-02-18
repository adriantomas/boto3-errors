# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class LambdaError(Boto3Error):
    _SERVICE = "lambda"


class CallbackTimeoutException(LambdaError):
    """The callback ID token has either expired or the callback associated with the token
    has already been closed.
    """

    _ERROR_CODE = "CallbackTimeoutException"

    @property
    def type(self) -> str | None:
        """The exception type."""
        return self.response.get("Type")


class CapacityProviderLimitExceededException(LambdaError):
    """The maximum number of capacity providers for your account has been exceeded. For
    more information, see Lambda quotas
    """

    _ERROR_CODE = "CapacityProviderLimitExceededException"

    @property
    def type(self) -> str | None:
        """The exception type."""
        return self.response.get("Type")


class CodeSigningConfigNotFoundException(LambdaError):
    """The specified code signing configuration does not exist."""
    _ERROR_CODE = "CodeSigningConfigNotFoundException"

    @property
    def type(self) -> str | None:
        return self.response.get("Type")


class CodeStorageExceededException(LambdaError):
    """Your Amazon Web Services account has exceeded its maximum total code size. For more
    information, see Lambda quotas.
    """

    _ERROR_CODE = "CodeStorageExceededException"

    @property
    def type(self) -> str | None:
        """The exception type."""
        return self.response.get("Type")


class CodeVerificationFailedException(LambdaError):
    """The code signature failed one or more of the validation checks for signature
    mismatch or expiry, and the code signing policy is set to ENFORCE. Lambda blocks the
    deployment.
    """

    _ERROR_CODE = "CodeVerificationFailedException"

    @property
    def type(self) -> str | None:
        return self.response.get("Type")


class DurableExecutionAlreadyStartedException(LambdaError):
    """The durable execution with the specified name has already been started. Each durable
    execution name must be unique within the function. Use a different name or check the
    status of the existing execution.
    """

    _ERROR_CODE = "DurableExecutionAlreadyStartedException"

    @property
    def type(self) -> str | None:
        """The exception type."""
        return self.response.get("Type")


class EC2AccessDeniedException(LambdaError):
    """Need additional permissions to configure VPC settings."""
    _ERROR_CODE = "EC2AccessDeniedException"

    @property
    def type(self) -> str | None:
        return self.response.get("Type")


class EC2ThrottledException(LambdaError):
    """Amazon EC2 throttled Lambda during Lambda function initialization using the
    execution role provided for the function.
    """

    _ERROR_CODE = "EC2ThrottledException"

    @property
    def type(self) -> str | None:
        return self.response.get("Type")


class EC2UnexpectedException(LambdaError):
    """Lambda received an unexpected Amazon EC2 client exception while setting up for the
    Lambda function.
    """

    _ERROR_CODE = "EC2UnexpectedException"

    @property
    def ec2_error_code(self) -> str | None:
        return self.response.get("EC2ErrorCode")

    @property
    def type(self) -> str | None:
        return self.response.get("Type")


class EFSIOException(LambdaError):
    """An error occurred when reading from or writing to a connected file system."""
    _ERROR_CODE = "EFSIOException"

    @property
    def type(self) -> str | None:
        return self.response.get("Type")


class EFSMountConnectivityException(LambdaError):
    """The Lambda function couldn't make a network connection to the configured file
    system.
    """

    _ERROR_CODE = "EFSMountConnectivityException"

    @property
    def type(self) -> str | None:
        return self.response.get("Type")


class EFSMountFailureException(LambdaError):
    """The Lambda function couldn't mount the configured file system due to a permission or
    configuration issue.
    """

    _ERROR_CODE = "EFSMountFailureException"

    @property
    def type(self) -> str | None:
        return self.response.get("Type")


class EFSMountTimeoutException(LambdaError):
    """The Lambda function made a network connection to the configured file system, but the
    mount operation timed out.
    """

    _ERROR_CODE = "EFSMountTimeoutException"

    @property
    def type(self) -> str | None:
        return self.response.get("Type")


class ENILimitReachedException(LambdaError):
    """Lambda couldn't create an elastic network interface in the VPC, specified as part of
    Lambda function configuration, because the limit for network interfaces has been
    reached. For more information, see Lambda quotas.
    """

    _ERROR_CODE = "ENILimitReachedException"

    @property
    def type(self) -> str | None:
        return self.response.get("Type")


class FunctionVersionsPerCapacityProviderLimitExceededException(LambdaError):
    """The maximum number of function versions that can be associated with a single
    capacity provider has been exceeded. For more information, see Lambda quotas.
    """

    _ERROR_CODE = "FunctionVersionsPerCapacityProviderLimitExceededException"

    @property
    def type(self) -> str | None:
        """The exception type."""
        return self.response.get("Type")


class InvalidCodeSignatureException(LambdaError):
    """The code signature failed the integrity check. If the integrity check fails, then
    Lambda blocks deployment, even if the code signing policy is set to WARN.
    """

    _ERROR_CODE = "InvalidCodeSignatureException"

    @property
    def type(self) -> str | None:
        return self.response.get("Type")


class InvalidParameterValueException(LambdaError):
    """One of the parameters in the request is not valid."""
    _ERROR_CODE = "InvalidParameterValueException"

    @property
    def type(self) -> str | None:
        """The exception type."""
        return self.response.get("Type")


class InvalidRequestContentException(LambdaError):
    """The request body could not be parsed as JSON, or a request header is invalid. For
    example, the 'x-amzn-RequestId' header is not a valid UUID string.
    """

    _ERROR_CODE = "InvalidRequestContentException"

    @property
    def type(self) -> str | None:
        """The exception type."""
        return self.response.get("Type")


class InvalidRuntimeException(LambdaError):
    """The runtime or runtime version specified is not supported."""
    _ERROR_CODE = "InvalidRuntimeException"

    @property
    def type(self) -> str | None:
        return self.response.get("Type")


class InvalidSecurityGroupIDException(LambdaError):
    """The security group ID provided in the Lambda function VPC configuration is not
    valid.
    """

    _ERROR_CODE = "InvalidSecurityGroupIDException"

    @property
    def type(self) -> str | None:
        return self.response.get("Type")


class InvalidSubnetIDException(LambdaError):
    """The subnet ID provided in the Lambda function VPC configuration is not valid."""
    _ERROR_CODE = "InvalidSubnetIDException"

    @property
    def type(self) -> str | None:
        return self.response.get("Type")


class InvalidZipFileException(LambdaError):
    """Lambda could not unzip the deployment package."""
    _ERROR_CODE = "InvalidZipFileException"

    @property
    def type(self) -> str | None:
        return self.response.get("Type")


class KMSAccessDeniedException(LambdaError):
    """Lambda couldn't decrypt the environment variables because KMS access was denied.
    Check the Lambda function's KMS permissions.
    """

    _ERROR_CODE = "KMSAccessDeniedException"

    @property
    def type(self) -> str | None:
        return self.response.get("Type")


class KMSDisabledException(LambdaError):
    """Lambda couldn't decrypt the environment variables because the KMS key used is
    disabled. Check the Lambda function's KMS key settings.
    """

    _ERROR_CODE = "KMSDisabledException"

    @property
    def type(self) -> str | None:
        return self.response.get("Type")


class KMSInvalidStateException(LambdaError):
    """Lambda couldn't decrypt the environment variables because the state of the KMS key
    used is not valid for Decrypt. Check the function's KMS key settings.
    """

    _ERROR_CODE = "KMSInvalidStateException"

    @property
    def type(self) -> str | None:
        return self.response.get("Type")


class KMSNotFoundException(LambdaError):
    """Lambda couldn't decrypt the environment variables because the KMS key was not found.
    Check the function's KMS key settings.
    """

    _ERROR_CODE = "KMSNotFoundException"

    @property
    def type(self) -> str | None:
        return self.response.get("Type")


class NoPublishedVersionException(LambdaError):
    """The function has no published versions available."""
    _ERROR_CODE = "NoPublishedVersionException"

    @property
    def type(self) -> str | None:
        """The exception type."""
        return self.response.get("Type")


class PolicyLengthExceededException(LambdaError):
    """The permissions policy for the resource is too large. For more information, see
    Lambda quotas.
    """

    _ERROR_CODE = "PolicyLengthExceededException"

    @property
    def type(self) -> str | None:
        return self.response.get("Type")


class PreconditionFailedException(LambdaError):
    """The RevisionId provided does not match the latest RevisionId for the Lambda function
    or alias.

    - For AddPermission and RemovePermission API operations: Call `GetPolicy` to
      retrieve the latest RevisionId for your resource.
    - For all other API operations: Call `GetFunction` or `GetAlias` to retrieve the
      latest RevisionId for your resource.
    """

    _ERROR_CODE = "PreconditionFailedException"

    @property
    def type(self) -> str | None:
        """The exception type."""
        return self.response.get("Type")


class ProvisionedConcurrencyConfigNotFoundException(LambdaError):
    """The specified configuration does not exist."""
    _ERROR_CODE = "ProvisionedConcurrencyConfigNotFoundException"

    @property
    def type(self) -> str | None:
        return self.response.get("Type")


class RecursiveInvocationException(LambdaError):
    """Lambda has detected your function being invoked in a recursive loop with other
    Amazon Web Services resources and stopped your function's invocation.
    """

    _ERROR_CODE = "RecursiveInvocationException"

    @property
    def type(self) -> str | None:
        """The exception type."""
        return self.response.get("Type")


class RequestTooLargeException(LambdaError):
    """The request payload exceeded the `Invoke` request body JSON input quota. For more
    information, see Lambda quotas.
    """

    _ERROR_CODE = "RequestTooLargeException"

    @property
    def type(self) -> str | None:
        return self.response.get("Type")


class ResourceConflictException(LambdaError):
    """The resource already exists, or another operation is in progress."""
    _ERROR_CODE = "ResourceConflictException"

    @property
    def type(self) -> str | None:
        """The exception type."""
        return self.response.get("Type")


class ResourceInUseException(LambdaError):
    """The operation conflicts with the resource's availability. For example, you tried to
    update an event source mapping in the CREATING state, or you tried to delete an
    event source mapping currently UPDATING.
    """

    _ERROR_CODE = "ResourceInUseException"

    @property
    def type(self) -> str | None:
        return self.response.get("Type")


class ResourceNotFoundException(LambdaError):
    """The resource specified in the request does not exist."""
    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def type(self) -> str | None:
        return self.response.get("Type")


class ResourceNotReadyException(LambdaError):
    """The function is inactive and its VPC connection is no longer available. Wait for the
    VPC connection to reestablish and try again.
    """

    _ERROR_CODE = "ResourceNotReadyException"

    @property
    def type(self) -> str | None:
        """The exception type."""
        return self.response.get("Type")


class SerializedRequestEntityTooLargeException(LambdaError):
    """The request payload exceeded the maximum allowed size for serialized request
    entities.
    """

    _ERROR_CODE = "SerializedRequestEntityTooLargeException"

    @property
    def type(self) -> str | None:
        """The error type."""
        return self.response.get("Type")


class ServiceException(LambdaError):
    """The Lambda service encountered an internal error."""
    _ERROR_CODE = "ServiceException"

    @property
    def type(self) -> str | None:
        return self.response.get("Type")


class SnapStartException(LambdaError):
    """The `afterRestore()` runtime hook encountered an error. For more information, check
    the Amazon CloudWatch logs.
    """

    _ERROR_CODE = "SnapStartException"

    @property
    def type(self) -> str | None:
        return self.response.get("Type")


class SnapStartNotReadyException(LambdaError):
    """Lambda is initializing your function. You can invoke the function when the function
    state becomes `Active`.
    """

    _ERROR_CODE = "SnapStartNotReadyException"

    @property
    def type(self) -> str | None:
        return self.response.get("Type")


class SnapStartTimeoutException(LambdaError):
    """Lambda couldn't restore the snapshot within the timeout limit."""
    _ERROR_CODE = "SnapStartTimeoutException"

    @property
    def type(self) -> str | None:
        return self.response.get("Type")


class SubnetIPAddressLimitReachedException(LambdaError):
    """Lambda couldn't set up VPC access for the Lambda function because one or more
    configured subnets has no available IP addresses.
    """

    _ERROR_CODE = "SubnetIPAddressLimitReachedException"

    @property
    def type(self) -> str | None:
        return self.response.get("Type")


class TooManyRequestsException(LambdaError):
    """The request throughput limit was exceeded. For more information, see Lambda quotas."""
    _ERROR_CODE = "TooManyRequestsException"

    @property
    def reason(self) -> str | None:
        return self.response.get("Reason")

    @property
    def type(self) -> str | None:
        return self.response.get("Type")

    @property
    def retry_after_seconds(self) -> str | None:
        """The number of seconds the caller should wait before retrying."""
        return self.response.get("retryAfterSeconds")


class UnsupportedMediaTypeException(LambdaError):
    """The content type of the `Invoke` request body is not JSON."""
    _ERROR_CODE = "UnsupportedMediaTypeException"

    @property
    def type(self) -> str | None:
        return self.response.get("Type")


EXCEPTIONS: dict[str, type[LambdaError]] = {
    "CallbackTimeoutException": CallbackTimeoutException,
    "CapacityProviderLimitExceededException": CapacityProviderLimitExceededException,
    "CodeSigningConfigNotFoundException": CodeSigningConfigNotFoundException,
    "CodeStorageExceededException": CodeStorageExceededException,
    "CodeVerificationFailedException": CodeVerificationFailedException,
    "DurableExecutionAlreadyStartedException": DurableExecutionAlreadyStartedException,
    "EC2AccessDeniedException": EC2AccessDeniedException,
    "EC2ThrottledException": EC2ThrottledException,
    "EC2UnexpectedException": EC2UnexpectedException,
    "EFSIOException": EFSIOException,
    "EFSMountConnectivityException": EFSMountConnectivityException,
    "EFSMountFailureException": EFSMountFailureException,
    "EFSMountTimeoutException": EFSMountTimeoutException,
    "ENILimitReachedException": ENILimitReachedException,
    "FunctionVersionsPerCapacityProviderLimitExceededException": FunctionVersionsPerCapacityProviderLimitExceededException,
    "InvalidCodeSignatureException": InvalidCodeSignatureException,
    "InvalidParameterValueException": InvalidParameterValueException,
    "InvalidRequestContentException": InvalidRequestContentException,
    "InvalidRuntimeException": InvalidRuntimeException,
    "InvalidSecurityGroupIDException": InvalidSecurityGroupIDException,
    "InvalidSubnetIDException": InvalidSubnetIDException,
    "InvalidZipFileException": InvalidZipFileException,
    "KMSAccessDeniedException": KMSAccessDeniedException,
    "KMSDisabledException": KMSDisabledException,
    "KMSInvalidStateException": KMSInvalidStateException,
    "KMSNotFoundException": KMSNotFoundException,
    "NoPublishedVersionException": NoPublishedVersionException,
    "PolicyLengthExceededException": PolicyLengthExceededException,
    "PreconditionFailedException": PreconditionFailedException,
    "ProvisionedConcurrencyConfigNotFoundException": ProvisionedConcurrencyConfigNotFoundException,
    "RecursiveInvocationException": RecursiveInvocationException,
    "RequestTooLargeException": RequestTooLargeException,
    "ResourceConflictException": ResourceConflictException,
    "ResourceInUseException": ResourceInUseException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ResourceNotReadyException": ResourceNotReadyException,
    "SerializedRequestEntityTooLargeException": SerializedRequestEntityTooLargeException,
    "ServiceException": ServiceException,
    "SnapStartException": SnapStartException,
    "SnapStartNotReadyException": SnapStartNotReadyException,
    "SnapStartTimeoutException": SnapStartTimeoutException,
    "SubnetIPAddressLimitReachedException": SubnetIPAddressLimitReachedException,
    "TooManyRequestsException": TooManyRequestsException,
    "UnsupportedMediaTypeException": UnsupportedMediaTypeException,
}
