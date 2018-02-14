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
    def __init__(self, *args, **kwargs):
        """User constructor, inheriting id, created_at, updated_at
        from BaseModel"""
        super().__init__()
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
