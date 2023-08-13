#!/usr/bin/python3
"""File Storage class
"""
from models.base_model import BaseModel
from models.user import User
import os.path
import json


class FileStorage:
    """Serializes instances to a JSON file
    and deserializes JSON file to instances
    Attributes:
        __file_path (str): Path to the JSON file
        __objects (dict): Stores all the instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id
        Args:
            obj (instance): The object to add
        """
        name = obj.__class__.__name__
        self.__objects["{}.{}".format(name, obj.id)] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)
        """
        objectdict = self.__objects
        objdict = {obj: objectdict[obj].to_dict() for obj in objectdict.keys()}
        with open(self.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        """Deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists ; otherwise, do nothing. If the file does not
        exist, no exception should be raised)
        """
        try:
            with open(self.__file_path) as f:
                objectdict = json.load(f)
                for o in objectdict.values():
                    name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(name)(**o))
        except FileNotFoundError:
            return

