# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class ECRPUBLICError(Boto3Error):
    _SERVICE = "ecr-public"


class EmptyUploadException(ECRPUBLICError):
    """The specified layer upload doesn't contain any layer parts."""
    _ERROR_CODE = "EmptyUploadException"


class ImageAlreadyExistsException(ECRPUBLICError):
    """The specified image has already been pushed, and there were no changes to the
    manifest or image tag after the last push.
    """

    _ERROR_CODE = "ImageAlreadyExistsException"


class ImageDigestDoesNotMatchException(ECRPUBLICError):
    """The specified image digest doesn't match the digest that Amazon ECR calculated for
    the image.
    """

    _ERROR_CODE = "ImageDigestDoesNotMatchException"


class ImageNotFoundException(ECRPUBLICError):
    """The image requested doesn't exist in the specified repository."""
    _ERROR_CODE = "ImageNotFoundException"


class ImageTagAlreadyExistsException(ECRPUBLICError):
    """The specified image is tagged with a tag that already exists. The repository is
    configured for tag immutability.
    """

    _ERROR_CODE = "ImageTagAlreadyExistsException"


class InvalidLayerException(ECRPUBLICError):
    """The layer digest calculation performed by Amazon ECR when the image layer doesn't
    match the digest specified.
    """

    _ERROR_CODE = "InvalidLayerException"


class InvalidLayerPartException(ECRPUBLICError):
    """The layer part size isn't valid, or the first byte specified isn't consecutive to
    the last byte of a previous layer part upload.
    """

    _ERROR_CODE = "InvalidLayerPartException"

    @property
    def last_valid_byte_received(self) -> int | None:
        """The position of the last byte of the layer part."""
        return self.response.get("lastValidByteReceived")

    @property
    def registry_id(self) -> str | None:
        """The Amazon Web Services account ID that's associated with the layer part."""
        return self.response.get("registryId")

    @property
    def repository_name(self) -> str | None:
        """The name of the repository."""
        return self.response.get("repositoryName")

    @property
    def upload_id(self) -> str | None:
        """The upload ID that's associated with the layer part."""
        return self.response.get("uploadId")


class InvalidParameterException(ECRPUBLICError):
    """The specified parameter is invalid. Review the available parameters for the API
    request.
    """

    _ERROR_CODE = "InvalidParameterException"


class InvalidTagParameterException(ECRPUBLICError):
    """An invalid parameter has been specified. Tag keys can have a maximum character
    length of 128 characters, and tag values can have a maximum length of 256
    characters.
    """

    _ERROR_CODE = "InvalidTagParameterException"


class LayerAlreadyExistsException(ECRPUBLICError):
    """The image layer already exists in the associated repository."""
    _ERROR_CODE = "LayerAlreadyExistsException"


class LayerPartTooSmallException(ECRPUBLICError):
    """Layer parts must be at least 5 MiB in size."""
    _ERROR_CODE = "LayerPartTooSmallException"


class LayersNotFoundException(ECRPUBLICError):
    """The specified layers can't be found, or the specified layer isn't valid for this
    repository.
    """

    _ERROR_CODE = "LayersNotFoundException"


class LimitExceededException(ECRPUBLICError):
    """The operation didn't succeed because it would have exceeded a service limit for your
    account. For more information, see Amazon ECR Service Quotas in the Amazon Elastic
    Container Registry User Guide.
    """

    _ERROR_CODE = "LimitExceededException"


class ReferencedImagesNotFoundException(ECRPUBLICError):
    """The manifest list is referencing an image that doesn't exist."""
    _ERROR_CODE = "ReferencedImagesNotFoundException"


class RegistryNotFoundException(ECRPUBLICError):
    """The registry doesn't exist."""
    _ERROR_CODE = "RegistryNotFoundException"


class RepositoryAlreadyExistsException(ECRPUBLICError):
    """The specified repository already exists in the specified registry."""
    _ERROR_CODE = "RepositoryAlreadyExistsException"


class RepositoryCatalogDataNotFoundException(ECRPUBLICError):
    """The repository catalog data doesn't exist."""
    _ERROR_CODE = "RepositoryCatalogDataNotFoundException"


class RepositoryNotEmptyException(ECRPUBLICError):
    """The specified repository contains images. To delete a repository that contains
    images, you must force the deletion with the `force` parameter.
    """

    _ERROR_CODE = "RepositoryNotEmptyException"


class RepositoryNotFoundException(ECRPUBLICError):
    """The specified repository can't be found. Check the spelling of the specified
    repository and ensure that you're performing operations on the correct registry.
    """

    _ERROR_CODE = "RepositoryNotFoundException"


class RepositoryPolicyNotFoundException(ECRPUBLICError):
    """The specified repository and registry combination doesn't have an associated
    repository policy.
    """

    _ERROR_CODE = "RepositoryPolicyNotFoundException"


class ServerException(ECRPUBLICError):
    """These errors are usually caused by a server-side issue."""
    _ERROR_CODE = "ServerException"


class TooManyTagsException(ECRPUBLICError):
    """The list of tags on the repository is over the limit. The maximum number of tags
    that can be applied to a repository is 50.
    """

    _ERROR_CODE = "TooManyTagsException"


class UnsupportedCommandException(ECRPUBLICError):
    """The action isn't supported in this Region."""
    _ERROR_CODE = "UnsupportedCommandException"


class UploadNotFoundException(ECRPUBLICError):
    """The upload can't be found, or the specified upload ID isn't valid for this
    repository.
    """

    _ERROR_CODE = "UploadNotFoundException"


EXCEPTIONS: dict[str, type[ECRPUBLICError]] = {
    "EmptyUploadException": EmptyUploadException,
    "ImageAlreadyExistsException": ImageAlreadyExistsException,
    "ImageDigestDoesNotMatchException": ImageDigestDoesNotMatchException,
    "ImageNotFoundException": ImageNotFoundException,
    "ImageTagAlreadyExistsException": ImageTagAlreadyExistsException,
    "InvalidLayerException": InvalidLayerException,
    "InvalidLayerPartException": InvalidLayerPartException,
    "InvalidParameterException": InvalidParameterException,
    "InvalidTagParameterException": InvalidTagParameterException,
    "LayerAlreadyExistsException": LayerAlreadyExistsException,
    "LayerPartTooSmallException": LayerPartTooSmallException,
    "LayersNotFoundException": LayersNotFoundException,
    "LimitExceededException": LimitExceededException,
    "ReferencedImagesNotFoundException": ReferencedImagesNotFoundException,
    "RegistryNotFoundException": RegistryNotFoundException,
    "RepositoryAlreadyExistsException": RepositoryAlreadyExistsException,
    "RepositoryCatalogDataNotFoundException": RepositoryCatalogDataNotFoundException,
    "RepositoryNotEmptyException": RepositoryNotEmptyException,
    "RepositoryNotFoundException": RepositoryNotFoundException,
    "RepositoryPolicyNotFoundException": RepositoryPolicyNotFoundException,
    "ServerException": ServerException,
    "TooManyTagsException": TooManyTagsException,
    "UnsupportedCommandException": UnsupportedCommandException,
    "UploadNotFoundException": UploadNotFoundException,
}
