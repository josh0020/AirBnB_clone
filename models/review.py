#!/usr/bin/python3
"""Review Module
Contains the attributes to be assigned user reviews
Inherits from BaseModel class
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review Class
    Attributes:
        place_id (str): Place UUID
        user_id (str): User UUID
        text (str): Review text
    """
    place_id = ''
    user_id = ''
    text = ''

