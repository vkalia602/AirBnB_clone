#!/usr/bin/python3
"""
Amenity test suite: contains unittest test cases for Amenity models
"""

import unittest
from datetime import datetime
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenityModel(unittest.TestCase):

    """
    TestAmenityModel: unittest test cases for Amenity models
    """

    def test_Amenity_inherits_from_BaseModel(self):
        """tests that Amenity models inherit from BaseModel"""
        cali = Amenity()
        self.assertEqual(issubclass(type(cali), BaseModel), True)

    def test_Amenity_has_name_attr(self):
        """tests that Amenity instances has a name class attribute"""
        self.assertEqual('name' in Amenity.__dict__, True)

    def test_Amenity_has_created_at_attribute(self):
        """tests that Amenity has created_at attribute from BaseModel"""
        cali = Amenity()
        self.assertEqual(type(cali.created_at) is datetime, True)

    def test_Amenity_has_updated_at_attribute(self):
        """tests that Amenity has updated_at attribute from BaseModel"""
        cali = Amenity()
        self.assertEqual(type(cali.updated_at) is datetime, True)

    def test_Amenity_has_id_attribute(self):
        """tests that Amenity has created_at attribute from BaseModel"""
        cali = Amenity()
        self.assertEqual(type(cali.id) is str, True)
