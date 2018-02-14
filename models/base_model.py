#!/usr/bin/python3
"""
Module that defines all common attributes and models for base class
"""


from datetime import datetime
import uuid
import models


class BaseModel():
    """
    class BaseModel
    """

    def __init__(self, *args, **kwargs):
        """BaseModel instance constructor"""
        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if '__class__' not in key:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        Method that returns string representation on an instance
        """
        class_name = self.__class__.__name__
        string = ("[{}] ({}) {}".format(class_name, self.id, self.__dict__))
        return string

    def __repr__(self):
        """
        Method that returns string representation on an instance
        """
        class_name = self.__class__.__name__
        string = ("[{}] ({}) {}".format(class_name, self.id, self.__dict__))
        return string

    def save(self):
        """
        Method that saves an instance
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Method that creates a dictionary representation of an instance
        """
        my_dict = {}
        for key, val in self.__dict__.items():
            if key in ['created_at', 'updated_at']:
                my_dict[key] = val.isoformat()
            else:
                my_dict[key] = val
        my_dict['__class__'] = self.__class__.__name__
        return my_dict
        """lee
        json_dict = self.__dict__
        json_dict['__class__'] = type(self).__name__
        if type(json_dict['created_at']) is datetime:
            json_dict['created_at'] = self.created_at.isoformat()
        if type(json_dict['updated_at']) is datetime:
            json_dict['updated_at'] = self.updated_at.isoformat()
        return json_dict
        """
