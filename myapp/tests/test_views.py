from django.urls import reverse
from django.test import TestCase, Client
from ..models import Students
import json


class TestViews(TestCase):

    def test_students_GET(self):
        client = Client()

        response = client.get(reverse('resume'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'resume.html')

