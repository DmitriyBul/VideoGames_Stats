from django import forms
from .models import Game, Comment


class SearchForm(forms.Form):
    query = forms.CharField()


class GameCreationForm(forms.ModelForm):
    image = forms.ImageField()

    class Meta:
        model = Game
        fields = ('category', 'title', 'image', 'description', 'year')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body', )

