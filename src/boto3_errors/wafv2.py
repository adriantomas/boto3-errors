# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class WAFV2Error(Boto3Error):
    _SERVICE = "wafv2"


class WAFAssociatedItemException(WAFV2Error):
    """WAF couldn’t perform the operation because your resource is being used by another
    resource or it’s associated with another resource.
    """

    _ERROR_CODE = "WAFAssociatedItemException"


class WAFConfigurationWarningException(WAFV2Error):
    """The operation failed because you are inspecting the web request body, headers, or
    cookies without specifying how to handle oversize components. Rules that inspect the
    body must either provide an `OversizeHandling` configuration or they must be
    preceded by a `SizeConstraintStatement` that blocks the body content from being too
    large. Rules that inspect the headers or cookies must provide an `OversizeHandling`
    configuration.

    Provide the handling configuration and retry your operation.

    Alternately, you can suppress this warning by adding the following tag to the
    resource that you provide to this operation: `Tag`
    (key:`WAF:OversizeFieldsHandlingConstraintOptOut`, value:`true`).
    """

    _ERROR_CODE = "WAFConfigurationWarningException"


class WAFDuplicateItemException(WAFV2Error):
    """WAF couldn’t perform the operation because the resource that you tried to save is a
    duplicate of an existing one.
    """

    _ERROR_CODE = "WAFDuplicateItemException"


class WAFExpiredManagedRuleGroupVersionException(WAFV2Error):
    """The operation failed because the specified version for the managed rule group has
    expired. You can retrieve the available versions for the managed rule group by
    calling ListAvailableManagedRuleGroupVersions.
    """

    _ERROR_CODE = "WAFExpiredManagedRuleGroupVersionException"


class WAFFeatureNotIncludedInPricingPlanException(WAFV2Error):
    """The operation failed because the specified WAF feature isn't supported by the
    CloudFront pricing plan associated with the web ACL.
    """

    _ERROR_CODE = "WAFFeatureNotIncludedInPricingPlanException"

    @property
    def disallowed_features(self) -> list[Any] | None:
        """The names of the disallowed WAF features."""
        return self.response.get("DisallowedFeatures")


class WAFInternalErrorException(WAFV2Error):
    """Your request is valid, but WAF couldn’t perform the operation because of a system
    problem. Retry your request.
    """

    _ERROR_CODE = "WAFInternalErrorException"


class WAFInvalidOperationException(WAFV2Error):
    """The operation isn't valid."""
    _ERROR_CODE = "WAFInvalidOperationException"


class WAFInvalidParameterException(WAFV2Error):
    """The operation failed because WAF didn't recognize a parameter in the request. For
    example:

    - You specified a parameter name or value that isn't valid.
    - Your nested statement isn't valid. You might have tried to nest a statement that
      can’t be nested.
    - You tried to update a `WebACL` with a `DefaultAction` that isn't among the types
      available at DefaultAction.
    - Your request references an ARN that is malformed, or corresponds to a resource
      with which a web ACL can't be associated.
    """

    _ERROR_CODE = "WAFInvalidParameterException"

    @property
    def field(self) -> str | None:
        """The settings where the invalid parameter was found."""
        return self.response.get("Field")

    @property
    def parameter(self) -> str | None:
        """The invalid parameter that resulted in the exception."""
        return self.response.get("Parameter")

    @property
    def reason(self) -> str | None:
        """Additional information about the exception."""
        return self.response.get("Reason")


class WAFInvalidPermissionPolicyException(WAFV2Error):
    """The operation failed because the specified policy isn't in the proper format.

    The policy specifications must conform to the following:

    - The policy must be composed using IAM Policy version 2012-10-17.
    - The policy must include specifications for `Effect`, `Action`, and `Principal`.
    - `Effect` must specify `Allow`.
    - `Action` must specify `wafv2:CreateWebACL`, `wafv2:UpdateWebACL`, and
      `wafv2:PutFirewallManagerRuleGroups` and may optionally specify
      `wafv2:GetRuleGroup`. WAF rejects any extra actions or wildcard actions in the
      policy.
    - The policy must not include a `Resource` parameter.

    For more information, see IAM Policies.
    """

    _ERROR_CODE = "WAFInvalidPermissionPolicyException"


class WAFInvalidResourceException(WAFV2Error):
    """WAF couldn’t perform the operation because the resource that you requested isn’t
    valid. Check the resource, and try again.
    """

    _ERROR_CODE = "WAFInvalidResourceException"


class WAFLimitsExceededException(WAFV2Error):
    """WAF couldn’t perform the operation because you exceeded your resource limit. For
    example, the maximum number of `WebACL` objects that you can create for an Amazon
    Web Services account. For more information, see WAF quotas in the WAF Developer
    Guide.
    """

    _ERROR_CODE = "WAFLimitsExceededException"

    @property
    def source_type(self) -> str | None:
        """Source type for the exception."""
        return self.response.get("SourceType")


class WAFLogDestinationPermissionIssueException(WAFV2Error):
    """The operation failed because you don't have the permissions that your logging
    configuration requires. For information, see Logging web ACL traffic information in
    the WAF Developer Guide.
    """

    _ERROR_CODE = "WAFLogDestinationPermissionIssueException"


class WAFNonexistentItemException(WAFV2Error):
    """WAF couldn’t perform the operation because your resource doesn't exist. If you've
    just created a resource that you're using in this operation, you might just need to
    wait a few minutes. It can take from a few seconds to a number of minutes for
    changes to propagate.
    """

    _ERROR_CODE = "WAFNonexistentItemException"


class WAFOptimisticLockException(WAFV2Error):
    """WAF couldn’t save your changes because you tried to update or delete a resource that
    has changed since you last retrieved it. Get the resource again, make any changes
    you need to make to the new copy, and retry your operation.
    """

    _ERROR_CODE = "WAFOptimisticLockException"


class WAFServiceLinkedRoleErrorException(WAFV2Error):
    """WAF is not able to access the service linked role. This can be caused by a previous
    `PutLoggingConfiguration` request, which can lock the service linked role for about
    20 seconds. Please try your request again. The service linked role can also be
    locked by a previous `DeleteServiceLinkedRole` request, which can lock the role for
    15 minutes or more. If you recently made a call to `DeleteServiceLinkedRole`, wait
    at least 15 minutes and try the request again. If you receive this same exception
    again, you will have to wait additional time until the role is unlocked.
    """

    _ERROR_CODE = "WAFServiceLinkedRoleErrorException"


class WAFSubscriptionNotFoundException(WAFV2Error):
    """You tried to use a managed rule group that's available by subscription, but you
    aren't subscribed to it yet.
    """

    _ERROR_CODE = "WAFSubscriptionNotFoundException"


class WAFTagOperationException(WAFV2Error):
    """An error occurred during the tagging operation. Retry your request."""
    _ERROR_CODE = "WAFTagOperationException"


class WAFTagOperationInternalErrorException(WAFV2Error):
    """WAF couldn’t perform your tagging operation because of an internal error. Retry your
    request.
    """

    _ERROR_CODE = "WAFTagOperationInternalErrorException"


class WAFUnavailableEntityException(WAFV2Error):
    """WAF couldn’t retrieve a resource that you specified for this operation. If you've
    just created a resource that you're using in this operation, you might just need to
    wait a few minutes. It can take from a few seconds to a number of minutes for
    changes to propagate. Verify the resource specifications in your request parameters
    and then retry the operation.
    """

    _ERROR_CODE = "WAFUnavailableEntityException"


class WAFUnsupportedAggregateKeyTypeException(WAFV2Error):
    """The rule that you've named doesn't aggregate solely on the IP address or solely on
    the forwarded IP address. This call is only available for rate-based rules with an
    `AggregateKeyType` setting of `IP` or `FORWARDED_IP`.
    """

    _ERROR_CODE = "WAFUnsupportedAggregateKeyTypeException"


EXCEPTIONS: dict[str, type[WAFV2Error]] = {
    "WAFAssociatedItemException": WAFAssociatedItemException,
    "WAFConfigurationWarningException": WAFConfigurationWarningException,
    "WAFDuplicateItemException": WAFDuplicateItemException,
    "WAFExpiredManagedRuleGroupVersionException": WAFExpiredManagedRuleGroupVersionException,
    "WAFFeatureNotIncludedInPricingPlanException": WAFFeatureNotIncludedInPricingPlanException,
    "WAFInternalErrorException": WAFInternalErrorException,
    "WAFInvalidOperationException": WAFInvalidOperationException,
    "WAFInvalidParameterException": WAFInvalidParameterException,
    "WAFInvalidPermissionPolicyException": WAFInvalidPermissionPolicyException,
    "WAFInvalidResourceException": WAFInvalidResourceException,
    "WAFLimitsExceededException": WAFLimitsExceededException,
    "WAFLogDestinationPermissionIssueException": WAFLogDestinationPermissionIssueException,
    "WAFNonexistentItemException": WAFNonexistentItemException,
    "WAFOptimisticLockException": WAFOptimisticLockException,
    "WAFServiceLinkedRoleErrorException": WAFServiceLinkedRoleErrorException,
    "WAFSubscriptionNotFoundException": WAFSubscriptionNotFoundException,
    "WAFTagOperationException": WAFTagOperationException,
    "WAFTagOperationInternalErrorException": WAFTagOperationInternalErrorException,
    "WAFUnavailableEntityException": WAFUnavailableEntityException,
    "WAFUnsupportedAggregateKeyTypeException": WAFUnsupportedAggregateKeyTypeException,
}
