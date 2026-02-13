# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class CodeCommitError(Boto3Error):
    _SERVICE = "codecommit"


class ActorDoesNotExistException(CodeCommitError):
    """The specified Amazon Resource Name (ARN) does not exist in the Amazon Web Services
    account.
    """

    _ERROR_CODE = "ActorDoesNotExistException"


class ApprovalRuleContentRequiredException(CodeCommitError):
    """The content for the approval rule is empty. You must provide some content for an
    approval rule. The content cannot be null.
    """

    _ERROR_CODE = "ApprovalRuleContentRequiredException"


class ApprovalRuleDoesNotExistException(CodeCommitError):
    """The specified approval rule does not exist."""
    _ERROR_CODE = "ApprovalRuleDoesNotExistException"


class ApprovalRuleNameAlreadyExistsException(CodeCommitError):
    """An approval rule with that name already exists. Approval rule names must be unique
    within the scope of a pull request.
    """

    _ERROR_CODE = "ApprovalRuleNameAlreadyExistsException"


class ApprovalRuleNameRequiredException(CodeCommitError):
    """An approval rule name is required, but was not specified."""
    _ERROR_CODE = "ApprovalRuleNameRequiredException"


class ApprovalRuleTemplateContentRequiredException(CodeCommitError):
    """The content for the approval rule template is empty. You must provide some content
    for an approval rule template. The content cannot be null.
    """

    _ERROR_CODE = "ApprovalRuleTemplateContentRequiredException"


class ApprovalRuleTemplateDoesNotExistException(CodeCommitError):
    """The specified approval rule template does not exist. Verify that the name is correct
    and that you are signed in to the Amazon Web Services Region where the template was
    created, and then try again.
    """

    _ERROR_CODE = "ApprovalRuleTemplateDoesNotExistException"


class ApprovalRuleTemplateInUseException(CodeCommitError):
    """The approval rule template is associated with one or more repositories. You cannot
    delete a template that is associated with a repository. Remove all associations, and
    then try again.
    """

    _ERROR_CODE = "ApprovalRuleTemplateInUseException"


class ApprovalRuleTemplateNameAlreadyExistsException(CodeCommitError):
    """You cannot create an approval rule template with that name because a template with
    that name already exists in this Amazon Web Services Region for your Amazon Web
    Services account. Approval rule template names must be unique.
    """

    _ERROR_CODE = "ApprovalRuleTemplateNameAlreadyExistsException"


class ApprovalRuleTemplateNameRequiredException(CodeCommitError):
    """An approval rule template name is required, but was not specified."""
    _ERROR_CODE = "ApprovalRuleTemplateNameRequiredException"


class ApprovalStateRequiredException(CodeCommitError):
    """An approval state is required, but was not specified."""
    _ERROR_CODE = "ApprovalStateRequiredException"


class AuthorDoesNotExistException(CodeCommitError):
    """The specified Amazon Resource Name (ARN) does not exist in the Amazon Web Services
    account.
    """

    _ERROR_CODE = "AuthorDoesNotExistException"


class BeforeCommitIdAndAfterCommitIdAreSameException(CodeCommitError):
    """The before commit ID and the after commit ID are the same, which is not valid. The
    before commit ID and the after commit ID must be different commit IDs.
    """

    _ERROR_CODE = "BeforeCommitIdAndAfterCommitIdAreSameException"


class BlobIdDoesNotExistException(CodeCommitError):
    """The specified blob does not exist."""
    _ERROR_CODE = "BlobIdDoesNotExistException"


class BlobIdRequiredException(CodeCommitError):
    """A blob ID is required, but was not specified."""
    _ERROR_CODE = "BlobIdRequiredException"


class BranchDoesNotExistException(CodeCommitError):
    """The specified branch does not exist."""
    _ERROR_CODE = "BranchDoesNotExistException"


class BranchNameExistsException(CodeCommitError):
    """Cannot create the branch with the specified name because the commit conflicts with
    an existing branch with the same name. Branch names must be unique.
    """

    _ERROR_CODE = "BranchNameExistsException"


class BranchNameIsTagNameException(CodeCommitError):
    """The specified branch name is not valid because it is a tag name. Enter the name of a
    branch in the repository. For a list of valid branch names, use ListBranches.
    """

    _ERROR_CODE = "BranchNameIsTagNameException"


class BranchNameRequiredException(CodeCommitError):
    """A branch name is required, but was not specified."""
    _ERROR_CODE = "BranchNameRequiredException"


class CannotDeleteApprovalRuleFromTemplateException(CodeCommitError):
    """The approval rule cannot be deleted from the pull request because it was created by
    an approval rule template and applied to the pull request automatically.
    """

    _ERROR_CODE = "CannotDeleteApprovalRuleFromTemplateException"


class CannotModifyApprovalRuleFromTemplateException(CodeCommitError):
    """The approval rule cannot be modified for the pull request because it was created by
    an approval rule template and applied to the pull request automatically.
    """

    _ERROR_CODE = "CannotModifyApprovalRuleFromTemplateException"


class ClientRequestTokenRequiredException(CodeCommitError):
    """A client request token is required. A client request token is an unique, client-
    generated idempotency token that, when provided in a request, ensures the request
    cannot be repeated with a changed parameter. If a request is received with the same
    parameters and a token is included, the request returns information about the
    initial request that used that token.
    """

    _ERROR_CODE = "ClientRequestTokenRequiredException"


class CommentContentRequiredException(CodeCommitError):
    """The comment is empty. You must provide some content for a comment. The content
    cannot be null.
    """

    _ERROR_CODE = "CommentContentRequiredException"


class CommentContentSizeLimitExceededException(CodeCommitError):
    """The comment is too large. Comments are limited to 10,240 characters."""
    _ERROR_CODE = "CommentContentSizeLimitExceededException"


class CommentDeletedException(CodeCommitError):
    """This comment has already been deleted. You cannot edit or delete a deleted comment."""
    _ERROR_CODE = "CommentDeletedException"


class CommentDoesNotExistException(CodeCommitError):
    """No comment exists with the provided ID. Verify that you have used the correct ID,
    and then try again.
    """

    _ERROR_CODE = "CommentDoesNotExistException"


class CommentIdRequiredException(CodeCommitError):
    """The comment ID is missing or null. A comment ID is required."""
    _ERROR_CODE = "CommentIdRequiredException"


class CommentNotCreatedByCallerException(CodeCommitError):
    """You cannot modify or delete this comment. Only comment authors can modify or delete
    their comments.
    """

    _ERROR_CODE = "CommentNotCreatedByCallerException"


class CommitDoesNotExistException(CodeCommitError):
    """The specified commit does not exist or no commit was specified, and the specified
    repository has no default branch.
    """

    _ERROR_CODE = "CommitDoesNotExistException"


class CommitIdDoesNotExistException(CodeCommitError):
    """The specified commit ID does not exist."""
    _ERROR_CODE = "CommitIdDoesNotExistException"


class CommitIdRequiredException(CodeCommitError):
    """A commit ID was not specified."""
    _ERROR_CODE = "CommitIdRequiredException"


class CommitIdsLimitExceededException(CodeCommitError):
    """The maximum number of allowed commit IDs in a batch request is 100. Verify that your
    batch requests contains no more than 100 commit IDs, and then try again.
    """

    _ERROR_CODE = "CommitIdsLimitExceededException"


class CommitIdsListRequiredException(CodeCommitError):
    """A list of commit IDs is required, but was either not specified or the list was
    empty.
    """

    _ERROR_CODE = "CommitIdsListRequiredException"


class CommitMessageLengthExceededException(CodeCommitError):
    """The commit message is too long. Provide a shorter string."""
    _ERROR_CODE = "CommitMessageLengthExceededException"


class CommitRequiredException(CodeCommitError):
    """A commit was not specified."""
    _ERROR_CODE = "CommitRequiredException"


class ConcurrentReferenceUpdateException(CodeCommitError):
    """The merge cannot be completed because the target branch has been modified. Another
    user might have modified the target branch while the merge was in progress. Wait a
    few minutes, and then try again.
    """

    _ERROR_CODE = "ConcurrentReferenceUpdateException"


class DefaultBranchCannotBeDeletedException(CodeCommitError):
    """The specified branch is the default branch for the repository, and cannot be
    deleted. To delete this branch, you must first set another branch as the default
    branch.
    """

    _ERROR_CODE = "DefaultBranchCannotBeDeletedException"


class DirectoryNameConflictsWithFileNameException(CodeCommitError):
    """A file cannot be added to the repository because the specified path name has the
    same name as a file that already exists in this repository. Either provide a
    different name for the file, or specify a different path for the file.
    """

    _ERROR_CODE = "DirectoryNameConflictsWithFileNameException"


class EncryptionIntegrityChecksFailedException(CodeCommitError):
    """An encryption integrity check failed."""
    _ERROR_CODE = "EncryptionIntegrityChecksFailedException"


class EncryptionKeyAccessDeniedException(CodeCommitError):
    """An encryption key could not be accessed."""
    _ERROR_CODE = "EncryptionKeyAccessDeniedException"


class EncryptionKeyDisabledException(CodeCommitError):
    """The encryption key is disabled."""
    _ERROR_CODE = "EncryptionKeyDisabledException"


class EncryptionKeyInvalidIdException(CodeCommitError):
    """The Key Management Service encryption key is not valid."""
    _ERROR_CODE = "EncryptionKeyInvalidIdException"


class EncryptionKeyInvalidUsageException(CodeCommitError):
    """A KMS encryption key was used to try and encrypt or decrypt a repository, but either
    the repository or the key was not in a valid state to support the operation.
    """

    _ERROR_CODE = "EncryptionKeyInvalidUsageException"


class EncryptionKeyNotFoundException(CodeCommitError):
    """No encryption key was found."""
    _ERROR_CODE = "EncryptionKeyNotFoundException"


class EncryptionKeyRequiredException(CodeCommitError):
    """A KMS encryption key ID is required but was not specified."""
    _ERROR_CODE = "EncryptionKeyRequiredException"


class EncryptionKeyUnavailableException(CodeCommitError):
    """The encryption key is not available."""
    _ERROR_CODE = "EncryptionKeyUnavailableException"


class FileContentAndSourceFileSpecifiedException(CodeCommitError):
    """The commit cannot be created because both a source file and file content have been
    specified for the same file. You cannot provide both. Either specify a source file
    or provide the file content directly.
    """

    _ERROR_CODE = "FileContentAndSourceFileSpecifiedException"


class FileContentRequiredException(CodeCommitError):
    """The file cannot be added because it is empty. Empty files cannot be added to the
    repository with this API.
    """

    _ERROR_CODE = "FileContentRequiredException"


class FileContentSizeLimitExceededException(CodeCommitError):
    """The file cannot be added because it is too large. The maximum file size is 6 MB, and
    the combined file content change size is 7 MB. Consider making these changes using a
    Git client.
    """

    _ERROR_CODE = "FileContentSizeLimitExceededException"


class FileDoesNotExistException(CodeCommitError):
    """The specified file does not exist. Verify that you have used the correct file name,
    full path, and extension.
    """

    _ERROR_CODE = "FileDoesNotExistException"


class FileEntryRequiredException(CodeCommitError):
    """The commit cannot be created because no files have been specified as added, updated,
    or changed (PutFile or DeleteFile) for the commit.
    """

    _ERROR_CODE = "FileEntryRequiredException"


class FileModeRequiredException(CodeCommitError):
    """The commit cannot be created because no file mode has been specified. A file mode is
    required to update mode permissions for a file.
    """

    _ERROR_CODE = "FileModeRequiredException"


class FileNameConflictsWithDirectoryNameException(CodeCommitError):
    """A file cannot be added to the repository because the specified file name has the
    same name as a directory in this repository. Either provide another name for the
    file, or add the file in a directory that does not match the file name.
    """

    _ERROR_CODE = "FileNameConflictsWithDirectoryNameException"


class FilePathConflictsWithSubmodulePathException(CodeCommitError):
    """The commit cannot be created because a specified file path points to a submodule.
    Verify that the destination files have valid file paths that do not point to a
    submodule.
    """

    _ERROR_CODE = "FilePathConflictsWithSubmodulePathException"


class FileTooLargeException(CodeCommitError):
    """The specified file exceeds the file size limit for CodeCommit. For more information
    about limits in CodeCommit, see Quotas in the CodeCommit User Guide.
    """

    _ERROR_CODE = "FileTooLargeException"


class FolderContentSizeLimitExceededException(CodeCommitError):
    """The commit cannot be created because at least one of the overall changes in the
    commit results in a folder whose contents exceed the limit of 6 MB. Either reduce
    the number and size of your changes, or split the changes across multiple folders.
    """

    _ERROR_CODE = "FolderContentSizeLimitExceededException"


class FolderDoesNotExistException(CodeCommitError):
    """The specified folder does not exist. Either the folder name is not correct, or you
    did not enter the full path to the folder.
    """

    _ERROR_CODE = "FolderDoesNotExistException"


class IdempotencyParameterMismatchException(CodeCommitError):
    """The client request token is not valid. Either the token is not in a valid format, or
    the token has been used in a previous request and cannot be reused.
    """

    _ERROR_CODE = "IdempotencyParameterMismatchException"


class InvalidActorArnException(CodeCommitError):
    """The Amazon Resource Name (ARN) is not valid. Make sure that you have provided the
    full ARN for the user who initiated the change for the pull request, and then try
    again.
    """

    _ERROR_CODE = "InvalidActorArnException"


class InvalidApprovalRuleContentException(CodeCommitError):
    """The content for the approval rule is not valid."""
    _ERROR_CODE = "InvalidApprovalRuleContentException"


class InvalidApprovalRuleNameException(CodeCommitError):
    """The name for the approval rule is not valid."""
    _ERROR_CODE = "InvalidApprovalRuleNameException"


class InvalidApprovalRuleTemplateContentException(CodeCommitError):
    """The content of the approval rule template is not valid."""
    _ERROR_CODE = "InvalidApprovalRuleTemplateContentException"


class InvalidApprovalRuleTemplateDescriptionException(CodeCommitError):
    """The description for the approval rule template is not valid because it exceeds the
    maximum characters allowed for a description. For more information about limits in
    CodeCommit, see Quotas in the CodeCommit User Guide.
    """

    _ERROR_CODE = "InvalidApprovalRuleTemplateDescriptionException"


class InvalidApprovalRuleTemplateNameException(CodeCommitError):
    """The name of the approval rule template is not valid. Template names must be between
    1 and 100 valid characters in length. For more information about limits in
    CodeCommit, see Quotas in the CodeCommit User Guide.
    """

    _ERROR_CODE = "InvalidApprovalRuleTemplateNameException"


class InvalidApprovalStateException(CodeCommitError):
    """The state for the approval is not valid. Valid values include APPROVE and REVOKE."""
    _ERROR_CODE = "InvalidApprovalStateException"


class InvalidAuthorArnException(CodeCommitError):
    """The Amazon Resource Name (ARN) is not valid. Make sure that you have provided the
    full ARN for the author of the pull request, and then try again.
    """

    _ERROR_CODE = "InvalidAuthorArnException"


class InvalidBlobIdException(CodeCommitError):
    """The specified blob is not valid."""
    _ERROR_CODE = "InvalidBlobIdException"


class InvalidBranchNameException(CodeCommitError):
    """The specified reference name is not valid."""
    _ERROR_CODE = "InvalidBranchNameException"


class InvalidClientRequestTokenException(CodeCommitError):
    """The client request token is not valid."""
    _ERROR_CODE = "InvalidClientRequestTokenException"


class InvalidCommentIdException(CodeCommitError):
    """The comment ID is not in a valid format. Make sure that you have provided the full
    comment ID.
    """

    _ERROR_CODE = "InvalidCommentIdException"


class InvalidCommitException(CodeCommitError):
    """The specified commit is not valid."""
    _ERROR_CODE = "InvalidCommitException"


class InvalidCommitIdException(CodeCommitError):
    """The specified commit ID is not valid."""
    _ERROR_CODE = "InvalidCommitIdException"


class InvalidConflictDetailLevelException(CodeCommitError):
    """The specified conflict detail level is not valid."""
    _ERROR_CODE = "InvalidConflictDetailLevelException"


class InvalidConflictResolutionException(CodeCommitError):
    """The specified conflict resolution list is not valid."""
    _ERROR_CODE = "InvalidConflictResolutionException"


class InvalidConflictResolutionStrategyException(CodeCommitError):
    """The specified conflict resolution strategy is not valid."""
    _ERROR_CODE = "InvalidConflictResolutionStrategyException"


class InvalidContinuationTokenException(CodeCommitError):
    """The specified continuation token is not valid."""
    _ERROR_CODE = "InvalidContinuationTokenException"


class InvalidDeletionParameterException(CodeCommitError):
    """The specified deletion parameter is not valid."""
    _ERROR_CODE = "InvalidDeletionParameterException"


class InvalidDescriptionException(CodeCommitError):
    """The pull request description is not valid. Descriptions cannot be more than 1,000
    characters.
    """

    _ERROR_CODE = "InvalidDescriptionException"


class InvalidDestinationCommitSpecifierException(CodeCommitError):
    """The destination commit specifier is not valid. You must provide a valid branch name,
    tag, or full commit ID.
    """

    _ERROR_CODE = "InvalidDestinationCommitSpecifierException"


class InvalidEmailException(CodeCommitError):
    """The specified email address either contains one or more characters that are not
    allowed, or it exceeds the maximum number of characters allowed for an email
    address.
    """

    _ERROR_CODE = "InvalidEmailException"


class InvalidFileLocationException(CodeCommitError):
    """The location of the file is not valid. Make sure that you include the file name and
    extension.
    """

    _ERROR_CODE = "InvalidFileLocationException"


class InvalidFileModeException(CodeCommitError):
    """The specified file mode permission is not valid. For a list of valid file mode
    permissions, see PutFile.
    """

    _ERROR_CODE = "InvalidFileModeException"


class InvalidFilePositionException(CodeCommitError):
    """The position is not valid. Make sure that the line number exists in the version of
    the file you want to comment on.
    """

    _ERROR_CODE = "InvalidFilePositionException"


class InvalidMaxConflictFilesException(CodeCommitError):
    """The specified value for the number of conflict files to return is not valid."""
    _ERROR_CODE = "InvalidMaxConflictFilesException"


class InvalidMaxMergeHunksException(CodeCommitError):
    """The specified value for the number of merge hunks to return is not valid."""
    _ERROR_CODE = "InvalidMaxMergeHunksException"


class InvalidMaxResultsException(CodeCommitError):
    """The specified number of maximum results is not valid."""
    _ERROR_CODE = "InvalidMaxResultsException"


class InvalidMergeOptionException(CodeCommitError):
    """The specified merge option is not valid for this operation. Not all merge strategies
    are supported for all operations.
    """

    _ERROR_CODE = "InvalidMergeOptionException"


class InvalidOrderException(CodeCommitError):
    """The specified sort order is not valid."""
    _ERROR_CODE = "InvalidOrderException"


class InvalidOverrideStatusException(CodeCommitError):
    """The override status is not valid. Valid statuses are OVERRIDE and REVOKE."""
    _ERROR_CODE = "InvalidOverrideStatusException"


class InvalidParentCommitIdException(CodeCommitError):
    """The parent commit ID is not valid. The commit ID cannot be empty, and must match the
    head commit ID for the branch of the repository where you want to add or update a
    file.
    """

    _ERROR_CODE = "InvalidParentCommitIdException"


class InvalidPathException(CodeCommitError):
    """The specified path is not valid."""
    _ERROR_CODE = "InvalidPathException"


class InvalidPullRequestEventTypeException(CodeCommitError):
    """The pull request event type is not valid."""
    _ERROR_CODE = "InvalidPullRequestEventTypeException"


class InvalidPullRequestIdException(CodeCommitError):
    """The pull request ID is not valid. Make sure that you have provided the full ID and
    that the pull request is in the specified repository, and then try again.
    """

    _ERROR_CODE = "InvalidPullRequestIdException"


class InvalidPullRequestStatusException(CodeCommitError):
    """The pull request status is not valid. The only valid values are `OPEN` and `CLOSED`."""
    _ERROR_CODE = "InvalidPullRequestStatusException"


class InvalidPullRequestStatusUpdateException(CodeCommitError):
    """The pull request status update is not valid. The only valid update is from `OPEN` to
    `CLOSED`.
    """

    _ERROR_CODE = "InvalidPullRequestStatusUpdateException"


class InvalidReactionUserArnException(CodeCommitError):
    """The Amazon Resource Name (ARN) of the user or identity is not valid."""
    _ERROR_CODE = "InvalidReactionUserArnException"


class InvalidReactionValueException(CodeCommitError):
    """The value of the reaction is not valid. For more information, see the CodeCommit
    User Guide.
    """

    _ERROR_CODE = "InvalidReactionValueException"


class InvalidReferenceNameException(CodeCommitError):
    """The specified reference name format is not valid. Reference names must conform to
    the Git references format (for example, refs/heads/main). For more information, see
    Git Internals - Git References or consult your Git documentation.
    """

    _ERROR_CODE = "InvalidReferenceNameException"


class InvalidRelativeFileVersionEnumException(CodeCommitError):
    """Either the enum is not in a valid format, or the specified file version enum is not
    valid in respect to the current file version.
    """

    _ERROR_CODE = "InvalidRelativeFileVersionEnumException"


class InvalidReplacementContentException(CodeCommitError):
    """Automerge was specified for resolving the conflict, but the replacement type is not
    valid or content is missing.
    """

    _ERROR_CODE = "InvalidReplacementContentException"


class InvalidReplacementTypeException(CodeCommitError):
    """Automerge was specified for resolving the conflict, but the specified replacement
    type is not valid.
    """

    _ERROR_CODE = "InvalidReplacementTypeException"


class InvalidRepositoryDescriptionException(CodeCommitError):
    """The specified repository description is not valid."""
    _ERROR_CODE = "InvalidRepositoryDescriptionException"


class InvalidRepositoryNameException(CodeCommitError):
    """A specified repository name is not valid.

    Note:

    This exception occurs only when a specified repository name is not valid. Other
    exceptions occur when a required repository parameter is missing, or when a
    specified repository does not exist.
    """

    _ERROR_CODE = "InvalidRepositoryNameException"


class InvalidRepositoryTriggerBranchNameException(CodeCommitError):
    """One or more branch names specified for the trigger is not valid."""
    _ERROR_CODE = "InvalidRepositoryTriggerBranchNameException"


class InvalidRepositoryTriggerCustomDataException(CodeCommitError):
    """The custom data provided for the trigger is not valid."""
    _ERROR_CODE = "InvalidRepositoryTriggerCustomDataException"


class InvalidRepositoryTriggerDestinationArnException(CodeCommitError):
    """The Amazon Resource Name (ARN) for the trigger is not valid for the specified
    destination. The most common reason for this error is that the ARN does not meet the
    requirements for the service type.
    """

    _ERROR_CODE = "InvalidRepositoryTriggerDestinationArnException"


class InvalidRepositoryTriggerEventsException(CodeCommitError):
    """One or more events specified for the trigger is not valid. Check to make sure that
    all events specified match the requirements for allowed events.
    """

    _ERROR_CODE = "InvalidRepositoryTriggerEventsException"


class InvalidRepositoryTriggerNameException(CodeCommitError):
    """The name of the trigger is not valid."""
    _ERROR_CODE = "InvalidRepositoryTriggerNameException"


class InvalidRepositoryTriggerRegionException(CodeCommitError):
    """The Amazon Web Services Region for the trigger target does not match the Amazon Web
    Services Region for the repository. Triggers must be created in the same Amazon Web
    Services Region as the target for the trigger.
    """

    _ERROR_CODE = "InvalidRepositoryTriggerRegionException"


class InvalidResourceArnException(CodeCommitError):
    """The value for the resource ARN is not valid. For more information about resources in
    CodeCommit, see CodeCommit Resources and Operations in the CodeCommit User Guide.
    """

    _ERROR_CODE = "InvalidResourceArnException"


class InvalidRevisionIdException(CodeCommitError):
    """The revision ID is not valid. Use GetPullRequest to determine the value."""
    _ERROR_CODE = "InvalidRevisionIdException"


class InvalidRuleContentSha256Exception(CodeCommitError):
    """The SHA-256 hash signature for the rule content is not valid."""
    _ERROR_CODE = "InvalidRuleContentSha256Exception"


class InvalidSortByException(CodeCommitError):
    """The specified sort by value is not valid."""
    _ERROR_CODE = "InvalidSortByException"


class InvalidSourceCommitSpecifierException(CodeCommitError):
    """The source commit specifier is not valid. You must provide a valid branch name, tag,
    or full commit ID.
    """

    _ERROR_CODE = "InvalidSourceCommitSpecifierException"


class InvalidSystemTagUsageException(CodeCommitError):
    """The specified tag is not valid. Key names cannot be prefixed with aws:."""
    _ERROR_CODE = "InvalidSystemTagUsageException"


class InvalidTagKeysListException(CodeCommitError):
    """The list of tags is not valid."""
    _ERROR_CODE = "InvalidTagKeysListException"


class InvalidTagsMapException(CodeCommitError):
    """The map of tags is not valid."""
    _ERROR_CODE = "InvalidTagsMapException"


class InvalidTargetBranchException(CodeCommitError):
    """The specified target branch is not valid."""
    _ERROR_CODE = "InvalidTargetBranchException"


class InvalidTargetException(CodeCommitError):
    """The target for the pull request is not valid. A target must contain the full values
    for the repository name, source branch, and destination branch for the pull request.
    """

    _ERROR_CODE = "InvalidTargetException"


class InvalidTargetsException(CodeCommitError):
    """The targets for the pull request is not valid or not in a valid format. Targets are
    a list of target objects. Each target object must contain the full values for the
    repository name, source branch, and destination branch for a pull request.
    """

    _ERROR_CODE = "InvalidTargetsException"


class InvalidTitleException(CodeCommitError):
    """The title of the pull request is not valid. Pull request titles cannot exceed 100
    characters in length.
    """

    _ERROR_CODE = "InvalidTitleException"


class ManualMergeRequiredException(CodeCommitError):
    """The pull request cannot be merged automatically into the destination branch. You
    must manually merge the branches and resolve any conflicts.
    """

    _ERROR_CODE = "ManualMergeRequiredException"


class MaximumBranchesExceededException(CodeCommitError):
    """The number of branches for the trigger was exceeded."""
    _ERROR_CODE = "MaximumBranchesExceededException"


class MaximumConflictResolutionEntriesExceededException(CodeCommitError):
    """The number of allowed conflict resolution entries was exceeded."""
    _ERROR_CODE = "MaximumConflictResolutionEntriesExceededException"


class MaximumFileContentToLoadExceededException(CodeCommitError):
    """The number of files to load exceeds the allowed limit."""
    _ERROR_CODE = "MaximumFileContentToLoadExceededException"


class MaximumFileEntriesExceededException(CodeCommitError):
    """The number of specified files to change as part of this commit exceeds the maximum
    number of files that can be changed in a single commit. Consider using a Git client
    for these changes.
    """

    _ERROR_CODE = "MaximumFileEntriesExceededException"


class MaximumItemsToCompareExceededException(CodeCommitError):
    """The number of items to compare between the source or destination branches and the
    merge base has exceeded the maximum allowed.
    """

    _ERROR_CODE = "MaximumItemsToCompareExceededException"


class MaximumNumberOfApprovalsExceededException(CodeCommitError):
    """The number of approvals required for the approval rule exceeds the maximum number
    allowed.
    """

    _ERROR_CODE = "MaximumNumberOfApprovalsExceededException"


class MaximumOpenPullRequestsExceededException(CodeCommitError):
    """You cannot create the pull request because the repository has too many open pull
    requests. The maximum number of open pull requests for a repository is 1,000. Close
    one or more open pull requests, and then try again.
    """

    _ERROR_CODE = "MaximumOpenPullRequestsExceededException"


class MaximumRepositoryNamesExceededException(CodeCommitError):
    """The maximum number of allowed repository names was exceeded. Currently, this number
    is 100.
    """

    _ERROR_CODE = "MaximumRepositoryNamesExceededException"


class MaximumRepositoryTriggersExceededException(CodeCommitError):
    """The number of triggers allowed for the repository was exceeded."""
    _ERROR_CODE = "MaximumRepositoryTriggersExceededException"


class MaximumRuleTemplatesAssociatedWithRepositoryException(CodeCommitError):
    """The maximum number of approval rule templates for a repository has been exceeded.
    You cannot associate more than 25 approval rule templates with a repository.
    """

    _ERROR_CODE = "MaximumRuleTemplatesAssociatedWithRepositoryException"


class MergeOptionRequiredException(CodeCommitError):
    """A merge option or stategy is required, and none was provided."""
    _ERROR_CODE = "MergeOptionRequiredException"


class MultipleConflictResolutionEntriesException(CodeCommitError):
    """More than one conflict resolution entries exists for the conflict. A conflict can
    have only one conflict resolution entry.
    """

    _ERROR_CODE = "MultipleConflictResolutionEntriesException"


class MultipleRepositoriesInPullRequestException(CodeCommitError):
    """You cannot include more than one repository in a pull request. Make sure you have
    specified only one repository name in your request, and then try again.
    """

    _ERROR_CODE = "MultipleRepositoriesInPullRequestException"


class NameLengthExceededException(CodeCommitError):
    """The user name is not valid because it has exceeded the character limit for author
    names.
    """

    _ERROR_CODE = "NameLengthExceededException"


class NoChangeException(CodeCommitError):
    """The commit cannot be created because no changes will be made to the repository as a
    result of this commit. A commit must contain at least one change.
    """

    _ERROR_CODE = "NoChangeException"


class NumberOfRuleTemplatesExceededException(CodeCommitError):
    """The maximum number of approval rule templates has been exceeded for this Amazon Web
    Services Region.
    """

    _ERROR_CODE = "NumberOfRuleTemplatesExceededException"


class NumberOfRulesExceededException(CodeCommitError):
    """The approval rule cannot be added. The pull request has the maximum number of
    approval rules associated with it.
    """

    _ERROR_CODE = "NumberOfRulesExceededException"


class OperationNotAllowedException(CodeCommitError):
    """The requested action is not allowed."""
    _ERROR_CODE = "OperationNotAllowedException"


class OverrideAlreadySetException(CodeCommitError):
    """The pull request has already had its approval rules set to override."""
    _ERROR_CODE = "OverrideAlreadySetException"


class OverrideStatusRequiredException(CodeCommitError):
    """An override status is required, but no value was provided. Valid values include
    OVERRIDE and REVOKE.
    """

    _ERROR_CODE = "OverrideStatusRequiredException"


class ParentCommitDoesNotExistException(CodeCommitError):
    """The parent commit ID is not valid because it does not exist. The specified parent
    commit ID does not exist in the specified branch of the repository.
    """

    _ERROR_CODE = "ParentCommitDoesNotExistException"


class ParentCommitIdOutdatedException(CodeCommitError):
    """The file could not be added because the provided parent commit ID is not the current
    tip of the specified branch. To view the full commit ID of the current head of the
    branch, use GetBranch.
    """

    _ERROR_CODE = "ParentCommitIdOutdatedException"


class ParentCommitIdRequiredException(CodeCommitError):
    """A parent commit ID is required. To view the full commit ID of a branch in a
    repository, use GetBranch or a Git command (for example, git pull or git log).
    """

    _ERROR_CODE = "ParentCommitIdRequiredException"


class PathDoesNotExistException(CodeCommitError):
    """The specified path does not exist."""
    _ERROR_CODE = "PathDoesNotExistException"


class PathRequiredException(CodeCommitError):
    """The folderPath for a location cannot be null."""
    _ERROR_CODE = "PathRequiredException"


class PullRequestAlreadyClosedException(CodeCommitError):
    """The pull request status cannot be updated because it is already closed."""
    _ERROR_CODE = "PullRequestAlreadyClosedException"


class PullRequestApprovalRulesNotSatisfiedException(CodeCommitError):
    """The pull request cannot be merged because one or more approval rules applied to the
    pull request have conditions that have not been met.
    """

    _ERROR_CODE = "PullRequestApprovalRulesNotSatisfiedException"


class PullRequestCannotBeApprovedByAuthorException(CodeCommitError):
    """The approval cannot be applied because the user approving the pull request matches
    the user who created the pull request. You cannot approve a pull request that you
    created.
    """

    _ERROR_CODE = "PullRequestCannotBeApprovedByAuthorException"


class PullRequestDoesNotExistException(CodeCommitError):
    """The pull request ID could not be found. Make sure that you have specified the
    correct repository name and pull request ID, and then try again.
    """

    _ERROR_CODE = "PullRequestDoesNotExistException"


class PullRequestIdRequiredException(CodeCommitError):
    """A pull request ID is required, but none was provided."""
    _ERROR_CODE = "PullRequestIdRequiredException"


class PullRequestStatusRequiredException(CodeCommitError):
    """A pull request status is required, but none was provided."""
    _ERROR_CODE = "PullRequestStatusRequiredException"


class PutFileEntryConflictException(CodeCommitError):
    """The commit cannot be created because one or more files specified in the commit
    reference both a file and a folder.
    """

    _ERROR_CODE = "PutFileEntryConflictException"


class ReactionLimitExceededException(CodeCommitError):
    """The number of reactions has been exceeded. Reactions are limited to one reaction per
    user for each individual comment ID.
    """

    _ERROR_CODE = "ReactionLimitExceededException"


class ReactionValueRequiredException(CodeCommitError):
    """A reaction value is required."""
    _ERROR_CODE = "ReactionValueRequiredException"


class ReferenceDoesNotExistException(CodeCommitError):
    """The specified reference does not exist. You must provide a full commit ID."""
    _ERROR_CODE = "ReferenceDoesNotExistException"


class ReferenceNameRequiredException(CodeCommitError):
    """A reference name is required, but none was provided."""
    _ERROR_CODE = "ReferenceNameRequiredException"


class ReferenceTypeNotSupportedException(CodeCommitError):
    """The specified reference is not a supported type."""
    _ERROR_CODE = "ReferenceTypeNotSupportedException"


class ReplacementContentRequiredException(CodeCommitError):
    """USE_NEW_CONTENT was specified, but no replacement content has been provided."""
    _ERROR_CODE = "ReplacementContentRequiredException"


class ReplacementTypeRequiredException(CodeCommitError):
    """A replacement type is required."""
    _ERROR_CODE = "ReplacementTypeRequiredException"


class RepositoryDoesNotExistException(CodeCommitError):
    """The specified repository does not exist."""
    _ERROR_CODE = "RepositoryDoesNotExistException"


class RepositoryLimitExceededException(CodeCommitError):
    """A repository resource limit was exceeded."""
    _ERROR_CODE = "RepositoryLimitExceededException"


class RepositoryNameExistsException(CodeCommitError):
    """The specified repository name already exists."""
    _ERROR_CODE = "RepositoryNameExistsException"


class RepositoryNameRequiredException(CodeCommitError):
    """A repository name is required, but was not specified."""
    _ERROR_CODE = "RepositoryNameRequiredException"


class RepositoryNamesRequiredException(CodeCommitError):
    """At least one repository name object is required, but was not specified."""
    _ERROR_CODE = "RepositoryNamesRequiredException"


class RepositoryNotAssociatedWithPullRequestException(CodeCommitError):
    """The repository does not contain any pull requests with that pull request ID. Use
    GetPullRequest to verify the correct repository name for the pull request ID.
    """

    _ERROR_CODE = "RepositoryNotAssociatedWithPullRequestException"


class RepositoryTriggerBranchNameListRequiredException(CodeCommitError):
    """At least one branch name is required, but was not specified in the trigger
    configuration.
    """

    _ERROR_CODE = "RepositoryTriggerBranchNameListRequiredException"


class RepositoryTriggerDestinationArnRequiredException(CodeCommitError):
    """A destination ARN for the target service for the trigger is required, but was not
    specified.
    """

    _ERROR_CODE = "RepositoryTriggerDestinationArnRequiredException"


class RepositoryTriggerEventsListRequiredException(CodeCommitError):
    """At least one event for the trigger is required, but was not specified."""
    _ERROR_CODE = "RepositoryTriggerEventsListRequiredException"


class RepositoryTriggerNameRequiredException(CodeCommitError):
    """A name for the trigger is required, but was not specified."""
    _ERROR_CODE = "RepositoryTriggerNameRequiredException"


class RepositoryTriggersListRequiredException(CodeCommitError):
    """The list of triggers for the repository is required, but was not specified."""
    _ERROR_CODE = "RepositoryTriggersListRequiredException"


class ResourceArnRequiredException(CodeCommitError):
    """A valid Amazon Resource Name (ARN) for an CodeCommit resource is required. For a
    list of valid resources in CodeCommit, see CodeCommit Resources and Operations in
    the CodeCommit User Guide.
    """

    _ERROR_CODE = "ResourceArnRequiredException"


class RestrictedSourceFileException(CodeCommitError):
    """The commit cannot be created because one of the changes specifies copying or moving
    a .gitkeep file.
    """

    _ERROR_CODE = "RestrictedSourceFileException"


class RevisionIdRequiredException(CodeCommitError):
    """A revision ID is required, but was not provided."""
    _ERROR_CODE = "RevisionIdRequiredException"


class RevisionNotCurrentException(CodeCommitError):
    """The revision ID provided in the request does not match the current revision ID. Use
    GetPullRequest to retrieve the current revision ID.
    """

    _ERROR_CODE = "RevisionNotCurrentException"


class SameFileContentException(CodeCommitError):
    """The file was not added or updated because the content of the file is exactly the
    same as the content of that file in the repository and branch that you specified.
    """

    _ERROR_CODE = "SameFileContentException"


class SamePathRequestException(CodeCommitError):
    """The commit cannot be created because one or more changes in this commit duplicate
    actions in the same file path. For example, you cannot make the same delete request
    to the same file in the same file path twice, or make a delete request and a move
    request to the same file as part of the same commit.
    """

    _ERROR_CODE = "SamePathRequestException"


class SourceAndDestinationAreSameException(CodeCommitError):
    """The source branch and destination branch for the pull request are the same. You must
    specify different branches for the source and destination.
    """

    _ERROR_CODE = "SourceAndDestinationAreSameException"


class SourceFileOrContentRequiredException(CodeCommitError):
    """The commit cannot be created because no source files or file content have been
    specified for the commit.
    """

    _ERROR_CODE = "SourceFileOrContentRequiredException"


class TagKeysListRequiredException(CodeCommitError):
    """A list of tag keys is required. The list cannot be empty or null."""
    _ERROR_CODE = "TagKeysListRequiredException"


class TagPolicyException(CodeCommitError):
    """The tag policy is not valid."""
    _ERROR_CODE = "TagPolicyException"


class TagsMapRequiredException(CodeCommitError):
    """A map of tags is required."""
    _ERROR_CODE = "TagsMapRequiredException"


class TargetRequiredException(CodeCommitError):
    """A pull request target is required. It cannot be empty or null. A pull request target
    must contain the full values for the repository name, source branch, and destination
    branch for the pull request.
    """

    _ERROR_CODE = "TargetRequiredException"


class TargetsRequiredException(CodeCommitError):
    """An array of target objects is required. It cannot be empty or null."""
    _ERROR_CODE = "TargetsRequiredException"


class TipOfSourceReferenceIsDifferentException(CodeCommitError):
    """The tip of the source branch in the destination repository does not match the tip of
    the source branch specified in your request. The pull request might have been
    updated. Make sure that you have the latest changes.
    """

    _ERROR_CODE = "TipOfSourceReferenceIsDifferentException"


class TipsDivergenceExceededException(CodeCommitError):
    """The divergence between the tips of the provided commit specifiers is too great to
    determine whether there might be any merge conflicts. Locally compare the specifiers
    using `git diff` or a diff tool.
    """

    _ERROR_CODE = "TipsDivergenceExceededException"


class TitleRequiredException(CodeCommitError):
    """A pull request title is required. It cannot be empty or null."""
    _ERROR_CODE = "TitleRequiredException"


class TooManyTagsException(CodeCommitError):
    """The maximum number of tags for an CodeCommit resource has been exceeded."""
    _ERROR_CODE = "TooManyTagsException"


EXCEPTIONS: dict[str, type[CodeCommitError]] = {
    "ActorDoesNotExistException": ActorDoesNotExistException,
    "ApprovalRuleContentRequiredException": ApprovalRuleContentRequiredException,
    "ApprovalRuleDoesNotExistException": ApprovalRuleDoesNotExistException,
    "ApprovalRuleNameAlreadyExistsException": ApprovalRuleNameAlreadyExistsException,
    "ApprovalRuleNameRequiredException": ApprovalRuleNameRequiredException,
    "ApprovalRuleTemplateContentRequiredException": ApprovalRuleTemplateContentRequiredException,
    "ApprovalRuleTemplateDoesNotExistException": ApprovalRuleTemplateDoesNotExistException,
    "ApprovalRuleTemplateInUseException": ApprovalRuleTemplateInUseException,
    "ApprovalRuleTemplateNameAlreadyExistsException": ApprovalRuleTemplateNameAlreadyExistsException,
    "ApprovalRuleTemplateNameRequiredException": ApprovalRuleTemplateNameRequiredException,
    "ApprovalStateRequiredException": ApprovalStateRequiredException,
    "AuthorDoesNotExistException": AuthorDoesNotExistException,
    "BeforeCommitIdAndAfterCommitIdAreSameException": BeforeCommitIdAndAfterCommitIdAreSameException,
    "BlobIdDoesNotExistException": BlobIdDoesNotExistException,
    "BlobIdRequiredException": BlobIdRequiredException,
    "BranchDoesNotExistException": BranchDoesNotExistException,
    "BranchNameExistsException": BranchNameExistsException,
    "BranchNameIsTagNameException": BranchNameIsTagNameException,
    "BranchNameRequiredException": BranchNameRequiredException,
    "CannotDeleteApprovalRuleFromTemplateException": CannotDeleteApprovalRuleFromTemplateException,
    "CannotModifyApprovalRuleFromTemplateException": CannotModifyApprovalRuleFromTemplateException,
    "ClientRequestTokenRequiredException": ClientRequestTokenRequiredException,
    "CommentContentRequiredException": CommentContentRequiredException,
    "CommentContentSizeLimitExceededException": CommentContentSizeLimitExceededException,
    "CommentDeletedException": CommentDeletedException,
    "CommentDoesNotExistException": CommentDoesNotExistException,
    "CommentIdRequiredException": CommentIdRequiredException,
    "CommentNotCreatedByCallerException": CommentNotCreatedByCallerException,
    "CommitDoesNotExistException": CommitDoesNotExistException,
    "CommitIdDoesNotExistException": CommitIdDoesNotExistException,
    "CommitIdRequiredException": CommitIdRequiredException,
    "CommitIdsLimitExceededException": CommitIdsLimitExceededException,
    "CommitIdsListRequiredException": CommitIdsListRequiredException,
    "CommitMessageLengthExceededException": CommitMessageLengthExceededException,
    "CommitRequiredException": CommitRequiredException,
    "ConcurrentReferenceUpdateException": ConcurrentReferenceUpdateException,
    "DefaultBranchCannotBeDeletedException": DefaultBranchCannotBeDeletedException,
    "DirectoryNameConflictsWithFileNameException": DirectoryNameConflictsWithFileNameException,
    "EncryptionIntegrityChecksFailedException": EncryptionIntegrityChecksFailedException,
    "EncryptionKeyAccessDeniedException": EncryptionKeyAccessDeniedException,
    "EncryptionKeyDisabledException": EncryptionKeyDisabledException,
    "EncryptionKeyInvalidIdException": EncryptionKeyInvalidIdException,
    "EncryptionKeyInvalidUsageException": EncryptionKeyInvalidUsageException,
    "EncryptionKeyNotFoundException": EncryptionKeyNotFoundException,
    "EncryptionKeyRequiredException": EncryptionKeyRequiredException,
    "EncryptionKeyUnavailableException": EncryptionKeyUnavailableException,
    "FileContentAndSourceFileSpecifiedException": FileContentAndSourceFileSpecifiedException,
    "FileContentRequiredException": FileContentRequiredException,
    "FileContentSizeLimitExceededException": FileContentSizeLimitExceededException,
    "FileDoesNotExistException": FileDoesNotExistException,
    "FileEntryRequiredException": FileEntryRequiredException,
    "FileModeRequiredException": FileModeRequiredException,
    "FileNameConflictsWithDirectoryNameException": FileNameConflictsWithDirectoryNameException,
    "FilePathConflictsWithSubmodulePathException": FilePathConflictsWithSubmodulePathException,
    "FileTooLargeException": FileTooLargeException,
    "FolderContentSizeLimitExceededException": FolderContentSizeLimitExceededException,
    "FolderDoesNotExistException": FolderDoesNotExistException,
    "IdempotencyParameterMismatchException": IdempotencyParameterMismatchException,
    "InvalidActorArnException": InvalidActorArnException,
    "InvalidApprovalRuleContentException": InvalidApprovalRuleContentException,
    "InvalidApprovalRuleNameException": InvalidApprovalRuleNameException,
    "InvalidApprovalRuleTemplateContentException": InvalidApprovalRuleTemplateContentException,
    "InvalidApprovalRuleTemplateDescriptionException": InvalidApprovalRuleTemplateDescriptionException,
    "InvalidApprovalRuleTemplateNameException": InvalidApprovalRuleTemplateNameException,
    "InvalidApprovalStateException": InvalidApprovalStateException,
    "InvalidAuthorArnException": InvalidAuthorArnException,
    "InvalidBlobIdException": InvalidBlobIdException,
    "InvalidBranchNameException": InvalidBranchNameException,
    "InvalidClientRequestTokenException": InvalidClientRequestTokenException,
    "InvalidCommentIdException": InvalidCommentIdException,
    "InvalidCommitException": InvalidCommitException,
    "InvalidCommitIdException": InvalidCommitIdException,
    "InvalidConflictDetailLevelException": InvalidConflictDetailLevelException,
    "InvalidConflictResolutionException": InvalidConflictResolutionException,
    "InvalidConflictResolutionStrategyException": InvalidConflictResolutionStrategyException,
    "InvalidContinuationTokenException": InvalidContinuationTokenException,
    "InvalidDeletionParameterException": InvalidDeletionParameterException,
    "InvalidDescriptionException": InvalidDescriptionException,
    "InvalidDestinationCommitSpecifierException": InvalidDestinationCommitSpecifierException,
    "InvalidEmailException": InvalidEmailException,
    "InvalidFileLocationException": InvalidFileLocationException,
    "InvalidFileModeException": InvalidFileModeException,
    "InvalidFilePositionException": InvalidFilePositionException,
    "InvalidMaxConflictFilesException": InvalidMaxConflictFilesException,
    "InvalidMaxMergeHunksException": InvalidMaxMergeHunksException,
    "InvalidMaxResultsException": InvalidMaxResultsException,
    "InvalidMergeOptionException": InvalidMergeOptionException,
    "InvalidOrderException": InvalidOrderException,
    "InvalidOverrideStatusException": InvalidOverrideStatusException,
    "InvalidParentCommitIdException": InvalidParentCommitIdException,
    "InvalidPathException": InvalidPathException,
    "InvalidPullRequestEventTypeException": InvalidPullRequestEventTypeException,
    "InvalidPullRequestIdException": InvalidPullRequestIdException,
    "InvalidPullRequestStatusException": InvalidPullRequestStatusException,
    "InvalidPullRequestStatusUpdateException": InvalidPullRequestStatusUpdateException,
    "InvalidReactionUserArnException": InvalidReactionUserArnException,
    "InvalidReactionValueException": InvalidReactionValueException,
    "InvalidReferenceNameException": InvalidReferenceNameException,
    "InvalidRelativeFileVersionEnumException": InvalidRelativeFileVersionEnumException,
    "InvalidReplacementContentException": InvalidReplacementContentException,
    "InvalidReplacementTypeException": InvalidReplacementTypeException,
    "InvalidRepositoryDescriptionException": InvalidRepositoryDescriptionException,
    "InvalidRepositoryNameException": InvalidRepositoryNameException,
    "InvalidRepositoryTriggerBranchNameException": InvalidRepositoryTriggerBranchNameException,
    "InvalidRepositoryTriggerCustomDataException": InvalidRepositoryTriggerCustomDataException,
    "InvalidRepositoryTriggerDestinationArnException": InvalidRepositoryTriggerDestinationArnException,
    "InvalidRepositoryTriggerEventsException": InvalidRepositoryTriggerEventsException,
    "InvalidRepositoryTriggerNameException": InvalidRepositoryTriggerNameException,
    "InvalidRepositoryTriggerRegionException": InvalidRepositoryTriggerRegionException,
    "InvalidResourceArnException": InvalidResourceArnException,
    "InvalidRevisionIdException": InvalidRevisionIdException,
    "InvalidRuleContentSha256Exception": InvalidRuleContentSha256Exception,
    "InvalidSortByException": InvalidSortByException,
    "InvalidSourceCommitSpecifierException": InvalidSourceCommitSpecifierException,
    "InvalidSystemTagUsageException": InvalidSystemTagUsageException,
    "InvalidTagKeysListException": InvalidTagKeysListException,
    "InvalidTagsMapException": InvalidTagsMapException,
    "InvalidTargetBranchException": InvalidTargetBranchException,
    "InvalidTargetException": InvalidTargetException,
    "InvalidTargetsException": InvalidTargetsException,
    "InvalidTitleException": InvalidTitleException,
    "ManualMergeRequiredException": ManualMergeRequiredException,
    "MaximumBranchesExceededException": MaximumBranchesExceededException,
    "MaximumConflictResolutionEntriesExceededException": MaximumConflictResolutionEntriesExceededException,
    "MaximumFileContentToLoadExceededException": MaximumFileContentToLoadExceededException,
    "MaximumFileEntriesExceededException": MaximumFileEntriesExceededException,
    "MaximumItemsToCompareExceededException": MaximumItemsToCompareExceededException,
    "MaximumNumberOfApprovalsExceededException": MaximumNumberOfApprovalsExceededException,
    "MaximumOpenPullRequestsExceededException": MaximumOpenPullRequestsExceededException,
    "MaximumRepositoryNamesExceededException": MaximumRepositoryNamesExceededException,
    "MaximumRepositoryTriggersExceededException": MaximumRepositoryTriggersExceededException,
    "MaximumRuleTemplatesAssociatedWithRepositoryException": MaximumRuleTemplatesAssociatedWithRepositoryException,
    "MergeOptionRequiredException": MergeOptionRequiredException,
    "MultipleConflictResolutionEntriesException": MultipleConflictResolutionEntriesException,
    "MultipleRepositoriesInPullRequestException": MultipleRepositoriesInPullRequestException,
    "NameLengthExceededException": NameLengthExceededException,
    "NoChangeException": NoChangeException,
    "NumberOfRuleTemplatesExceededException": NumberOfRuleTemplatesExceededException,
    "NumberOfRulesExceededException": NumberOfRulesExceededException,
    "OperationNotAllowedException": OperationNotAllowedException,
    "OverrideAlreadySetException": OverrideAlreadySetException,
    "OverrideStatusRequiredException": OverrideStatusRequiredException,
    "ParentCommitDoesNotExistException": ParentCommitDoesNotExistException,
    "ParentCommitIdOutdatedException": ParentCommitIdOutdatedException,
    "ParentCommitIdRequiredException": ParentCommitIdRequiredException,
    "PathDoesNotExistException": PathDoesNotExistException,
    "PathRequiredException": PathRequiredException,
    "PullRequestAlreadyClosedException": PullRequestAlreadyClosedException,
    "PullRequestApprovalRulesNotSatisfiedException": PullRequestApprovalRulesNotSatisfiedException,
    "PullRequestCannotBeApprovedByAuthorException": PullRequestCannotBeApprovedByAuthorException,
    "PullRequestDoesNotExistException": PullRequestDoesNotExistException,
    "PullRequestIdRequiredException": PullRequestIdRequiredException,
    "PullRequestStatusRequiredException": PullRequestStatusRequiredException,
    "PutFileEntryConflictException": PutFileEntryConflictException,
    "ReactionLimitExceededException": ReactionLimitExceededException,
    "ReactionValueRequiredException": ReactionValueRequiredException,
    "ReferenceDoesNotExistException": ReferenceDoesNotExistException,
    "ReferenceNameRequiredException": ReferenceNameRequiredException,
    "ReferenceTypeNotSupportedException": ReferenceTypeNotSupportedException,
    "ReplacementContentRequiredException": ReplacementContentRequiredException,
    "ReplacementTypeRequiredException": ReplacementTypeRequiredException,
    "RepositoryDoesNotExistException": RepositoryDoesNotExistException,
    "RepositoryLimitExceededException": RepositoryLimitExceededException,
    "RepositoryNameExistsException": RepositoryNameExistsException,
    "RepositoryNameRequiredException": RepositoryNameRequiredException,
    "RepositoryNamesRequiredException": RepositoryNamesRequiredException,
    "RepositoryNotAssociatedWithPullRequestException": RepositoryNotAssociatedWithPullRequestException,
    "RepositoryTriggerBranchNameListRequiredException": RepositoryTriggerBranchNameListRequiredException,
    "RepositoryTriggerDestinationArnRequiredException": RepositoryTriggerDestinationArnRequiredException,
    "RepositoryTriggerEventsListRequiredException": RepositoryTriggerEventsListRequiredException,
    "RepositoryTriggerNameRequiredException": RepositoryTriggerNameRequiredException,
    "RepositoryTriggersListRequiredException": RepositoryTriggersListRequiredException,
    "ResourceArnRequiredException": ResourceArnRequiredException,
    "RestrictedSourceFileException": RestrictedSourceFileException,
    "RevisionIdRequiredException": RevisionIdRequiredException,
    "RevisionNotCurrentException": RevisionNotCurrentException,
    "SameFileContentException": SameFileContentException,
    "SamePathRequestException": SamePathRequestException,
    "SourceAndDestinationAreSameException": SourceAndDestinationAreSameException,
    "SourceFileOrContentRequiredException": SourceFileOrContentRequiredException,
    "TagKeysListRequiredException": TagKeysListRequiredException,
    "TagPolicyException": TagPolicyException,
    "TagsMapRequiredException": TagsMapRequiredException,
    "TargetRequiredException": TargetRequiredException,
    "TargetsRequiredException": TargetsRequiredException,
    "TipOfSourceReferenceIsDifferentException": TipOfSourceReferenceIsDifferentException,
    "TipsDivergenceExceededException": TipsDivergenceExceededException,
    "TitleRequiredException": TitleRequiredException,
    "TooManyTagsException": TooManyTagsException,
}
