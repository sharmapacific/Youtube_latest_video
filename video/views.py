from rest_framework.response import Response
from rest_framework.views import APIView

from video.handlers.video_info import VideoData
from video.services import video_scheduler


class VideoDetailView(APIView):
    http_method_names = ['get']

    def get(self, request):
        """
        Retreive videos information in paginated response
        """
        objs = VideoData().get_latest(request)
        if objs:
            result = []
            for obj in objs.object_list:
                data = {
                    'video_id': obj.video_id,
                    'title': obj.title,
                    'description': obj.description,
                    'published_at': obj.published,
                    'thumbnail_url': obj.thumbnail
                }
                result.append(data)
            return Response(result)
        return Response({'message': 'No Result Found!!'})


class VideoQueryView(APIView):
    http_method_names = ['get']

    def get(self, request):
        """
        Retreive videos information based on the search parameter in
        title and description
        """
        word = request.GET.get('word')
        response = VideoData().search_in_video(word)
        if response:
            result = []
            for obj in response:
                data = {
                    'video_id': obj.get('video_id'),
                    'title': obj.get('title'),
                    'description': obj.get('description'),
                    'published_at': obj.get('published'),
                    'thumbnail_url': obj.get('thumbnail')
                }
                result.append(data)
            return Response(result)
        return Response({'message': 'No Result Found!!'})


class StartScripts(APIView):

    def get(self, request):
        """
        To run the video scheduler
        """
        video_scheduler()
        return Response({'result': 'Script Not Running!!'})
