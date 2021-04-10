from audioFile.models import Song, Podcast, AudioBook
from audioFile.serializers import SongSerializer, PodcastSerializer, AudioBookSerializer
from rest_framework import generics


class AudioList(generics.ListCreateAPIView):
    """
    Generic View for creating and getting list of audio files 
    the endpoint is GET: /<audioFileType>/
    """

    def get_queryset(self):
        """ Function for dynamically selecting model to be used
         for getting and creating audiofiles based on url parameters
        """
        if self.kwargs['audioFileType'].lower() == 'songs':
           return Song.objects.all()
        elif self.kwargs['audioFileType'].lower() == 'podcasts':
            return Podcast.objects.all()
        elif self.kwargs['audioFileType'].lower() == 'audiobooks':
            return AudioBook.objects.all()

    def get_serializer_class(self):
        """ Function for dynamically getting serializer class to be used
         for getting and creating audiofiles based on url parameters
        """
        if self.kwargs['audioFileType'].lower() == 'songs':
           return SongSerializer
        elif self.kwargs['audioFileType'].lower() == 'podcasts':
            return PodcastSerializer
        elif self.kwargs['audioFileType'].lower() == 'audiobooks':
            return AudioBookSerializer
 


class AudioDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Generic view for automatically retirving
     a single audio file ,updating and deleting it at endpoints -
     GET: /<audioFileType>/<id>
     PUT: /<audioFileType>/<id>
     DELETE: /<audioFileType>/<id>
    """

    def get_queryset(self):
        """ Function for dynamically selecting model to be used
         for retrieving, updating and deleting audiofiles based on url parameters
        """
        if self.kwargs['audioFileType'] == 'songs':
           return Song.objects.all()
        elif self.kwargs['audioFileType'] == 'podcasts':
            return Podcast.objects.all()
        elif self.kwargs['audioFileType'] == 'audiobooks':
            return AudioBook.objects.all()

    def get_serializer_class(self):
        """ Function for dynamically getting serializer class to be used
         for retrieving, upldating and deleting audiofiles based on url parameters
        """
        if self.kwargs['audioFileType'] == 'songs':
           return SongSerializer
        elif self.kwargs['audioFileType'] == 'podcasts':
            return PodcastSerializer
        elif self.kwargs['audioFileType'] == 'audiobooks':
            return AudioBookSerializer