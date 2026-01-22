from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()


class UserModelTests(TestCase):
    '''
    Test cases for the custom User model.
    '''

    def test_create_user_with_email(self):
        '''
        Test that the email is set correctly and the password is hashed.
        1. Create a user with a specific email and password.
        2. Verify that the email is stored correctly.
        3. Verify that the password is hashed and can be checked.
        '''
        
        user = User.objects.create_user(
            email="test@example.com",
            password="testpass123"
        )

        # Check data
        self.assertEqual(user.email, "test@example.com")

        # Password should be hashed
        self.assertNotEqual(user.password, "testpass123")
        self.assertTrue(user.check_password("testpass123"))
