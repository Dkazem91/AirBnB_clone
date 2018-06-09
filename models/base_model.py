#!/usr/bin/python3
"""BaseModel that defines all common attributes/methods for other classes:"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """
    This class contains basic info such as uuid, created at, and updated at
    """

    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        returns a string
        """
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def __repr__(self):
        """
        returns __str__
        """
        return self.__str__()

    def save(self):
        """
        changes updated_at time
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        copy_of = dict(self.__dict__)
        copy_of["__class__"] = self.__class__.__name__
        copy_of["created_at"] = self.created_at.isoformat()
        copy_of["updated_at"] = self.updated_at.isoformat()
        return copy_of
