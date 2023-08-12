#!/usr/bin/python3
"""city class that inherit from BaseModel"""

from models.base_model import BaseModel


class City(BaseModel):
    """class for city"""
    state_id = ""
    name = ""
