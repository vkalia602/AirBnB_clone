#!/usr/bin/python3

"""UserModel test suite"""
import unittest
import datetime
from models.user import User
from models.base_model import BaseModel


class TestUserModel(unittest.TestCase):
    """UserModel unit tests"""

    def test_User_inherits_from_BaseModel(self):
        """tests that User inherits from BaseModel"""
        user = User()
        self.assertEqual(issubclass(user.__class__, BaseModel), True)

    def test_User_has_email_attr(self):
        """tests that User.email exists"""
        user = User()
        self.assertEqual('email' in user.__dict__, True)

    def test_email_is_a_string(self):
        """tests that User.email is a string"""
        user = User()
        self.assertEqual(type(user.email), str)

    def test_User_has_password_attr(self):
        """tests that User.password exists"""
        user = User()
        self.assertEqual('password' in user.__dict__, True)

    def test_password_is_a_string(self):
        """tests that User.password is a string"""
        user = User()
        self.assertEqual(type(user.password), str)

    def test_User_has_first_name_attr(self):
        """tests that User.first_name exists"""
        user = User()
        self.assertEqual('first_name' in user.__dict__, True)

    def test_first_name_is_a_string(self):
        """tests that User.first_name is a string"""
        user = User()
        self.assertEqual(type(user.first_name), str)

    def test_User_has_last_name_attr(self):
        """tests that User.last_name exists"""
        user = User()
        self.assertEqual('last_name' in user.__dict__, True)

    def test_last_name_is_a_string(self):
        """tests that User.last_name is a string"""
        user = User()
        self.assertEqual(type(user.last_name), str)

    def test_User_has_id_attr(self):
        """tests that user has id inherited from BaseModel"""
        user = User()
        self.assertEqual(type(user.id), str)

    def test_User_has_created_at_attr(self):
        """tests that user has created_at attr from BaseModel"""
        user = User()
        self.assertEqual(type(user.created_at), datetime.datetime)

    def test_User_has_update_at_attr(self):
        """tests that user has updated_at attr from BaseModel"""
        user = User()
        self.assertEqual(type(user.updated_at), datetime.datetime)

    def test_User_has_to_dict_method(self):
        """tests that user has to_dict() inherited from BaseModel"""
        user = User()
        self.assertEqual('to_dict' in dir(user), True)
