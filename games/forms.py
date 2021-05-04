from django import forms
from .models import Game


class SearchForm(forms.Form):
    query = forms.CharField()


class GameCreationForm(forms.ModelForm):
    image = forms.ImageField()

    class Meta:
        model = Game
        fields = ('category', 'title', 'image', 'description', 'year')
