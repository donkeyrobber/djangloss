from django.test import TestCase
from django.urls import reverse


class ArticleListTest(TestCase):

    fixtures = ['users.json', 'articles.json']

    TEST_USERNAME = "testuser_1"
    TEST_PASSWORD = "testuser_1_pw"

    def test_article_list_page_redirects_if_unauthenticated(self):
        response = self.client.get(reverse('article_list'))
        self.assertEqual(response.status_code, 302)

    def test_article_list_page_contains_header(self):
        self.client.login(username=self.TEST_USERNAME,password=self.TEST_PASSWORD)
        response = self.client.get(reverse('article_list'))
        self.assertContains(response, '<h1>Articles</h1>')


    def test_article_list_page_contains_test_article(self):
        self.client.login(username=self.TEST_USERNAME,password=self.TEST_PASSWORD)
        response = self.client.get(reverse('article_list'))
        self.assertContains(response, '<td>Test Article</td>')
        self.assertContains(response, '<td>Test User</td>')