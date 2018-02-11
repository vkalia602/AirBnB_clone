#!/usr/bin/python3

"""file_storage module"""
import json


class FileStorage:
    """FileStorage class"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """returns the dict __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets <obj class name>.id as the key to obj in __objects"""
        key = "{}.{}".format(obj['__class__'], obj['id'])
        del obj['__class__']
        #print('before.........')
        #print(self.__objects)
        self.__objects.update({key: obj})
        #print('after.........')
        #print(self.__objects)

    def save(self):
        """serializes __objects to the JSON file __file_path"""
        with open(self.__file_path, 'w', encoding='UTF-8') as f:
            json.dump(self.__objects, f)

    def reload(self):
        """deserializes the JSON file to __objects if JSON file exists"""
        try:
            with open(self.__file_path, encoding='UTF-8') as f:
                self.__objects = json.load(f)
        except FileNotFoundError:
            pass
