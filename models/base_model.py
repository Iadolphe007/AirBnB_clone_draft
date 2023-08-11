#!/usr/bin/python3
"""class that defines common attribute"""

import uuid
from datetime import datetime

class BaseModel:
    """class where other classes inherit"""
    def __init__(self, *args, **kwargs):
        """initialise instance attribute"""
        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                            kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] =  datetime.strptime(
                            kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uui.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """return string representation"""
        return  "[{}] ({}) {}".\
                format(type(self).__name__, self.id, self.__dict__)
    def save(self):
        """update time with current datetime"""
         self.updated_at = datetime.datetime.now

    def to_dict(self):
        """return dixt containing key/values"""
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = type(self).__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return my_dict
