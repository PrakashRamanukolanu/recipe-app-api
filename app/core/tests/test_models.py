from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_user_creation_with_email(self):
        email = "test@example.com"
        password = "testpass123"

        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        sample_emails = [
            ["test1@EXAMPLE.COM", "test1@example.com"],
            ["Test2@example.com", "Test2@example.com"],
            ["TEST3@EXAMPLE.COM", "TEST3@example.com"],
        ]
        for email, expected_email in sample_emails:
            user = get_user_model().objects.create_user(
                email,
                password='test123'
            )
            self.assertEqual(user.email, expected_email)

    def test_superuser_creation(self):
        user = get_user_model().objects.create_superuser(
            email="supertest@email.com",
            password='test123'
        )
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
