from django.test import TestCase, SimpleTestCase, TransactionTestCase
from api import models
from rest_framework.test import APIClient, RequestsClient


# Django, Writing and Running Unit Tests: https://docs.djangoproject.com/en/2.0/topics/testing/overview/
# Django, Automated Unit Testing Tutorial: https://docs.djangoproject.com/en/2.0/intro/tutorial05/

class ExampleTestCase(TestCase):
    def setUp(self):
        pass

    def test_example(self):
        self.assertTrue(True)

class ExampleModelTestCase(TestCase):
    def setUp(self):
        pass

    def test_model(self):
        self.assertTrue(True)


# https://docs.djangoproject.com/en/2.0/topics/testing/tools/#django.test.SimpleTestCase
class ExampleSimpleTestCase(SimpleTestCase):
    def test_simple_example(self):
        self.assertTrue(True)

# https://docs.djangoproject.com/en/2.0/topics/testing/tools/#transactiontestcase
class ExampleTransactionTestCase(TransactionTestCase):
    def test_transaction_example(self):
        self.assertTrue(True)

class RootEndpointsTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
    def test_list_200_response(self):
        response = self.client.get('/local-elections/')
        assert response.status_code == 200
