#!/usr/bin/python3
""" Creating a unique FileStorage instance for the application """

from models.engine.filestorage import FileStorage

storage = FileStorage()
storage.reload()
