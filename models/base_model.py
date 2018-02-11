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
        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                   value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if '__class__' not in key:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = (datetime.now())
            self.updated_at = (datetime.now())
            models.storage.new(self)        
    def __str__(self):
        """
        Method that returns string representation on an instance
        """

        string = ("[{}] ({}) {}". format(self.__class__.__name__, self.id, self.__dict__))
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

        my_dict = self.__dict__
        my_dict['__class__'] = self.__class__.__name__
        my_dict['created_at'] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        my_dict['updated_at'] = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        return my_dict

