'''Script used to test filter effects. '''

from django.core.urlresolvers import reverse_lazy

from photoapp.tests.test_view import UserSetupTestCase
from photoapp.effects import PillowImageView


class FilterPhotoTestCase(UserSetupTestCase):

    def test_effects_applied(self):

        data = {'image': self.photo.image.path, 'effect': 'brigthness'}

        request = self.factory.get(reverse_lazy('addeffects'), data)
        request.user = self.user1
        response = PillowImageView.as_view()(request)
        self.assertEquals(response.status_code, 200)
