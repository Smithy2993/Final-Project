from django.contrib.auth.models import AnonymousUser, User
from django.test import TestCase, RequestFactory

from.views import user_login, auth_view

class SimpleTest(TestCase):
        def setUp(self):
                self.factory = RequestFactory()
                self.user = User.objects.create_user(username='sc13dad', email='ddal10@hotmail.co.uk', password='password')
                

        def test_details(self):
                request = self.factory.get('/accounts/login')
                request.user = self.user
                request.user = AnonymousUser()
                response = auth_view(request)
                response = user_login.as_view(request)
                self.assertEqual(response.status_code, 200)
