#!/usr/bin/python3
"""class user that inherit BaseModel"""

from models.base_model import BaseModel


class User(BaseModel):
    """user class inheriting BaseModel"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
