#!/usr/bin/python3

"""file_storage module"""
import json


class FileStorage:
    """FileStorage class"""
    def __init__(self, file_path, objects):
        self.file_path = file_path
        self.objects = objects

    @property
    def file_path(self):
        """file_path getter"""
        return self.__file_path

    @file_path.setter
    def file_path(self, path):
        """file_path setter"""
        self.__file_path = path

    @property
    def objects(self):
        """objects getter"""
        return self.__objects

    @objects.setter
    def objects(self, obj):
        """objects setter"""
        self.__objects = obj

    def all(self):
        """returns the dict __objects"""
        return self.objects

    def new(self, obj):
        """sets <obj class name>.id as the key to obj in __objects"""
        key = "{}.{}".format(obj['__class__'], obj['id'])
        self.objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file __file_path"""
        with open(self.file_path, 'w', encoding='UTF-8') as f:
            json.dump(self.objects, f)

    def reload(self):
        """deserializes the JSON file to __objects if JSON file exists"""
        try:
            with open(self.file_path, encoding='UTF-8') as f:
                self.objects = json.load(f)
        except FileNotFoundError:
            pass
