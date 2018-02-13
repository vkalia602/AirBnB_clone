#!/usr/bin/python3

"""BaseModel module: contains the BaseModel class"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """BaseModel Class"""


    def __init__(self, *args, **kwargs):
        """BaseModel constructor
        *args: won't be used
        **kwargs: a dict representation of an instance:
            key = attr name
            val = value of attr name
        id: uuid random id (needs to be a string)
        created_at: datetime object
        updated_at: datetime object
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        # if loading from json we must convert created_at and updated_at
        # from strings back into datetime objects
        if len(kwargs) > 0:
            datetime_keys = {'created_at', 'updated_at'}
            for k, v in kwargs.items():
                if k in datetime_keys:
                    self.__dict__[k] = datetime.strptime(v,'%Y-%m-%dT%H:%M:%S.%f')
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def __str__(self):
        """string representation of a BaseModel object"""
        return "[{}] ({}) {}".format(
                type(self).__name__, self.id, self.__dict__)

    def __repr__(self):
        """string representation of a BaseModel object"""
        return "[{}] ({}) {}".format(
                type(self).__name__, self.id, self.__dict__)

    def save(self):
        """updates the updated_at attr with current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dict containing all key/vals of the instance.
        this method is called when we prepare the object for json.
        it produces a dict representation with 'simple object type'
        of our BaseModel"""
        json_dict = self.__dict__
        json_dict['__class__'] = type(self).__name__
        if type(json_dict['created_at']) is datetime:
            json_dict['created_at'] = self.created_at.isoformat()
        if type(json_dict['updated_at']) is datetime:
            json_dict['updated_at'] = self.updated_at.isoformat()
        return json_dict
