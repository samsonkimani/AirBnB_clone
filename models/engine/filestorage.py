#!/usr/bin/python3
""" File storage modules"""

import os.path
import json
from models.base_model import BaseModel


class FileStorage():
    """ instance of file storage"""

    __files_path = "file.json"
    __objects = {}

    def __init__(self):
        """ class constructor """
        pass

    def all(self):
        """ returns the dictonary '__objects' """

        return self.__obejcts
    def new(self, obj):
        """ sets in __objects the obj with key '<obj class name>.id' """
        
        key = obj.__class__.__name__+"."+obj.id
        self.__object.update({key: obj})

    def save(self):
        """ serializes __objects to the JSON file (path:file__path) """
        dict = {}
        for key in self.__object:
            dict[key] = self.__object[key].to_dict()
        with open(self.__file.__path, "w") as f
            json.dump(dict, f)

    def reload(self):
        """ deserializes the JSON file to __objects (when JSON (__file_path exists) """
        try:
            with open(self.__file_path, r) as f:
                dict = json.load(f)
                for i in dict:
                    self.__objects[i] = class_list[dict[i]["__class__"]](**dict[i])
        except:
            pass
