import uuid

from django.db import models


class VideoInfo(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4,
                            editable=False)
    video_id = models.CharField(max_length=1000, blank=True, null=True)
    title = models.CharField(max_length=2000, db_index=True, null=True)
    description = models.CharField(max_length=5000, db_index=True, null=True)
    published = models.CharField(max_length=1000, blank=True, null=True)
    thumbnail = models.CharField(max_length=5000, blank=True, null=True)

    def __str__(self):
        return '%s ' % (self.video_id)

    class Meta:
        ordering = ('-published',)
        verbose_name = 'Video Information'
        verbose_name_plural = 'Video Informations'


class Configuration(models.Model):
    key = models.CharField(max_length=1000, blank=True, null=True)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name='Created At',
                                      db_index=True)
    exhaust_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name = 'Key Information'
        verbose_name_plural = 'Keys Informations'
