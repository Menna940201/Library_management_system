from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class AuthFlowTests(TestCase):
    def test_login_redirects_to_book_list_for_valid_user(self):
        user = get_user_model().objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='StrongPass123',
        )

        response = self.client.post(
            reverse('login'),
            {'username': 'testuser', 'password': 'StrongPass123'},
            follow=True,
        )

        self.assertTrue(response.wsgi_request.user.is_authenticated)
        self.assertRedirects(response, reverse('book_list'))

    def test_logout_clears_authenticated_session(self):
        user = get_user_model().objects.create_user(
            username='logoutuser',
            email='logoutuser@example.com',
            password='StrongPass123',
        )

        self.client.login(username='logoutuser', password='StrongPass123')
        response = self.client.post(reverse('logout'))

        self.assertRedirects(response, reverse('login'))
        self.assertFalse('_auth_user_id' in self.client.session)
