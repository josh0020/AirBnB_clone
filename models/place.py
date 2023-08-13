#!/usr/bin/python3
"""Place Module
Contains the attributes to be assigned to places created
Inherits from BaseModel class.
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Place Class

    Attributes:
        city_id (str): City UUID
        user_id (str): User UUID
        name (str): Place name
        description (str): Place description
        number_rooms (int): Number of rooms
        number_bathrooms (int): Number of bathrooms
        max_guest (int): Maximum guests
        price_by_night (int): Price per night
        latitude (float): Latitude of the Place
        longitude (float): Longitude of the Place
        amenity_ids (list): Amenities list
    """
    city_id = ''
    user_id = ''
    name = ''
    description = ''
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

