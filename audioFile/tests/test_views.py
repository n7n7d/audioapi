from django.test import TestCase
from django.test.client import JSON_CONTENT_TYPE_RE
from audioFile.models import Song, AudioBook, Podcast
from rest_framework.test import APIClient
from rest_framework import status

class CreateApiTestCase(TestCase):
    """ Class used to test the create endpoints of the API"""
    def test_api_can_create_a_song(self):
        """Test if api can create a song"""
        self.client = APIClient()
        self.song_data = {'name': 'Go to Ibiza','duration': 4}
        self.response = self.client.post(
            '/songs/',
            self.song_data,
            format="json")
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
    
    def test_post_request_can_create_a_new_song_instance(self):
        """Testing if an instance is created after the post request"""
        data = {
            'name': 'foobar',
            'duration': 4
        }
        response = self.client.post(
            '/songs/',
            data = data
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Song.objects.count(), 1)

 #######################################################################       
    
    def test_api_can_create_a_podcast(self):
        """Test if api can create a podcast"""
        self.client = APIClient()
        self.podcast_data = {'name': 'Go to Ibiza','duration': 4,'host':'foo'}
        self.response = self.client.post(
            '/podcasts/',
            self.podcast_data,
            format="json")
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
    
    def test_post_request_can_create_a_new_podcast_instance(self):
        """Testing if an instance is created after the post request"""
        data = {
            'name': 'foobar',
            'duration': 4,
            'host': 'foo',
        }
        response = self.client.post(
            '/podcasts/',
            data = data
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Podcast.objects.count(), 1)
    
 #######################################################################       

    def test_api_can_create_a_AudioBook(self):
        """Test if api can create a AudioBook"""
        self.client = APIClient()
        self.audioBook_data ={
            'title': 'foobar',
            'author': 'foo',
            'duration': 4,
            'narrator': 'bar',
        }
        self.response = self.client.post(
            '/audiobooks/',
            self.audioBook_data,
            format="json")
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
    
    def test_post_request_can_create_a_new_audioBook_instance(self):
        """Testing if an instance is created after the post request"""
        data = {
            'title': 'foobar',
            'author': 'foo',
            'duration': 4,
            'narrator': 'bar',
        }
        response = self.client.post(
            '/audiobooks/',
            data = data
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(AudioBook.objects.count(), 1)

#######################################################################

class UpdateApiTestCase(TestCase):
    """ Class used to test the update behaviour of the API"""
     
    def setUp(self):
        """ Setting up instanes to test """

        self.client = APIClient()
        self.song = Song.objects.create(name ='foobar',duration = 4)
        self.correct_song_data = {
            'name':'foobar',
            'duration': 4
        }
        self.incorrect_song_data = {
            'name':'',
            'duration': 4
        }

        self.podcast = Podcast.objects.create(name='foobar',duration = 4,host = 'bar')
        self.correct_podcast_data = {
            'name':'foobar',
            'duration': 4,
            'host': 'bar'
        }
        self.incorrect_podcast_data = {
            'name':'',
            'duration': 4,
            'host': ''
        }

        self.audiobook = AudioBook.objects.create(title = 'foobar',author = 'bar', narrator = 'nono', duration = 3)
        self.correct_audioBook_data = {
            'title':'we',
            'author': 'we',
            'narrator': 'a',
            'duration':5
        }
        self.incorrect_audioBook_data = {
            'title':'',
            'author': 'bar',
            'narrator': '',
            'duration':5
        }

    #######################################################################

    def test_correct_song_update(self):
       response = self.client.put(
           f'/songs/{self.song.pk}/',
           data = self.correct_song_data
       )
       self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_incorrect_song_update(self):
       response = self.client.put(
           f'/songs/{self.song.pk}/',
           data = self.incorrect_song_data
       )
       self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    #######################################################################

    def test_correct_podcast_update(self):
       response = self.client.put(
           f'/podcasts/{self.podcast.pk}/',
           data = self.correct_podcast_data
       )
       self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_incorrect_podcast_update(self):
       response = self.client.put(
           f'/podcasts/{self.podcast.pk}/',
           data = self.incorrect_podcast_data
       )
       self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    #######################################################################

    def test_correct_audioBook_update(self):
       response = self.client.put(
           f'/audiobooks/{self.audiobook.pk}/',
           data = self.correct_audioBook_data
       )
       self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_incorrect_audiobook_update(self):
       response = self.client.put(
           f'/audiobooks/{self.audiobook.pk}/',
           data = self.incorrect_audioBook_data
       )
       self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

#######################################################################

class GetApiTestCase(TestCase):
    """ Class used to test the GEt behaviour of the API"""

    def setUp(self):
        self.client = APIClient()
        self.song = Song.objects.create(name='foobar',duration=4)
        self.podcast = Podcast.objects.create(name='foobar',duration = 4,host = 'bar')
        self.audiobook = AudioBook.objects.create(title = 'foobar',author = 'bar', narrator = 'nono', duration = 3)
    
    def test_songs_list(self):
        response = self.client.get('/songs/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_podcasts_list(self):
        response = self.client.get('/podcasts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_audiobooks_list(self):
        response = self.client.get('/audiobooks/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

#######################################################################

class DeleteApiTestCase(TestCase):
    """ Class used to test the Delete behaviour of the API"""

    def setUp(self):
        self.client = APIClient()
        self.song = Song.objects.create(name='foobar',duration=4)
        self.podcast = Podcast.objects.create(name='foobar',duration = 4,host = 'bar')
        self.audiobook = AudioBook.objects.create(title = 'foobar',author = 'bar', narrator = 'nono', duration = 3)
    
    def test_song_delete_api(self):
        response = self.client.delete(f'/songs/{self.song.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Song.objects.count(), 0)
    
    def test_podcast_delete_api(self):
        response = self.client.delete(f'/podcasts/{self.podcast.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Podcast.objects.count(), 0)
    
    def test_podcast_delete_api(self):
        response = self.client.delete(f'/audiobooks/{self.audiobook.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(AudioBook.objects.count(), 0)