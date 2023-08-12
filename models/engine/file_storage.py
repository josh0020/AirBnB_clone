#!/usr/bin/python3
"""File Storage class"
"""

import os.path
import json


class FileStorage:
    """Serializes instances to a JSON file
    and deserializes JSON file to instances
    Attributes:
        __file_path (str): Path to the JSON file
        __objects (dict): Stores all the instances
    """
    __file_path = 'objects.json'
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id
        Args:
            obj (inst): The object to add in the __object class attribute
        """
        objectId = obj.__class__.__name__ + '.' + obj.id
        self.__objects[objectId] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)
        """
        json_dict = {}
        for k, v in self.__objects.items():
            json_dict[k] = v.to_dict()
        with open(self.__file_path, mode='w') as f:
            json.dump(json_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists ; otherwise, do nothing. If the file does not
        exist, no exception should be raised)
        """
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return

