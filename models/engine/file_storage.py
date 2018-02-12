#!/usr/bin/python3
"""
Module that serializes instances to JSON file
"""

import json
import os
from models.base_model import BaseModel
class FileStorage():
    """
    Class FileStorage to serialize/deserialize a JSON file
    """
    __file_path = "file.json"
    __objects = {}
    def all(self):
        return self.__objects

    def new(self, obj):
        x = ("{}.{}".format(obj.__class__.__name__, obj.id))
        print(obj)
        self.__objects[x] = obj

    def save(self):
        new_dict = {}
        for key, value in self.__objects.items():
            new_dict[key] = value.to_dict()
        with open(self.__file_path, mode="w+", encoding="UTF-8") as my_file:
            json.dump(new_dict, my_file)

    def reload(self):
        if os.path.isfile(self.__file_path):
            if os.stat(self.__file_path).st_size != 0:
                with open(self.__file_path, mode='r', encoding="UTF-8") as my_file:
                    new_object = json.load(my_file)
            for key, value in new_object.items():
                class_name = value['__class__']
                self.__objects[key] = eval(class_name)(**value)
                
