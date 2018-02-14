#!/usr/bin/python3
"""
State test suite: contains unittest test cases for State models
"""

import unittest
from datetime import datetime
from models.state import State
from models.base_model import BaseModel


class TestStateModel(unittest.TestCase):

    """
    TestStateModel: unittest test cases for State models
    """

    def test_State_inherits_from_BaseModel(self):
        """tests that State models inherit from BaseModel"""
        cali = State()
        self.assertEqual(issubclass(type(cali), BaseModel), True)

    def test_State_has_name_attr(self):
        """tests that State instances has a name class attribute"""
        self.assertEqual('name' in State.__dict__, True)

    def test_State_has_created_at_attribute(self):
        """tests that State has created_at attribute from BaseModel"""
        cali = State()
        self.assertEqual(type(cali.created_at) is datetime, True)

    def test_State_has_updated_at_attribute(self):
        """tests that State has updated_at attribute from BaseModel"""
        cali = State()
        self.assertEqual(type(cali.updated_at) is datetime, True)

    def test_State_has_id_attribute(self):
        """tests that State has created_at attribute from BaseModel"""
        cali = State()
        self.assertEqual(type(cali.id) is str, True)
