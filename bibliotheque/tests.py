
from django.test import TestCase
from django.urls import reverse
from bibliotheque.models import*




class TestViews(TestCase):
    def test_p(self):
        response = self.client.get(reverse("login"))

        self.assertTemplateUsed(response, "accounts/login.html")

    






# Create your tests here.
