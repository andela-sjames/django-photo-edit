import os

from django.conf import settings
from django.views.generic.base import TemplateView
from django.http import HttpResponse

from photoapp.views import LoginRequiredMixin
from photoapp.selecteffects import Applyeffects


class PillowImageView(TemplateView, LoginRequiredMixin):

    ''' Class defined to apply effect to image.'''

    def get(self, request, *args, **kwargs):

        pilimage = str(request.GET.get('image'))
        effect = request.GET.get('effect')

        filepath, ext = os.path.splitext(pilimage)
        edit_path = filepath + 'edited' + ext

        image_effects = Applyeffects(pilimage)
        image_effects.effect(effect)

        return HttpResponse(os.path.relpath(edit_path, settings.BASE_DIR),
                            content_type="text/plain")
