#!/usr/bin/python3
"""
Place test suite: contains unittest test cases for Place models
"""

import unittest
from datetime import datetime
from models.place import Place
from models.base_model import BaseModel


class TestPlaceModel(unittest.TestCase):

    """
    TestPlaceModel: unittest test cases for Place models
    """

    def test_Place_inherits_from_BaseModel(self):
        """tests that Place models inherit from BaseModel"""
        cali = Place()
        self.assertEqual(issubclass(type(cali), BaseModel), True)

    def test_Place_has_name_attr(self):
        """tests that Place instances has a name class attribute"""
        self.assertEqual('name' in Place.__dict__, True)

    def test_Place_has_created_at_attribute(self):
        """tests that Place has created_at attribute from BaseModel"""
        cali = Place()
        self.assertEqual(type(cali.created_at) is datetime, True)

    def test_Place_has_updated_at_attribute(self):
        """tests that Place has updated_at attribute from BaseModel"""
        cali = Place()
        self.assertEqual(type(cali.updated_at) is datetime, True)

    def test_Place_has_id_attribute(self):
        """tests that Place has created_at attribute from BaseModel"""
        cali = Place()
        self.assertEqual(type(cali.id) is str, True)

    def test_Place_has_city_id_attribute(self):
        """tests that Place has city_id attr"""
        home = Place()
        self.assertEqual(type(home.city_id) is str, True)

    def test_Place_has_user_id_attribute(self):
        """tests that Place has user_id attr"""
        home = Place()
        self.assertEqual(type(home.user_id) is str, True)

    def test_place_has_description_attribute(self):
        """tests that place has description attr"""
        home = Place()
        self.assertEqual(type(home.description) is str, True)

    def test_place_has_number_rooms_attribute(self):
        """tests that place has number_rooms attr"""
        home = Place()
        self.assertEqual(type(home.number_rooms) is int, True)

    def test_place_has_number_bathrooms_attribute(self):
        """tests that place has number_bathrooms attr"""
        home = Place()
        self.assertEqual(type(home.number_bathrooms) is int, True)

    def test_place_has_max_guest_attribute(self):
        """tests that place has max_guest attr"""
        home = Place()
        self.assertEqual(type(home.max_guest) is int, True)

    def test_place_has_price_by_night_attribute(self):
        """tests that place has price_by_night attr"""
        home = Place()
        self.assertEqual(type(home.price_by_night) is int, True)

    def test_place_has_latitude_attribute(self):
        """tests that place has latitude attr"""
        home = Place()
        self.assertEqual(type(home.latitude) is float, True)

    def test_place_has_longitude_attribute(self):
        """tests that place has longitude attr"""
        home = Place()
        self.assertEqual(type(home.longitude) is float, True)

    def test_place_has_amenity_ids_attribute(self):
        """tests that place has amenity_ids attr"""
        home = Place()
        self.assertEqual(type(home.amenity_ids) is list, True)
