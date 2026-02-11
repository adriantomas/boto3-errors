# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class SimpleDBError(Boto3Error):
    _SERVICE = "sdb"


class AttributeDoesNotExist(SimpleDBError):
    """The specified attribute does not exist."""
    _ERROR_CODE = "AttributeDoesNotExist"

    @property
    def box_usage(self) -> float | None:
        return self.response.get("BoxUsage")


class DuplicateItemName(SimpleDBError):
    """The item name was specified more than once."""
    _ERROR_CODE = "DuplicateItemName"

    @property
    def box_usage(self) -> float | None:
        return self.response.get("BoxUsage")


class InvalidNextToken(SimpleDBError):
    """The specified NextToken is not valid."""
    _ERROR_CODE = "InvalidNextToken"

    @property
    def box_usage(self) -> float | None:
        return self.response.get("BoxUsage")


class InvalidNumberPredicates(SimpleDBError):
    """Too many predicates exist in the query expression."""
    _ERROR_CODE = "InvalidNumberPredicates"

    @property
    def box_usage(self) -> float | None:
        return self.response.get("BoxUsage")


class InvalidNumberValueTests(SimpleDBError):
    """Too many predicates exist in the query expression."""
    _ERROR_CODE = "InvalidNumberValueTests"

    @property
    def box_usage(self) -> float | None:
        return self.response.get("BoxUsage")


class InvalidParameterValue(SimpleDBError):
    """The value for a parameter is invalid."""
    _ERROR_CODE = "InvalidParameterValue"

    @property
    def box_usage(self) -> float | None:
        return self.response.get("BoxUsage")


class InvalidQueryExpression(SimpleDBError):
    """The specified query expression syntax is not valid."""
    _ERROR_CODE = "InvalidQueryExpression"

    @property
    def box_usage(self) -> float | None:
        return self.response.get("BoxUsage")


class MissingParameter(SimpleDBError):
    """The request must contain the specified missing parameter."""
    _ERROR_CODE = "MissingParameter"

    @property
    def box_usage(self) -> float | None:
        return self.response.get("BoxUsage")


class NoSuchDomain(SimpleDBError):
    """The specified domain does not exist."""
    _ERROR_CODE = "NoSuchDomain"

    @property
    def box_usage(self) -> float | None:
        return self.response.get("BoxUsage")


class NumberDomainAttributesExceeded(SimpleDBError):
    """Too many attributes in this domain."""
    _ERROR_CODE = "NumberDomainAttributesExceeded"

    @property
    def box_usage(self) -> float | None:
        return self.response.get("BoxUsage")


class NumberDomainBytesExceeded(SimpleDBError):
    """Too many bytes in this domain."""
    _ERROR_CODE = "NumberDomainBytesExceeded"

    @property
    def box_usage(self) -> float | None:
        return self.response.get("BoxUsage")


class NumberDomainsExceeded(SimpleDBError):
    """Too many domains exist per this account."""
    _ERROR_CODE = "NumberDomainsExceeded"

    @property
    def box_usage(self) -> float | None:
        return self.response.get("BoxUsage")


class NumberItemAttributesExceeded(SimpleDBError):
    """Too many attributes in this item."""
    _ERROR_CODE = "NumberItemAttributesExceeded"

    @property
    def box_usage(self) -> float | None:
        return self.response.get("BoxUsage")


class NumberSubmittedAttributesExceeded(SimpleDBError):
    """Too many attributes exist in a single call."""
    _ERROR_CODE = "NumberSubmittedAttributesExceeded"

    @property
    def box_usage(self) -> float | None:
        return self.response.get("BoxUsage")


class NumberSubmittedItemsExceeded(SimpleDBError):
    """Too many items exist in a single call."""
    _ERROR_CODE = "NumberSubmittedItemsExceeded"

    @property
    def box_usage(self) -> float | None:
        return self.response.get("BoxUsage")


class RequestTimeout(SimpleDBError):
    """A timeout occurred when attempting to query the specified domain with specified
    query expression.
    """

    _ERROR_CODE = "RequestTimeout"

    @property
    def box_usage(self) -> float | None:
        return self.response.get("BoxUsage")


class TooManyRequestedAttributes(SimpleDBError):
    """Too many attributes requested."""
    _ERROR_CODE = "TooManyRequestedAttributes"

    @property
    def box_usage(self) -> float | None:
        return self.response.get("BoxUsage")


EXCEPTIONS: dict[str, type[SimpleDBError]] = {
    "AttributeDoesNotExist": AttributeDoesNotExist,
    "DuplicateItemName": DuplicateItemName,
    "InvalidNextToken": InvalidNextToken,
    "InvalidNumberPredicates": InvalidNumberPredicates,
    "InvalidNumberValueTests": InvalidNumberValueTests,
    "InvalidParameterValue": InvalidParameterValue,
    "InvalidQueryExpression": InvalidQueryExpression,
    "MissingParameter": MissingParameter,
    "NoSuchDomain": NoSuchDomain,
    "NumberDomainAttributesExceeded": NumberDomainAttributesExceeded,
    "NumberDomainBytesExceeded": NumberDomainBytesExceeded,
    "NumberDomainsExceeded": NumberDomainsExceeded,
    "NumberItemAttributesExceeded": NumberItemAttributesExceeded,
    "NumberSubmittedAttributesExceeded": NumberSubmittedAttributesExceeded,
    "NumberSubmittedItemsExceeded": NumberSubmittedItemsExceeded,
    "RequestTimeout": RequestTimeout,
    "TooManyRequestedAttributes": TooManyRequestedAttributes,
}
