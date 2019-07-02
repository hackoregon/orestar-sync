from django.test import TestCase, SimpleTestCase, TransactionTestCase
from ..api import models
from rest_framework.test import APIClient, RequestsClient


# Django, Writing and Running Unit Tests: https://docs.djangoproject.com/en/2.0/topics/testing/overview/
# Django, Automated Unit Testing Tutorial: https://docs.djangoproject.com/en/2.0/intro/tutorial05/


class RootEndpointsTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
    
    def test_list_200_response(self):
        response = self.client.get('/local-elections/')
        assert response.status_code == 200
