#!/usr/bin/python3
"""This module creates a User class, Defines the User class."""
from models.base_model import BaseModel


class User(BaseModel):
    """User class
    Represents a User
    Attributes:
        email (str): user email.
        password (str): user password.
        first_name (str): user first_name.
        last_name (str): user last_name.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

