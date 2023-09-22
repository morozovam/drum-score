import unittest
from django.test import TestCase, Client


class UrlTestCase(unittest.TestCase):
    client = Client()

    def test_admin_url(self):
        response = self.client.get('/admin/login/')
        self.assertEqual(response.status_code, 200)

    def test_api_auth_login_url(self):
        response = self.client.get('/api/auth/login/')
        self.assertEqual(response.status_code, 200)

    def test_api_auth_logout_url(self):
        response = self.client.get('/api/auth/logout/')
        self.assertEqual(response.status_code, 200)

    def test_api_v1_url(self):
        response = self.client.get('/api/v1/')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
