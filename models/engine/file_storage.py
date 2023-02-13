#!/usr/bin/env python3
""" model - storage model"""

import json
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = "{}.{}".format(type(obj).__name__,
                             obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        with open(FileStorage.__file_path,
                  mode="w",
                  encoding="utf-8") as f:
            json_str = json.dumps(FileStorage.__objects,
                                  default=lambda obj: obj.to_dict())
            f.write(json_str)

    def reload(self):
        try:
            with open(FileStorage.__file_path, encoding="utf-8")as f:
                FileStorage.__objects = json.loads(f.
                                                   read(),
                                                   object_hook=self.
                                                   json_to_python)
        except FileNotFoundError:
            pass

    @staticmethod
    def json_to_python(json_dict):
        """static metod to pass to json loads"""
        if "__class__" in json_dict:
            class_name = json_dict["__class__"]
            if class_name == "BaseModel":
                return BaseModel(**json_dict)
            else:
                return json_dict
        else:
            return json_dict
