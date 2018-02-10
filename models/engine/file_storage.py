#!/usr/bin/python3
"""
Module that serializes instances to JSON file
"""

import json
import os
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
        self.__objects[x] = obj.to_dict

    def save(self):
        with open(self.__file_path, mode="w", encoding="UTF-8") as my_file:
            json.dump(self.__objects, my_file)

    def reload(self):
        if os.path.isfile(self.__file_path) and os.stat(self.__file_path).st_size != 0:
            with open(self.__file_path, mode='r', encoding="UTF-8") as my_file:
               self.__objects = json.load(my_file)
        else:
            pass
            
