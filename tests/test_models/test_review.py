#!/usr/bin/python3
"""
Review test suite: contains unittest test cases for Review models
"""

import unittest
from datetime import datetime
from models.review import Review
from models.base_model import BaseModel


class TestReviewModel(unittest.TestCase):

    """
    TestReviewModel: unittest test cases for Review models
    """

    def test_Review_inherits_from_BaseModel(self):
        """tests that Review models inherit from BaseModel"""
        cali = Review()
        self.assertEqual(issubclass(type(cali), BaseModel), True)

    def test_Review_has_created_at_attribute(self):
        """tests that Review has created_at attribute from BaseModel"""
        cali = Review()
        self.assertEqual(type(cali.created_at) is datetime, True)

    def test_Review_has_updated_at_attribute(self):
        """tests that Review has updated_at attribute from BaseModel"""
        cali = Review()
        self.assertEqual(type(cali.updated_at) is datetime, True)

    def test_Review_has_id_attribute(self):
        """tests that Review has created_at attribute from BaseModel"""
        cali = Review()
        self.assertEqual(type(cali.id) is str, True)

    def test_Review_has_place_id_attribute(self):
        """tests that Review has place_id attribute from BaseModel"""
        rev = Review()
        self.assertEqual(type(rev.place_id) is str, True)

    def test_Review_has_user_id_attribute(self):
        """tests that Review has user_id attribute from BaseModel"""
        rev = Review()
        self.assertEqual(type(rev.user_id) is str, True)

    def test_Review_has_text_attribute(self):
        """tests that Review has text attribute from BaseModel"""
        rev = Review()
        self.assertEqual(type(rev.text) is str, True)
