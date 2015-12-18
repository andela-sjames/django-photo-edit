import os
from PIL import Image, ImageFilter, ImageEnhance

from django.conf import settings
from django.views.generic.base import TemplateView
from django.http import HttpResponse

from photoapp.views import LoginRequiredMixin


def make_linear_ramp(white):
    ramp = []
    r, g, b = white
    for i in range(255):
        ramp.extend((r * i / 255, g * i / 255, b * i / 255))
    return ramp


class PillowImageView(TemplateView, LoginRequiredMixin):

    def get(self, request, *args, **kwargs):
        pilimage = str(request.GET.get('image'))
        effect = request.GET.get('effect')

        if effect == 'brightness':

            img = Image.open(pilimage)
            enh = ImageEnhance.Brightness(img)
            img = enh.enhance(1.8)

        if effect == 'sharpness':

            img = Image.open(pilimage)
            enh = ImageEnhance.Sharpness(img)
            img = enh.enhance(2.5)

        if effect == 'grayscale':

            img = Image.open(pilimage).convert('L')

        if effect == 'blackwhite':

            img = Image.open(pilimage).convert('1')

        if effect == 'sepia':

            serpia = make_linear_ramp((255, 240, 192))
            img = Image.open(pilimage).convert('L')

            img.putpalette(serpia)

        if effect == 'contrast':

            img = Image.open(pilimage)

            enh = ImageEnhance.Contrast(img)
            img = enh.enhance(2.0)

        # Filters here
        if effect == 'blur':

            img = Image.open(pilimage)
            img = img.filter(ImageFilter.BLUR)

        if effect == 'findedges':

            img = Image.open(pilimage)
            img = img.filter(ImageFilter.FIND_EDGES)

        if effect == 'bigenhance':

            img = Image.open(pilimage)
            img = img.filter(ImageFilter.EDGE_ENHANCE_MORE)

        if effect == 'enhance':

            img = Image.open(pilimage)
            img = img.filter(ImageFilter.EDGE_ENHANCE)

        if effect == 'smooth':

            img = Image.open(pilimage)
            img = img.filter(ImageFilter.SMOOTH_MORE)

        if effect == 'emboss':

            img = Image.open(pilimage)
            img = img.filter(ImageFilter.EMBOSS)

        if effect == 'contour':

            img = Image.open(pilimage)
            img = img.filter(ImageFilter.CONTOUR)

        if effect == 'sharpen':

            img = Image.open(pilimage)
            img = img.filter(ImageFilter.SHARPEN)

        filepath, ext = os.path.splitext(pilimage)
        edit_path = filepath + 'edited' + ext
        img.save(edit_path, format='PNG', quality=100)

        return HttpResponse(os.path.relpath(edit_path, settings.BASE_DIR),
                            content_type="text/plain")
