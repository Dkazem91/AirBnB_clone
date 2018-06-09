#!/usr/bin/python3
"""serializes instances to JSON file, deserializes JSON file to instances"""
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.review import Review


class FileStorage:

        __file_path = "file.json"
        __objects = {}
        
        def all(self):
                """
                returns the objects dictionary
                """
                return FileStorage.__objects

        def new(self, obj):
                """
                adds to objects dictionary
                """
                FileStorage.__objects[type(obj).__name__ + "." + obj.id] = obj
        
        def save(self):
                """
                writes to a file
                """
                temp_dict = {}
                for key, value in FileStorage.__objects.items():
                        temp_dict[key] = value.to_dict()
                with open(FileStorage.__file_path, 'w') as files:
                        json.dump(temp_dict, files)

        def reload(self):
                """
                get data from a json file
                """
                try:
                        with open(FileStorage.__file_path, 'r') as open_file:
                                temp = json.load(open_file)
                                for key, value in temp.items():
                                        self.new(eval(temp[key]["__class__"])(**value))
                                        
                except:
                        pass