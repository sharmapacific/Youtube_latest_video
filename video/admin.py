from django.contrib import admin

from video.models import Configuration, VideoInfo


@admin.register(VideoInfo)
class VideoInfoAdmin(admin.ModelAdmin):
    list_display = ('video_id', 'title', 'description',
                    'published', 'thumbnail',)
    search_fields = ('video_id', 'title', 'description',)


@admin.register(Configuration)
class ConfigurationAdmin(admin.ModelAdmin):
    list_display = ('key', 'is_active', 'created_at', 'exhaust_on',)
    search_fields = ('key', 'is_active',)
