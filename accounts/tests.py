from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class SignupPageTests(TestCase):
    username = 'newuser'
    email = 'newuser@email.com'

    def test_signup_page_status_code(self):
        response = self.client.get('/accounts/signup/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/signup.html')

    def test_signup_form(self):
        new_user = get_user_model().objects.create_user(self.username, self.email)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, self.username)
        self.assertEqual(get_user_model().objects.all()[0].email, self.email)


class PasswordResetPageTests(TestCase):
    username = 'newuser'
    email = 'newuser@email.com'

    def test_password_reset_page_status_code(self):
        response = self.client.get('/accounts/password_reset/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('password_reset'))
        self.assertEqual(response.status_code, 200)

class PasswordChangePageTests(TestCase):
    username = 'newuser'
    email = 'newuser@email.com'

    def test_password_change_page_status_code_no_logon(self):
        response = self.client.get('/accounts/password_change/')
        self.assertEqual(response.status_code, 302)

    def test_view_url_by_name_no_logon(self):
        response = self.client.get(reverse('password_change'))
        self.assertEqual(response.status_code, 302)

