from django import forms

class HighscoreForm(forms.Form):
    name = forms.CharField(max_length=255)
    score = forms.IntegerField()

    