from django.test import TestCase
from django.contrib.admin.sites import site
from django.contrib.auth import get_user_model

# Get the custom User model
User = get_user_model()


class AdminRegistrationTests(TestCase):
    '''
    Test cases for admin registration of the custom User model.
    '''

    def test_user_is_registered_in_admin(self):
        '''
        Test that the custom User model is registered in the Django admin site.
        '''
        
        self.assertIn(User, site._registry)
