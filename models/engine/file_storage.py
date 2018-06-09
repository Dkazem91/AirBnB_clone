#!/usr/bin/python3
"""serializes instances to JSON file, deserializes JSON file to instances"""
import os.path
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.Place import Place
from models.Review import Review

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary of objects"""
        return FileStorage.__objects

    def new(self, obj):
        """adds new object to __objects"""
        name = obj.__class__.__name__
        FileStorage.__objects[name + '.' + obj.id] = obj

    def save(self):
        """saves objects to json file"""
        jsonData = {}
        for key, value in FileStorage.__objects.items():
            jsonData[key] = value.to_dict()
            with open(FileStorage.__file_path, 'w') as f:
                data = json.dump(jsonData, f)

    def reload(self):
        try:
            with open(FileStorage.__file_path, 'r') as f:
                data = json.load(f)
                for key, obj in data.items():
                    self.new(eval(obj['__class__'])(**obj))
        except:
            return
