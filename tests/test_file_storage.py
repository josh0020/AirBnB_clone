#!/usr/bin/python3
"""Test case FileStorage module"""
import sys
import unittest
import os
import contextlib
import json
import models
import pep8

"""Get the current script's directory
Add the parent directory to the Python path
Get the absolute path of the parent directory (project root)"""
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.insert(0, parent_dir)

#class
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
