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
            pilimage = str(request.GET.get('image'))

            img = Image.open(pilimage)
            enh = ImageEnhance.Contrast(img)
            out = enh.enhance(2.3)
            filepath, ext = os.path.splitext(pilimage)

            edit_path = filepath + 'edited' + ext
            # if os.path.isdir(edit_path):
            #     os.rmdir(edit_path)
            out.save(edit_path, 'png', quality=100)

        if effect == 'sharp':

            img = Image.open(pilimage)
            enh = ImageEnhance.Contrast(img)
            out = enh.enhance(1.5)
            filepath, ext = os.path.splitext(pilimage)

            edit_path = filepath + 'edited' + ext
            # if os.path.isdir(edit_path):
            #     os.rmdir(edit_path)
            out.save(edit_path, 'png', quality=100)

        if effect == 'grayscale':

            img = Image.open(pilimage).convert('L')

            filepath, ext = os.path.splitext(pilimage)
            edit_path = filepath + 'edited' + ext

            # if os.path.isdir(edit_path):
            #     os.rmdir(edit_path)

            img.save(edit_path, 'png', quality=100)

        if effect == 'blur':

            img = Image.open(pilimage)
            img = img.filter(ImageFilter.BLUR)

            filepath, ext = os.path.splitext(pilimage)
            edit_path = filepath + 'edited' + ext

            if os.path.isdir(edit_path):
                os.rmdir(edit_path)

            img.save(edit_path, 'png', quality=100)

        if effect == 'contour':

            img = Image.open(pilimage)
            img = img.filter(ImageFilter.CONTOUR)

            filepath, ext = os.path.splitext(pilimage)
            edit_path = filepath + 'edited' + ext

            # if os.path.isdir(edit_path):
            #     os.rmdir(edit_path)

            img.save(edit_path, 'png', quality=100)

        if effect == 'hue':

            img = Image.open(pilimage).convert('HSV')

            enh = ImageEnhance.Contrast(img)
            out = enh.enhance(-1.5)

            filepath, ext = os.path.splitext(pilimage)
            edit_path = filepath + 'edited' + ext

            # if os.path.isdir(edit_path):
            #     os.rmdir(edit_path)

            out.save(edit_path, 'png', quality=100)

        return HttpResponse(os.path.relpath(edit_path, settings.BASE_DIR),
                            content_type="text/plain")

