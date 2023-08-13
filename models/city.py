#!/usr/bin/python3
"""City Module
Contains the attributes to be assigned to the cities.
Inherits from BaseModel
"""
from models.base_model import BaseModel


class City(BaseModel):
    """City Class
    Attributes:
        state_id (str): City UUID
        name (str): City name
    """
    state_id = ""
    name = ""

