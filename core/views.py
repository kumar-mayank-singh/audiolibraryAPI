from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import PodcastSerializer,SongSerializer,AudiobookSerializer
from rest_framework import status
from .models import SongModel, PodcastModel, AudioBookModel


class CreateAPI(APIView):
    """
    Provide a valid audio_type as parameter and the metadata of the audio_type in body, it will return the created record.
    """
    def post(self,request,format='json'):
        if self.request.query_params['audio_type'] == 'podcast':

            podcase_participant = self.request.data['podcast_participant'].split(',')
            if len(podcase_participant) > 10:
                    return Response({"Message":"Maximum 10 participant allowed."}, status=status.HTTP_400_BAD_REQUEST)

            for i in podcase_participant:
                if len(i) > 100:
                    return Response({"Message":"Participant name should be less than 100 characters."}, status=status.HTTP_400_BAD_REQUEST)

            serializer = PodcastSerializer(data=self.request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'Podcast Record Created':serializer.data},status=status.HTTP_201_CREATED)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

        elif self.request.query_params['audio_type'] == 'song':
            serializer = SongSerializer(data=self.request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'Song Record Created':serializer.data},status=status.HTTP_201_CREATED)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

        elif self.request.query_params['audio_type'] == 'audiobook':
            serializer = AudiobookSerializer(data=self.request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'Audiobook Record Created':serializer.data},status=status.HTTP_201_CREATED)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

        else:
            return Response({'Message':'Invalid audio type','Should be':'podcast or song or audiobook'}, 
                                status=status.HTTP_400_BAD_REQUEST)


class GetRecordsAPI(APIView):

    def get(self,request,audiotype,id,format='json'):
        if audiotype == 'podcast':
            try:
                record_obj = PodcastModel.objects.get(podcast_id = id)
                serializer = PodcastSerializer(record_obj)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except PodcastModel.DoesNotExist:
                return Response({"No record found with id : ":id},status=status.HTTP_400_BAD_REQUEST)

        elif audiotype == 'song':
            try:
                record_obj = SongModel.objects.get(song_id = id)
                serializer = SongSerializer(record_obj)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except SongModel.DoesNotExist:
                return Response({"No record found with id : ":id},status=status.HTTP_400_BAD_REQUEST)

        elif audiotype == 'audiobook':
            try:
                record_obj = AudioBookModel.objects.get(audiobook_id = id)
                serializer = AudiobookSerializer(record_obj)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except AudioBookModel.DoesNotExist:
                return Response({"No record found with id : ":id},status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'Message':'Invalid audio type','Should be':'podcast or song or audiobook'}, 
                                status=status.HTTP_400_BAD_REQUEST)

class UpdateRecordAPI(APIView):

    def put(self,request,audiotype,id,format='json'):
        if audiotype == 'podcast':
            podcase_participant = self.request.data['podcast_participant']
            if len(podcase_participant) > 10:
                    return Response({"Message":"Maximum 10 participant allowed."}, status=status.HTTP_400_BAD_REQUEST)

            for i in podcase_participant:
                if len(i) > 100:
                    return Response({"Message":"Participant name should be less than 100 characters."}, status=status.HTTP_400_BAD_REQUEST)
            try:
                record_obj = PodcastModel.objects.get(podcast_id = id)
                serializer = PodcastSerializer(record_obj,data=self.request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response({"Record Updated as ":serializer.data}, status=status.HTTP_200_OK)
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
            except PodcastModel.DoesNotExist:
                return Response({"No record found with id : ":id},status=status.HTTP_400_BAD_REQUEST)

        elif audiotype == 'song':
            try:
                record_obj = SongModel.objects.get(song_id = id)
                serializer = SongSerializer(record_obj,data=self.request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response({"Record Updated as ":serializer.data}, status=status.HTTP_200_OK)
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
            except SongModel.DoesNotExist:
                return Response({"No record found with id : ":id},status=status.HTTP_400_BAD_REQUEST)

        elif audiotype == 'audiobook':
            try:
                record_obj = AudioBookModel.objects.get(audiobook_id = id)
                serializer = AudiobookSerializer(record_obj,data=self.request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response({"Record Updated as ":serializer.data}, status=status.HTTP_200_OK)
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
            except AudioBookModel.DoesNotExist:
                return Response({"No record found with id : ":id},status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'Message':'Invalid audio type','Should be':'podcast or song or audiobook'}, 
                                status=status.HTTP_400_BAD_REQUEST)



class DeleteRecordAPI(APIView):

    def put(self,request,audiotype,id,format='json'):
        if audiotype == 'podcast':
            try:
                record_obj = PodcastModel.objects.get(podcast_id = id)
                record_obj.delete()
                return Response({"Message":"Record deleted"}, status=status.HTTP_200_OK)
            except PodcastModel.DoesNotExist:
                return Response({"No record found with id : ":id},status=status.HTTP_400_BAD_REQUEST)

        elif audiotype == 'song':
            try:
                record_obj = SongModel.objects.get(song_id = id)
                record_obj.delete()
                return Response({"Message":"Record deleted"}, status=status.HTTP_200_OK)
            except SongModel.DoesNotExist:
                return Response({"No record found with id : ":id},status=status.HTTP_400_BAD_REQUEST)

        elif audiotype == 'audiobook':
            try:
                record_obj = AudioBookModel.objects.get(audiobook_id = id)
                record_obj.delete()
                return Response({"Message":"Record deleted"}, status=status.HTTP_200_OK)
            except AudioBookModel.DoesNotExist:
                return Response({"No record found with id : ":id},status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'Message':'Invalid audio type','Should be':'podcast or song or audiobook'}, 
                                status=status.HTTP_400_BAD_REQUEST)