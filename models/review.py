#!/usr/bin/python3
"""
Review: module that contains the attributs and methods used by Review models.
Review models inherit the following attributes and methods from BaseModel:

    attributes
    --------------------------------------------------------------------
            id - random uuid
    created_at - datetime object set at time of init
    updated_at - datetime object set at time of init (subject to change)

    methods
    --------------------------------------------------------------------
    __init__() - constructor that sets id, created_at, and updated_at.
                 accepts kwargs. if kwargs are sent (via storage.reload())
                 created_at and updated_at will be converted from strings
                 back to datetime objects. __class__ will be set to the name
                 of the Model's class (ex: 'Review')
    __str__()  - returns a string representation of the model
    __repr__() - returns a string representation of the model
    save()     - updates the model's udpated_at attr and saves to storage
    to_dict()  - creates a dict representation of a model
"""


from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review: class for Review models. inherits from BaseModel
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """
        init: constructor for Review instances. inherits created_at, updated_at
        and id attributes from BaseModel
        """
        super().__init__(self, *args, **kwargs)
        if kwargs:
            for key, val in kwargs.items():
                if key == 'place_id':
                    self.place_id = val
                elif key == 'user_id':
                    self.user_id = val
                elif key == 'text':
                    self.text = val
        else:
            self.place_id = Review.place_id
            self.user_id = Review.user_id
            self.text = Review.text
