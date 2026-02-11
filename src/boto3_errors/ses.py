# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class SESError(Boto3Error):
    _SERVICE = "ses"


class AccountSendingPausedException(SESError):
    """Indicates that email sending is disabled for your entire Amazon SES account.

    You can enable or disable email sending for your Amazon SES account using
    UpdateAccountSendingEnabled.
    """

    _ERROR_CODE = "AccountSendingPausedException"


class AlreadyExistsException(SESError):
    """Indicates that a resource could not be created because of a naming conflict."""
    _ERROR_CODE = "AlreadyExists"

    @property
    def name(self) -> str | None:
        """Indicates that a resource could not be created because the resource name already
        exists.
        """
        return self.response.get("Name")


class CannotDeleteException(SESError):
    """Indicates that the delete operation could not be completed."""
    _ERROR_CODE = "CannotDelete"

    @property
    def name(self) -> str | None:
        """Indicates that a resource could not be deleted because no resource with the
        specified name exists.
        """
        return self.response.get("Name")


class ConfigurationSetAlreadyExistsException(SESError):
    """Indicates that the configuration set could not be created because of a naming
    conflict.
    """

    _ERROR_CODE = "ConfigurationSetAlreadyExists"

    @property
    def configuration_set_name(self) -> str | None:
        """Indicates that the configuration set does not exist."""
        return self.response.get("ConfigurationSetName")


class ConfigurationSetDoesNotExistException(SESError):
    """Indicates that the configuration set does not exist."""
    _ERROR_CODE = "ConfigurationSetDoesNotExist"

    @property
    def configuration_set_name(self) -> str | None:
        """Indicates that the configuration set does not exist."""
        return self.response.get("ConfigurationSetName")


class ConfigurationSetSendingPausedException(SESError):
    """Indicates that email sending is disabled for the configuration set.

    You can enable or disable email sending for a configuration set using
    UpdateConfigurationSetSendingEnabled.
    """

    _ERROR_CODE = "ConfigurationSetSendingPausedException"

    @property
    def configuration_set_name(self) -> str | None:
        """The name of the configuration set for which email sending is disabled."""
        return self.response.get("ConfigurationSetName")


class CustomVerificationEmailInvalidContentException(SESError):
    """Indicates that custom verification email template provided content is invalid."""
    _ERROR_CODE = "CustomVerificationEmailInvalidContent"


class CustomVerificationEmailTemplateAlreadyExistsException(SESError):
    """Indicates that a custom verification email template with the name you specified
    already exists.
    """

    _ERROR_CODE = "CustomVerificationEmailTemplateAlreadyExists"

    @property
    def custom_verification_email_template_name(self) -> str | None:
        """Indicates that the provided custom verification email template with the
        specified template name already exists.
        """
        return self.response.get("CustomVerificationEmailTemplateName")


class CustomVerificationEmailTemplateDoesNotExistException(SESError):
    """Indicates that a custom verification email template with the name you specified does
    not exist.
    """

    _ERROR_CODE = "CustomVerificationEmailTemplateDoesNotExist"

    @property
    def custom_verification_email_template_name(self) -> str | None:
        """Indicates that the provided custom verification email template does not exist."""
        return self.response.get("CustomVerificationEmailTemplateName")


class EventDestinationAlreadyExistsException(SESError):
    """Indicates that the event destination could not be created because of a naming
    conflict.
    """

    _ERROR_CODE = "EventDestinationAlreadyExists"

    @property
    def configuration_set_name(self) -> str | None:
        """Indicates that the configuration set does not exist."""
        return self.response.get("ConfigurationSetName")

    @property
    def event_destination_name(self) -> str | None:
        """Indicates that the event destination does not exist."""
        return self.response.get("EventDestinationName")


class EventDestinationDoesNotExistException(SESError):
    """Indicates that the event destination does not exist."""
    _ERROR_CODE = "EventDestinationDoesNotExist"

    @property
    def configuration_set_name(self) -> str | None:
        """Indicates that the configuration set does not exist."""
        return self.response.get("ConfigurationSetName")

    @property
    def event_destination_name(self) -> str | None:
        """Indicates that the event destination does not exist."""
        return self.response.get("EventDestinationName")


class FromEmailAddressNotVerifiedException(SESError):
    """Indicates that the sender address specified for a custom verification email is not
    verified, and is therefore not eligible to send the custom verification email.
    """

    _ERROR_CODE = "FromEmailAddressNotVerified"

    @property
    def from_email_address(self) -> str | None:
        """Indicates that the from email address associated with the custom verification
        email template is not verified.
        """
        return self.response.get("FromEmailAddress")


class InvalidCloudWatchDestinationException(SESError):
    """Indicates that the Amazon CloudWatch destination is invalid. See the error message
    for details.
    """

    _ERROR_CODE = "InvalidCloudWatchDestination"

    @property
    def configuration_set_name(self) -> str | None:
        """Indicates that the configuration set does not exist."""
        return self.response.get("ConfigurationSetName")

    @property
    def event_destination_name(self) -> str | None:
        """Indicates that the event destination does not exist."""
        return self.response.get("EventDestinationName")


class InvalidConfigurationSetException(SESError):
    """Indicates that the configuration set is invalid. See the error message for details."""
    _ERROR_CODE = "InvalidConfigurationSet"


class InvalidDeliveryOptionsException(SESError):
    """Indicates that provided delivery option is invalid."""
    _ERROR_CODE = "InvalidDeliveryOptions"


class InvalidFirehoseDestinationException(SESError):
    """Indicates that the Amazon Kinesis Firehose destination is invalid. See the error
    message for details.
    """

    _ERROR_CODE = "InvalidFirehoseDestination"

    @property
    def configuration_set_name(self) -> str | None:
        """Indicates that the configuration set does not exist."""
        return self.response.get("ConfigurationSetName")

    @property
    def event_destination_name(self) -> str | None:
        """Indicates that the event destination does not exist."""
        return self.response.get("EventDestinationName")


class InvalidLambdaFunctionException(SESError):
    """Indicates that the provided Amazon Web Services Lambda function is invalid, or that
    Amazon SES could not execute the provided function, possibly due to permissions
    issues. For information about giving permissions, see the Amazon SES Developer
    Guide.
    """

    _ERROR_CODE = "InvalidLambdaFunction"

    @property
    def function_arn(self) -> str | None:
        """Indicates that the ARN of the function was not found."""
        return self.response.get("FunctionArn")


class InvalidPolicyException(SESError):
    """Indicates that the provided policy is invalid. Check the error stack for more
    information about what caused the error.
    """

    _ERROR_CODE = "InvalidPolicy"


class InvalidRenderingParameterException(SESError):
    """Indicates that one or more of the replacement values you provided is invalid. This
    error may occur when the TemplateData object contains invalid JSON.
    """

    _ERROR_CODE = "InvalidRenderingParameter"

    @property
    def template_name(self) -> str | None:
        return self.response.get("TemplateName")


class InvalidS3ConfigurationException(SESError):
    """Indicates that the provided Amazon S3 bucket or Amazon Web Services KMS encryption
    key is invalid, or that Amazon SES could not publish to the bucket, possibly due to
    permissions issues. For information about giving permissions, see the Amazon SES
    Developer Guide.
    """

    _ERROR_CODE = "InvalidS3Configuration"

    @property
    def bucket(self) -> str | None:
        """Indicated that the S3 Bucket was not found."""
        return self.response.get("Bucket")


class InvalidSNSDestinationException(SESError):
    """Indicates that the Amazon Simple Notification Service (Amazon SNS) destination is
    invalid. See the error message for details.
    """

    _ERROR_CODE = "InvalidSNSDestination"

    @property
    def configuration_set_name(self) -> str | None:
        """Indicates that the configuration set does not exist."""
        return self.response.get("ConfigurationSetName")

    @property
    def event_destination_name(self) -> str | None:
        """Indicates that the event destination does not exist."""
        return self.response.get("EventDestinationName")


class InvalidSnsTopicException(SESError):
    """Indicates that the provided Amazon SNS topic is invalid, or that Amazon SES could
    not publish to the topic, possibly due to permissions issues. For information about
    giving permissions, see the Amazon SES Developer Guide.
    """

    _ERROR_CODE = "InvalidSnsTopic"

    @property
    def topic(self) -> str | None:
        """Indicates that the topic does not exist."""
        return self.response.get("Topic")


class InvalidTemplateException(SESError):
    """Indicates that the template that you specified could not be rendered. This issue may
    occur when a template refers to a partial that does not exist.
    """

    _ERROR_CODE = "InvalidTemplate"

    @property
    def template_name(self) -> str | None:
        return self.response.get("TemplateName")


class InvalidTrackingOptionsException(SESError):
    """Indicates that the custom domain to be used for open and click tracking redirects is
    invalid. This error appears most often in the following situations:

    - When the tracking domain you specified is not verified in Amazon SES.
    - When the tracking domain you specified is not a valid domain or subdomain.
    """

    _ERROR_CODE = "InvalidTrackingOptions"


class LimitExceededException(SESError):
    """Indicates that a resource could not be created because of service limits. For a list
    of Amazon SES limits, see the Amazon SES Developer Guide.
    """

    _ERROR_CODE = "LimitExceeded"


class MailFromDomainNotVerifiedException(SESError):
    """Indicates that the message could not be sent because Amazon SES could not read the
    MX record required to use the specified MAIL FROM domain. For information about
    editing the custom MAIL FROM domain settings for an identity, see the Amazon SES
    Developer Guide.
    """

    _ERROR_CODE = "MailFromDomainNotVerifiedException"


class MessageRejected(SESError):
    """Indicates that the action failed, and the message could not be sent. Check the error
    stack for more information about what caused the error.
    """

    _ERROR_CODE = "MessageRejected"


class MissingRenderingAttributeException(SESError):
    """Indicates that one or more of the replacement values for the specified template was
    not specified. Ensure that the TemplateData object contains references to all of the
    replacement tags in the specified template.
    """

    _ERROR_CODE = "MissingRenderingAttribute"

    @property
    def template_name(self) -> str | None:
        return self.response.get("TemplateName")


class ProductionAccessNotGrantedException(SESError):
    """Indicates that the account has not been granted production access."""
    _ERROR_CODE = "ProductionAccessNotGranted"


class RuleDoesNotExistException(SESError):
    """Indicates that the provided receipt rule does not exist."""
    _ERROR_CODE = "RuleDoesNotExist"

    @property
    def name(self) -> str | None:
        """Indicates that the named receipt rule does not exist."""
        return self.response.get("Name")


class RuleSetDoesNotExistException(SESError):
    """Indicates that the provided receipt rule set does not exist."""
    _ERROR_CODE = "RuleSetDoesNotExist"

    @property
    def name(self) -> str | None:
        """Indicates that the named receipt rule set does not exist."""
        return self.response.get("Name")


class TemplateDoesNotExistException(SESError):
    """Indicates that the Template object you specified does not exist in your Amazon SES
    account.
    """

    _ERROR_CODE = "TemplateDoesNotExist"

    @property
    def template_name(self) -> str | None:
        return self.response.get("TemplateName")


class TrackingOptionsAlreadyExistsException(SESError):
    """Indicates that the configuration set you specified already contains a
    TrackingOptions object.
    """

    _ERROR_CODE = "TrackingOptionsAlreadyExistsException"

    @property
    def configuration_set_name(self) -> str | None:
        """Indicates that a TrackingOptions object already exists in the specified
        configuration set.
        """
        return self.response.get("ConfigurationSetName")


class TrackingOptionsDoesNotExistException(SESError):
    """Indicates that the TrackingOptions object you specified does not exist."""
    _ERROR_CODE = "TrackingOptionsDoesNotExistException"

    @property
    def configuration_set_name(self) -> str | None:
        """Indicates that a TrackingOptions object does not exist in the specified
        configuration set.
        """
        return self.response.get("ConfigurationSetName")


EXCEPTIONS: dict[str, type[SESError]] = {
    "AccountSendingPausedException": AccountSendingPausedException,
    "AlreadyExists": AlreadyExistsException,
    "CannotDelete": CannotDeleteException,
    "ConfigurationSetAlreadyExists": ConfigurationSetAlreadyExistsException,
    "ConfigurationSetDoesNotExist": ConfigurationSetDoesNotExistException,
    "ConfigurationSetSendingPausedException": ConfigurationSetSendingPausedException,
    "CustomVerificationEmailInvalidContent": CustomVerificationEmailInvalidContentException,
    "CustomVerificationEmailTemplateAlreadyExists": CustomVerificationEmailTemplateAlreadyExistsException,
    "CustomVerificationEmailTemplateDoesNotExist": CustomVerificationEmailTemplateDoesNotExistException,
    "EventDestinationAlreadyExists": EventDestinationAlreadyExistsException,
    "EventDestinationDoesNotExist": EventDestinationDoesNotExistException,
    "FromEmailAddressNotVerified": FromEmailAddressNotVerifiedException,
    "InvalidCloudWatchDestination": InvalidCloudWatchDestinationException,
    "InvalidConfigurationSet": InvalidConfigurationSetException,
    "InvalidDeliveryOptions": InvalidDeliveryOptionsException,
    "InvalidFirehoseDestination": InvalidFirehoseDestinationException,
    "InvalidLambdaFunction": InvalidLambdaFunctionException,
    "InvalidPolicy": InvalidPolicyException,
    "InvalidRenderingParameter": InvalidRenderingParameterException,
    "InvalidS3Configuration": InvalidS3ConfigurationException,
    "InvalidSNSDestination": InvalidSNSDestinationException,
    "InvalidSnsTopic": InvalidSnsTopicException,
    "InvalidTemplate": InvalidTemplateException,
    "InvalidTrackingOptions": InvalidTrackingOptionsException,
    "LimitExceeded": LimitExceededException,
    "MailFromDomainNotVerifiedException": MailFromDomainNotVerifiedException,
    "MessageRejected": MessageRejected,
    "MissingRenderingAttribute": MissingRenderingAttributeException,
    "ProductionAccessNotGranted": ProductionAccessNotGrantedException,
    "RuleDoesNotExist": RuleDoesNotExistException,
    "RuleSetDoesNotExist": RuleSetDoesNotExistException,
    "TemplateDoesNotExist": TemplateDoesNotExistException,
    "TrackingOptionsAlreadyExistsException": TrackingOptionsAlreadyExistsException,
    "TrackingOptionsDoesNotExistException": TrackingOptionsDoesNotExistException,
}
