from django import forms
from app1.models import *

class EventForm(forms.ModelForm):
    class Meta:
        model = Events
        fields = ['image', 'year', 'description']


class NotesForm(forms.ModelForm):
    class Meta :
        model = notes
        fields = ['std','subject','chaptername','notesFile']