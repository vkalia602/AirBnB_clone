#!/usr/bin/python3
"""
Place: module that contains the attributs and methods used by Place models.
Place models inherit the following attributes and methods from BaseModel:

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
                 of the Model's class (ex: 'Place')
    __str__()  - returns a string representation of the model
    __repr__() - returns a string representation of the model
    save()     - updates the model's udpated_at attr and saves to storage
    to_dict()  - creates a dict representation of a model
"""


from models.base_model import BaseModel


class Place(BaseModel):
    """
    Place: class for Place models. inherits from BaseModel
    """

    place_attrs = {'city_id', 'user_id', 'name', 'description',
                   'number_rooms', 'number_bathrooms', 'max_guest',
                   'price_by_night', 'latitude', 'longitude', 'amenity_ids'}

    def __init__(self, *args, **kwargs):
        """
        init: constructor for Place instances. inherits created_at, updated_at
        and id attributes from BaseModel
        """
        super().__init__(self, *args, **kwargs)
        if kwargs:
            for key, val in kwargs.items():
                if key in Place.place_attrs:
                    self.name = val
        else:
            self.city_id = ""
            self.user_id = ""
            self.name = ""
            self.description = ""
            self.number_rooms = 0
            self.number_bathrooms = 0
            self.max_guest = 0
            self.price_by_night = 0
            self.latitude = 0.0
            self.longitude = 0.0
            self.amenity_ids = []
