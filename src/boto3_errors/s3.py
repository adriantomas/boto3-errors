# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class S3Error(Boto3Error):
    _SERVICE = "s3"


class AccessDenied(S3Error):
    """You might receive this error for several reasons. For details, see the description
    of this API operation.
    """

    _ERROR_CODE = "AccessDenied"


class BucketAlreadyExists(S3Error):
    """The requested bucket name is not available. The bucket namespace is shared by all
    users of the system. Select a different name and try again.
    """

    _ERROR_CODE = "BucketAlreadyExists"


class BucketAlreadyOwnedByYou(S3Error):
    """The bucket you tried to create already exists, and you own it. Amazon S3 returns
    this error in all Amazon Web Services Regions except in the North Virginia Region.
    For legacy compatibility, if you re-create an existing bucket that you already own
    in the North Virginia Region, Amazon S3 returns 200 OK and resets the bucket access
    control lists (ACLs).
    """

    _ERROR_CODE = "BucketAlreadyOwnedByYou"


class EncryptionTypeMismatch(S3Error):
    """The existing object was created with a different encryption type. Subsequent write
    requests must include the appropriate encryption parameters in the request or while
    creating the session.
    """

    _ERROR_CODE = "EncryptionTypeMismatch"


class IdempotencyParameterMismatch(S3Error):
    """Parameters on this idempotent request are inconsistent with parameters used in
    previous request(s).

    For a list of error codes and more information on Amazon S3 errors, see Error codes.

    Note:

    Idempotency ensures that an API request completes no more than one time. With an
    idempotent request, if the original request completes successfully, any subsequent
    retries complete successfully without performing any further actions.
    """

    _ERROR_CODE = "IdempotencyParameterMismatch"


class InvalidObjectState(S3Error):
    """Object is archived and inaccessible until restored.

    If the object you are retrieving is stored in the S3 Glacier Flexible Retrieval
    storage class, the S3 Glacier Deep Archive storage class, the S3 Intelligent-Tiering
    Archive Access tier, or the S3 Intelligent-Tiering Deep Archive Access tier, before
    you can retrieve the object you must first restore a copy using RestoreObject.
    Otherwise, this operation returns an `InvalidObjectState` error. For information
    about restoring archived objects, see Restoring Archived Objects in the Amazon S3
    User Guide.
    """

    _ERROR_CODE = "InvalidObjectState"

    @property
    def storage_class(self) -> str | None:
        return self.response.get("StorageClass")

    @property
    def access_tier(self) -> str | None:
        return self.response.get("AccessTier")


class InvalidRequest(S3Error):
    """A parameter or header in your request isn't valid. For details, see the description
    of this API operation.
    """

    _ERROR_CODE = "InvalidRequest"


class InvalidWriteOffset(S3Error):
    """The write offset value that you specified does not match the current object size."""
    _ERROR_CODE = "InvalidWriteOffset"


class NoSuchBucket(S3Error):
    """The specified bucket does not exist."""
    _ERROR_CODE = "NoSuchBucket"


class NoSuchKey(S3Error):
    """The specified key does not exist."""
    _ERROR_CODE = "NoSuchKey"


class NoSuchUpload(S3Error):
    """The specified multipart upload does not exist."""
    _ERROR_CODE = "NoSuchUpload"


class ObjectAlreadyInActiveTierError(S3Error):
    """This action is not allowed against this storage tier."""
    _ERROR_CODE = "ObjectAlreadyInActiveTierError"


class ObjectNotInActiveTierError(S3Error):
    """The source object of the COPY action is not in the active tier and is only stored in
    Amazon S3 Glacier.
    """

    _ERROR_CODE = "ObjectNotInActiveTierError"


class TooManyParts(S3Error):
    """You have attempted to add more parts than the maximum of 10000 that are allowed for
    this object. You can use the CopyObject operation to copy this object to another and
    then add more data to the newly copied object.
    """

    _ERROR_CODE = "TooManyParts"


EXCEPTIONS: dict[str, type[S3Error]] = {
    "AccessDenied": AccessDenied,
    "BucketAlreadyExists": BucketAlreadyExists,
    "BucketAlreadyOwnedByYou": BucketAlreadyOwnedByYou,
    "EncryptionTypeMismatch": EncryptionTypeMismatch,
    "IdempotencyParameterMismatch": IdempotencyParameterMismatch,
    "InvalidObjectState": InvalidObjectState,
    "InvalidRequest": InvalidRequest,
    "InvalidWriteOffset": InvalidWriteOffset,
    "NoSuchBucket": NoSuchBucket,
    "NoSuchKey": NoSuchKey,
    "NoSuchUpload": NoSuchUpload,
    "ObjectAlreadyInActiveTierError": ObjectAlreadyInActiveTierError,
    "ObjectNotInActiveTierError": ObjectNotInActiveTierError,
    "TooManyParts": TooManyParts,
}
