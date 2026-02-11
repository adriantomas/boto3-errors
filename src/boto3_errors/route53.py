# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class Route53Error(Boto3Error):
    _SERVICE = "route53"


class CidrBlockInUseException(Route53Error):
    """This CIDR block is already in use."""
    _ERROR_CODE = "CidrBlockInUseException"


class CidrCollectionAlreadyExistsException(Route53Error):
    """A CIDR collection with this name and a different caller reference already exists in
    this account.
    """

    _ERROR_CODE = "CidrCollectionAlreadyExistsException"


class CidrCollectionInUseException(Route53Error):
    """This CIDR collection is in use, and isn't empty."""
    _ERROR_CODE = "CidrCollectionInUseException"


class CidrCollectionVersionMismatchException(Route53Error):
    """The CIDR collection version you provided, doesn't match the one in the
    `ListCidrCollections` operation.
    """

    _ERROR_CODE = "CidrCollectionVersionMismatchException"


class ConcurrentModification(Route53Error):
    """Another user submitted a request to create, update, or delete the object at the same
    time that you did. Retry the request.
    """

    _ERROR_CODE = "ConcurrentModification"


class ConflictingDomainExists(Route53Error):
    """The cause of this error depends on the operation that you're performing:

    - Create a public hosted zone: Two hosted zones that have the same name or that have
      a parent/child relationship (example.com and test.example.com) can't have any
      common name servers. You tried to create a hosted zone that has the same name as
      an existing hosted zone or that's the parent or child of an existing hosted zone,
      and you specified a delegation set that shares one or more name servers with the
      existing hosted zone. For more information, see CreateReusableDelegationSet.
    - Create a private hosted zone: A hosted zone with the specified name already exists
      and is already associated with the Amazon VPC that you specified.
    - Associate VPCs with a private hosted zone: The VPC that you specified is already
      associated with another hosted zone that has the same name.
    """

    _ERROR_CODE = "ConflictingDomainExists"


class ConflictingTypes(Route53Error):
    """You tried to update a traffic policy instance by using a traffic policy version that
    has a different DNS type than the current type for the instance. You specified the
    type in the JSON document in the `CreateTrafficPolicy` or
    `CreateTrafficPolicyVersion`request.
    """

    _ERROR_CODE = "ConflictingTypes"


class DNSSECNotFound(Route53Error):
    """The hosted zone doesn't have any DNSSEC resources."""
    _ERROR_CODE = "DNSSECNotFound"


class DelegationSetAlreadyCreated(Route53Error):
    """A delegation set with the same owner and caller reference combination has already
    been created.
    """

    _ERROR_CODE = "DelegationSetAlreadyCreated"


class DelegationSetAlreadyReusable(Route53Error):
    """The specified delegation set has already been marked as reusable."""
    _ERROR_CODE = "DelegationSetAlreadyReusable"


class DelegationSetInUse(Route53Error):
    """The specified delegation contains associated hosted zones which must be deleted
    before the reusable delegation set can be deleted.
    """

    _ERROR_CODE = "DelegationSetInUse"


class DelegationSetNotAvailable(Route53Error):
    """You can create a hosted zone that has the same name as an existing hosted zone
    (example.com is common), but there is a limit to the number of hosted zones that
    have the same name. If you get this error, Amazon Route 53 has reached that limit.
    If you own the domain name and Route 53 generates this error, contact Customer
    Support.
    """

    _ERROR_CODE = "DelegationSetNotAvailable"


class DelegationSetNotReusable(Route53Error):
    """A reusable delegation set with the specified ID does not exist."""
    _ERROR_CODE = "DelegationSetNotReusable"


class HealthCheckAlreadyExists(Route53Error):
    """The health check you're attempting to create already exists. Amazon Route 53 returns
    this error when you submit a request that has the following values:

    - The same value for `CallerReference` as an existing health check, and one or more
      values that differ from the existing health check that has the same caller
      reference.
    - The same value for `CallerReference` as a health check that you created and later
      deleted, regardless of the other settings in the request.
    """

    _ERROR_CODE = "HealthCheckAlreadyExists"


class HealthCheckInUse(Route53Error):
    """This error code is not in use."""
    _ERROR_CODE = "HealthCheckInUse"


class HealthCheckVersionMismatch(Route53Error):
    """The value of `HealthCheckVersion` in the request doesn't match the value of
    `HealthCheckVersion` in the health check.
    """

    _ERROR_CODE = "HealthCheckVersionMismatch"


class HostedZoneAlreadyExists(Route53Error):
    """The hosted zone you're trying to create already exists. Amazon Route 53 returns this
    error when a hosted zone has already been created with the specified
    `CallerReference`.
    """

    _ERROR_CODE = "HostedZoneAlreadyExists"


class HostedZoneNotEmpty(Route53Error):
    """The hosted zone contains resource records that are not SOA or NS records."""
    _ERROR_CODE = "HostedZoneNotEmpty"


class HostedZoneNotFound(Route53Error):
    """The specified HostedZone can't be found."""
    _ERROR_CODE = "HostedZoneNotFound"


class HostedZoneNotPrivate(Route53Error):
    """The specified hosted zone is a public hosted zone, not a private hosted zone."""
    _ERROR_CODE = "HostedZoneNotPrivate"


class HostedZonePartiallyDelegated(Route53Error):
    """The hosted zone nameservers don't match the parent nameservers. The hosted zone and
    parent must have the same nameservers.
    """

    _ERROR_CODE = "HostedZonePartiallyDelegated"


class IncompatibleVersion(Route53Error):
    """The resource you're trying to access is unsupported on this Amazon Route 53
    endpoint.
    """

    _ERROR_CODE = "IncompatibleVersion"


class InsufficientCloudWatchLogsResourcePolicy(Route53Error):
    """Amazon Route 53 doesn't have the permissions required to create log streams and send
    query logs to log streams. Possible causes include the following:

    - There is no resource policy that specifies the log group ARN in the value for
      `Resource`.
    - The resource policy that includes the log group ARN in the value for `Resource`
      doesn't have the necessary permissions.
    - The resource policy hasn't finished propagating yet.
    - The Key management service (KMS) key you specified doesn’t exist or it can’t be
      used with the log group associated with query log. Update or provide a resource
      policy to grant permissions for the KMS key.
    - The Key management service (KMS) key you specified is marked as disabled for the
      log group associated with query log. Update or provide a resource policy to grant
      permissions for the KMS key.
    """

    _ERROR_CODE = "InsufficientCloudWatchLogsResourcePolicy"


class InvalidArgument(Route53Error):
    """Parameter name is not valid."""
    _ERROR_CODE = "InvalidArgument"


class InvalidChangeBatch(Route53Error):
    """This exception contains a list of messages that might contain one or more error
    messages. Each error message indicates one error in the change batch.
    """

    _ERROR_CODE = "InvalidChangeBatch"

    @property
    def messages(self) -> list[Any] | None:
        return self.response.get("messages")


class InvalidDomainName(Route53Error):
    """The specified domain name is not valid."""
    _ERROR_CODE = "InvalidDomainName"


class InvalidInput(Route53Error):
    """The input is not valid."""
    _ERROR_CODE = "InvalidInput"


class InvalidKMSArn(Route53Error):
    """The KeyManagementServiceArn that you specified isn't valid to use with DNSSEC
    signing.
    """

    _ERROR_CODE = "InvalidKMSArn"


class InvalidKeySigningKeyName(Route53Error):
    """The key-signing key (KSK) name that you specified isn't a valid name."""
    _ERROR_CODE = "InvalidKeySigningKeyName"


class InvalidKeySigningKeyStatus(Route53Error):
    """The key-signing key (KSK) status isn't valid or another KSK has the status
    `INTERNAL_FAILURE`.
    """

    _ERROR_CODE = "InvalidKeySigningKeyStatus"


class InvalidPaginationToken(Route53Error):
    """The value that you specified to get the second or subsequent page of results is
    invalid.
    """

    _ERROR_CODE = "InvalidPaginationToken"


class InvalidSigningStatus(Route53Error):
    """Your hosted zone status isn't valid for this operation. In the hosted zone, change
    the status to enable `DNSSEC` or disable `DNSSEC`.
    """

    _ERROR_CODE = "InvalidSigningStatus"


class InvalidTrafficPolicyDocument(Route53Error):
    """The format of the traffic policy document that you specified in the `Document`
    element is not valid.
    """

    _ERROR_CODE = "InvalidTrafficPolicyDocument"


class InvalidVPCId(Route53Error):
    """The VPC ID that you specified either isn't a valid ID or the current account is not
    authorized to access this VPC.
    """

    _ERROR_CODE = "InvalidVPCId"


class KeySigningKeyAlreadyExists(Route53Error):
    """You've already created a key-signing key (KSK) with this name or with the same
    customer managed key ARN.
    """

    _ERROR_CODE = "KeySigningKeyAlreadyExists"


class KeySigningKeyInParentDSRecord(Route53Error):
    """The key-signing key (KSK) is specified in a parent DS record."""
    _ERROR_CODE = "KeySigningKeyInParentDSRecord"


class KeySigningKeyInUse(Route53Error):
    """The key-signing key (KSK) that you specified can't be deactivated because it's the
    only KSK for a currently-enabled DNSSEC. Disable DNSSEC signing, or add or enable
    another KSK.
    """

    _ERROR_CODE = "KeySigningKeyInUse"


class KeySigningKeyWithActiveStatusNotFound(Route53Error):
    """A key-signing key (KSK) with `ACTIVE` status wasn't found."""
    _ERROR_CODE = "KeySigningKeyWithActiveStatusNotFound"


class LastVPCAssociation(Route53Error):
    """The VPC that you're trying to disassociate from the private hosted zone is the last
    VPC that is associated with the hosted zone. Amazon Route 53 doesn't support
    disassociating the last VPC from a hosted zone.
    """

    _ERROR_CODE = "LastVPCAssociation"


class LimitsExceeded(Route53Error):
    """This operation can't be completed because the current account has reached the limit
    on the resource you are trying to create. To request a higher limit, create a case
    with the Amazon Web Services Support Center.
    """

    _ERROR_CODE = "LimitsExceeded"


class NoSuchChange(Route53Error):
    """A change with the specified change ID does not exist."""
    _ERROR_CODE = "NoSuchChange"


class NoSuchCidrCollectionException(Route53Error):
    """The CIDR collection you specified, doesn't exist."""
    _ERROR_CODE = "NoSuchCidrCollectionException"


class NoSuchCidrLocationException(Route53Error):
    """The CIDR collection location doesn't match any locations in your account."""
    _ERROR_CODE = "NoSuchCidrLocationException"


class NoSuchCloudWatchLogsLogGroup(Route53Error):
    """There is no CloudWatch Logs log group with the specified ARN."""
    _ERROR_CODE = "NoSuchCloudWatchLogsLogGroup"


class NoSuchDelegationSet(Route53Error):
    """A reusable delegation set with the specified ID does not exist."""
    _ERROR_CODE = "NoSuchDelegationSet"


class NoSuchGeoLocation(Route53Error):
    """Amazon Route 53 doesn't support the specified geographic location. For a list of
    supported geolocation codes, see the GeoLocation data type.
    """

    _ERROR_CODE = "NoSuchGeoLocation"


class NoSuchHealthCheck(Route53Error):
    """No health check exists with the specified ID."""
    _ERROR_CODE = "NoSuchHealthCheck"


class NoSuchHostedZone(Route53Error):
    """No hosted zone exists with the ID that you specified."""
    _ERROR_CODE = "NoSuchHostedZone"


class NoSuchKeySigningKey(Route53Error):
    """The specified key-signing key (KSK) doesn't exist."""
    _ERROR_CODE = "NoSuchKeySigningKey"


class NoSuchQueryLoggingConfig(Route53Error):
    """There is no DNS query logging configuration with the specified ID."""
    _ERROR_CODE = "NoSuchQueryLoggingConfig"


class NoSuchTrafficPolicy(Route53Error):
    """No traffic policy exists with the specified ID."""
    _ERROR_CODE = "NoSuchTrafficPolicy"


class NoSuchTrafficPolicyInstance(Route53Error):
    """No traffic policy instance exists with the specified ID."""
    _ERROR_CODE = "NoSuchTrafficPolicyInstance"


class NotAuthorizedException(Route53Error):
    """Associating the specified VPC with the specified hosted zone has not been
    authorized.
    """

    _ERROR_CODE = "NotAuthorizedException"


class PriorRequestNotComplete(Route53Error):
    """If Amazon Route 53 can't process a request before the next request arrives, it will
    reject subsequent requests for the same hosted zone and return an `HTTP 400 error`
    (`Bad request`). If Route 53 returns this error repeatedly for the same request, we
    recommend that you wait, in intervals of increasing duration, before you try the
    request again.
    """

    _ERROR_CODE = "PriorRequestNotComplete"


class PublicZoneVPCAssociation(Route53Error):
    """You're trying to associate a VPC with a public hosted zone. Amazon Route 53 doesn't
    support associating a VPC with a public hosted zone.
    """

    _ERROR_CODE = "PublicZoneVPCAssociation"


class QueryLoggingConfigAlreadyExists(Route53Error):
    """You can create only one query logging configuration for a hosted zone, and a query
    logging configuration already exists for this hosted zone.
    """

    _ERROR_CODE = "QueryLoggingConfigAlreadyExists"


class ThrottlingException(Route53Error):
    """The limit on the number of requests per second was exceeded."""
    _ERROR_CODE = "ThrottlingException"


class TooManyHealthChecks(Route53Error):
    """This health check can't be created because the current account has reached the limit
    on the number of active health checks.

    For information about default limits, see Limits in the Amazon Route 53 Developer
    Guide.

    For information about how to get the current limit for an account, see
    GetAccountLimit. To request a higher limit, create a case with the Amazon Web
    Services Support Center.

    You have reached the maximum number of active health checks for an Amazon Web
    Services account. To request a higher limit, create a case with the Amazon Web
    Services Support Center.
    """

    _ERROR_CODE = "TooManyHealthChecks"


class TooManyHostedZones(Route53Error):
    """This operation can't be completed either because the current account has reached the
    limit on the number of hosted zones or because you've reached the limit on the
    number of hosted zones that can be associated with a reusable delegation set.

    For information about default limits, see Limits in the Amazon Route 53 Developer
    Guide.

    To get the current limit on hosted zones that can be created by an account, see
    GetAccountLimit.

    To get the current limit on hosted zones that can be associated with a reusable
    delegation set, see GetReusableDelegationSetLimit.

    To request a higher limit, create a case with the Amazon Web Services Support
    Center.
    """

    _ERROR_CODE = "TooManyHostedZones"


class TooManyKeySigningKeys(Route53Error):
    """You've reached the limit for the number of key-signing keys (KSKs). Remove at least
    one KSK, and then try again.
    """

    _ERROR_CODE = "TooManyKeySigningKeys"


class TooManyTrafficPolicies(Route53Error):
    """This traffic policy can't be created because the current account has reached the
    limit on the number of traffic policies.

    For information about default limits, see Limits in the Amazon Route 53 Developer
    Guide.

    To get the current limit for an account, see GetAccountLimit.

    To request a higher limit, create a case with the Amazon Web Services Support
    Center.
    """

    _ERROR_CODE = "TooManyTrafficPolicies"


class TooManyTrafficPolicyInstances(Route53Error):
    """This traffic policy instance can't be created because the current account has
    reached the limit on the number of traffic policy instances.

    For information about default limits, see Limits in the Amazon Route 53 Developer
    Guide.

    For information about how to get the current limit for an account, see
    GetAccountLimit.

    To request a higher limit, create a case with the Amazon Web Services Support
    Center.
    """

    _ERROR_CODE = "TooManyTrafficPolicyInstances"


class TooManyTrafficPolicyVersionsForCurrentPolicy(Route53Error):
    """This traffic policy version can't be created because you've reached the limit of
    1000 on the number of versions that you can create for the current traffic policy.

    To create more traffic policy versions, you can use GetTrafficPolicy to get the
    traffic policy document for a specified traffic policy version, and then use
    CreateTrafficPolicy to create a new traffic policy using the traffic policy
    document.
    """

    _ERROR_CODE = "TooManyTrafficPolicyVersionsForCurrentPolicy"


class TooManyVPCAssociationAuthorizations(Route53Error):
    """You've created the maximum number of authorizations that can be created for the
    specified hosted zone. To authorize another VPC to be associated with the hosted
    zone, submit a `DeleteVPCAssociationAuthorization` request to remove an existing
    authorization. To get a list of existing authorizations, submit a
    `ListVPCAssociationAuthorizations` request.
    """

    _ERROR_CODE = "TooManyVPCAssociationAuthorizations"


class TrafficPolicyAlreadyExists(Route53Error):
    """A traffic policy that has the same value for `Name` already exists."""
    _ERROR_CODE = "TrafficPolicyAlreadyExists"


class TrafficPolicyInUse(Route53Error):
    """One or more traffic policy instances were created by using the specified traffic
    policy.
    """

    _ERROR_CODE = "TrafficPolicyInUse"


class TrafficPolicyInstanceAlreadyExists(Route53Error):
    """There is already a traffic policy instance with the specified ID."""
    _ERROR_CODE = "TrafficPolicyInstanceAlreadyExists"


class VPCAssociationAuthorizationNotFound(Route53Error):
    """The VPC that you specified is not authorized to be associated with the hosted zone."""
    _ERROR_CODE = "VPCAssociationAuthorizationNotFound"


class VPCAssociationNotFound(Route53Error):
    """The specified VPC and hosted zone are not currently associated."""
    _ERROR_CODE = "VPCAssociationNotFound"


EXCEPTIONS: dict[str, type[Route53Error]] = {
    "CidrBlockInUseException": CidrBlockInUseException,
    "CidrCollectionAlreadyExistsException": CidrCollectionAlreadyExistsException,
    "CidrCollectionInUseException": CidrCollectionInUseException,
    "CidrCollectionVersionMismatchException": CidrCollectionVersionMismatchException,
    "ConcurrentModification": ConcurrentModification,
    "ConflictingDomainExists": ConflictingDomainExists,
    "ConflictingTypes": ConflictingTypes,
    "DNSSECNotFound": DNSSECNotFound,
    "DelegationSetAlreadyCreated": DelegationSetAlreadyCreated,
    "DelegationSetAlreadyReusable": DelegationSetAlreadyReusable,
    "DelegationSetInUse": DelegationSetInUse,
    "DelegationSetNotAvailable": DelegationSetNotAvailable,
    "DelegationSetNotReusable": DelegationSetNotReusable,
    "HealthCheckAlreadyExists": HealthCheckAlreadyExists,
    "HealthCheckInUse": HealthCheckInUse,
    "HealthCheckVersionMismatch": HealthCheckVersionMismatch,
    "HostedZoneAlreadyExists": HostedZoneAlreadyExists,
    "HostedZoneNotEmpty": HostedZoneNotEmpty,
    "HostedZoneNotFound": HostedZoneNotFound,
    "HostedZoneNotPrivate": HostedZoneNotPrivate,
    "HostedZonePartiallyDelegated": HostedZonePartiallyDelegated,
    "IncompatibleVersion": IncompatibleVersion,
    "InsufficientCloudWatchLogsResourcePolicy": InsufficientCloudWatchLogsResourcePolicy,
    "InvalidArgument": InvalidArgument,
    "InvalidChangeBatch": InvalidChangeBatch,
    "InvalidDomainName": InvalidDomainName,
    "InvalidInput": InvalidInput,
    "InvalidKMSArn": InvalidKMSArn,
    "InvalidKeySigningKeyName": InvalidKeySigningKeyName,
    "InvalidKeySigningKeyStatus": InvalidKeySigningKeyStatus,
    "InvalidPaginationToken": InvalidPaginationToken,
    "InvalidSigningStatus": InvalidSigningStatus,
    "InvalidTrafficPolicyDocument": InvalidTrafficPolicyDocument,
    "InvalidVPCId": InvalidVPCId,
    "KeySigningKeyAlreadyExists": KeySigningKeyAlreadyExists,
    "KeySigningKeyInParentDSRecord": KeySigningKeyInParentDSRecord,
    "KeySigningKeyInUse": KeySigningKeyInUse,
    "KeySigningKeyWithActiveStatusNotFound": KeySigningKeyWithActiveStatusNotFound,
    "LastVPCAssociation": LastVPCAssociation,
    "LimitsExceeded": LimitsExceeded,
    "NoSuchChange": NoSuchChange,
    "NoSuchCidrCollectionException": NoSuchCidrCollectionException,
    "NoSuchCidrLocationException": NoSuchCidrLocationException,
    "NoSuchCloudWatchLogsLogGroup": NoSuchCloudWatchLogsLogGroup,
    "NoSuchDelegationSet": NoSuchDelegationSet,
    "NoSuchGeoLocation": NoSuchGeoLocation,
    "NoSuchHealthCheck": NoSuchHealthCheck,
    "NoSuchHostedZone": NoSuchHostedZone,
    "NoSuchKeySigningKey": NoSuchKeySigningKey,
    "NoSuchQueryLoggingConfig": NoSuchQueryLoggingConfig,
    "NoSuchTrafficPolicy": NoSuchTrafficPolicy,
    "NoSuchTrafficPolicyInstance": NoSuchTrafficPolicyInstance,
    "NotAuthorizedException": NotAuthorizedException,
    "PriorRequestNotComplete": PriorRequestNotComplete,
    "PublicZoneVPCAssociation": PublicZoneVPCAssociation,
    "QueryLoggingConfigAlreadyExists": QueryLoggingConfigAlreadyExists,
    "ThrottlingException": ThrottlingException,
    "TooManyHealthChecks": TooManyHealthChecks,
    "TooManyHostedZones": TooManyHostedZones,
    "TooManyKeySigningKeys": TooManyKeySigningKeys,
    "TooManyTrafficPolicies": TooManyTrafficPolicies,
    "TooManyTrafficPolicyInstances": TooManyTrafficPolicyInstances,
    "TooManyTrafficPolicyVersionsForCurrentPolicy": TooManyTrafficPolicyVersionsForCurrentPolicy,
    "TooManyVPCAssociationAuthorizations": TooManyVPCAssociationAuthorizations,
    "TrafficPolicyAlreadyExists": TrafficPolicyAlreadyExists,
    "TrafficPolicyInUse": TrafficPolicyInUse,
    "TrafficPolicyInstanceAlreadyExists": TrafficPolicyInstanceAlreadyExists,
    "VPCAssociationAuthorizationNotFound": VPCAssociationAuthorizationNotFound,
    "VPCAssociationNotFound": VPCAssociationNotFound,
}
