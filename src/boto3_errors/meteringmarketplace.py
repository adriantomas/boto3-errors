# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class MarketplaceMeteringError(Boto3Error):
    _SERVICE = "meteringmarketplace"


class CustomerNotEntitledException(MarketplaceMeteringError):
    """Exception thrown when the customer does not have a valid subscription for the
    product.
    """

    _ERROR_CODE = "CustomerNotEntitledException"


class DisabledApiException(MarketplaceMeteringError):
    """The API is disabled in the Region."""
    _ERROR_CODE = "DisabledApiException"


class DuplicateRequestException(MarketplaceMeteringError):
    """A metering record has already been emitted by the same EC2 instance, ECS task, or
    EKS pod for the given {`usageDimension`, `timestamp`} with a different
    `usageQuantity`.
    """

    _ERROR_CODE = "DuplicateRequestException"


class ExpiredTokenException(MarketplaceMeteringError):
    """The submitted registration token has expired. This can happen if the buyer's browser
    takes too long to redirect to your page, the buyer has resubmitted the registration
    token, or your application has held on to the registration token for too long. Your
    SaaS registration website should redeem this token as soon as it is submitted by the
    buyer's browser.
    """

    _ERROR_CODE = "ExpiredTokenException"


class IdempotencyConflictException(MarketplaceMeteringError):
    """The `ClientToken` is being used for multiple requests."""
    _ERROR_CODE = "IdempotencyConflictException"


class InternalServiceErrorException(MarketplaceMeteringError):
    """An internal error has occurred. Retry your request. If the problem persists, post a
    message with details on the Amazon Web Services forums.
    """

    _ERROR_CODE = "InternalServiceErrorException"


class InvalidCustomerIdentifierException(MarketplaceMeteringError):
    """You have metered usage for a `CustomerIdentifier` that does not exist."""
    _ERROR_CODE = "InvalidCustomerIdentifierException"


class InvalidEndpointRegionException(MarketplaceMeteringError):
    """The endpoint being called is in a Amazon Web Services Region different from your EC2
    instance, ECS task, or EKS pod. The Region of the Metering Service endpoint and the
    Amazon Web Services Region of the resource must match.
    """

    _ERROR_CODE = "InvalidEndpointRegionException"


class InvalidProductCodeException(MarketplaceMeteringError):
    """The product code passed does not match the product code used for publishing the
    product.
    """

    _ERROR_CODE = "InvalidProductCodeException"


class InvalidPublicKeyVersionException(MarketplaceMeteringError):
    """Public Key version is invalid."""
    _ERROR_CODE = "InvalidPublicKeyVersionException"


class InvalidRegionException(MarketplaceMeteringError):
    """`RegisterUsage` must be called in the same Amazon Web Services Region the ECS task
    was launched in. This prevents a container from hardcoding a Region (e.g.
    withRegion(“us-east-1”) when calling `RegisterUsage`.
    """

    _ERROR_CODE = "InvalidRegionException"


class InvalidTagException(MarketplaceMeteringError):
    """The tag is invalid, or the number of tags is greater than 5."""
    _ERROR_CODE = "InvalidTagException"


class InvalidTokenException(MarketplaceMeteringError):
    """Registration token is invalid."""
    _ERROR_CODE = "InvalidTokenException"


class InvalidUsageAllocationsException(MarketplaceMeteringError):
    """Sum of allocated usage quantities is not equal to the usage quantity."""
    _ERROR_CODE = "InvalidUsageAllocationsException"


class InvalidUsageDimensionException(MarketplaceMeteringError):
    """The usage dimension does not match one of the `UsageDimensions` associated with
    products.
    """

    _ERROR_CODE = "InvalidUsageDimensionException"


class PlatformNotSupportedException(MarketplaceMeteringError):
    """Amazon Web Services Marketplace does not support metering usage from the underlying
    platform. Currently, Amazon ECS, Amazon EKS, and Fargate are supported.
    """

    _ERROR_CODE = "PlatformNotSupportedException"


class ThrottlingException(MarketplaceMeteringError):
    """The calls to the API are throttled."""
    _ERROR_CODE = "ThrottlingException"


class TimestampOutOfBoundsException(MarketplaceMeteringError):
    """The `timestamp` value passed in the `UsageRecord` is out of allowed range.

    For `BatchMeterUsage`, if any of the records are outside of the allowed range, the
    entire batch is not processed. You must remove invalid records and try again.
    """

    _ERROR_CODE = "TimestampOutOfBoundsException"


EXCEPTIONS: dict[str, type[MarketplaceMeteringError]] = {
    "CustomerNotEntitledException": CustomerNotEntitledException,
    "DisabledApiException": DisabledApiException,
    "DuplicateRequestException": DuplicateRequestException,
    "ExpiredTokenException": ExpiredTokenException,
    "IdempotencyConflictException": IdempotencyConflictException,
    "InternalServiceErrorException": InternalServiceErrorException,
    "InvalidCustomerIdentifierException": InvalidCustomerIdentifierException,
    "InvalidEndpointRegionException": InvalidEndpointRegionException,
    "InvalidProductCodeException": InvalidProductCodeException,
    "InvalidPublicKeyVersionException": InvalidPublicKeyVersionException,
    "InvalidRegionException": InvalidRegionException,
    "InvalidTagException": InvalidTagException,
    "InvalidTokenException": InvalidTokenException,
    "InvalidUsageAllocationsException": InvalidUsageAllocationsException,
    "InvalidUsageDimensionException": InvalidUsageDimensionException,
    "PlatformNotSupportedException": PlatformNotSupportedException,
    "ThrottlingException": ThrottlingException,
    "TimestampOutOfBoundsException": TimestampOutOfBoundsException,
}
