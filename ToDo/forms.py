from django import forms
from .models import *
from django.forms import ModelForm

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'dates']
        labels = {'title' : 'Title', 'dates' : 'Dates'}
        widgets = {
            'dates' : forms.DateInput(attrs={'class': 'form-control',
                                        'type' : 'date'}),
            'title' : forms.TextInput(attrs={'class': 'form-control',
                                        'type' : 'text',
                                        'placeholder' : "Wat's in ur mind"})
        }
