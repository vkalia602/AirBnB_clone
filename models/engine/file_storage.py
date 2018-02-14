#!/usr/bin/python3

"""file_storage module"""
import os
import json
from models.base_model import BaseModel


class FileStorage:
    """FileStorage class:
        __file_path: name of the json file
        __objects: storage objects by K: <class name>.id V: ??
            example: {'BaseModel.123abc-456def': {'id': '123abc', ...}}"""
    __file_path = 'file.json'
    __objects = {}
    #datetime_keys = {'created_at', 'updated_at'}

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
        new_dict = {}
        for key, value in self.__objects.items():
            new_dict[key] = value.to_dict()
        with open(self.__file_path, mode="w+", encoding="UTF-8") as my_file:
            json.dump(new_dict, my_file)
        """ lee
        json_dict = {}
        for keystring, obj in self.__objects.items():
            if type(obj) is not dict:
                json_dict[keystring] = obj.to_dict()
            elif type(obj) is dict:
                json_dict[keystring] = obj
        with open(self.__file_path, 'w', encoding='UTF-8') as json_file:
            json.dump(json_dict, json_file)
            """

    def reload(self):
        """deserializes the JSON file to __objects if JSON file exists"""
        if os.path.isfile(self.__file_path):
            if os.stat(self.__file_path).st_size != 0:
                with open(self.__file_path, mode='r', encoding="UTF-8") as my_file:
                    new_object = json.load(my_file)
            for key, value in new_object.items():
                class_name = value['__class__']
                del value['__class__']
                self.__objects[key] = eval(class_name)(**value)
        """lee
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
        """
