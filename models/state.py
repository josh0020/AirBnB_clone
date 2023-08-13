#!/usr/bin/python3
"""State Module
Contains the attributes to be assigned to the State
Inherits from BaseModel class.
"""
from models.base_model import BaseModel


class State(BaseModel):
    """State Class
    Attributes:
        name (str): State name
    """
    name = ''

