from django.test import TestCase
from django.urls import reverse


class ArticleViewTest(TestCase):

    fixtures = ['users.json', 'articles.json']

    TEST_USERNAME = "testuser_1"
    TEST_PASSWORD = "testuser_1_pw"

    def test_article_view_page_redirects_if_unauthenticated(self):
        response = self.client.get(reverse('article_view', args=[1]))
        self.assertEqual(response.status_code, 302)

    def test_article_view_page_contains_nav(self):
        self.client.login(username=self.TEST_USERNAME, password=self.TEST_PASSWORD)
        response = self.client.get(reverse('article_view', args=[1]))
        self.assertContains(response,'<ul class="navbar-nav mr-auto">')

    def test_article_view_page_contains_article(self):
        self.client.login(username=self.TEST_USERNAME,password=self.TEST_PASSWORD)
        response = self.client.get(reverse('article_view', args=[1]))
        self.assertContains(response, '<h1>Test Article</h1>')
        self.assertContains(response, '<h2>Test User</h2>')