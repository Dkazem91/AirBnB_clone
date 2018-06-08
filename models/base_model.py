#!/usr/bin/python3
"""BaseModel that defines all common attributes/methods for other classes:"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
        """
        This class contains basic info such as uuid, created at, and updated at times
        """
        def __init__(self):
                self.id = str(uuid4())
                self.created_at = datetime.now()
                self.updated_at = datetime.now()

        def __str__(self):
                """
                returns a string
                """
                return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

        def save(self):
                """
                changes updated_at time
                """
                self.updated_at = datetime.now()

        def to_dict(self):
                copy_of = dict(self.__dict__)
                copy_of["__class__"] = self.__class__.__name__
                copy_of["created_at"] = self.created_at.isoformat()
                copy_of["updated_at"] = self.updated_at.isoformat()
                return copy_of
