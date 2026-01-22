from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()


class UserManagerTests(TestCase):
    '''
    Test cases for the custom UserManager.
    '''

    def test_create_superuser(self):
        '''
        Test that a superuser is created with the correct attributes.
        '''
        
        admin = User.objects.create_superuser(
            email="admin@example.com",
            password="adminpass123"
        )

        self.assertTrue(admin.is_staff)
        self.assertTrue(admin.is_superuser)
        self.assertTrue(admin.is_active)
        
    def test_create_user_without_email_raises_error(self):
        '''
        Test that creating a user without an email raises a ValueError.
        '''
        
        with self.assertRaises(ValueError):
            User.objects.create_user(
                email="",
                password="testpass123"
            )
    
    def test_create_superuser_without_is_staff_raises_error(self):
        '''
        Test that creating a superuser without is_staff=True raises a ValueError.
        '''
        
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                email="test@example.com",
                password="testpass123",
                is_staff=False
            )
            
    def test_create_superuser_without_is_superuser_raises_error(self):
        '''
        Test that creating a superuser without is_superuser=True raises a ValueError.
        '''
        
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                email="test@example.com",
                password="testpass123",
                is_superuser=False
            )
            
    def test_create_user_without_password_raises_error(self):
        '''
        Test that creating a user without a password raises a ValueError.
        '''
        
        with self.assertRaises(ValueError):
            User.objects.create_user(
                email="test@example.com",
                password=""
            )
    
    def test_create_user_without_email_normalizes_email(self):
        '''
        Test that the email is normalized (lowercased) when creating a user.
        '''
        
        email = "test@Example.com"
        expectation = "test@example.com"
        user = User.objects.create_user(
            email=email,
            password="testpass123"
        )
        self.assertEqual(user.email, expectation)
    
    def test_create_superuser_without_email_normalizes_email(self):
        '''
        Test that the email is normalized (lowercased) when creating a superuser.
        '''
        
        email = "test@Example.com"
        expectation = "test@example.com"
        admin = User.objects.create_superuser(
            email=email,
            password="adminpass123"
        )
        self.assertEqual(admin.email, expectation)
    
    def test_create_user_trims_whitespace_in_email(self):
        '''
        Test that leading and trailing whitespace is trimmed from the email when creating a user.
        '''
        
        email = "test@example.com"
        user = User.objects.create_user(
            email=f"  {email}  ",
            password="testpass123"
        )
        self.assertEqual(user.email, email)
    
    def test_create_superuser_trims_whitespace_in_email(self):
        '''
        Test that leading and trailing whitespace is trimmed from the email when creating a superuser.
        '''
        
        email = "test@example.com"
        admin = User.objects.create_superuser(
            email=f"  {email}  ",
            password="adminpass123"
        )
        self.assertEqual(admin.email, email)
