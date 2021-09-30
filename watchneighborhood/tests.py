from django.test import TestCase
from . models import*
# Create your tests here.

class TestNeighbor(TestCase):
    def setUp(self):
        self.kataret = Neighborhood(name='Kataret')
        self.kataret.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.Kataret,Neighborhood))
