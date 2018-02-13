#!/usr/bin/python3

"""file_storage module"""
import json
from models.base_model import BaseModel


class FileStorage:
    """FileStorage class:
        __file_path: name of the json file
        __objects: storage objects by K: <class name>.id V: ??
            example: {'BaseModel.123abc-456def': {'id': '123abc', ...}}"""
    __file_path = 'file.json'
    __objects = {}
    datetime_keys = {'created_at', 'updated_at'}

    def all(self):
        """returns the dict __objects"""
        return self.__objects

    def new(self, obj):
        """sets <obj class name>.id as the key to obj in __objects
        and the value is the dict representation of the obj"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file __file_path"""
        # turn __objects into dict reps
        json_dict = {}
        for keystring, obj in self.__objects.items():
            if type(obj) is not dict:
                json_dict[keystring] = obj.to_dict()
            if type(obj) is dict:
                json_dict[keystring] = obj
        with open(self.__file_path, 'w', encoding='UTF-8') as json_file:
            json.dump(json_dict, json_file)

    def reload(self):
        """deserializes the JSON file to __objects if JSON file exists"""
        new_object = {}
        try:
            with open(self.__file_path, encoding='UTF-8') as f:
                new_object = json.load(f)
        except FileNotFoundError:
            pass
        for key, val in new_object.items():
            class_name = val['__class__']
            del val['__class__']
            self.__objects[key] = eval(class_name)(**val) 
