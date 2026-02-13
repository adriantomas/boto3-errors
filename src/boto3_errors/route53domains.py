# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class Route53DomainsError(Boto3Error):
    _SERVICE = "route53domains"


class DnssecLimitExceeded(Route53DomainsError):
    """This error is returned if you call `AssociateDelegationSignerToDomain` when the
    specified domain has reached the maximum number of DS records. You can't add any
    additional DS records unless you delete an existing one first.
    """

    _ERROR_CODE = "DnssecLimitExceeded"


class DomainLimitExceeded(Route53DomainsError):
    """The number of domains has exceeded the allowed threshold for the account."""
    _ERROR_CODE = "DomainLimitExceeded"


class DuplicateRequest(Route53DomainsError):
    """The request is already in progress for the domain."""
    _ERROR_CODE = "DuplicateRequest"

    @property
    def request_id(self) -> str | None:
        """ID of the request operation."""
        return self.response.get("requestId")


class InvalidInput(Route53DomainsError):
    """The requested item is not acceptable. For example, for APIs that accept a domain
    name, the request might specify a domain name that doesn't belong to the account
    that submitted the request. For `AcceptDomainTransferFromAnotherAwsAccount`, the
    password might be invalid.
    """

    _ERROR_CODE = "InvalidInput"


class OperationLimitExceeded(Route53DomainsError):
    """The number of operations or jobs running exceeded the allowed threshold for the
    account.
    """

    _ERROR_CODE = "OperationLimitExceeded"


class TLDRulesViolation(Route53DomainsError):
    """The top-level domain does not support this operation."""
    _ERROR_CODE = "TLDRulesViolation"


class UnsupportedTLD(Route53DomainsError):
    """Amazon Route 53 does not support this top-level domain (TLD)."""
    _ERROR_CODE = "UnsupportedTLD"


EXCEPTIONS: dict[str, type[Route53DomainsError]] = {
    "DnssecLimitExceeded": DnssecLimitExceeded,
    "DomainLimitExceeded": DomainLimitExceeded,
    "DuplicateRequest": DuplicateRequest,
    "InvalidInput": InvalidInput,
    "OperationLimitExceeded": OperationLimitExceeded,
    "TLDRulesViolation": TLDRulesViolation,
    "UnsupportedTLD": UnsupportedTLD,
}
