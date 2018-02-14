#!/usr/bin/python3
"""
City test suite: contains unittest test cases for City models
"""

import unittest
from datetime import datetime
from models.city import City
from models.base_model import BaseModel


class TestCityModel(unittest.TestCase):

    """
    TestCityModel: unittest test cases for City models
    """

    def test_City_inherits_from_BaseModel(self):
        """tests that City models inherit from BaseModel"""
        cali = City()
        self.assertEqual(issubclass(type(cali), BaseModel), True)

    def test_City_has_name_attr(self):
        """tests that City instances has a name class attribute"""
        self.assertEqual('name' in City.__dict__, True)

    def test_City_has_created_at_attribute(self):
        """tests that City has created_at attribute from BaseModel"""
        cali = City()
        self.assertEqual(type(cali.created_at) is datetime, True)

    def test_City_has_updated_at_attribute(self):
        """tests that City has updated_at attribute from BaseModel"""
        cali = City()
        self.assertEqual(type(cali.updated_at) is datetime, True)

    def test_City_has_id_attribute(self):
        """tests that City has created_at attribute from BaseModel"""
        cali = City()
        self.assertEqual(type(cali.id) is str, True)

    def test_City_has_state_id_attribute(self):
        """tests that City has state_id attribute"""
        phoenix = City()
        self.assertEqual(type(phoenix.state_id) is str, True)
