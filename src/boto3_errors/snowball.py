# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class SnowballError(Boto3Error):
    _SERVICE = "snowball"


class ClusterLimitExceededException(SnowballError):
    """Job creation failed. Currently, clusters support five nodes. If you have fewer than
    five nodes for your cluster and you have more nodes to create for this cluster, try
    again and create jobs until your cluster has exactly five nodes.
    """

    _ERROR_CODE = "ClusterLimitExceededException"


class ConflictException(SnowballError):
    """You get this exception when you call `CreateReturnShippingLabel` more than once when
    other requests are not completed.
    """

    _ERROR_CODE = "ConflictException"

    @property
    def conflict_resource(self) -> str | None:
        """You get this resource when you call `CreateReturnShippingLabel` more than once
        when other requests are not completed. .
        """
        return self.response.get("ConflictResource")


class Ec2RequestFailedException(SnowballError):
    """Your user lacks the necessary Amazon EC2 permissions to perform the attempted
    action.
    """

    _ERROR_CODE = "Ec2RequestFailedException"


class InvalidAddressException(SnowballError):
    """The address provided was invalid. Check the address with your region's carrier, and
    try again.
    """

    _ERROR_CODE = "InvalidAddressException"


class InvalidInputCombinationException(SnowballError):
    """Job or cluster creation failed. One or more inputs were invalid. Confirm that the
    CreateClusterRequest$SnowballType value supports your CreateJobRequest$JobType, and
    try again.
    """

    _ERROR_CODE = "InvalidInputCombinationException"


class InvalidJobStateException(SnowballError):
    """The action can't be performed because the job's current state doesn't allow that
    action to be performed.
    """

    _ERROR_CODE = "InvalidJobStateException"


class InvalidNextTokenException(SnowballError):
    """The `NextToken` string was altered unexpectedly, and the operation has stopped. Run
    the operation without changing the `NextToken` string, and try again.
    """

    _ERROR_CODE = "InvalidNextTokenException"


class InvalidResourceException(SnowballError):
    """The specified resource can't be found. Check the information you provided in your
    last request, and try again.
    """

    _ERROR_CODE = "InvalidResourceException"

    @property
    def resource_type(self) -> str | None:
        """The provided resource value is invalid."""
        return self.response.get("ResourceType")


class KMSRequestFailedException(SnowballError):
    """The provided Key Management Service key lacks the permissions to perform the
    specified CreateJob or UpdateJob action.
    """

    _ERROR_CODE = "KMSRequestFailedException"


class ReturnShippingLabelAlreadyExistsException(SnowballError):
    """You get this exception if you call `CreateReturnShippingLabel` and a valid return
    shipping label already exists. In this case, use `DescribeReturnShippingLabel` to
    get the URL.
    """

    _ERROR_CODE = "ReturnShippingLabelAlreadyExistsException"


class UnsupportedAddressException(SnowballError):
    """The address is either outside the serviceable area for your region, or an error
    occurred. Check the address with your region's carrier and try again. If the issue
    persists, contact Amazon Web Services Support.
    """

    _ERROR_CODE = "UnsupportedAddressException"


EXCEPTIONS: dict[str, type[SnowballError]] = {
    "ClusterLimitExceededException": ClusterLimitExceededException,
    "ConflictException": ConflictException,
    "Ec2RequestFailedException": Ec2RequestFailedException,
    "InvalidAddressException": InvalidAddressException,
    "InvalidInputCombinationException": InvalidInputCombinationException,
    "InvalidJobStateException": InvalidJobStateException,
    "InvalidNextTokenException": InvalidNextTokenException,
    "InvalidResourceException": InvalidResourceException,
    "KMSRequestFailedException": KMSRequestFailedException,
    "ReturnShippingLabelAlreadyExistsException": ReturnShippingLabelAlreadyExistsException,
    "UnsupportedAddressException": UnsupportedAddressException,
}
