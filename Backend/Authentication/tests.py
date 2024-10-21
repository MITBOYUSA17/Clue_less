from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User
from django.urls import reverse
# Create your tests here.
class RegisterViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.register_url = reverse('register')

    def test_get_csrf_token(self):
        """
        Test if the GET request returns a valid CSRF token.
        """
        response = self.client.get(self.register_url)
        csrf_token = response.json().get('csrfToken')
        
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(csrf_token)

    def test_valid_registration(self):
        user_data = {
            'username': 'testuser',
            'password1': 'elemental',
            'password2': 'elemental',
        }
        response = self.client.post(self.register_url, data=user_data)

        message = response.json().get('message')
        user_exists = User.objects.filter(username='testuser').exists()

        self.assertEqual(response.status_code, 201)
        self.assertEqual(message, 'User created successfully')
        self.assertTrue(user_exists)

    def test_invalid_registration(self):
        invalid_data = {
            'username': '',  # Missing username
            'password1': 'elemental12345',
            'password2': 'elemental123',
        }
        response = self.client.post(self.register_url, data=invalid_data)

        errors = response.json().get('errors')

        self.assertEqual(response.status_code, 400)
        self.assertIn('username', errors)
        self.assertIn('password2', errors)
    
    def test_invalid_registration_common_pass(self):
        invalid_data = {
        'username': 'john3',  # Missing username
        'password1': 'password',
        'password2': 'password',
        }
        response = self.client.post(self.register_url, data=invalid_data)

        # Extract errors from the response
        errors = response.json().get('errors')

        # Error Response reported
        self.assertEqual(response.status_code, 400)

        # Error message shows that the password is too common
        self.assertIn('password2', errors)
        self.assertIn('This password is too common.', errors['password2'])


class LoginViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.login_url = reverse('login')
        self.user = User.objects.create_user(username='testuser', password='password12345')

    def test_valid_login(self):
        login_data = {
            'username': 'testuser',
            'password': 'password12345',
        }
        response = self.client.post(self.login_url, data=login_data)

        message = response.json().get('message')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(message, 'Logged in successfully')

    def test_invalid_login(self):
        invalid_data = {
            'username': 'wronguser',
            'password': 'wrongpassword',
        }
        response = self.client.post(self.login_url, data=invalid_data)

        error_message = response.json().get('error')

        self.assertEqual(response.status_code, 403)
        self.assertEqual(error_message, 'Invalid credentials')


class LogoutViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.logout_url = reverse('logout')
        self.user = User.objects.create_user(username='testuser', password='password12345')

    def test_logout(self):
        """
        Test if a logged-in user can log out successfully.
        """
        # Log the user in first
        self.client.login(username='testuser', password='password12345')

        # Call the logout view
        response = self.client.post(self.logout_url)

        message = response.json().get('message')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(message, 'Logged out successfully')

    def test_logout_without_login(self):
        response = self.client.post(self.logout_url)

        message = response.json().get('message')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(message, 'Logged out successfully')