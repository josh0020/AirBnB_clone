#!/usr/bin/python3
"""Amenity Module
Contains the attributes to be assigned to the Amenities
Inherits from BaseModel class.
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity Class
    Attributes:
        name (str): Amenity name
    """
    name = ''

