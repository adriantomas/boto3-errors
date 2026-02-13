# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class CloudSearchDomainError(Boto3Error):
    _SERVICE = "cloudsearchdomain"


class DocumentServiceException(CloudSearchDomainError):
    """Information about any problems encountered while processing an upload request."""
    _ERROR_CODE = "DocumentServiceException"

    @property
    def status(self) -> str | None:
        """The return status of a document upload request, `error` or `success`."""
        return self.response.get("status")


class SearchException(CloudSearchDomainError):
    """Information about any problems encountered while processing a search request."""
    _ERROR_CODE = "SearchException"


EXCEPTIONS: dict[str, type[CloudSearchDomainError]] = {
    "DocumentServiceException": DocumentServiceException,
    "SearchException": SearchException,
}
