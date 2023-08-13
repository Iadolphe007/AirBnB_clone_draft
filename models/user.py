#!/usr/bin/python3
<<<<<<< HEAD
"""class user that inherit BaseModel"""

=======
"""Defines a class User that inherits from BaseModel"""
>>>>>>> branch_2
from models.base_model import BaseModel


class User(BaseModel):
<<<<<<< HEAD
    """user class inheriting BaseModel"""
=======
    """ Class that defines properties of User """
>>>>>>> branch_2

    email = ""
    password = ""
    first_name = ""
    last_name = ""
<<<<<<< HEAD
=======

    def __init__(self, *args, **kwargs):
        """Creates new instances of User.
        """
        super().__init__(*args, **kwargs)
>>>>>>> branch_2
