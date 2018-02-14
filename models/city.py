#!/usr/bin/python3
"""Module for city class
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Class city inherited from BaseModel
    """
    state_id = ""
    name = ""
