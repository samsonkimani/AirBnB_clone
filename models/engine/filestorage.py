#!/usr/bin/python3
""" File storage modules"""

import os.path
import json
from models.base_model import BaseModel


class FileStorage():
    """ instance of file storage"""

    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        """ class constructor """
        pass

    def all(self):
        """ returns the dictonary '__objects' """

        return self.__objects
    def new(self, obj):
        """ sets in __objects the obj with key '<obj class name>.id' """

        key = obj.__class__.__name__+"."+obj.id
        self.__objects.update({key: obj})

    def save(self):
        """ serializes __objects to the JSON file (path:file__path) """
        obj_dict = {}
        for key in self.__objects:
            obj_dict[key] = self.__objects[key].to_dict()
        with open(self.__file_path, "w") as f:
            json_data = json.dumps(obj_dict)
            f.write(json_data)


    def reload(self):
        """ deserializes the JSON file to __objects (when JSON (__file_path exists) """
        try:
            with open(self.__file_path, r) as f:
                obj_dict = f.read()
                json.loads(obj_dict)
                for i in obj_dict.items():
                    self.__objects[i] = class_list[obj_dict[i]["__class__"]](**obj_dict[i])
        except:
            pass
