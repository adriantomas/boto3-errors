# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class EC2InstanceConnectError(Boto3Error):
    _SERVICE = "ec2-instance-connect"


class AuthException(EC2InstanceConnectError):
    """Either your AWS credentials are not valid or you do not have access to the EC2
    instance.
    """

    _ERROR_CODE = "AuthException"


class EC2InstanceNotFoundException(EC2InstanceConnectError):
    """The specified instance was not found."""
    _ERROR_CODE = "EC2InstanceNotFoundException"


class EC2InstanceStateInvalidException(EC2InstanceConnectError):
    """Unable to connect because the instance is not in a valid state. Connecting to a
    stopped or terminated instance is not supported. If the instance is stopped, start
    your instance, and try to connect again.
    """

    _ERROR_CODE = "EC2InstanceStateInvalidException"


class EC2InstanceTypeInvalidException(EC2InstanceConnectError):
    """The instance type is not supported for connecting via the serial console. Only Nitro
    instance types are currently supported.
    """

    _ERROR_CODE = "EC2InstanceTypeInvalidException"


class EC2InstanceUnavailableException(EC2InstanceConnectError):
    """The instance is currently unavailable. Wait a few minutes and try again."""
    _ERROR_CODE = "EC2InstanceUnavailableException"


class InvalidArgsException(EC2InstanceConnectError):
    """One of the parameters is not valid."""
    _ERROR_CODE = "InvalidArgsException"


class SerialConsoleAccessDisabledException(EC2InstanceConnectError):
    """Your account is not authorized to use the EC2 Serial Console. To authorize your
    account, run the EnableSerialConsoleAccess API. For more information, see
    EnableSerialConsoleAccess in the Amazon EC2 API Reference.
    """

    _ERROR_CODE = "SerialConsoleAccessDisabledException"


class SerialConsoleSessionLimitExceededException(EC2InstanceConnectError):
    """The instance currently has 1 active serial console session. Only 1 session is
    supported at a time.
    """

    _ERROR_CODE = "SerialConsoleSessionLimitExceededException"


class SerialConsoleSessionUnavailableException(EC2InstanceConnectError):
    """Unable to start a serial console session. Please try again."""
    _ERROR_CODE = "SerialConsoleSessionUnavailableException"


class SerialConsoleSessionUnsupportedException(EC2InstanceConnectError):
    """Your instance's BIOS version is unsupported for serial console connection. Reboot
    your instance to update its BIOS, and then try again to connect.
    """

    _ERROR_CODE = "SerialConsoleSessionUnsupportedException"


class ServiceException(EC2InstanceConnectError):
    """The service encountered an error. Follow the instructions in the error message and
    try again.
    """

    _ERROR_CODE = "ServiceException"


class ThrottlingException(EC2InstanceConnectError):
    """The requests were made too frequently and have been throttled. Wait a while and try
    again. To increase the limit on your request frequency, contact AWS Support.
    """

    _ERROR_CODE = "ThrottlingException"


EXCEPTIONS: dict[str, type[EC2InstanceConnectError]] = {
    "AuthException": AuthException,
    "EC2InstanceNotFoundException": EC2InstanceNotFoundException,
    "EC2InstanceStateInvalidException": EC2InstanceStateInvalidException,
    "EC2InstanceTypeInvalidException": EC2InstanceTypeInvalidException,
    "EC2InstanceUnavailableException": EC2InstanceUnavailableException,
    "InvalidArgsException": InvalidArgsException,
    "SerialConsoleAccessDisabledException": SerialConsoleAccessDisabledException,
    "SerialConsoleSessionLimitExceededException": SerialConsoleSessionLimitExceededException,
    "SerialConsoleSessionUnavailableException": SerialConsoleSessionUnavailableException,
    "SerialConsoleSessionUnsupportedException": SerialConsoleSessionUnsupportedException,
    "ServiceException": ServiceException,
    "ThrottlingException": ThrottlingException,
}
