#!/usr/bin/python3
"""
Imports FileStorage
Creates a unique FileStorage instance for your application
"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()

