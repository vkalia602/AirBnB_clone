#!/usr/bin/python3
"""
Module that defines all common attributes and methods for Users
"""


from datetime import datetime
import uuid
import models
from models.base_model import BaseModel


class User(BaseModel):
    """
    class BaseModel
    """
    email = ''
    password = ''
    first_name = ''
    last_name = ''

    def __init__(self, *args, **kwargs):
        """User constructor, inheriting id, created_at, updated_at
        from BaseModel"""
        super().__init__(self, *args, **kwargs)
        if kwargs:
            for key, val in kwargs.items():
                if key == 'email':
                    self.email = val
                elif key == 'password':
                    self.password = val
                elif key == 'first_name':
                    self.first_name = val
                elif key == 'last_name':
                    self.last_name = val
        else:
            self.email = User.email
            self.password = User.password
            self.first_name = User.first_name
            self.last_name = User.last_name
