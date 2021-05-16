from storages.backends.s3boto3 import S3Boto3Storage

# from storages.backends.azure_storage import AzureStorage


class StaticRootS3Boto3Storage(S3Boto3Storage):
    location = "static"
    default_acl = "public-read"


class MediaRootS3Boto3Storage(S3Boto3Storage):
    location = "media"
    file_overwrite = False


# class PublicAzureStorage(AzureStorage):
#     account_name = 'myaccount'
#     account_key = 'mykey'
#     azure_container = 'mypublic_container'
#     expiration_secs = None
