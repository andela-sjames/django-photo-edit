from django.test import TestCase, Client, RequestFactory
from photoapp.models import FacebookUser
from photoapp.views import FacebookLogin

from django.contrib.auth.models import User
from django.conf import settings
from django.utils.importlib import import_module


class UserCreateViewTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.factory = RequestFactory()
        self.user1 = User.objects.create(username = 'Johndoe', email='johndoe@doe.com')
        self.facebook_user1 = FacebookUser.objects.create(facebook_id=1, contrib_user=self.user1)

        self.data = {
            'first_name':'andela',
            'last_name':'andela',
            'email':'email@email.com',
            'id':2,
            'picture[data][url]': 'https://fbkamaihd.net/hprofile'
        }

    def test_non_existing_user_login(self):

        request = self.factory.post('/photo/login/',self.data)
        engine = import_module(settings.SESSION_ENGINE)
        session_key = None
        request.session = engine.SessionStore(session_key)
        
        #assert that user loggedIn successfully
        response = FacebookLogin.as_view()(request)
        self.assertEquals(response.status_code, 200)

    def test_model_creation(self):

        #assert that user does not exist in the database
        facebook_user2 = FacebookUser.objects.filter(id=2)
        self.assertEqual(len(facebook_user2), 0)

        #assert that user was successfully created and saved in db
        user2 = User.objects.create(username = self.data['first_name'], email=self.data['email'])
        facebook_user2 = FacebookUser.objects.create(facebook_id=self.data['id'], contrib_user=user2)
        facebook_user2 = FacebookUser.objects.filter(id=2)
        self.assertEqual(len(facebook_user2), 1)
