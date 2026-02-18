# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class CloudFrontError(Boto3Error):
    _SERVICE = "cloudfront"


class AccessDenied(CloudFrontError):
    """Access denied."""
    _ERROR_CODE = "AccessDenied"


class BatchTooLarge(CloudFrontError):
    """Invalidation batch specified is too large."""
    _ERROR_CODE = "BatchTooLarge"


class CNAMEAlreadyExists(CloudFrontError):
    """The CNAME specified is already defined for CloudFront."""
    _ERROR_CODE = "CNAMEAlreadyExists"


class CachePolicyAlreadyExists(CloudFrontError):
    """A cache policy with this name already exists. You must provide a unique name. To
    modify an existing cache policy, use `UpdateCachePolicy`.
    """

    _ERROR_CODE = "CachePolicyAlreadyExists"


class CachePolicyInUse(CloudFrontError):
    """Cannot delete the cache policy because it is attached to one or more cache
    behaviors.
    """

    _ERROR_CODE = "CachePolicyInUse"


class CannotChangeImmutablePublicKeyFields(CloudFrontError):
    """You can't change the value of a public key."""
    _ERROR_CODE = "CannotChangeImmutablePublicKeyFields"


class CannotDeleteEntityWhileInUse(CloudFrontError):
    """The Key Value Store entity cannot be deleted while it is in use."""
    _ERROR_CODE = "CannotDeleteEntityWhileInUse"


class CloudFrontOriginAccessIdentityAlreadyExists(CloudFrontError):
    """If the `CallerReference` is a value you already sent in a previous request to create
    an identity but the content of the `CloudFrontOriginAccessIdentityConfig` is
    different from the original request, CloudFront returns a
    `CloudFrontOriginAccessIdentityAlreadyExists` error.
    """

    _ERROR_CODE = "CloudFrontOriginAccessIdentityAlreadyExists"


class CloudFrontOriginAccessIdentityInUse(CloudFrontError):
    """The Origin Access Identity specified is already in use."""
    _ERROR_CODE = "CloudFrontOriginAccessIdentityInUse"


class ContinuousDeploymentPolicyAlreadyExists(CloudFrontError):
    """A continuous deployment policy with this configuration already exists."""
    _ERROR_CODE = "ContinuousDeploymentPolicyAlreadyExists"


class ContinuousDeploymentPolicyInUse(CloudFrontError):
    """You cannot delete a continuous deployment policy that is associated with a primary
    distribution.
    """

    _ERROR_CODE = "ContinuousDeploymentPolicyInUse"


class DistributionAlreadyExists(CloudFrontError):
    """The caller reference you attempted to create the distribution with is associated
    with another distribution.
    """

    _ERROR_CODE = "DistributionAlreadyExists"


class DistributionNotDisabled(CloudFrontError):
    """The specified CloudFront distribution is not disabled. You must disable the
    distribution before you can delete it.
    """

    _ERROR_CODE = "DistributionNotDisabled"


class EntityAlreadyExists(CloudFrontError):
    """The Key Value Store entity already exists. You must provide a unique Key Value Store
    entity.
    """

    _ERROR_CODE = "EntityAlreadyExists"


class EntityLimitExceeded(CloudFrontError):
    """The Key Value Store entity limit has been exceeded."""
    _ERROR_CODE = "EntityLimitExceeded"


class EntityNotFound(CloudFrontError):
    """The Key Value Store entity was not found."""
    _ERROR_CODE = "EntityNotFound"


class EntitySizeLimitExceeded(CloudFrontError):
    """The Key Value Store entity size limit was exceeded."""
    _ERROR_CODE = "EntitySizeLimitExceeded"


class FieldLevelEncryptionConfigAlreadyExists(CloudFrontError):
    """The specified configuration for field-level encryption already exists."""
    _ERROR_CODE = "FieldLevelEncryptionConfigAlreadyExists"


class FieldLevelEncryptionConfigInUse(CloudFrontError):
    """The specified configuration for field-level encryption is in use."""
    _ERROR_CODE = "FieldLevelEncryptionConfigInUse"


class FieldLevelEncryptionProfileAlreadyExists(CloudFrontError):
    """The specified profile for field-level encryption already exists."""
    _ERROR_CODE = "FieldLevelEncryptionProfileAlreadyExists"


class FieldLevelEncryptionProfileInUse(CloudFrontError):
    """The specified profile for field-level encryption is in use."""
    _ERROR_CODE = "FieldLevelEncryptionProfileInUse"


class FieldLevelEncryptionProfileSizeExceeded(CloudFrontError):
    """The maximum size of a profile for field-level encryption was exceeded."""
    _ERROR_CODE = "FieldLevelEncryptionProfileSizeExceeded"


class FunctionAlreadyExists(CloudFrontError):
    """A function with the same name already exists in this Amazon Web Services account. To
    create a function, you must provide a unique name. To update an existing function,
    use `UpdateFunction`.
    """

    _ERROR_CODE = "FunctionAlreadyExists"


class FunctionInUse(CloudFrontError):
    """Cannot delete the function because it's attached to one or more cache behaviors."""
    _ERROR_CODE = "FunctionInUse"


class FunctionSizeLimitExceeded(CloudFrontError):
    """The function is too large. For more information, see Quotas (formerly known as
    limits) in the Amazon CloudFront Developer Guide.
    """

    _ERROR_CODE = "FunctionSizeLimitExceeded"


class IllegalDelete(CloudFrontError):
    """You cannot delete a managed policy."""
    _ERROR_CODE = "IllegalDelete"


class IllegalFieldLevelEncryptionConfigAssociationWithCacheBehavior(CloudFrontError):
    """The specified configuration for field-level encryption can't be associated with the
    specified cache behavior.
    """

    _ERROR_CODE = "IllegalFieldLevelEncryptionConfigAssociationWithCacheBehavior"


class IllegalOriginAccessConfiguration(CloudFrontError):
    """An origin cannot contain both an origin access control (OAC) and an origin access
    identity (OAI).
    """

    _ERROR_CODE = "IllegalOriginAccessConfiguration"


class IllegalUpdate(CloudFrontError):
    """The update contains modifications that are not allowed."""
    _ERROR_CODE = "IllegalUpdate"


class InconsistentQuantities(CloudFrontError):
    """The value of `Quantity` and the size of `Items` don't match."""
    _ERROR_CODE = "InconsistentQuantities"


class InvalidArgument(CloudFrontError):
    """An argument is invalid."""
    _ERROR_CODE = "InvalidArgument"


class InvalidDefaultRootObject(CloudFrontError):
    """The default root object file name is too big or contains an invalid character."""
    _ERROR_CODE = "InvalidDefaultRootObject"


class InvalidDomainNameForOriginAccessControl(CloudFrontError):
    """An origin access control is associated with an origin whose domain name is not
    supported.
    """

    _ERROR_CODE = "InvalidDomainNameForOriginAccessControl"


class InvalidErrorCode(CloudFrontError):
    """An invalid error code was specified."""
    _ERROR_CODE = "InvalidErrorCode"


class InvalidForwardCookies(CloudFrontError):
    """Your request contains forward cookies option which doesn't match with the
    expectation for the `whitelisted` list of cookie names. Either list of cookie names
    has been specified when not allowed or list of cookie names is missing when
    expected.
    """

    _ERROR_CODE = "InvalidForwardCookies"


class InvalidFunctionAssociation(CloudFrontError):
    """A CloudFront function association is invalid."""
    _ERROR_CODE = "InvalidFunctionAssociation"


class InvalidGeoRestrictionParameter(CloudFrontError):
    """The specified geo restriction parameter is not valid."""
    _ERROR_CODE = "InvalidGeoRestrictionParameter"


class InvalidHeadersForS3Origin(CloudFrontError):
    """The headers specified are not valid for an Amazon S3 origin."""
    _ERROR_CODE = "InvalidHeadersForS3Origin"


class InvalidIfMatchVersion(CloudFrontError):
    """The `If-Match` version is missing or not valid."""
    _ERROR_CODE = "InvalidIfMatchVersion"


class InvalidLambdaFunctionAssociation(CloudFrontError):
    """The specified Lambda@Edge function association is invalid."""
    _ERROR_CODE = "InvalidLambdaFunctionAssociation"


class InvalidLocationCode(CloudFrontError):
    """The location code specified is not valid."""
    _ERROR_CODE = "InvalidLocationCode"


class InvalidMinimumProtocolVersion(CloudFrontError):
    """The minimum protocol version specified is not valid."""
    _ERROR_CODE = "InvalidMinimumProtocolVersion"


class InvalidOrigin(CloudFrontError):
    """The Amazon S3 origin server specified does not refer to a valid Amazon S3 bucket."""
    _ERROR_CODE = "InvalidOrigin"


class InvalidOriginAccessControl(CloudFrontError):
    """The origin access control is not valid."""
    _ERROR_CODE = "InvalidOriginAccessControl"


class InvalidOriginAccessIdentity(CloudFrontError):
    """The origin access identity is not valid or doesn't exist."""
    _ERROR_CODE = "InvalidOriginAccessIdentity"


class InvalidOriginKeepaliveTimeout(CloudFrontError):
    """The keep alive timeout specified for the origin is not valid."""
    _ERROR_CODE = "InvalidOriginKeepaliveTimeout"


class InvalidOriginReadTimeout(CloudFrontError):
    """The read timeout specified for the origin is not valid."""
    _ERROR_CODE = "InvalidOriginReadTimeout"


class InvalidProtocolSettings(CloudFrontError):
    """You cannot specify SSLv3 as the minimum protocol version if you only want to support
    only clients that support Server Name Indication (SNI).
    """

    _ERROR_CODE = "InvalidProtocolSettings"


class InvalidQueryStringParameters(CloudFrontError):
    """The query string parameters specified are not valid."""
    _ERROR_CODE = "InvalidQueryStringParameters"


class InvalidRelativePath(CloudFrontError):
    """The relative path is too big, is not URL-encoded, or does not begin with a slash
    (/).
    """

    _ERROR_CODE = "InvalidRelativePath"


class InvalidRequiredProtocol(CloudFrontError):
    """This operation requires the HTTPS protocol. Ensure that you specify the HTTPS
    protocol in your request, or omit the `RequiredProtocols` element from your
    distribution configuration.
    """

    _ERROR_CODE = "InvalidRequiredProtocol"


class InvalidResponseCode(CloudFrontError):
    """A response code is not valid."""
    _ERROR_CODE = "InvalidResponseCode"


class InvalidTTLOrder(CloudFrontError):
    """The TTL order specified is not valid."""
    _ERROR_CODE = "InvalidTTLOrder"


class InvalidTagging(CloudFrontError):
    """The tagging specified is not valid."""
    _ERROR_CODE = "InvalidTagging"


class InvalidViewerCertificate(CloudFrontError):
    """A viewer certificate specified is not valid."""
    _ERROR_CODE = "InvalidViewerCertificate"


class InvalidWebACLId(CloudFrontError):
    """A web ACL ID specified is not valid. To specify a web ACL created using the latest
    version of WAF, use the ACL ARN, for example `arn:aws:wafv2:us-east-
    1:123456789012:global/webacl/ExampleWebACL/473e64fd-f30b-4765-81a0-62ad96dd167a`. To
    specify a web ACL created using WAF Classic, use the ACL ID, for example
    `473e64fd-f30b-4765-81a0-62ad96dd167a`.
    """

    _ERROR_CODE = "InvalidWebACLId"


class KeyGroupAlreadyExists(CloudFrontError):
    """A key group with this name already exists. You must provide a unique name. To modify
    an existing key group, use `UpdateKeyGroup`.
    """

    _ERROR_CODE = "KeyGroupAlreadyExists"


class MissingBody(CloudFrontError):
    """This operation requires a body. Ensure that the body is present and the `Content-
    Type` header is set.
    """

    _ERROR_CODE = "MissingBody"


class MonitoringSubscriptionAlreadyExists(CloudFrontError):
    """A monitoring subscription already exists for the specified distribution."""
    _ERROR_CODE = "MonitoringSubscriptionAlreadyExists"


class NoSuchCachePolicy(CloudFrontError):
    """The cache policy does not exist."""
    _ERROR_CODE = "NoSuchCachePolicy"


class NoSuchCloudFrontOriginAccessIdentity(CloudFrontError):
    """The specified origin access identity does not exist."""
    _ERROR_CODE = "NoSuchCloudFrontOriginAccessIdentity"


class NoSuchContinuousDeploymentPolicy(CloudFrontError):
    """The continuous deployment policy doesn't exist."""
    _ERROR_CODE = "NoSuchContinuousDeploymentPolicy"


class NoSuchDistribution(CloudFrontError):
    """The specified distribution does not exist."""
    _ERROR_CODE = "NoSuchDistribution"


class NoSuchFieldLevelEncryptionConfig(CloudFrontError):
    """The specified configuration for field-level encryption doesn't exist."""
    _ERROR_CODE = "NoSuchFieldLevelEncryptionConfig"


class NoSuchFieldLevelEncryptionProfile(CloudFrontError):
    """The specified profile for field-level encryption doesn't exist."""
    _ERROR_CODE = "NoSuchFieldLevelEncryptionProfile"


class NoSuchFunctionExists(CloudFrontError):
    """The function does not exist."""
    _ERROR_CODE = "NoSuchFunctionExists"


class NoSuchInvalidation(CloudFrontError):
    """The specified invalidation does not exist."""
    _ERROR_CODE = "NoSuchInvalidation"


class NoSuchMonitoringSubscription(CloudFrontError):
    """A monitoring subscription does not exist for the specified distribution."""
    _ERROR_CODE = "NoSuchMonitoringSubscription"


class NoSuchOrigin(CloudFrontError):
    """No origin exists with the specified `Origin Id`."""
    _ERROR_CODE = "NoSuchOrigin"


class NoSuchOriginAccessControl(CloudFrontError):
    """The origin access control does not exist."""
    _ERROR_CODE = "NoSuchOriginAccessControl"


class NoSuchOriginRequestPolicy(CloudFrontError):
    """The origin request policy does not exist."""
    _ERROR_CODE = "NoSuchOriginRequestPolicy"


class NoSuchPublicKey(CloudFrontError):
    """The specified public key doesn't exist."""
    _ERROR_CODE = "NoSuchPublicKey"


class NoSuchRealtimeLogConfig(CloudFrontError):
    """The real-time log configuration does not exist."""
    _ERROR_CODE = "NoSuchRealtimeLogConfig"


class NoSuchResource(CloudFrontError):
    """A resource that was specified is not valid."""
    _ERROR_CODE = "NoSuchResource"


class NoSuchResponseHeadersPolicy(CloudFrontError):
    """The response headers policy does not exist."""
    _ERROR_CODE = "NoSuchResponseHeadersPolicy"


class NoSuchStreamingDistribution(CloudFrontError):
    """The specified streaming distribution does not exist."""
    _ERROR_CODE = "NoSuchStreamingDistribution"


class OriginAccessControlAlreadyExists(CloudFrontError):
    """An origin access control with the specified parameters already exists."""
    _ERROR_CODE = "OriginAccessControlAlreadyExists"


class OriginAccessControlInUse(CloudFrontError):
    """Cannot delete the origin access control because it's in use by one or more
    distributions.
    """

    _ERROR_CODE = "OriginAccessControlInUse"


class OriginRequestPolicyAlreadyExists(CloudFrontError):
    """An origin request policy with this name already exists. You must provide a unique
    name. To modify an existing origin request policy, use `UpdateOriginRequestPolicy`.
    """

    _ERROR_CODE = "OriginRequestPolicyAlreadyExists"


class OriginRequestPolicyInUse(CloudFrontError):
    """Cannot delete the origin request policy because it is attached to one or more cache
    behaviors.
    """

    _ERROR_CODE = "OriginRequestPolicyInUse"


class PreconditionFailed(CloudFrontError):
    """The precondition in one or more of the request fields evaluated to `false`."""
    _ERROR_CODE = "PreconditionFailed"


class PublicKeyAlreadyExists(CloudFrontError):
    """The specified public key already exists."""
    _ERROR_CODE = "PublicKeyAlreadyExists"


class PublicKeyInUse(CloudFrontError):
    """The specified public key is in use."""
    _ERROR_CODE = "PublicKeyInUse"


class QueryArgProfileEmpty(CloudFrontError):
    """No profile specified for the field-level encryption query argument."""
    _ERROR_CODE = "QueryArgProfileEmpty"


class RealtimeLogConfigAlreadyExists(CloudFrontError):
    """A real-time log configuration with this name already exists. You must provide a
    unique name. To modify an existing real-time log configuration, use
    `UpdateRealtimeLogConfig`.
    """

    _ERROR_CODE = "RealtimeLogConfigAlreadyExists"


class RealtimeLogConfigInUse(CloudFrontError):
    """Cannot delete the real-time log configuration because it is attached to one or more
    cache behaviors.
    """

    _ERROR_CODE = "RealtimeLogConfigInUse"


class RealtimeLogConfigOwnerMismatch(CloudFrontError):
    """The specified real-time log configuration belongs to a different Amazon Web Services
    account.
    """

    _ERROR_CODE = "RealtimeLogConfigOwnerMismatch"


class ResourceInUse(CloudFrontError):
    """Cannot delete this resource because it is in use."""
    _ERROR_CODE = "ResourceInUse"


class ResponseHeadersPolicyAlreadyExists(CloudFrontError):
    """A response headers policy with this name already exists. You must provide a unique
    name. To modify an existing response headers policy, use
    `UpdateResponseHeadersPolicy`.
    """

    _ERROR_CODE = "ResponseHeadersPolicyAlreadyExists"


class ResponseHeadersPolicyInUse(CloudFrontError):
    """Cannot delete the response headers policy because it is attached to one or more
    cache behaviors in a CloudFront distribution.
    """

    _ERROR_CODE = "ResponseHeadersPolicyInUse"


class StagingDistributionInUse(CloudFrontError):
    """A continuous deployment policy for this staging distribution already exists."""
    _ERROR_CODE = "StagingDistributionInUse"


class StreamingDistributionAlreadyExists(CloudFrontError):
    """The caller reference you attempted to create the streaming distribution with is
    associated with another distribution
    """

    _ERROR_CODE = "StreamingDistributionAlreadyExists"


class StreamingDistributionNotDisabled(CloudFrontError):
    """The specified CloudFront distribution is not disabled. You must disable the
    distribution before you can delete it.
    """

    _ERROR_CODE = "StreamingDistributionNotDisabled"


class TestFunctionFailed(CloudFrontError):
    """The CloudFront function failed."""
    _ERROR_CODE = "TestFunctionFailed"


class TooLongCSPInResponseHeadersPolicy(CloudFrontError):
    """The length of the `Content-Security-Policy` header value in the response headers
    policy exceeds the maximum.

    For more information, see Quotas (formerly known as limits) in the Amazon CloudFront
    Developer Guide.
    """

    _ERROR_CODE = "TooLongCSPInResponseHeadersPolicy"


class TooManyCacheBehaviors(CloudFrontError):
    """You cannot create more cache behaviors for the distribution."""
    _ERROR_CODE = "TooManyCacheBehaviors"


class TooManyCachePolicies(CloudFrontError):
    """You have reached the maximum number of cache policies for this Amazon Web Services
    account. For more information, see Quotas (formerly known as limits) in the Amazon
    CloudFront Developer Guide.
    """

    _ERROR_CODE = "TooManyCachePolicies"


class TooManyCertificates(CloudFrontError):
    """You cannot create anymore custom SSL/TLS certificates."""
    _ERROR_CODE = "TooManyCertificates"


class TooManyCloudFrontOriginAccessIdentities(CloudFrontError):
    """Processing your request would cause you to exceed the maximum number of origin
    access identities allowed.
    """

    _ERROR_CODE = "TooManyCloudFrontOriginAccessIdentities"


class TooManyContinuousDeploymentPolicies(CloudFrontError):
    """You have reached the maximum number of continuous deployment policies for this
    Amazon Web Services account.
    """

    _ERROR_CODE = "TooManyContinuousDeploymentPolicies"


class TooManyCookieNamesInWhiteList(CloudFrontError):
    """Your request contains more cookie names in the whitelist than are allowed per cache
    behavior.
    """

    _ERROR_CODE = "TooManyCookieNamesInWhiteList"


class TooManyCookiesInCachePolicy(CloudFrontError):
    """The number of cookies in the cache policy exceeds the maximum. For more information,
    see Quotas (formerly known as limits) in the Amazon CloudFront Developer Guide.
    """

    _ERROR_CODE = "TooManyCookiesInCachePolicy"


class TooManyCookiesInOriginRequestPolicy(CloudFrontError):
    """The number of cookies in the origin request policy exceeds the maximum. For more
    information, see Quotas (formerly known as limits) in the Amazon CloudFront
    Developer Guide.
    """

    _ERROR_CODE = "TooManyCookiesInOriginRequestPolicy"


class TooManyCustomHeadersInResponseHeadersPolicy(CloudFrontError):
    """The number of custom headers in the response headers policy exceeds the maximum.

    For more information, see Quotas (formerly known as limits) in the Amazon CloudFront
    Developer Guide.
    """

    _ERROR_CODE = "TooManyCustomHeadersInResponseHeadersPolicy"


class TooManyDistributionCNAMEs(CloudFrontError):
    """Your request contains more CNAMEs than are allowed per distribution."""
    _ERROR_CODE = "TooManyDistributionCNAMEs"


class TooManyDistributions(CloudFrontError):
    """Processing your request would cause you to exceed the maximum number of
    distributions allowed.
    """

    _ERROR_CODE = "TooManyDistributions"


class TooManyDistributionsAssociatedToCachePolicy(CloudFrontError):
    """The maximum number of distributions have been associated with the specified cache
    policy. For more information, see Quotas (formerly known as limits) in the Amazon
    CloudFront Developer Guide.
    """

    _ERROR_CODE = "TooManyDistributionsAssociatedToCachePolicy"


class TooManyDistributionsAssociatedToFieldLevelEncryptionConfig(CloudFrontError):
    """The maximum number of distributions have been associated with the specified
    configuration for field-level encryption.
    """

    _ERROR_CODE = "TooManyDistributionsAssociatedToFieldLevelEncryptionConfig"


class TooManyDistributionsAssociatedToKeyGroup(CloudFrontError):
    """The number of distributions that reference this key group is more than the maximum
    allowed. For more information, see Quotas (formerly known as limits) in the Amazon
    CloudFront Developer Guide.
    """

    _ERROR_CODE = "TooManyDistributionsAssociatedToKeyGroup"


class TooManyDistributionsAssociatedToOriginAccessControl(CloudFrontError):
    """The maximum number of distributions have been associated with the specified origin
    access control.

    For more information, see Quotas (formerly known as limits) in the Amazon CloudFront
    Developer Guide.
    """

    _ERROR_CODE = "TooManyDistributionsAssociatedToOriginAccessControl"


class TooManyDistributionsAssociatedToOriginRequestPolicy(CloudFrontError):
    """The maximum number of distributions have been associated with the specified origin
    request policy. For more information, see Quotas (formerly known as limits) in the
    Amazon CloudFront Developer Guide.
    """

    _ERROR_CODE = "TooManyDistributionsAssociatedToOriginRequestPolicy"


class TooManyDistributionsAssociatedToResponseHeadersPolicy(CloudFrontError):
    """The maximum number of distributions have been associated with the specified response
    headers policy.

    For more information, see Quotas (formerly known as limits) in the Amazon CloudFront
    Developer Guide.
    """

    _ERROR_CODE = "TooManyDistributionsAssociatedToResponseHeadersPolicy"


class TooManyDistributionsWithFunctionAssociations(CloudFrontError):
    """You have reached the maximum number of distributions that are associated with a
    CloudFront function. For more information, see Quotas (formerly known as limits) in
    the Amazon CloudFront Developer Guide.
    """

    _ERROR_CODE = "TooManyDistributionsWithFunctionAssociations"


class TooManyDistributionsWithLambdaAssociations(CloudFrontError):
    """Processing your request would cause the maximum number of distributions with
    Lambda@Edge function associations per owner to be exceeded.
    """

    _ERROR_CODE = "TooManyDistributionsWithLambdaAssociations"


class TooManyDistributionsWithSingleFunctionARN(CloudFrontError):
    """The maximum number of distributions have been associated with the specified
    Lambda@Edge function.
    """

    _ERROR_CODE = "TooManyDistributionsWithSingleFunctionARN"


class TooManyFieldLevelEncryptionConfigs(CloudFrontError):
    """The maximum number of configurations for field-level encryption have been created."""
    _ERROR_CODE = "TooManyFieldLevelEncryptionConfigs"


class TooManyFieldLevelEncryptionContentTypeProfiles(CloudFrontError):
    """The maximum number of content type profiles for field-level encryption have been
    created.
    """

    _ERROR_CODE = "TooManyFieldLevelEncryptionContentTypeProfiles"


class TooManyFieldLevelEncryptionEncryptionEntities(CloudFrontError):
    """The maximum number of encryption entities for field-level encryption have been
    created.
    """

    _ERROR_CODE = "TooManyFieldLevelEncryptionEncryptionEntities"


class TooManyFieldLevelEncryptionFieldPatterns(CloudFrontError):
    """The maximum number of field patterns for field-level encryption have been created."""
    _ERROR_CODE = "TooManyFieldLevelEncryptionFieldPatterns"


class TooManyFieldLevelEncryptionProfiles(CloudFrontError):
    """The maximum number of profiles for field-level encryption have been created."""
    _ERROR_CODE = "TooManyFieldLevelEncryptionProfiles"


class TooManyFieldLevelEncryptionQueryArgProfiles(CloudFrontError):
    """The maximum number of query arg profiles for field-level encryption have been
    created.
    """

    _ERROR_CODE = "TooManyFieldLevelEncryptionQueryArgProfiles"


class TooManyFunctionAssociations(CloudFrontError):
    """You have reached the maximum number of CloudFront function associations for this
    distribution. For more information, see Quotas (formerly known as limits) in the
    Amazon CloudFront Developer Guide.
    """

    _ERROR_CODE = "TooManyFunctionAssociations"


class TooManyFunctions(CloudFrontError):
    """You have reached the maximum number of CloudFront functions for this Amazon Web
    Services account. For more information, see Quotas (formerly known as limits) in the
    Amazon CloudFront Developer Guide.
    """

    _ERROR_CODE = "TooManyFunctions"


class TooManyHeadersInCachePolicy(CloudFrontError):
    """The number of headers in the cache policy exceeds the maximum. For more information,
    see Quotas (formerly known as limits) in the Amazon CloudFront Developer Guide.
    """

    _ERROR_CODE = "TooManyHeadersInCachePolicy"


class TooManyHeadersInForwardedValues(CloudFrontError):
    """Your request contains too many headers in forwarded values."""
    _ERROR_CODE = "TooManyHeadersInForwardedValues"


class TooManyHeadersInOriginRequestPolicy(CloudFrontError):
    """The number of headers in the origin request policy exceeds the maximum. For more
    information, see Quotas (formerly known as limits) in the Amazon CloudFront
    Developer Guide.
    """

    _ERROR_CODE = "TooManyHeadersInOriginRequestPolicy"


class TooManyInvalidationsInProgress(CloudFrontError):
    """You have exceeded the maximum number of allowable InProgress invalidation batch
    requests, or invalidation objects.
    """

    _ERROR_CODE = "TooManyInvalidationsInProgress"


class TooManyKeyGroups(CloudFrontError):
    """You have reached the maximum number of key groups for this Amazon Web Services
    account. For more information, see Quotas (formerly known as limits) in the Amazon
    CloudFront Developer Guide.
    """

    _ERROR_CODE = "TooManyKeyGroups"


class TooManyKeyGroupsAssociatedToDistribution(CloudFrontError):
    """The number of key groups referenced by this distribution is more than the maximum
    allowed. For more information, see Quotas (formerly known as limits) in the Amazon
    CloudFront Developer Guide.
    """

    _ERROR_CODE = "TooManyKeyGroupsAssociatedToDistribution"


class TooManyLambdaFunctionAssociations(CloudFrontError):
    """Your request contains more Lambda@Edge function associations than are allowed per
    distribution.
    """

    _ERROR_CODE = "TooManyLambdaFunctionAssociations"


class TooManyOriginAccessControls(CloudFrontError):
    """The number of origin access controls in your Amazon Web Services account exceeds the
    maximum allowed.

    For more information, see Quotas (formerly known as limits) in the Amazon CloudFront
    Developer Guide.
    """

    _ERROR_CODE = "TooManyOriginAccessControls"


class TooManyOriginCustomHeaders(CloudFrontError):
    """Your request contains too many origin custom headers."""
    _ERROR_CODE = "TooManyOriginCustomHeaders"


class TooManyOriginGroupsPerDistribution(CloudFrontError):
    """Processing your request would cause you to exceed the maximum number of origin
    groups allowed.
    """

    _ERROR_CODE = "TooManyOriginGroupsPerDistribution"


class TooManyOriginRequestPolicies(CloudFrontError):
    """You have reached the maximum number of origin request policies for this Amazon Web
    Services account. For more information, see Quotas (formerly known as limits) in the
    Amazon CloudFront Developer Guide.
    """

    _ERROR_CODE = "TooManyOriginRequestPolicies"


class TooManyOrigins(CloudFrontError):
    """You cannot create more origins for the distribution."""
    _ERROR_CODE = "TooManyOrigins"


class TooManyPublicKeys(CloudFrontError):
    """The maximum number of public keys for field-level encryption have been created. To
    create a new public key, delete one of the existing keys.
    """

    _ERROR_CODE = "TooManyPublicKeys"


class TooManyPublicKeysInKeyGroup(CloudFrontError):
    """The number of public keys in this key group is more than the maximum allowed. For
    more information, see Quotas (formerly known as limits) in the Amazon CloudFront
    Developer Guide.
    """

    _ERROR_CODE = "TooManyPublicKeysInKeyGroup"


class TooManyQueryStringParameters(CloudFrontError):
    """Your request contains too many query string parameters."""
    _ERROR_CODE = "TooManyQueryStringParameters"


class TooManyQueryStringsInCachePolicy(CloudFrontError):
    """The number of query strings in the cache policy exceeds the maximum. For more
    information, see Quotas (formerly known as limits) in the Amazon CloudFront
    Developer Guide.
    """

    _ERROR_CODE = "TooManyQueryStringsInCachePolicy"


class TooManyQueryStringsInOriginRequestPolicy(CloudFrontError):
    """The number of query strings in the origin request policy exceeds the maximum. For
    more information, see Quotas (formerly known as limits) in the Amazon CloudFront
    Developer Guide.
    """

    _ERROR_CODE = "TooManyQueryStringsInOriginRequestPolicy"


class TooManyRealtimeLogConfigs(CloudFrontError):
    """You have reached the maximum number of real-time log configurations for this Amazon
    Web Services account. For more information, see Quotas (formerly known as limits) in
    the Amazon CloudFront Developer Guide.
    """

    _ERROR_CODE = "TooManyRealtimeLogConfigs"


class TooManyRemoveHeadersInResponseHeadersPolicy(CloudFrontError):
    """The number of headers in `RemoveHeadersConfig` in the response headers policy
    exceeds the maximum.

    For more information, see Quotas (formerly known as limits) in the Amazon CloudFront
    Developer Guide.
    """

    _ERROR_CODE = "TooManyRemoveHeadersInResponseHeadersPolicy"


class TooManyResponseHeadersPolicies(CloudFrontError):
    """You have reached the maximum number of response headers policies for this Amazon Web
    Services account.

    For more information, see Quotas (formerly known as limits) in the Amazon CloudFront
    Developer Guide.
    """

    _ERROR_CODE = "TooManyResponseHeadersPolicies"


class TooManyStreamingDistributionCNAMEs(CloudFrontError):
    """Your request contains more CNAMEs than are allowed per distribution."""
    _ERROR_CODE = "TooManyStreamingDistributionCNAMEs"


class TooManyStreamingDistributions(CloudFrontError):
    """Processing your request would cause you to exceed the maximum number of streaming
    distributions allowed.
    """

    _ERROR_CODE = "TooManyStreamingDistributions"


class TooManyTrustedSigners(CloudFrontError):
    """Your request contains more trusted signers than are allowed per distribution."""
    _ERROR_CODE = "TooManyTrustedSigners"


class TrustedKeyGroupDoesNotExist(CloudFrontError):
    """The specified key group does not exist."""
    _ERROR_CODE = "TrustedKeyGroupDoesNotExist"


class TrustedSignerDoesNotExist(CloudFrontError):
    """One or more of your trusted signers don't exist."""
    _ERROR_CODE = "TrustedSignerDoesNotExist"


class UnsupportedOperation(CloudFrontError):
    """This operation is not supported in this region."""
    _ERROR_CODE = "UnsupportedOperation"


EXCEPTIONS: dict[str, type[CloudFrontError]] = {
    "AccessDenied": AccessDenied,
    "BatchTooLarge": BatchTooLarge,
    "CNAMEAlreadyExists": CNAMEAlreadyExists,
    "CachePolicyAlreadyExists": CachePolicyAlreadyExists,
    "CachePolicyInUse": CachePolicyInUse,
    "CannotChangeImmutablePublicKeyFields": CannotChangeImmutablePublicKeyFields,
    "CannotDeleteEntityWhileInUse": CannotDeleteEntityWhileInUse,
    "CloudFrontOriginAccessIdentityAlreadyExists": CloudFrontOriginAccessIdentityAlreadyExists,
    "CloudFrontOriginAccessIdentityInUse": CloudFrontOriginAccessIdentityInUse,
    "ContinuousDeploymentPolicyAlreadyExists": ContinuousDeploymentPolicyAlreadyExists,
    "ContinuousDeploymentPolicyInUse": ContinuousDeploymentPolicyInUse,
    "DistributionAlreadyExists": DistributionAlreadyExists,
    "DistributionNotDisabled": DistributionNotDisabled,
    "EntityAlreadyExists": EntityAlreadyExists,
    "EntityLimitExceeded": EntityLimitExceeded,
    "EntityNotFound": EntityNotFound,
    "EntitySizeLimitExceeded": EntitySizeLimitExceeded,
    "FieldLevelEncryptionConfigAlreadyExists": FieldLevelEncryptionConfigAlreadyExists,
    "FieldLevelEncryptionConfigInUse": FieldLevelEncryptionConfigInUse,
    "FieldLevelEncryptionProfileAlreadyExists": FieldLevelEncryptionProfileAlreadyExists,
    "FieldLevelEncryptionProfileInUse": FieldLevelEncryptionProfileInUse,
    "FieldLevelEncryptionProfileSizeExceeded": FieldLevelEncryptionProfileSizeExceeded,
    "FunctionAlreadyExists": FunctionAlreadyExists,
    "FunctionInUse": FunctionInUse,
    "FunctionSizeLimitExceeded": FunctionSizeLimitExceeded,
    "IllegalDelete": IllegalDelete,
    "IllegalFieldLevelEncryptionConfigAssociationWithCacheBehavior": IllegalFieldLevelEncryptionConfigAssociationWithCacheBehavior,
    "IllegalOriginAccessConfiguration": IllegalOriginAccessConfiguration,
    "IllegalUpdate": IllegalUpdate,
    "InconsistentQuantities": InconsistentQuantities,
    "InvalidArgument": InvalidArgument,
    "InvalidDefaultRootObject": InvalidDefaultRootObject,
    "InvalidDomainNameForOriginAccessControl": InvalidDomainNameForOriginAccessControl,
    "InvalidErrorCode": InvalidErrorCode,
    "InvalidForwardCookies": InvalidForwardCookies,
    "InvalidFunctionAssociation": InvalidFunctionAssociation,
    "InvalidGeoRestrictionParameter": InvalidGeoRestrictionParameter,
    "InvalidHeadersForS3Origin": InvalidHeadersForS3Origin,
    "InvalidIfMatchVersion": InvalidIfMatchVersion,
    "InvalidLambdaFunctionAssociation": InvalidLambdaFunctionAssociation,
    "InvalidLocationCode": InvalidLocationCode,
    "InvalidMinimumProtocolVersion": InvalidMinimumProtocolVersion,
    "InvalidOrigin": InvalidOrigin,
    "InvalidOriginAccessControl": InvalidOriginAccessControl,
    "InvalidOriginAccessIdentity": InvalidOriginAccessIdentity,
    "InvalidOriginKeepaliveTimeout": InvalidOriginKeepaliveTimeout,
    "InvalidOriginReadTimeout": InvalidOriginReadTimeout,
    "InvalidProtocolSettings": InvalidProtocolSettings,
    "InvalidQueryStringParameters": InvalidQueryStringParameters,
    "InvalidRelativePath": InvalidRelativePath,
    "InvalidRequiredProtocol": InvalidRequiredProtocol,
    "InvalidResponseCode": InvalidResponseCode,
    "InvalidTTLOrder": InvalidTTLOrder,
    "InvalidTagging": InvalidTagging,
    "InvalidViewerCertificate": InvalidViewerCertificate,
    "InvalidWebACLId": InvalidWebACLId,
    "KeyGroupAlreadyExists": KeyGroupAlreadyExists,
    "MissingBody": MissingBody,
    "MonitoringSubscriptionAlreadyExists": MonitoringSubscriptionAlreadyExists,
    "NoSuchCachePolicy": NoSuchCachePolicy,
    "NoSuchCloudFrontOriginAccessIdentity": NoSuchCloudFrontOriginAccessIdentity,
    "NoSuchContinuousDeploymentPolicy": NoSuchContinuousDeploymentPolicy,
    "NoSuchDistribution": NoSuchDistribution,
    "NoSuchFieldLevelEncryptionConfig": NoSuchFieldLevelEncryptionConfig,
    "NoSuchFieldLevelEncryptionProfile": NoSuchFieldLevelEncryptionProfile,
    "NoSuchFunctionExists": NoSuchFunctionExists,
    "NoSuchInvalidation": NoSuchInvalidation,
    "NoSuchMonitoringSubscription": NoSuchMonitoringSubscription,
    "NoSuchOrigin": NoSuchOrigin,
    "NoSuchOriginAccessControl": NoSuchOriginAccessControl,
    "NoSuchOriginRequestPolicy": NoSuchOriginRequestPolicy,
    "NoSuchPublicKey": NoSuchPublicKey,
    "NoSuchRealtimeLogConfig": NoSuchRealtimeLogConfig,
    "NoSuchResource": NoSuchResource,
    "NoSuchResponseHeadersPolicy": NoSuchResponseHeadersPolicy,
    "NoSuchStreamingDistribution": NoSuchStreamingDistribution,
    "OriginAccessControlAlreadyExists": OriginAccessControlAlreadyExists,
    "OriginAccessControlInUse": OriginAccessControlInUse,
    "OriginRequestPolicyAlreadyExists": OriginRequestPolicyAlreadyExists,
    "OriginRequestPolicyInUse": OriginRequestPolicyInUse,
    "PreconditionFailed": PreconditionFailed,
    "PublicKeyAlreadyExists": PublicKeyAlreadyExists,
    "PublicKeyInUse": PublicKeyInUse,
    "QueryArgProfileEmpty": QueryArgProfileEmpty,
    "RealtimeLogConfigAlreadyExists": RealtimeLogConfigAlreadyExists,
    "RealtimeLogConfigInUse": RealtimeLogConfigInUse,
    "RealtimeLogConfigOwnerMismatch": RealtimeLogConfigOwnerMismatch,
    "ResourceInUse": ResourceInUse,
    "ResponseHeadersPolicyAlreadyExists": ResponseHeadersPolicyAlreadyExists,
    "ResponseHeadersPolicyInUse": ResponseHeadersPolicyInUse,
    "StagingDistributionInUse": StagingDistributionInUse,
    "StreamingDistributionAlreadyExists": StreamingDistributionAlreadyExists,
    "StreamingDistributionNotDisabled": StreamingDistributionNotDisabled,
    "TestFunctionFailed": TestFunctionFailed,
    "TooLongCSPInResponseHeadersPolicy": TooLongCSPInResponseHeadersPolicy,
    "TooManyCacheBehaviors": TooManyCacheBehaviors,
    "TooManyCachePolicies": TooManyCachePolicies,
    "TooManyCertificates": TooManyCertificates,
    "TooManyCloudFrontOriginAccessIdentities": TooManyCloudFrontOriginAccessIdentities,
    "TooManyContinuousDeploymentPolicies": TooManyContinuousDeploymentPolicies,
    "TooManyCookieNamesInWhiteList": TooManyCookieNamesInWhiteList,
    "TooManyCookiesInCachePolicy": TooManyCookiesInCachePolicy,
    "TooManyCookiesInOriginRequestPolicy": TooManyCookiesInOriginRequestPolicy,
    "TooManyCustomHeadersInResponseHeadersPolicy": TooManyCustomHeadersInResponseHeadersPolicy,
    "TooManyDistributionCNAMEs": TooManyDistributionCNAMEs,
    "TooManyDistributions": TooManyDistributions,
    "TooManyDistributionsAssociatedToCachePolicy": TooManyDistributionsAssociatedToCachePolicy,
    "TooManyDistributionsAssociatedToFieldLevelEncryptionConfig": TooManyDistributionsAssociatedToFieldLevelEncryptionConfig,
    "TooManyDistributionsAssociatedToKeyGroup": TooManyDistributionsAssociatedToKeyGroup,
    "TooManyDistributionsAssociatedToOriginAccessControl": TooManyDistributionsAssociatedToOriginAccessControl,
    "TooManyDistributionsAssociatedToOriginRequestPolicy": TooManyDistributionsAssociatedToOriginRequestPolicy,
    "TooManyDistributionsAssociatedToResponseHeadersPolicy": TooManyDistributionsAssociatedToResponseHeadersPolicy,
    "TooManyDistributionsWithFunctionAssociations": TooManyDistributionsWithFunctionAssociations,
    "TooManyDistributionsWithLambdaAssociations": TooManyDistributionsWithLambdaAssociations,
    "TooManyDistributionsWithSingleFunctionARN": TooManyDistributionsWithSingleFunctionARN,
    "TooManyFieldLevelEncryptionConfigs": TooManyFieldLevelEncryptionConfigs,
    "TooManyFieldLevelEncryptionContentTypeProfiles": TooManyFieldLevelEncryptionContentTypeProfiles,
    "TooManyFieldLevelEncryptionEncryptionEntities": TooManyFieldLevelEncryptionEncryptionEntities,
    "TooManyFieldLevelEncryptionFieldPatterns": TooManyFieldLevelEncryptionFieldPatterns,
    "TooManyFieldLevelEncryptionProfiles": TooManyFieldLevelEncryptionProfiles,
    "TooManyFieldLevelEncryptionQueryArgProfiles": TooManyFieldLevelEncryptionQueryArgProfiles,
    "TooManyFunctionAssociations": TooManyFunctionAssociations,
    "TooManyFunctions": TooManyFunctions,
    "TooManyHeadersInCachePolicy": TooManyHeadersInCachePolicy,
    "TooManyHeadersInForwardedValues": TooManyHeadersInForwardedValues,
    "TooManyHeadersInOriginRequestPolicy": TooManyHeadersInOriginRequestPolicy,
    "TooManyInvalidationsInProgress": TooManyInvalidationsInProgress,
    "TooManyKeyGroups": TooManyKeyGroups,
    "TooManyKeyGroupsAssociatedToDistribution": TooManyKeyGroupsAssociatedToDistribution,
    "TooManyLambdaFunctionAssociations": TooManyLambdaFunctionAssociations,
    "TooManyOriginAccessControls": TooManyOriginAccessControls,
    "TooManyOriginCustomHeaders": TooManyOriginCustomHeaders,
    "TooManyOriginGroupsPerDistribution": TooManyOriginGroupsPerDistribution,
    "TooManyOriginRequestPolicies": TooManyOriginRequestPolicies,
    "TooManyOrigins": TooManyOrigins,
    "TooManyPublicKeys": TooManyPublicKeys,
    "TooManyPublicKeysInKeyGroup": TooManyPublicKeysInKeyGroup,
    "TooManyQueryStringParameters": TooManyQueryStringParameters,
    "TooManyQueryStringsInCachePolicy": TooManyQueryStringsInCachePolicy,
    "TooManyQueryStringsInOriginRequestPolicy": TooManyQueryStringsInOriginRequestPolicy,
    "TooManyRealtimeLogConfigs": TooManyRealtimeLogConfigs,
    "TooManyRemoveHeadersInResponseHeadersPolicy": TooManyRemoveHeadersInResponseHeadersPolicy,
    "TooManyResponseHeadersPolicies": TooManyResponseHeadersPolicies,
    "TooManyStreamingDistributionCNAMEs": TooManyStreamingDistributionCNAMEs,
    "TooManyStreamingDistributions": TooManyStreamingDistributions,
    "TooManyTrustedSigners": TooManyTrustedSigners,
    "TrustedKeyGroupDoesNotExist": TrustedKeyGroupDoesNotExist,
    "TrustedSignerDoesNotExist": TrustedSignerDoesNotExist,
    "UnsupportedOperation": UnsupportedOperation,
}
