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
    class User
    """
    email = ''
    password = ''
    first_name = ''
    last_name = ''
