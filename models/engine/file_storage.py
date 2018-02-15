#!/usr/bin/python3

"""
File Storage: module for storing models to disk. works with HBHCommand shell
commands and contains the following methods and attributes:

    attributes
    -------------------------------------------------------------------
    __file_path - the pathname of the json file to store the objects in
    __objects - a dictionary of all objects
                key: <class_name>.<id>
                val: dictionary of the instances attribute (from to_dict)

    methods
    -------------------------------------------------------------------
    all    - returns __objects (the dictionary containing all objects)
    new    - generates a keystring and sets an entry in __objects
    save   - converts objects (from __objects) to a json-friendly dictionary
             then saves them to storage
    reload - converts objects from the json file (__file_path) to a dictionary
             of objects.

"""
import os
import json
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User


class FileStorage:
    """
    FileStorage class - contains the attributes and methods needed for
    serialization and deserialization of data and allows data to persist by
    saving them to disk in json format
    """

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """
        all: returns the dictionary of all objects
        """
        return self.__objects

    def new(self, obj):
        """
        new: generates a keystring and sets an entry of a model in __objects
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        save: converts objects (from __objects) to a json-friendly dictionary
        then saves the objects to the json file in __file_path
        """
        new_dict = {}
        for keystring, obj in self.__objects.items():
            if type(obj) is dict:
                new_dict[keystring] = obj
            else:
                new_dict[keystring] = obj.to_dict()
        with open(self.__file_path, mode="w+", encoding="UTF-8") as my_file:
            json.dump(new_dict, my_file)

    def reload(self):
        """
        reload: converts objects from the json file (__file_path) to a
        dictionary of objects. the key/val will look like:

            key: <class_name>.<id>
            val: <object>
        """
        if os.path.isfile(self.__file_path):
            if os.stat(self.__file_path).st_size != 0:
                with open(self.__file_path, encoding='UTF-8') as my_file:
                    new_object = json.load(my_file)
                for key, value in new_object.items():
                    class_name = value['__class__']
                    del value['__class__']
                    self.__objects[key] = eval(class_name)(**value)
        else:
            pass
