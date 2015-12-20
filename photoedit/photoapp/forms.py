from django import forms
from photoapp.models import Photo


class PhotoForm(forms.ModelForm):
    ''' Form class defined to represent Photo model.'''
    class Meta:
        model = Photo
        fields = ('title', 'user', 'image')
