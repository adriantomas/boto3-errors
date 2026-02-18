# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class EFSError(Boto3Error):
    _SERVICE = "efs"


class AccessPointAlreadyExists(EFSError):
    """Returned if the access point that you are trying to create already exists, with the
    creation token you provided in the request.
    """

    _ERROR_CODE = "AccessPointAlreadyExists"

    @property
    def access_point_id(self) -> str | None:
        return self.response.get("AccessPointId")

    @property
    def error_code(self) -> str | None:
        return self.response.get("ErrorCode")


class AccessPointLimitExceeded(EFSError):
    """Returned if the Amazon Web Services account has already created the maximum number
    of access points allowed per file system. For more informaton, see
    https://docs.aws.amazon.com/efs/latest/ug/limits.html#limits-efs-resources-per-
    account-per-region.
    """

    _ERROR_CODE = "AccessPointLimitExceeded"

    @property
    def error_code(self) -> str | None:
        return self.response.get("ErrorCode")


class AccessPointNotFound(EFSError):
    """Returned if the specified `AccessPointId` value doesn't exist in the requester's
    Amazon Web Services account.
    """

    _ERROR_CODE = "AccessPointNotFound"

    @property
    def error_code(self) -> str | None:
        return self.response.get("ErrorCode")


class AvailabilityZonesMismatch(EFSError):
    """Returned if the Availability Zone that was specified for a mount target is different
    from the Availability Zone that was specified for One Zone storage. For more
    information, see Regional and One Zone storage redundancy.
    """

    _ERROR_CODE = "AvailabilityZonesMismatch"

    @property
    def error_code(self) -> str | None:
        return self.response.get("ErrorCode")


class BadRequest(EFSError):
    """Returned if the request is malformed or contains an error such as an invalid
    parameter value or a missing required parameter.
    """

    _ERROR_CODE = "BadRequest"

    @property
    def error_code(self) -> str | None:
        return self.response.get("ErrorCode")


class ConflictException(EFSError):
    """Returned if the source file system in a replication is encrypted but the destination
    file system is unencrypted.
    """

    _ERROR_CODE = "ConflictException"

    @property
    def error_code(self) -> str | None:
        return self.response.get("ErrorCode")


class DependencyTimeout(EFSError):
    """The service timed out trying to fulfill the request, and the client should try the
    call again.
    """

    _ERROR_CODE = "DependencyTimeout"

    @property
    def error_code(self) -> str | None:
        return self.response.get("ErrorCode")


class FileSystemAlreadyExists(EFSError):
    """Returned if the file system you are trying to create already exists, with the
    creation token you provided.
    """

    _ERROR_CODE = "FileSystemAlreadyExists"

    @property
    def error_code(self) -> str | None:
        return self.response.get("ErrorCode")

    @property
    def file_system_id(self) -> str | None:
        return self.response.get("FileSystemId")


class FileSystemInUse(EFSError):
    """Returned if a file system has mount targets."""
    _ERROR_CODE = "FileSystemInUse"

    @property
    def error_code(self) -> str | None:
        return self.response.get("ErrorCode")


class FileSystemLimitExceeded(EFSError):
    """Returned if the Amazon Web Services account has already created the maximum number
    of file systems allowed per account.
    """

    _ERROR_CODE = "FileSystemLimitExceeded"

    @property
    def error_code(self) -> str | None:
        return self.response.get("ErrorCode")


class FileSystemNotFound(EFSError):
    """Returned if the specified `FileSystemId` value doesn't exist in the requester's
    Amazon Web Services account.
    """

    _ERROR_CODE = "FileSystemNotFound"

    @property
    def error_code(self) -> str | None:
        return self.response.get("ErrorCode")


class IncorrectFileSystemLifeCycleState(EFSError):
    """Returned if the file system's lifecycle state is not "available"."""
    _ERROR_CODE = "IncorrectFileSystemLifeCycleState"

    @property
    def error_code(self) -> str | None:
        return self.response.get("ErrorCode")


class IncorrectMountTargetState(EFSError):
    """Returned if the mount target is not in the correct state for the operation."""
    _ERROR_CODE = "IncorrectMountTargetState"

    @property
    def error_code(self) -> str | None:
        return self.response.get("ErrorCode")


class InsufficientThroughputCapacity(EFSError):
    """Returned if there's not enough capacity to provision additional throughput. This
    value might be returned when you try to create a file system in provisioned
    throughput mode, when you attempt to increase the provisioned throughput of an
    existing file system, or when you attempt to change an existing file system from
    Bursting Throughput to Provisioned Throughput mode. Try again later.
    """

    _ERROR_CODE = "InsufficientThroughputCapacity"

    @property
    def error_code(self) -> str | None:
        return self.response.get("ErrorCode")


class InternalServerError(EFSError):
    """Returned if an error occurred on the server side."""
    _ERROR_CODE = "InternalServerError"

    @property
    def error_code(self) -> str | None:
        return self.response.get("ErrorCode")


class InvalidPolicyException(EFSError):
    """Returned if the `FileSystemPolicy` is malformed or contains an error such as a
    parameter value that is not valid or a missing required parameter. Returned in the
    case of a policy lockout safety check error.
    """

    _ERROR_CODE = "InvalidPolicyException"

    @property
    def error_code(self) -> str | None:
        return self.response.get("ErrorCode")


class IpAddressInUse(EFSError):
    """Returned if the request specified an `IpAddress` that is already in use in the
    subnet.
    """

    _ERROR_CODE = "IpAddressInUse"

    @property
    def error_code(self) -> str | None:
        return self.response.get("ErrorCode")


class MountTargetConflict(EFSError):
    """Returned if the mount target would violate one of the specified restrictions based
    on the file system's existing mount targets.
    """

    _ERROR_CODE = "MountTargetConflict"

    @property
    def error_code(self) -> str | None:
        return self.response.get("ErrorCode")


class MountTargetNotFound(EFSError):
    """Returned if there is no mount target with the specified ID found in the caller's
    Amazon Web Services account.
    """

    _ERROR_CODE = "MountTargetNotFound"

    @property
    def error_code(self) -> str | None:
        return self.response.get("ErrorCode")


class NetworkInterfaceLimitExceeded(EFSError):
    """The calling account has reached the limit for elastic network interfaces for the
    specific Amazon Web Services Region. Either delete some network interfaces or
    request that the account quota be raised. For more information, see Amazon VPC
    Quotas in the Amazon VPC User Guide (see the Network interfaces per Region entry in
    the Network interfaces table).
    """

    _ERROR_CODE = "NetworkInterfaceLimitExceeded"

    @property
    def error_code(self) -> str | None:
        return self.response.get("ErrorCode")


class NoFreeAddressesInSubnet(EFSError):
    """Returned if `IpAddress` was not specified in the request and there are no free IP
    addresses in the subnet.
    """

    _ERROR_CODE = "NoFreeAddressesInSubnet"

    @property
    def error_code(self) -> str | None:
        return self.response.get("ErrorCode")


class PolicyNotFound(EFSError):
    """Returned if `no backup` is specified for a One Zone EFS file system."""
    _ERROR_CODE = "PolicyNotFound"

    @property
    def error_code(self) -> str | None:
        return self.response.get("ErrorCode")


class ReplicationAlreadyExists(EFSError):
    """Returned if the file system is already included in a replication configuration.>"""
    _ERROR_CODE = "ReplicationAlreadyExists"

    @property
    def error_code(self) -> str | None:
        return self.response.get("ErrorCode")


class ReplicationNotFound(EFSError):
    """Returned if the specified file system does not have a replication configuration."""
    _ERROR_CODE = "ReplicationNotFound"

    @property
    def error_code(self) -> str | None:
        """ReplicationNotFound"""
        return self.response.get("ErrorCode")


class SecurityGroupLimitExceeded(EFSError):
    """Returned if the number of `SecurityGroups` specified in the request is greater than
    the limit, which is based on account quota. Either delete some security groups or
    request that the account quota be raised. For more information, see Amazon VPC
    Quotas in the Amazon VPC User Guide (see the Security Groups table).
    """

    _ERROR_CODE = "SecurityGroupLimitExceeded"

    @property
    def error_code(self) -> str | None:
        return self.response.get("ErrorCode")


class SecurityGroupNotFound(EFSError):
    """Returned if one of the specified security groups doesn't exist in the subnet's
    virtual private cloud (VPC).
    """

    _ERROR_CODE = "SecurityGroupNotFound"

    @property
    def error_code(self) -> str | None:
        return self.response.get("ErrorCode")


class SubnetNotFound(EFSError):
    """Returned if there is no subnet with ID `SubnetId` provided in the request."""
    _ERROR_CODE = "SubnetNotFound"

    @property
    def error_code(self) -> str | None:
        return self.response.get("ErrorCode")


class ThrottlingException(EFSError):
    """Returned when the `CreateAccessPoint` API action is called too quickly and the
    number of Access Points on the file system is nearing the limit of 120.
    """

    _ERROR_CODE = "ThrottlingException"

    @property
    def error_code(self) -> str | None:
        return self.response.get("ErrorCode")


class ThroughputLimitExceeded(EFSError):
    """Returned if the throughput mode or amount of provisioned throughput can't be changed
    because the throughput limit of 1024 MiB/s has been reached.
    """

    _ERROR_CODE = "ThroughputLimitExceeded"

    @property
    def error_code(self) -> str | None:
        return self.response.get("ErrorCode")


class TooManyRequests(EFSError):
    """Returned if you don’t wait at least 24 hours before either changing the throughput
    mode, or decreasing the Provisioned Throughput value.
    """

    _ERROR_CODE = "TooManyRequests"

    @property
    def error_code(self) -> str | None:
        return self.response.get("ErrorCode")


class UnsupportedAvailabilityZone(EFSError):
    """Returned if the requested Amazon EFS functionality is not available in the specified
    Availability Zone.
    """

    _ERROR_CODE = "UnsupportedAvailabilityZone"

    @property
    def error_code(self) -> str | None:
        return self.response.get("ErrorCode")


class ValidationException(EFSError):
    """Returned if the Backup service is not available in the Amazon Web Services Region in
    which the request was made.
    """

    _ERROR_CODE = "ValidationException"

    @property
    def error_code(self) -> str | None:
        return self.response.get("ErrorCode")


EXCEPTIONS: dict[str, type[EFSError]] = {
    "AccessPointAlreadyExists": AccessPointAlreadyExists,
    "AccessPointLimitExceeded": AccessPointLimitExceeded,
    "AccessPointNotFound": AccessPointNotFound,
    "AvailabilityZonesMismatch": AvailabilityZonesMismatch,
    "BadRequest": BadRequest,
    "ConflictException": ConflictException,
    "DependencyTimeout": DependencyTimeout,
    "FileSystemAlreadyExists": FileSystemAlreadyExists,
    "FileSystemInUse": FileSystemInUse,
    "FileSystemLimitExceeded": FileSystemLimitExceeded,
    "FileSystemNotFound": FileSystemNotFound,
    "IncorrectFileSystemLifeCycleState": IncorrectFileSystemLifeCycleState,
    "IncorrectMountTargetState": IncorrectMountTargetState,
    "InsufficientThroughputCapacity": InsufficientThroughputCapacity,
    "InternalServerError": InternalServerError,
    "InvalidPolicyException": InvalidPolicyException,
    "IpAddressInUse": IpAddressInUse,
    "MountTargetConflict": MountTargetConflict,
    "MountTargetNotFound": MountTargetNotFound,
    "NetworkInterfaceLimitExceeded": NetworkInterfaceLimitExceeded,
    "NoFreeAddressesInSubnet": NoFreeAddressesInSubnet,
    "PolicyNotFound": PolicyNotFound,
    "ReplicationAlreadyExists": ReplicationAlreadyExists,
    "ReplicationNotFound": ReplicationNotFound,
    "SecurityGroupLimitExceeded": SecurityGroupLimitExceeded,
    "SecurityGroupNotFound": SecurityGroupNotFound,
    "SubnetNotFound": SubnetNotFound,
    "ThrottlingException": ThrottlingException,
    "ThroughputLimitExceeded": ThroughputLimitExceeded,
    "TooManyRequests": TooManyRequests,
    "UnsupportedAvailabilityZone": UnsupportedAvailabilityZone,
    "ValidationException": ValidationException,
}
