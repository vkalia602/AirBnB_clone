#!/usr/bin/python3

"""FileStorage test suite"""
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """FileStorage unit tests"""
    def test_file_path_attr_exists(self):
        """tests that file_path attr is set at init"""
        f = FileStorage('/tmp/', [])
        self.assertEqual(f.file_path, '/tmp/')

    def test_objects_attr_exists(self):
        """tests that objects attr is set at init"""
        f = FileStorage('/tmp/', 'objects attr')
        self.assertEqual(f.objects, 'objects attr')

    def test_storage_object_exists(self):
        """tests that storage FileStorage instance (set in __init__.py) exists"""
        from models import storage
        self.assertEqual(type(storage), FileStorage)

    def test_objects_attr_keys_are_its_class(self):
        """tests that the key in __objects is the name of the instances' class"""
        x = BaseModel()
        f = FileStorage('/tmp', x.to_dict)
        self.assertEqual(f.objects()['__class__'] == type(x).__name__, True)

