"""Typed, statically-importable exception classes for every AWS service."""

from boto3_errors._base import Boto3Error
from boto3_errors._patch import patch_client

__all__ = ["Boto3Error", "patch_client"]
