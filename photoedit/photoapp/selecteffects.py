import os
from PIL import Image, ImageFilter, ImageEnhance


def make_linear_ramp(white):
    ramp = []
    r, g, b = white
    for i in range(255):
        ramp.extend((r * i / 255, g * i / 255, b * i / 255))
    return ramp


class Applyeffects(object):

    def __init__(self, pilimage):

        self.pilimage = pilimage

    def effect(self, effect):

        filepath, ext = os.path.splitext(self.pilimage)
        edit_path = filepath + 'edited' + ext

        if effect == 'brightness':

            img = Image.open(self.pilimage)
            enh = ImageEnhance.Brightness(img)
            img = enh.enhance(1.8)
            img.save(edit_path, format='PNG', quality=100)

        if effect == 'sharpness':

            img = Image.open(self.pilimage)
            enh = ImageEnhance.Sharpness(img)
            img = enh.enhance(2.5)
            img.save(edit_path, format='PNG', quality=100)

        if effect == 'grayscale':

            img = Image.open(self.pilimage).convert('L')
            img.save(edit_path, format='PNG', quality=100)

        if effect == 'blackwhite':

            img = Image.open(self.pilimage).convert('1')
            img.save(edit_path, format='PNG', quality=100)

        if effect == 'sepia':

            serpia = make_linear_ramp((255, 240, 192))
            img = Image.open(self.pilimage).convert('L')
            img.putpalette(serpia)
            img.save(edit_path, format='PNG', quality=100)

        if effect == 'contrast':

            img = Image.open(self.pilimage)
            enh = ImageEnhance.Contrast(img)
            img = enh.enhance(2.0)
            img.save(edit_path, format='PNG', quality=100)

        # Filters here
        if effect == 'blur':

            img = Image.open(self.pilimage)
            img = img.filter(ImageFilter.BLUR)
            img.save(edit_path, format='PNG', quality=100)

        if effect == 'findedges':

            img = Image.open(self.pilimage)
            img = img.filter(ImageFilter.FIND_EDGES)
            img.save(edit_path, format='PNG', quality=100)

        if effect == 'bigenhance':

            img = Image.open(self.pilimage)
            img = img.filter(ImageFilter.EDGE_ENHANCE_MORE)
            img.save(edit_path, format='PNG', quality=100)

        if effect == 'enhance':

            img = Image.open(self.pilimage)
            img = img.filter(ImageFilter.EDGE_ENHANCE)
            img.save(edit_path, format='PNG', quality=100)

        if effect == 'smooth':

            img = Image.open(self.pilimage)
            img = img.filter(ImageFilter.SMOOTH_MORE)
            img.save(edit_path, format='PNG', quality=100)

        if effect == 'emboss':

            img = Image.open(self.pilimage)
            img = img.filter(ImageFilter.EMBOSS)
            img.save(edit_path, format='PNG', quality=100)

        if effect == 'contour':

            img = Image.open(self.pilimage)
            img = img.filter(ImageFilter.CONTOUR)
            img.save(edit_path, format='PNG', quality=100)

        if effect == 'sharpen':

            img = Image.open(self.pilimage)
            img = img.filter(ImageFilter.SHARPEN)
            img.save(edit_path, format='PNG', quality=100)
