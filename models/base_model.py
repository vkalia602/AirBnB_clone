#!/usr/bin/python3

"""BaseModel module: contains the BaseModel class"""
import uuid
import datetime
from . import storage


class BaseModel:
    """BaseModel Class"""
    def __init__(self, *args, **kwargs):
        """BaseModel constructor"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
        # for new instances not from a dict (kwargs), call storage.new()
        if len(kwargs) == 0:
            storage.new(self.to_dict())
        # we don't want the datetime attrs to get updated via a kwarg
        invalid_keys = {'created_at', 'updated_at'}
        filtered_kwargs = {}
        for k, v in kwargs.items():
            if k not in invalid_keys:
                filtered_kwargs[k] = v
        self.__dict__.update(filtered_kwargs)

    def __str__(self):
        """string representation of a BaseModel object"""
        return "[{}] ({}) {}".format(
                type(self).__name__, self.id, self.__dict__)

    def save(self):
        """updates the updated_at attr with current datetime"""
        storage.save()
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """returns a dict containing all key/vals of the instance"""
        json_dict = {}
        for k,v in self.__dict__.items():
            json_dict[k] = v
        json_dict['__class__'] = type(self).__name__
        json_dict['created_at'] = self.created_at.isoformat()
        json_dict['updated_at'] = self.updated_at.isoformat()
        return json_dict
