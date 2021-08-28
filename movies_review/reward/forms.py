from django import forms
from django.db import models
from django.db.models import fields
from django.forms import ModelForm, widgets
from .models import Artist, Award, Movie, Rating
from django import forms

class DateInput(forms.DateInput):
    input_type='date'

class ArtistForm(ModelForm):
    class Meta:
        model = Artist
        fields = '__all__'
        widgets={
            'dob':DateInput()
        }

class AwardForm(ModelForm):
    class Meta:
        model = Award
        fields = '__all__'
        widgets={
            'date':DateInput()
        }

class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'
        widgets={
            'release_date':DateInput()
        }


class RatingForm(ModelForm):
    class Meta:
        model = Rating
        exclude=['votes']
    
class SearchForm(ModelForm):
   class Meta:
     model = Movie
     fields = [ 'name']