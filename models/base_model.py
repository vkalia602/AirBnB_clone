#!/usr/bin/python3
"""
Module that defines all common attributes and models for base class
"""

import datetime
import uuid
class BaseModel():
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = (datetime.datetime.now())
        self.updated_at = (datetime.datetime.now())

    def __str__(self):
        string = ("[BaseModel] ({}) {}". format(self.id, self.__dict__))
        return string

    def save(self):
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        my_dict = self.__dict__
        my_dict['__class__']="BaseModel"
        my_dict['created_at'] = datetime.isoformat("value")
        my_dict['updated_at'] = datetime.isoformat("value")
        return my_dict

