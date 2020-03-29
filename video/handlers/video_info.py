from django.db.models import Q
import requests
from rest_framework import status

from video.constants import LATEST_VIDEO
from video.models import VideoInfo
from video.secrets import V3_KEY
from video.utils import paginate_objects


class VideoData:
    def __init__(self):
        self._s_key = V3_KEY[0]

    def get_latest(self, request):
        objs_qs = VideoInfo.objects.all()
        objs = paginate_objects(request, objs_qs)
        return objs

    def fetch_again(self):
        pass

    def fetch_latest(self):
        """
        Retreive latest video information and returning as json
        """
        url = LATEST_VIDEO.format(self._s_key)
        response = requests.get(url)
        if response.status_code == status.HTTP_200_OK:
            return response.json()

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
        # self.bulk_create(records)         #  Extra Functionality
        self.get_or_create(records)

    def search_in_video(self, word):
        objs = VideoInfo.objects.filter(
            title__icontains=word,
            description__icontains=word
        ).values()
        if not objs:
            objs = VideoInfo.objects.filter(
                Q(title__icontains=word) | Q(description__icontains=word)
            ).values()
        return objs
