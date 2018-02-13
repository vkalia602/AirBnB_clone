#!/usr/bin/python3

"""BaseModel test suite"""
import unittest
import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    """BaseModel unit tests"""

    def test_base_object_should_be_of_type_BaseModel(self):
        """tests that instances of BaseModel should be of type BaseModel"""
        model = BaseModel()
        self.assertEqual(type(model), BaseModel)

    def test_base_object_has_an_id(self):
        """tests that BaseModel objects have an id attribute"""
        model = BaseModel()
        self.assertEqual(model.id is None, False)

    def test_base_object_id_is_a_string(self):
        """tests that BaseModel objects id is of type str"""
        model = BaseModel()
        self.assertEqual(type(model.id) is str, True)

    def test_base_object_id_is_unique(self):
        """tests that BaseModel objects have unique ids"""
        model1 = BaseModel()
        model2 = BaseModel()
        self.assertEqual(model1.id == model2.id, False)

    def test_base_object_id_not_an_empty_string(self):
        """tests that BaseModel object ids are not empty"""
        model = BaseModel()
        self.assertEqual(model.id == "", False)

    def test_base_object_created_at_exists(self):
        """tests that BaseModel created_at attribute is not None"""
        model = BaseModel()
        self.assertEqual(model.created_at is None, False)

    def test_base_object_created_at_is_a_datetime(self):
        """tests that BaseModel created_at attribute is of type
        datetime.datetime"""
        model = BaseModel()
        self.assertEqual(type(model.created_at) is datetime.datetime, True)

    def test_base_object_updated_at_exists(self):
        """tests that BaseModel updated_at attribute is not None"""
        model = BaseModel()
        self.assertEqual(model.updated_at is None, False)

    def test_base_object_updated_at_is_a_datetime(self):
        """tests that BaseModel updated_at attribute is of type
        datetime.datetime"""
        model = BaseModel()
        self.assertEqual(type(model.updated_at) is datetime.datetime, True)

    def test_str_representation_is_formatted_correctly(self):
        """tests that __str__ returns a specific format (see example)"""
        model = BaseModel()
        model_string = str(model)
        self.assertEqual("[BaseModel]" in model_string, True)
        self.assertEqual("id" in model_string, True)
        self.assertEqual("created_at" in model_string, True)
        self.assertEqual("updated_at" in model_string, True)

    def test_save_changes_updated_at_attribute(self):
        """tests that save() changes updated_at"""
        model = BaseModel()
        update1 = model.updated_at
        model.save()
        update2 = model.updated_at
        self.assertEqual(update1 == update2, False)

    def test_updated_at_should_be_newer_than_previous_value_after_save(self):
        """tests that update_at is a later datetime after save()"""
        model = BaseModel()
        update1 = model.updated_at
        model.save()
        update2 = model.updated_at
        update2 = datetime.datetime.strptime(update2, '%Y-%m-%dT%H:%M:%S.%f')
        self.assertEqual(update1 < update2, True)

    def test_updated_at_changes_each_time_save_is_called(self):
        """tests that save() changes updated_at attr with multiple calls"""
        model = BaseModel()
        model.save()
        update1 = model.updated_at
        model.save()
        update2 = model.updated_at
        self.assertEqual(update1 == update2, False)

    def test_to_dict_returns_a_dictionary(self):
        """tests that to_dict() returns a dictionary"""
        model = BaseModel()
        result = model.to_dict()
        self.assertEqual(type(result), dict)

    def test_to_dict_includes_class_key(self):
        """tests that __class__ is in the to_dict() dictionary"""
        model = BaseModel()
        self.assertEqual('__class__' in model.to_dict(), True)

    def test_to_dict_includes_created_at_key(self):
        """tests that created_at is in the to_dict() dictionary"""
        model = BaseModel()
        self.assertEqual('created_at' in model.to_dict(), True)

    def test_to_dict_includes_updated_at_key(self):
        """tests that updated_at is in the to_dict() dictionary"""
        model = BaseModel()
        self.assertEqual('updated_at' in model.to_dict(), True)

    def test_created_at_is_a_string_in_dictionary(self):
        """tests that created_at is in isoformat in the dict representation"""
        model = BaseModel()
        self.assertEqual(type(model.to_dict()['created_at']) is str, True)

    def test_updated_at_is_a_string_in_dictionary(self):
        """tests that updated_at is in isoformat in the dict representation"""
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertEqual(type(model_dict['updated_at']) is str, True)

    def test_new_instance_assigns_attributes_from_kwargs(self):
        """tests that new instances can create attrs from kwargs"""
        model = BaseModel(name='Michael Jordan')
        self.assertEqual(model.name, 'Michael Jordan')

    def test_key_and_val_from_kwargs_is_and_attribute(self):
        """tests that kwargs gets attributes for an instance"""
        model = BaseModel(name='Michael Jordan', age=60, points=23.45)
        self.assertEqual(model.age, 60)
        self.assertEqual(model.name, 'Michael Jordan')
        self.assertEqual(model.points, 23.45)
