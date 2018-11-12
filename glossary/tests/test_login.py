from django.test import TestCase
from django.urls import reverse

# Create your tests here.

class HomepageTest(TestCase):

    fixtures = ['users.json']

    TEST_USERNAME = "testuser_1"
    TEST_PASSWORD = "testuser_1_pw"

    def test_login_redirects_if_authenticated(self):
        self.client.login(username=self.TEST_USERNAME, password=self.TEST_PASSWORD)
        response = self.client.get(reverse('login'))
        self.assertEquals(response.status_code, 302)

    def test_nav_content_does_not_display_if_unauthenticated(self):
        response = self.client.get(reverse('login'))
        self.assertNotContains(response,'<ul class="navbar-nav mr-auto">')

    def test_login_form_displays_if_unauthenticated(self):
        response = self.client.get(reverse('login'))
        self.assertContains(response, '<input type="text" name="username"')
        self.assertContains(response, '<input type="password" name="password"')
        self.assertContains(response, '<button type="submit">Login</button>')