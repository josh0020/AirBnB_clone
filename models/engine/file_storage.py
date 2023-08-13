#!/usr/bin/python3
"""FileStorage serialized and resererialized JSON
"""
from models.base_model import BaseModel
from models.user import User
import os.path
import json
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.amenity import Amenity


class FileStorage:
    """ File Storage class.
    Attributes:
        __file_path (str): file name to save objects to
        __objects (dict): A dict of instantiated objects
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        objname = obj.__class__.__name__
        self.__objects["{}.{}".format(objname, obj.id)] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        json_object = {}
        for key in self.__objects:
            json_object[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(json_object, f)

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON
        file (__file_path) exists ; otherwise, do nothing.
        If the file does not exist, no exception should be raised)
        """
        try:
            with open(self.__file_path) as f:
                objectdict = json.load(f)
                for o in objectdict.values():
                    cname = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cname)(**o))
        except FileNotFoundError:
            return

