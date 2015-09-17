from storages.backends.s3boto import S3BotoStorage
from ox_site import settings


class FixedS3BotoStorage(S3BotoStorage):
    def url(self, name):
        url = super(FixedS3BotoStorage, self).url(name)
        if name.endswith('/') and not url.endswith('/'):
            url += '/'
        return url

StaticRootS3BotoStorage = lambda: FixedS3BotoStorage(location=settings.STATIC_URL)
MediaRootS3BotoStorage  = lambda: FixedS3BotoStorage(location=settings.MEDIA_URL)