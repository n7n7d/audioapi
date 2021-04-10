from django.db import models
from django.db.models.fields import CharField, DateTimeField, PositiveBigIntegerField
from django.utils.timezone import now
from django.core.exceptions import ValidationError
from django.contrib.postgres.fields import ArrayField

# Create your models here.

def date_validator(date):
    """  
    The function validates if the uploaded_time field in a model 
    is not a past date and raises a ValidationError if it is a past date
    """
    if date < now():
        raise ValidationError("Date can't be in the past")


class Song(models.Model):  
    """ This class represents the model of the Song AudioFile"""

    name = CharField(max_length=100)
    duration = PositiveBigIntegerField()
    uploaded_time = DateTimeField(auto_now_add=True, validators=[date_validator])

    def __str__(self):
        """Returns the Name of an instance"""
        return f'{self.name}'


class Podcast(models.Model):
    """ This class represents the model of the Podcast AudioFile"""

    name = CharField(max_length=100)
    duration = PositiveBigIntegerField()
    uploaded_time = DateTimeField(auto_now_add=True, validators=[date_validator])
    host = CharField(max_length=100)
    participants = ArrayField(models.CharField(max_length=100), blank = True, size=10,null = True)
    
    def __str__(self):
        """Returns the Name of an instance"""
        return f'{self.name}'

class AudioBook(models.Model):
    """ This class represents the model of the Audiobook AudioFile"""

    title = CharField(max_length=100)
    author = CharField(max_length=100)
    narrator = CharField(max_length=100)
    duration = PositiveBigIntegerField()
    uploaded_time = DateTimeField(auto_now_add=True, validators=[date_validator])

    def __str__(self):
        """Returns the title of an instance"""
        return f'{self.title}'



