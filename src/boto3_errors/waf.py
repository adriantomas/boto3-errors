# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class WAFError(Boto3Error):
    _SERVICE = "waf"


class WAFBadRequestException(WAFError):
    _ERROR_CODE = "WAFBadRequestException"


class WAFDisallowedNameException(WAFError):
    """The name specified is invalid."""
    _ERROR_CODE = "WAFDisallowedNameException"


class WAFEntityMigrationException(WAFError):
    """The operation failed due to a problem with the migration. The failure cause is
    provided in the exception, in the `MigrationErrorType`:

    - `ENTITY_NOT_SUPPORTED` - The web ACL has an unsupported entity but the
      `IgnoreUnsupportedType` is not set to true.
    - `ENTITY_NOT_FOUND` - The web ACL doesn't exist.
    - `S3_BUCKET_NO_PERMISSION` - You don't have permission to perform the `PutObject`
      action to the specified Amazon S3 bucket.
    - `S3_BUCKET_NOT_ACCESSIBLE` - The bucket policy doesn't allow AWS WAF to perform
      the `PutObject` action in the bucket.
    - `S3_BUCKET_NOT_FOUND` - The S3 bucket doesn't exist.
    - `S3_BUCKET_INVALID_REGION` - The S3 bucket is not in the same Region as the web
      ACL.
    - `S3_INTERNAL_ERROR` - AWS WAF failed to create the template in the S3 bucket for
      another reason.
    """

    _ERROR_CODE = "WAFEntityMigrationException"

    @property
    def migration_error_type(self) -> str | None:
        return self.response.get("MigrationErrorType")

    @property
    def migration_error_reason(self) -> str | None:
        return self.response.get("MigrationErrorReason")


class WAFInternalErrorException(WAFError):
    """The operation failed because of a system problem, even though the request was valid.
    Retry your request.
    """

    _ERROR_CODE = "WAFInternalErrorException"


class WAFInvalidAccountException(WAFError):
    """The operation failed because you tried to create, update, or delete an object by
    using an invalid account identifier.
    """

    _ERROR_CODE = "WAFInvalidAccountException"


class WAFInvalidOperationException(WAFError):
    """The operation failed because there was nothing to do. For example:

    - You tried to remove a `Rule` from a `WebACL`, but the `Rule` isn't in the
      specified `WebACL`.
    - You tried to remove an IP address from an `IPSet`, but the IP address isn't in the
      specified `IPSet`.
    - You tried to remove a `ByteMatchTuple` from a `ByteMatchSet`, but the
      `ByteMatchTuple` isn't in the specified `WebACL`.
    - You tried to add a `Rule` to a `WebACL`, but the `Rule` already exists in the
      specified `WebACL`.
    - You tried to add a `ByteMatchTuple` to a `ByteMatchSet`, but the `ByteMatchTuple`
      already exists in the specified `WebACL`.
    """

    _ERROR_CODE = "WAFInvalidOperationException"


class WAFInvalidParameterException(WAFError):
    """The operation failed because AWS WAF didn't recognize a parameter in the request.
    For example:

    - You specified an invalid parameter name.
    - You specified an invalid value.
    - You tried to update an object (`ByteMatchSet`, `IPSet`, `Rule`, or `WebACL`) using
      an action other than `INSERT` or `DELETE`.
    - You tried to create a `WebACL` with a `DefaultAction` `Type` other than `ALLOW`,
      `BLOCK`, or `COUNT`.
    - You tried to create a `RateBasedRule` with a `RateKey` value other than `IP`.
    - You tried to update a `WebACL` with a `WafAction` `Type` other than `ALLOW`,
      `BLOCK`, or `COUNT`.
    - You tried to update a `ByteMatchSet` with a `FieldToMatch` `Type` other than
      HEADER, METHOD, QUERY_STRING, URI, or BODY.
    - You tried to update a `ByteMatchSet` with a `Field` of `HEADER` but no value for
      `Data`.
    - Your request references an ARN that is malformed, or corresponds to a resource
      with which a web ACL cannot be associated.
    """

    _ERROR_CODE = "WAFInvalidParameterException"

    @property
    def field(self) -> str | None:
        return self.response.get("field")

    @property
    def parameter(self) -> str | None:
        return self.response.get("parameter")

    @property
    def reason(self) -> str | None:
        return self.response.get("reason")


class WAFInvalidPermissionPolicyException(WAFError):
    """The operation failed because the specified policy is not in the proper format.

    The policy is subject to the following restrictions:

    - You can attach only one policy with each `PutPermissionPolicy` request.
    - The policy must include an `Effect`, `Action` and `Principal`.
    - `Effect` must specify `Allow`.
    - The `Action` in the policy must be `waf:UpdateWebACL`, `waf-
      regional:UpdateWebACL`, `waf:GetRuleGroup` and `waf-regional:GetRuleGroup` . Any
      extra or wildcard actions in the policy will be rejected.
    - The policy cannot include a `Resource` parameter.
    - The ARN in the request must be a valid WAF RuleGroup ARN and the RuleGroup must
      exist in the same region.
    - The user making the request must be the owner of the RuleGroup.
    - Your policy must be composed using IAM Policy version 2012-10-17.
    """

    _ERROR_CODE = "WAFInvalidPermissionPolicyException"


class WAFInvalidRegexPatternException(WAFError):
    """The regular expression (regex) you specified in `RegexPatternString` is invalid."""
    _ERROR_CODE = "WAFInvalidRegexPatternException"


class WAFLimitsExceededException(WAFError):
    """The operation exceeds a resource limit, for example, the maximum number of `WebACL`
    objects that you can create for an AWS account. For more information, see Limits in
    the AWS WAF Developer Guide.
    """

    _ERROR_CODE = "WAFLimitsExceededException"


class WAFNonEmptyEntityException(WAFError):
    """The operation failed because you tried to delete an object that isn't empty. For
    example:

    - You tried to delete a `WebACL` that still contains one or more `Rule` objects.
    - You tried to delete a `Rule` that still contains one or more `ByteMatchSet`
      objects or other predicates.
    - You tried to delete a `ByteMatchSet` that contains one or more `ByteMatchTuple`
      objects.
    - You tried to delete an `IPSet` that references one or more IP addresses.
    """

    _ERROR_CODE = "WAFNonEmptyEntityException"


class WAFNonexistentContainerException(WAFError):
    """The operation failed because you tried to add an object to or delete an object from
    another object that doesn't exist. For example:

    - You tried to add a `Rule` to or delete a `Rule` from a `WebACL` that doesn't
      exist.
    - You tried to add a `ByteMatchSet` to or delete a `ByteMatchSet` from a `Rule` that
      doesn't exist.
    - You tried to add an IP address to or delete an IP address from an `IPSet` that
      doesn't exist.
    - You tried to add a `ByteMatchTuple` to or delete a `ByteMatchTuple` from a
      `ByteMatchSet` that doesn't exist.
    """

    _ERROR_CODE = "WAFNonexistentContainerException"


class WAFNonexistentItemException(WAFError):
    """The operation failed because the referenced object doesn't exist."""
    _ERROR_CODE = "WAFNonexistentItemException"


class WAFReferencedItemException(WAFError):
    """The operation failed because you tried to delete an object that is still in use. For
    example:

    - You tried to delete a `ByteMatchSet` that is still referenced by a `Rule`.
    - You tried to delete a `Rule` that is still referenced by a `WebACL`.
    """

    _ERROR_CODE = "WAFReferencedItemException"


class WAFServiceLinkedRoleErrorException(WAFError):
    """AWS WAF is not able to access the service linked role. This can be caused by a
    previous `PutLoggingConfiguration` request, which can lock the service linked role
    for about 20 seconds. Please try your request again. The service linked role can
    also be locked by a previous `DeleteServiceLinkedRole` request, which can lock the
    role for 15 minutes or more. If you recently made a `DeleteServiceLinkedRole`, wait
    at least 15 minutes and try the request again. If you receive this same exception
    again, you will have to wait additional time until the role is unlocked.
    """

    _ERROR_CODE = "WAFServiceLinkedRoleErrorException"


class WAFStaleDataException(WAFError):
    """The operation failed because you tried to create, update, or delete an object by
    using a change token that has already been used.
    """

    _ERROR_CODE = "WAFStaleDataException"


class WAFSubscriptionNotFoundException(WAFError):
    """The specified subscription does not exist."""
    _ERROR_CODE = "WAFSubscriptionNotFoundException"


class WAFTagOperationException(WAFError):
    _ERROR_CODE = "WAFTagOperationException"


class WAFTagOperationInternalErrorException(WAFError):
    _ERROR_CODE = "WAFTagOperationInternalErrorException"


EXCEPTIONS: dict[str, type[WAFError]] = {
    "WAFBadRequestException": WAFBadRequestException,
    "WAFDisallowedNameException": WAFDisallowedNameException,
    "WAFEntityMigrationException": WAFEntityMigrationException,
    "WAFInternalErrorException": WAFInternalErrorException,
    "WAFInvalidAccountException": WAFInvalidAccountException,
    "WAFInvalidOperationException": WAFInvalidOperationException,
    "WAFInvalidParameterException": WAFInvalidParameterException,
    "WAFInvalidPermissionPolicyException": WAFInvalidPermissionPolicyException,
    "WAFInvalidRegexPatternException": WAFInvalidRegexPatternException,
    "WAFLimitsExceededException": WAFLimitsExceededException,
    "WAFNonEmptyEntityException": WAFNonEmptyEntityException,
    "WAFNonexistentContainerException": WAFNonexistentContainerException,
    "WAFNonexistentItemException": WAFNonexistentItemException,
    "WAFReferencedItemException": WAFReferencedItemException,
    "WAFServiceLinkedRoleErrorException": WAFServiceLinkedRoleErrorException,
    "WAFStaleDataException": WAFStaleDataException,
    "WAFSubscriptionNotFoundException": WAFSubscriptionNotFoundException,
    "WAFTagOperationException": WAFTagOperationException,
    "WAFTagOperationInternalErrorException": WAFTagOperationInternalErrorException,
}
