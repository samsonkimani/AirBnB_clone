#!/usr/bin/env python3
"""model - user test case"""
from tests.test_models.test_base_model import TestBaseModel
from models.user import User


class TestUser(TestBaseModel):
    """testing the user model"""

    def __init__(self, *args, **kwargs):
        """ the init function """

        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """  testing if the first name is a string"""
        User = self.value()
        self.assertEqual(type(User.first_name), str)

    def test_last_name(self):
        """testing whether the last name is a string"""
        user = self.value()
        self.assertEqual(type(user.last_name), str)

    def test_email(self):
        """testing if the email is a string"""
        user = self.value()
        self.assertEqual(type(user.email), str)

    def test_password(self):
        """testing if the password is a string """
        user = self.value()
        self.assertEqual(type(user.password), str)
