#!/usr/bin/python3
"""
State: module that contains the attributs and methods used by State models.
State models inherit the following attributes and methods from BaseModel:

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
                 of the Model's class (ex: 'State')
    __str__()  - returns a string representation of the model
    __repr__() - returns a string representation of the model
    save()     - updates the model's udpated_at attr and saves to storage
    to_dict()  - creates a dict representation of a model
"""


from models.base_model import BaseModel


class State(BaseModel):
    """
    State: class for State models. inherits from BaseModel
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """
        init: constructor for State instances. inherits created_at, updated_at
        and id attributes from BaseModel
        """
        super().__init__(self, *args, **kwargs)
        if kwargs:
            for key, val in kwargs.items():
                if key == 'name':
                    self.name = val
        else:
            self.name = State.name
