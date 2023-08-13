#!/usr/bin/python3
"""
file_storage module that contains the FileStorage class
definition and methods
"""
from models.base_model import BaseModel
import json
import os
<<<<<<< HEAD
import datetime
=======
import models
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.amenity import Amenity
>>>>>>> branch_2


class FileStorage:
    """
    FileStorage class which serializes instances to a JSON file
    and deserializes JSON files to instances.
    """

    __file_path = 'file.json'
    __objects = {}

    def all(self):
<<<<<<< HEAD
        """return dictionary object"""
        return FileStorage.__objects
=======
        """
        Returns the dictionary `__objects`.
        """
        return self.__objects
>>>>>>> branch_2

    def new(self, obj):
        """
        Sets in `__objects` the `obj` with key `<obj class name>.id`.
        """
        self.__objects[f'{obj.__class__.__name__}.{obj.id}'] = obj

    def save(self):
<<<<<<< HEAD
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
=======
        """
        Serializes `__objects` to the JSON file.
        """
        ObjectDict = {}
        for key, value in self.__objects.items():
            ObjectDict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding='utf=8') as f:
            f.write(json.dumps(ObjectDict))

    def reload(self):
        """
        Deserializes the JSON file to `__objects` if the file exists;
        otherwise, does nothing.
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                LoadDict = json.loads(f.read())
            for key, val in LoadDict.items():
                self.__objects[key] = eval(val["__class__"])(**val)
>>>>>>> branch_2
