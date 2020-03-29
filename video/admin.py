from django.contrib import admin

from video.models import VideoInfo


@admin.register(VideoInfo)
class VideoInfoAdmin(admin.ModelAdmin):
    list_display = ('video_id', 'title', 'description',
                    'published', 'thumbnail',)
    search_fields = ('video_id', 'title', 'description',)
