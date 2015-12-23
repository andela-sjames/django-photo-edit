'''Script used to test filter effects. '''

from django.core.urlresolvers import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from django.http import Http404

from photoapp.tests.test_view import UserSetupTestCase
from photoapp.views import PhotoAppView, DeletePhotoView, PillowImageView
from photoapp.models import Photo


class FilterPhotoTestCase(UserSetupTestCase):

    def test_effect_brightness_applied(self):

        # test File  Uploaded
        image = SimpleUploadedFile(self.file.name,
                                   self.file.read(),
                                   content_type="image")
        request = self.factory.post(
            '/photoapp/photos/',
            {'title': 'test',
             'image': image},
            enctype="multipart/form-data")
        request.user = self.user1
        response = PhotoAppView.as_view()(request)
        self.assertEquals(response.status_code, 200)

        photo = Photo.objects.get(id=2)

        # test effects applied to images
        data1 = {'image': photo.image.path, 'effect': 'brightness'}
        request = self.factory.get(reverse('addeffects'), data1)
        request.user = self.user1
        response = PillowImageView.as_view()(request)
        self.assertEquals(response.status_code, 200)

        data3 = {'image': photo.image.path, 'effect': 'grayscale'}
        request = self.factory.get(reverse('addeffects'), data3)
        request.user = self.user1
        response = PillowImageView.as_view()(request)
        self.assertEquals(response.status_code, 200)

        data4 = {'image': photo.image.path, 'effect': 'blackwhite'}
        request = self.factory.get(reverse('addeffects'), data4)
        request.user = self.user1
        response = PillowImageView.as_view()(request)
        self.assertEquals(response.status_code, 200)

        data5 = {'image': photo.image.path, 'effect': 'sepia'}
        request = self.factory.get(reverse('addeffects'), data5)
        request.user = self.user1
        response = PillowImageView.as_view()(request)
        self.assertEquals(response.status_code, 200)

        data6 = {'image': photo.image.path, 'effect': 'contrast'}
        request = self.factory.get(reverse('addeffects'), data6)
        request.user = self.user1
        response = PillowImageView.as_view()(request)
        self.assertEquals(response.status_code, 200)

        data7 = {'image': photo.image.path, 'effect': 'blur'}
        request = self.factory.get(reverse('addeffects'), data7)
        request.user = self.user1
        response = PillowImageView.as_view()(request)
        self.assertEquals(response.status_code, 200)

        data8 = {'image': photo.image.path, 'effect': 'findedges'}
        request = self.factory.get(reverse('addeffects'), data8)
        request.user = self.user1
        response = PillowImageView.as_view()(request)
        self.assertEquals(response.status_code, 200)

        data9 = {'image': photo.image.path, 'effect': 'bigenhance'}
        request = self.factory.get(reverse('addeffects'), data9)
        request.user = self.user1
        response = PillowImageView.as_view()(request)
        self.assertEquals(response.status_code, 200)

        data10 = {'image': photo.image.path, 'effect': 'enhance'}
        request = self.factory.get(reverse('addeffects'), data10)
        request.user = self.user1
        response = PillowImageView.as_view()(request)
        self.assertEquals(response.status_code, 200)

        data11 = {'image': photo.image.path, 'effect': 'smooth'}
        request = self.factory.get(reverse('addeffects'), data11)
        request.user = self.user1
        response = PillowImageView.as_view()(request)
        self.assertEquals(response.status_code, 200)

        data13 = {'image': photo.image.path, 'effect': 'emboss'}
        request = self.factory.get(reverse('addeffects'), data13)
        request.user = self.user1
        response = PillowImageView.as_view()(request)
        self.assertEquals(response.status_code, 200)

        data14 = {'image': photo.image.path, 'effect': 'contour'}
        request = self.factory.get(reverse('addeffects'), data14)
        request.user = self.user1
        response = PillowImageView.as_view()(request)
        self.assertEquals(response.status_code, 200)

        data15 = {'image': photo.image.path, 'effect': 'sharpen'}
        request = self.factory.get(reverse('addeffects'), data15)
        request.user = self.user1
        response = PillowImageView.as_view()(request)
        self.assertEquals(response.status_code, 200)

        # test photo deleted from datasse and python path
        delete_data = {'path': photo.image.path, 'id': 2}
        request = self.factory.get(reverse('delete'), delete_data)
        request.user = self.user1
        view = DeletePhotoView.as_view()
        response = view(request)
        self.assertEquals(response.status_code, 200)

        # test error handled if photo not found
        delete_data = {'path': photo.image.path, 'id': 4}
        request = self.factory.get(reverse('delete'), delete_data)
        request.user = self.user1
        view = DeletePhotoView.as_view()
        self.assertRaises(Http404, view, request, id=24)
