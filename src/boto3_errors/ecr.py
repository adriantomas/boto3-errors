# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class ECRError(Boto3Error):
    _SERVICE = "ecr"


class EmptyUploadException(ECRError):
    """The specified layer upload does not contain any layer parts."""
    _ERROR_CODE = "EmptyUploadException"


class ImageAlreadyExistsException(ECRError):
    """The specified image has already been pushed, and there were no changes to the
    manifest or image tag after the last push.
    """

    _ERROR_CODE = "ImageAlreadyExistsException"


class ImageDigestDoesNotMatchException(ECRError):
    """The specified image digest does not match the digest that Amazon ECR calculated for
    the image.
    """

    _ERROR_CODE = "ImageDigestDoesNotMatchException"


class ImageNotFoundException(ECRError):
    """The image requested does not exist in the specified repository."""
    _ERROR_CODE = "ImageNotFoundException"


class ImageTagAlreadyExistsException(ECRError):
    """The specified image is tagged with a tag that already exists. The repository is
    configured for tag immutability.
    """

    _ERROR_CODE = "ImageTagAlreadyExistsException"


class InvalidLayerException(ECRError):
    """The layer digest calculation performed by Amazon ECR upon receipt of the image layer
    does not match the digest specified.
    """

    _ERROR_CODE = "InvalidLayerException"


class InvalidLayerPartException(ECRError):
    """The layer part size is not valid, or the first byte specified is not consecutive to
    the last byte of a previous layer part upload.
    """

    _ERROR_CODE = "InvalidLayerPartException"

    @property
    def last_valid_byte_received(self) -> int | None:
        """The last valid byte received from the layer part upload that is associated with
        the exception.
        """
        return self.response.get("lastValidByteReceived")

    @property
    def registry_id(self) -> str | None:
        """The registry ID associated with the exception."""
        return self.response.get("registryId")

    @property
    def repository_name(self) -> str | None:
        """The repository name associated with the exception."""
        return self.response.get("repositoryName")

    @property
    def upload_id(self) -> str | None:
        """The upload ID associated with the exception."""
        return self.response.get("uploadId")


class InvalidParameterException(ECRError):
    """The specified parameter is invalid. Review the available parameters for the API
    request.
    """

    _ERROR_CODE = "InvalidParameterException"


class InvalidTagParameterException(ECRError):
    """An invalid parameter has been specified. Tag keys can have a maximum character
    length of 128 characters, and tag values can have a maximum length of 256
    characters.
    """

    _ERROR_CODE = "InvalidTagParameterException"


class KmsException(ECRError):
    """The operation failed due to a KMS exception."""
    _ERROR_CODE = "KmsException"

    @property
    def kms_error(self) -> str | None:
        """The error code returned by KMS."""
        return self.response.get("kmsError")


class LayerAlreadyExistsException(ECRError):
    """The image layer already exists in the associated repository."""
    _ERROR_CODE = "LayerAlreadyExistsException"


class LayerInaccessibleException(ECRError):
    """The specified layer is not available because it is not associated with an image.
    Unassociated image layers may be cleaned up at any time.
    """

    _ERROR_CODE = "LayerInaccessibleException"


class LayerPartTooSmallException(ECRError):
    """Layer parts must be at least 5 MiB in size."""
    _ERROR_CODE = "LayerPartTooSmallException"


class LayersNotFoundException(ECRError):
    """The specified layers could not be found, or the specified layer is not valid for
    this repository.
    """

    _ERROR_CODE = "LayersNotFoundException"


class LifecyclePolicyNotFoundException(ECRError):
    """The lifecycle policy could not be found, and no policy is set to the repository."""
    _ERROR_CODE = "LifecyclePolicyNotFoundException"


class LifecyclePolicyPreviewInProgressException(ECRError):
    """The previous lifecycle policy preview request has not completed. Wait and try again."""
    _ERROR_CODE = "LifecyclePolicyPreviewInProgressException"


class LifecyclePolicyPreviewNotFoundException(ECRError):
    """There is no dry run for this repository."""
    _ERROR_CODE = "LifecyclePolicyPreviewNotFoundException"


class LimitExceededException(ECRError):
    """The operation did not succeed because it would have exceeded a service limit for
    your account. For more information, see Amazon ECR service quotas in the Amazon
    Elastic Container Registry User Guide.
    """

    _ERROR_CODE = "LimitExceededException"


class PullThroughCacheRuleAlreadyExistsException(ECRError):
    """A pull through cache rule with these settings already exists for the private
    registry.
    """

    _ERROR_CODE = "PullThroughCacheRuleAlreadyExistsException"


class PullThroughCacheRuleNotFoundException(ECRError):
    """The pull through cache rule was not found. Specify a valid pull through cache rule
    and try again.
    """

    _ERROR_CODE = "PullThroughCacheRuleNotFoundException"


class ReferencedImagesNotFoundException(ECRError):
    """The manifest list is referencing an image that does not exist."""
    _ERROR_CODE = "ReferencedImagesNotFoundException"


class RegistryPolicyNotFoundException(ECRError):
    """The registry doesn't have an associated registry policy."""
    _ERROR_CODE = "RegistryPolicyNotFoundException"


class RepositoryAlreadyExistsException(ECRError):
    """The specified repository already exists in the specified registry."""
    _ERROR_CODE = "RepositoryAlreadyExistsException"


class RepositoryNotEmptyException(ECRError):
    """The specified repository contains images. To delete a repository that contains
    images, you must force the deletion with the `force` parameter.
    """

    _ERROR_CODE = "RepositoryNotEmptyException"


class RepositoryNotFoundException(ECRError):
    """The specified repository could not be found. Check the spelling of the specified
    repository and ensure that you are performing operations on the correct registry.
    """

    _ERROR_CODE = "RepositoryNotFoundException"


class RepositoryPolicyNotFoundException(ECRError):
    """The specified repository and registry combination does not have an associated
    repository policy.
    """

    _ERROR_CODE = "RepositoryPolicyNotFoundException"


class ScanNotFoundException(ECRError):
    """The specified image scan could not be found. Ensure that image scanning is enabled
    on the repository and try again.
    """

    _ERROR_CODE = "ScanNotFoundException"


class SecretNotFoundException(ECRError):
    """The ARN of the secret specified in the pull through cache rule was not found. Update
    the pull through cache rule with a valid secret ARN and try again.
    """

    _ERROR_CODE = "SecretNotFoundException"


class ServerException(ECRError):
    """These errors are usually caused by a server-side issue."""
    _ERROR_CODE = "ServerException"


class TooManyTagsException(ECRError):
    """The list of tags on the repository is over the limit. The maximum number of tags
    that can be applied to a repository is 50.
    """

    _ERROR_CODE = "TooManyTagsException"


class UnableToAccessSecretException(ECRError):
    """The secret is unable to be accessed. Verify the resource permissions for the secret
    and try again.
    """

    _ERROR_CODE = "UnableToAccessSecretException"


class UnableToDecryptSecretValueException(ECRError):
    """The secret is accessible but is unable to be decrypted. Verify the resource
    permisisons and try again.
    """

    _ERROR_CODE = "UnableToDecryptSecretValueException"


class UnableToGetUpstreamImageException(ECRError):
    """The image or images were unable to be pulled using the pull through cache rule. This
    is usually caused because of an issue with the Secrets Manager secret containing the
    credentials for the upstream registry.
    """

    _ERROR_CODE = "UnableToGetUpstreamImageException"


class UnableToGetUpstreamLayerException(ECRError):
    """There was an issue getting the upstream layer matching the pull through cache rule."""
    _ERROR_CODE = "UnableToGetUpstreamLayerException"


class UnsupportedImageTypeException(ECRError):
    """The image is of a type that cannot be scanned."""
    _ERROR_CODE = "UnsupportedImageTypeException"


class UnsupportedUpstreamRegistryException(ECRError):
    """The specified upstream registry isn't supported."""
    _ERROR_CODE = "UnsupportedUpstreamRegistryException"


class UploadNotFoundException(ECRError):
    """The upload could not be found, or the specified upload ID is not valid for this
    repository.
    """

    _ERROR_CODE = "UploadNotFoundException"


class ValidationException(ECRError):
    """There was an exception validating this request."""
    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[ECRError]] = {
    "EmptyUploadException": EmptyUploadException,
    "ImageAlreadyExistsException": ImageAlreadyExistsException,
    "ImageDigestDoesNotMatchException": ImageDigestDoesNotMatchException,
    "ImageNotFoundException": ImageNotFoundException,
    "ImageTagAlreadyExistsException": ImageTagAlreadyExistsException,
    "InvalidLayerException": InvalidLayerException,
    "InvalidLayerPartException": InvalidLayerPartException,
    "InvalidParameterException": InvalidParameterException,
    "InvalidTagParameterException": InvalidTagParameterException,
    "KmsException": KmsException,
    "LayerAlreadyExistsException": LayerAlreadyExistsException,
    "LayerInaccessibleException": LayerInaccessibleException,
    "LayerPartTooSmallException": LayerPartTooSmallException,
    "LayersNotFoundException": LayersNotFoundException,
    "LifecyclePolicyNotFoundException": LifecyclePolicyNotFoundException,
    "LifecyclePolicyPreviewInProgressException": LifecyclePolicyPreviewInProgressException,
    "LifecyclePolicyPreviewNotFoundException": LifecyclePolicyPreviewNotFoundException,
    "LimitExceededException": LimitExceededException,
    "PullThroughCacheRuleAlreadyExistsException": PullThroughCacheRuleAlreadyExistsException,
    "PullThroughCacheRuleNotFoundException": PullThroughCacheRuleNotFoundException,
    "ReferencedImagesNotFoundException": ReferencedImagesNotFoundException,
    "RegistryPolicyNotFoundException": RegistryPolicyNotFoundException,
    "RepositoryAlreadyExistsException": RepositoryAlreadyExistsException,
    "RepositoryNotEmptyException": RepositoryNotEmptyException,
    "RepositoryNotFoundException": RepositoryNotFoundException,
    "RepositoryPolicyNotFoundException": RepositoryPolicyNotFoundException,
    "ScanNotFoundException": ScanNotFoundException,
    "SecretNotFoundException": SecretNotFoundException,
    "ServerException": ServerException,
    "TooManyTagsException": TooManyTagsException,
    "UnableToAccessSecretException": UnableToAccessSecretException,
    "UnableToDecryptSecretValueException": UnableToDecryptSecretValueException,
    "UnableToGetUpstreamImageException": UnableToGetUpstreamImageException,
    "UnableToGetUpstreamLayerException": UnableToGetUpstreamLayerException,
    "UnsupportedImageTypeException": UnsupportedImageTypeException,
    "UnsupportedUpstreamRegistryException": UnsupportedUpstreamRegistryException,
    "UploadNotFoundException": UploadNotFoundException,
    "ValidationException": ValidationException,
}
