from django import forms
from app1.models import Events

class EventForm(forms.ModelForm):
    class Meta:
        model = Events
        fields = ['image', 'year', 'description']
