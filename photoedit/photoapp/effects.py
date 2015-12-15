import os
from PIL import Image, ImageFilter, ImageEnhance

from django.conf import settings
from django.views.generic.base import TemplateView
from django.http import HttpResponse

from photoapp.views import LoginRequiredMixin


class PillowImageView(TemplateView, LoginRequiredMixin):

    def get(self, request, *args, **kwargs):
        pilimage = str(request.GET.get('image'))
        effect = request.GET.get('effect')

        if effect == 'brightness':

            img = Image.open(pilimage)
            enh = ImageEnhance.Contrast(img)
            out = enh.enhance(2.3)
            # out = img.filter(ImageFilter.DETAIL)
            filepath, ext = os.path.splitext(pilimage)

            edit_path = filepath + 'edited' + ext
            out.save(edit_path, format='PNG')

        elif effect == 'sharp':

            img = Image.open(pilimage)
            enh = ImageEnhance.Contrast(img)
            out = enh.enhance(1.5)
            # out = img.filter(ImageFilter.DETAIL)
            filepath, ext = os.path.splitext(pilimage)

            edit_path = filepath + 'edited' + ext
            out.save(edit_path, format='PNG')

            # return response and we're done!

        return HttpResponse(os.path.relpath(edit_path, settings.BASE_DIR),
                            content_type="text/plain")
