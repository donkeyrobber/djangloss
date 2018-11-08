from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse_lazy

# Create your tests here.

class HomepageTest(TestCase):

    fixtures = ['users.json']

    def test_homepage_redirects_if_unauthenticated(self):
        response = self.client.get(reverse_lazy('home'))
        self.assertEqual(response.status_code, 302)

    def test_homepage_displays_if_authenticated(self):
        self.client.login(username="testuser_1", password='testuser_1_pw')
        response = self.client.get(reverse_lazy('home'))
        self.assertEqual(response.status_code, 200)

    def test_nav_content_does_not_display_if_unauthenticated(self):
        response = self.client.get(reverse_lazy('home'), follow=True)
        self.assertNotContains(response,'<ul class="navbar-nav mr-auto">')

    def test_nav_content_displays_if_authenticated(self):
        self.client.login(username="testuser_1", password='testuser_1_pw')
        response = self.client.get(reverse_lazy('home'), follow=True)
        self.assertContains(response,'<ul class="navbar-nav mr-auto">')
