import arrow

from django.db.models import Q
import requests

from rest_framework import status

from video.constants import LATEST_VIDEO
from video.models import Configuration, VideoInfo
from video.utils import paginate_objects


class VideoData:

    def get_latest(self, request):
        objs_qs = VideoInfo.objects.all()
        objs = paginate_objects(request, objs_qs)
        return objs

    def fetch_latest(self):
        """
        Retreive active key and latest video information and returning as json
        """
        count = True
        while count:
            _s_key = self.get_active_key()
            url = LATEST_VIDEO.format(_s_key)
            response = requests.get(url)
            if response.status_code == status.HTTP_200_OK:
                return response.json()
                count = False
            elif response.status_code == status.HTTP_403_FORBIDDEN:
                self.disable_key(_s_key)
            else:
                count = False

    def bulk_create(self, res_data):
        """
        In case if User is using maxResults in API to retreive data in large
        numbers, Then we can do bulk-update in any batch-size
        """
        res_list = []
        for data in res_data['items']:
            res_list.append(VideoInfo(
                video_id=data['id']['videoId'],
                title=data['snippet']['title'],
                description=data['snippet']['description'],
                published=data['snippet']['publishedAt'],
                thumbnail=data['snippet']['thumbnails']['medium']['url']
                ))
        VideoInfo.objects.bulk_create(res_list, batch_size=100)

    def get_or_create(self, res_data):
        """
        Inserting the results into DB.
        """
        for data in res_data['items']:
            VideoInfo.objects.get_or_create(
                    video_id=data['id']['videoId'],
                    title=data['snippet']['title'],
                    description=data['snippet']['description'],
                    published=data['snippet']['publishedAt'],
                    thumbnail=data['snippet']['thumbnails']['medium']['url']
                )

    def insert_data(self):
        records = self.fetch_latest()
        if records:
            # self.bulk_create(records)         #  Extra Functionality
            self.get_or_create(records)

    def search_in_video(self, word):
        """
        Perform search query in VideoInfo model
        """
        objs = VideoInfo.objects.filter(
            title__icontains=word,
            description__icontains=word
        ).values()
        if not objs:
            objs = VideoInfo.objects.filter(
                Q(title__icontains=word) | Q(description__icontains=word)
            ).values()
        return objs

    def get_active_key(self):
        """
        Get the Active API Key
        """
        keys = Configuration.objects.filter(is_active=True)
        if len(keys) > 0:
            return keys[0].key

    def disable_key(self, _s_key):
        """
        Update the API key when it is get exhausted
        """
        Configuration.objects.filter(key=_s_key).update(
            is_active=False,
            exhaust_on=arrow.utcnow().datetime
            )
