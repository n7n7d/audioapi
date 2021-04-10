from django.test import TestCase
from audioFile.models import Song, AudioBook, Podcast
from django.utils.timezone import now

class SongModelTest(TestCase):
    """ This classes tests the Song Model"""
    @classmethod
    def setUpTestData(cls):
        Song.objects.create(name = 'foobar', duration = 4)
    
    def test_name_label(self):
        song = Song.objects.get(id=1)
        field_label = song._meta.get_field('name').verbose_name
        self.assertEqual(field_label,'name')
    
    def test_name_max_length(self):
        song = Song.objects.get(id=1)
        max_length = song._meta.get_field('name').max_length
        self.assertEqual(max_length,100)
    
    def test_object_name_is_name(self):
        song = Song.objects.get(id=1)
        expected_object_name = f'{song.name}'
        self.assertEqual(expected_object_name,str(song))
    
    def test_duration_label(self):
        song = Song.objects.get(id=1)
        field_label = song._meta.get_field('duration').verbose_name
        self.assertEqual(field_label,'duration')
    
    def test_uploaded_time_label(self):
        song = Song.objects.get(id=1)
        field_label = song._meta.get_field('uploaded_time').verbose_name
        self.assertEqual(field_label,'uploaded time')
    
    def test_uploaded_time_is_not_past(self):
        song = Song.objects.get(id=1)
        uploded_time = song.uploaded_time
        self.assertLess(uploded_time, now())


class PodcastModelTest(TestCase):
    """ This classes tests the Podcast Model"""

    @classmethod
    def setUpTestData(cls):
        Podcast.objects.create(name = 'foobar', duration = 4,host ='bar',participants = ["foo","bar"])
    
    def test_name_label(self):
        podcast = Podcast.objects.get(id=1)
        field_label = podcast._meta.get_field('name').verbose_name
        self.assertEqual(field_label,'name')
    
    def test_name_max_length(self):
        podcast = Podcast.objects.get(id=1)
        max_length = podcast._meta.get_field('name').max_length
        self.assertEqual(max_length,100)
    
    def test_object_name_is_name(self):
        podcast = Podcast.objects.get(id=1)
        expected_object_name = f'{podcast.name}'
        self.assertEqual(expected_object_name,str(podcast))
    
    def test_duration_label(self):
        podcast = Podcast.objects.get(id=1)
        field_label = podcast._meta.get_field('duration').verbose_name
        self.assertEqual(field_label,'duration')
    
    def test_uploaded_time_label(self):
        podcast = Podcast.objects.get(id=1)
        field_label = podcast._meta.get_field('uploaded_time').verbose_name
        self.assertEqual(field_label,'uploaded time')
    
    def test_uploaded_time_is_not_past(self):
        podcast = Podcast.objects.get(id=1)
        uploded_time = podcast.uploaded_time
        self.assertLess(uploded_time, now())
    
    def test_host_label(self):
        podcast = Podcast.objects.get(id=1)
        field_label = podcast._meta.get_field('host').verbose_name
        self.assertEqual(field_label,'host')
    
    def test_participants_label(self):
        podcast = Podcast.objects.get(id=1)
        field_label = podcast._meta.get_field('participants').verbose_name
        self.assertEqual(field_label,'participants')


class AudioBookModelTest(TestCase):
    """ This classes tests the AudioBook Model"""

    @classmethod
    def setUpTestData(cls):
        AudioBook.objects.create(title = 'foobar', author = 'foo', narrator = 'bar', duration = 4)
    
    def test_name_label(self):
        audiobook = AudioBook.objects.get(id=1)
        field_label = audiobook._meta.get_field('title').verbose_name
        self.assertEqual(field_label,'title')
    
    def test_name_max_length(self):
        audiobook = AudioBook.objects.get(id=1)
        max_length = audiobook._meta.get_field('title').max_length
        self.assertEqual(max_length,100)
    
    def test_object_name_is_title(self):
        audiobook = AudioBook.objects.get(id=1)
        expected_object_name = f'{audiobook.title}'
        self.assertEqual(expected_object_name,str(audiobook))
    
    def test_duration_label(self):
        audiobook = AudioBook.objects.get(id=1)
        field_label = audiobook._meta.get_field('duration').verbose_name
        self.assertEqual(field_label,'duration')
    
    def test_uploaded_time_label(self):
        audiobook = AudioBook.objects.get(id=1)
        field_label = audiobook._meta.get_field('uploaded_time').verbose_name
        self.assertEqual(field_label,'uploaded time')
    
    def test_uploaded_time_is_not_past(self):
        audiobook = AudioBook.objects.get(id=1)
        uploded_time = audiobook.uploaded_time
        self.assertLess(uploded_time, now())
    
    def test_author_label(self):
        audiobook = AudioBook.objects.get(id=1)
        field_label = audiobook._meta.get_field('author').verbose_name
        self.assertEqual(field_label,'author')
    
    def test_author_max_length(self):
        audiobook = AudioBook.objects.get(id=1)
        max_length = audiobook._meta.get_field('author').max_length
        self.assertEqual(max_length,100)
    
    def test_narrator_label(self):
        audiobook = AudioBook.objects.get(id=1)
        field_label = audiobook._meta.get_field('narrator').verbose_name
        self.assertEqual(field_label,'narrator')
    
    def test_narrator_max_length(self):
        audiobook = AudioBook.objects.get(id=1)
        max_length = audiobook._meta.get_field('narrator').max_length
        self.assertEqual(max_length,100)