#!/usr/bin/python3
"""Defines AirBnB Clone BaseModel class"""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """The AirBnB Clone BaseModel"""

    def __init__(self, *args, **kwargs):
        """Init a new BaseModel.
        Args:
            *args (any): not used
            **kwargs (dict): Attributes key/value pairs
        """
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        timeform = "%Y-%m-%dT%H:%M:%S.%f"
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, timeform)
                else:
                    self.__dict__[k] = v
        else:
            self.id = str(uuid4())
            self.created_at = datetime.today()

    def __str__(self):
        """Return the print/str representation of the BaseModel instance."""
        name = self.__class__.__name__
        return "[{}] ({}) {}".format(name, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with the current datetime"""
        self.updated_at = datetime.today()

    def to_dict(self):
        """Return a dictionary containing all keys/values of
        __dict__ of the instance
        """
        kvdict = self.__dict__.copy()
        kvdict["__class__"] = self.__class__.__name__
        kvdict["created_at"] = self.created_at.isoformat()
        kvdict["updated_at"] = self.updated_at.isoformat()
        return kvdict

