from django import forms
from photoapp.models import Photo


class PhotoForm(forms.ModelForm):

    class Meta:
        model = Photo
        fields = ('title', 'user', 'image')
