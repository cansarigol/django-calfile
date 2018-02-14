from django.test import TestCase
from django.test import Client
from django.conf import settings
from .views import calfile

class ViewTestCase(TestCase):

    def test_view(self):
        response = self.client.get('/calfile/')
        self.assertEqual(response.status_code, 405, "Get not allowed")

        with self.assertRaises(KeyError):
            self.client.post('/calfile/', {'start_date': '', 'end_date': ''})
        with self.assertRaises(ValueError):
            self.client.post('/calfile/', {'start_date': 'x', 'end_date': 'y'})

        test_params = {'start_date': '1-1-2018 13:00', 'end_date': '1-1-2018 14:30'}
        settings.CALFILE_DF = "%d-%m-%Y"

        with self.assertRaises(ValueError):
             self.client.post('/calfile/', test_params)

        settings.CALFILE_DF = "%d-%m-%Y %H:%M"
        response = self.client.post('/calfile/', test_params)
        self.assertEqual(response.status_code, 200, "Post error")