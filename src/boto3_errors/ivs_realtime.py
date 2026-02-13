# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class IVSRealTimeError(Boto3Error):
    _SERVICE = "ivs-realtime"


class AccessDeniedException(IVSRealTimeError):
    _ERROR_CODE = "AccessDeniedException"

    @property
    def access_control_allow_origin(self) -> str | None:
        return self.response.get("accessControlAllowOrigin")

    @property
    def access_control_expose_headers(self) -> str | None:
        return self.response.get("accessControlExposeHeaders")

    @property
    def cache_control(self) -> str | None:
        return self.response.get("cacheControl")

    @property
    def content_security_policy(self) -> str | None:
        return self.response.get("contentSecurityPolicy")

    @property
    def strict_transport_security(self) -> str | None:
        return self.response.get("strictTransportSecurity")

    @property
    def x_content_type_options(self) -> str | None:
        return self.response.get("xContentTypeOptions")

    @property
    def x_frame_options(self) -> str | None:
        return self.response.get("xFrameOptions")

    @property
    def x_amzn_error_type(self) -> str | None:
        return self.response.get("xAmznErrorType")

    @property
    def exception_message(self) -> str | None:
        """User does not have sufficient access to perform this action."""
        return self.response.get("exceptionMessage")


class ConflictException(IVSRealTimeError):
    _ERROR_CODE = "ConflictException"

    @property
    def access_control_allow_origin(self) -> str | None:
        return self.response.get("accessControlAllowOrigin")

    @property
    def access_control_expose_headers(self) -> str | None:
        return self.response.get("accessControlExposeHeaders")

    @property
    def cache_control(self) -> str | None:
        return self.response.get("cacheControl")

    @property
    def content_security_policy(self) -> str | None:
        return self.response.get("contentSecurityPolicy")

    @property
    def strict_transport_security(self) -> str | None:
        return self.response.get("strictTransportSecurity")

    @property
    def x_content_type_options(self) -> str | None:
        return self.response.get("xContentTypeOptions")

    @property
    def x_frame_options(self) -> str | None:
        return self.response.get("xFrameOptions")

    @property
    def x_amzn_error_type(self) -> str | None:
        return self.response.get("xAmznErrorType")

    @property
    def exception_message(self) -> str | None:
        """Updating or deleting a resource can cause an inconsistent state."""
        return self.response.get("exceptionMessage")


class InternalServerException(IVSRealTimeError):
    _ERROR_CODE = "InternalServerException"

    @property
    def access_control_allow_origin(self) -> str | None:
        return self.response.get("accessControlAllowOrigin")

    @property
    def access_control_expose_headers(self) -> str | None:
        return self.response.get("accessControlExposeHeaders")

    @property
    def cache_control(self) -> str | None:
        return self.response.get("cacheControl")

    @property
    def content_security_policy(self) -> str | None:
        return self.response.get("contentSecurityPolicy")

    @property
    def strict_transport_security(self) -> str | None:
        return self.response.get("strictTransportSecurity")

    @property
    def x_content_type_options(self) -> str | None:
        return self.response.get("xContentTypeOptions")

    @property
    def x_frame_options(self) -> str | None:
        return self.response.get("xFrameOptions")

    @property
    def x_amzn_error_type(self) -> str | None:
        return self.response.get("xAmznErrorType")

    @property
    def exception_message(self) -> str | None:
        """Unexpected error during processing of request."""
        return self.response.get("exceptionMessage")


class PendingVerification(IVSRealTimeError):
    _ERROR_CODE = "PendingVerification"

    @property
    def access_control_allow_origin(self) -> str | None:
        return self.response.get("accessControlAllowOrigin")

    @property
    def access_control_expose_headers(self) -> str | None:
        return self.response.get("accessControlExposeHeaders")

    @property
    def cache_control(self) -> str | None:
        return self.response.get("cacheControl")

    @property
    def content_security_policy(self) -> str | None:
        return self.response.get("contentSecurityPolicy")

    @property
    def strict_transport_security(self) -> str | None:
        return self.response.get("strictTransportSecurity")

    @property
    def x_content_type_options(self) -> str | None:
        return self.response.get("xContentTypeOptions")

    @property
    def x_frame_options(self) -> str | None:
        return self.response.get("xFrameOptions")

    @property
    def x_amzn_error_type(self) -> str | None:
        return self.response.get("xAmznErrorType")

    @property
    def exception_message(self) -> str | None:
        """Your account is pending verification."""
        return self.response.get("exceptionMessage")


class ResourceNotFoundException(IVSRealTimeError):
    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def access_control_allow_origin(self) -> str | None:
        return self.response.get("accessControlAllowOrigin")

    @property
    def access_control_expose_headers(self) -> str | None:
        return self.response.get("accessControlExposeHeaders")

    @property
    def cache_control(self) -> str | None:
        return self.response.get("cacheControl")

    @property
    def content_security_policy(self) -> str | None:
        return self.response.get("contentSecurityPolicy")

    @property
    def strict_transport_security(self) -> str | None:
        return self.response.get("strictTransportSecurity")

    @property
    def x_content_type_options(self) -> str | None:
        return self.response.get("xContentTypeOptions")

    @property
    def x_frame_options(self) -> str | None:
        return self.response.get("xFrameOptions")

    @property
    def x_amzn_error_type(self) -> str | None:
        return self.response.get("xAmznErrorType")

    @property
    def exception_message(self) -> str | None:
        """Request references a resource which does not exist."""
        return self.response.get("exceptionMessage")


class ServiceQuotaExceededException(IVSRealTimeError):
    _ERROR_CODE = "ServiceQuotaExceededException"

    @property
    def access_control_allow_origin(self) -> str | None:
        return self.response.get("accessControlAllowOrigin")

    @property
    def access_control_expose_headers(self) -> str | None:
        return self.response.get("accessControlExposeHeaders")

    @property
    def cache_control(self) -> str | None:
        return self.response.get("cacheControl")

    @property
    def content_security_policy(self) -> str | None:
        return self.response.get("contentSecurityPolicy")

    @property
    def strict_transport_security(self) -> str | None:
        return self.response.get("strictTransportSecurity")

    @property
    def x_content_type_options(self) -> str | None:
        return self.response.get("xContentTypeOptions")

    @property
    def x_frame_options(self) -> str | None:
        return self.response.get("xFrameOptions")

    @property
    def x_amzn_error_type(self) -> str | None:
        return self.response.get("xAmznErrorType")

    @property
    def exception_message(self) -> str | None:
        """Request would cause a service quota to be exceeded."""
        return self.response.get("exceptionMessage")


class ValidationException(IVSRealTimeError):
    _ERROR_CODE = "ValidationException"

    @property
    def access_control_allow_origin(self) -> str | None:
        return self.response.get("accessControlAllowOrigin")

    @property
    def access_control_expose_headers(self) -> str | None:
        return self.response.get("accessControlExposeHeaders")

    @property
    def cache_control(self) -> str | None:
        return self.response.get("cacheControl")

    @property
    def content_security_policy(self) -> str | None:
        return self.response.get("contentSecurityPolicy")

    @property
    def strict_transport_security(self) -> str | None:
        return self.response.get("strictTransportSecurity")

    @property
    def x_content_type_options(self) -> str | None:
        return self.response.get("xContentTypeOptions")

    @property
    def x_frame_options(self) -> str | None:
        return self.response.get("xFrameOptions")

    @property
    def x_amzn_error_type(self) -> str | None:
        return self.response.get("xAmznErrorType")

    @property
    def exception_message(self) -> str | None:
        """The input fails to satisfy the constraints specified by an Amazon Web Services
        service.
        """
        return self.response.get("exceptionMessage")


EXCEPTIONS: dict[str, type[IVSRealTimeError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "PendingVerification": PendingVerification,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ValidationException": ValidationException,
}
