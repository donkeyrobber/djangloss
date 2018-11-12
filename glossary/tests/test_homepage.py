from django.test import TestCase
from django.urls import reverse
# Create your tests here.

class HomepageTest(TestCase):

    fixtures = ['users.json']

    TEST_USERNAME = "testuser_1"
    TEST_PASSWORD = "testuser_1_pw"

    def test_homepage_redirects_if_unauthenticated(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 302)

    def test_homepage_displays_if_authenticated(self):
        self.client.login(username=self.TEST_USERNAME, password=self.TEST_PASSWORD)
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_nav_content_does_not_display_if_unauthenticated(self):
        response = self.client.get(reverse('home'), follow=True)
        self.assertNotContains(response,'<ul class="navbar-nav mr-auto">')

    def test_nav_content_displays_if_authenticated(self):
        self.client.login(username=self.TEST_USERNAME, password=self.TEST_PASSWORD)
        response = self.client.get(reverse('home'), follow=True)
        self.assertContains(response,'<ul class="navbar-nav mr-auto">')
