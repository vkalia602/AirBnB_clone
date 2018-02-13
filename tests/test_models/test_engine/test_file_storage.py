#!/usr/bin/python3

"""FileStorage test suite"""
import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """FileStorage unit tests"""

    def tearDown(self):
        """removes file.json after tests"""
        if os.path.isfile('file.json'):
            os.remove('file.json')

    def test___file_path_attr_exists(self):
        """tests that __file_path attr is set at init
        (using file.json as an example)
        attr name will be mangled because its 'private'"""
        f = FileStorage()
        self.assertEqual(f._FileStorage__file_path, 'file.json')

    def test___file_path_is_a_string(self):
        """tests that __file_path attr is a string"""
        f = FileStorage()
        self.assertEqual(type(f._FileStorage__file_path), str)

    def test___objects_attr_exists(self):
        """tests that __objects attr is set at init. it should be
        an empty dict if there is nothing in file.json or that file
        doesn't exit"""
        f = FileStorage()
        self.assertNotEqual(f._FileStorage__objects, None)

    def test___objects_is_a_dict(self):
        """tests that __objects is a dict"""
        f = FileStorage()
        self.assertEqual(type(f._FileStorage__objects), dict)

    def test_all_method_returns___objects_dict(self):
        """tests that all() returns __objects"""
        f = FileStorage()
        d = f.all()
        self.assertEqual(f._FileStorage__objects, d)

    def test_save_method_serializes___objects_to_json_file(self):
        """tests that save() converts the __objects dict to json format
        and saves it to __file_path (file.json)"""
        f = FileStorage()
        model = BaseModel()
        f.new(model)
        f.save()
        result = os.path.isfile('file.json')
        self.assertEqual(result, True)

    def test_reload_method_updates___objects_dict(self):
        """tests that reload() updates __objects with data from json file"""
        f = FileStorage()
        model = BaseModel()
        f.new(model)
        f.save()
        f.reload()
        self.assertNotEqual(f._FileStorage__objects, {})

    def test_storage_object_exists(self):
        """tests that storage instance (set in __init__.py) exists"""
        from models import storage
        self.assertEqual(type(storage), FileStorage)

    def test_objects_attr_keys_include_its_class(self):
        """tests that the key in __objects is the name of the instances' class"""
        x = BaseModel()
        f = FileStorage()
        key = "{}.{}".format(x.__class__.__name__, x.id)
        self.assertEqual(key in f._FileStorage__objects.keys(), True)
