import uuid

from django.db import models


class VideoInfo(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4,
                            editable=False)
    video_id = models.CharField(max_length=1000, blank=True, null=True)
    title = models.CharField(max_length=2000, blank=True, null=True)
    description = models.CharField(max_length=5000, blank=True, null=True)
    published = models.CharField(max_length=1000, blank=True, null=True)
    thumbnail = models.CharField(max_length=5000, blank=True, null=True)

    def __str__(self):
        return '%s ' % (self.video_id)

    class Meta:
        ordering = ('-published',)
