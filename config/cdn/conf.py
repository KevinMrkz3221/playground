AWS_ACCESS_KEY_ID = 'DO003UW9LRKEZTNW9Q33'
AWS_SECRET_ACCESS_KEY ='shShz33WMxqBFUWa+NWBoBBKnhxB0un2MfiZmRomT7w'
AWS_STORAGE_BUCKET_NAME = 'playground-kev'
AWS_S3_ENDPOINT_URL ='https://nyc3.digitaloceanspaces.com'

AWS_S3_OBJECTS_PARAMETERS = {
    "CacheControl": "max-age=86400"
}
AWS_LOCATION = 'https://playground-kev.nyc3.digitaloceanspaces.com'


DEFAULT_FILE_STORAGE = "config.cdn.backends.MediaRootS3Boto3Storage"
STATICFILES_STORAGE= "config.cdn.backends.StaticRootS3Boto3Storage"

