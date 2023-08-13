#!/usr/bin/python3
<<<<<<< HEAD
"""state class inherit from basemodel"""

=======
"""Defines a class State that inherits from BaseModel"""
>>>>>>> branch_2
from models.base_model import BaseModel


class State(BaseModel):
<<<<<<< HEAD
    """state class"""
    name = ""
=======
    """Class that defines properties of State.
    Attributes:
        name (string): name of state.
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """Creates new instances of State.
        """
        super().__init__(*args, **kwargs)
>>>>>>> branch_2
