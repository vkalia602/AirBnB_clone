#!/usr/bin/python3
"""
City: module that contains the attributs and methods used by City models.
City models inherit the following attributes and methods from BaseModel:

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
                 of the Model's class (ex: 'City')
    __str__()  - returns a string representation of the model
    __repr__() - returns a string representation of the model
    save()     - updates the model's udpated_at attr and saves to storage
    to_dict()  - creates a dict representation of a model
"""


from models.base_model import BaseModel


class City(BaseModel):
    """
    City: class for City models. inherits from BaseModel
    """
    state_id = ''
    name = ''
