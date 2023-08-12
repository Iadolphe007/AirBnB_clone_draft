#!/usr/bin/python3
"""
serializes instances to a
JSON file and deserializes
JSON file to instances"""

import json
import os
import datetime


class FileStorage:
    """serializes and deserializes object"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """return dictionary object"""
        return FileStorage.__objects

    def new(self, obj):
        """return dict obj"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        serialized = {}
        for key, value in FileStorage.__objects.items():
            serialized[key] = value.to_dict()
            with open(FileStorage.__file_path, 'w') as file:
                file.write(json.dumps(serialized))

    def reload(self):
        """deserializes the JSON file to __objects"""
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r") as file:
            obj_dict = json.load(file)
            obj_dict = {key: self.classes()[v["__class__"]](**v)
                        for key, value in obj_dict.items()}
            FileStorage.__objects = obj_dict

    def classes(self):
        """Returns a dictionary of valid
        classes and their references"""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review


        classes = {
                "BaseModel": BaseModel,
                "User": User,
                "State": State,
                "City": City,
                "Amenity": Amenity,
                "Place": Place,
                "Review": Review}
        return classes

    def attribures(self):
        """Returns the valid attributes and their types for classname"""
        attributes = {
                "BaseModel": {
                    "id": str,
                    "created_at": datetime.datetime,
                    "updated_at": datetime.datetime
                    },
                "User": {
                    "email": str,
                    "password": str,
                    "first_name": str,
                    "last_name": str
                    },
                "State": {"name": str},
                "City": {
                    "state_id": str,
                    "name": str
                    },
                "Amenity": {"name": str},
                "Place": {
                    "city_id": str,
                    "user_id": str,
                    "name": str,
                    "description": str,
                    "number_rooms": int,
                    "number_bathrooms": int,
                    "max_guest": int,
                    "price_by_night": int,
                    "latitude": float,
                    "longitude": float,
                    "amenity_ids": list
                    },
                "Review": {
                    "place_id": str,
                    "user_id": str,
                    "text": str
                    }
                }
        return attributes
