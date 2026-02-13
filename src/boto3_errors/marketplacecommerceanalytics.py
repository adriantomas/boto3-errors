# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class MarketplaceCommerceAnalyticsError(Boto3Error):
    _SERVICE = "marketplacecommerceanalytics"


class MarketplaceCommerceAnalyticsException(MarketplaceCommerceAnalyticsError):
    """This exception is thrown when an internal service error occurs."""
    _ERROR_CODE = "MarketplaceCommerceAnalyticsException"


EXCEPTIONS: dict[str, type[MarketplaceCommerceAnalyticsError]] = {
    "MarketplaceCommerceAnalyticsException": MarketplaceCommerceAnalyticsException,
}
