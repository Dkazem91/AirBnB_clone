#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime
"""BaseModel that defines all common attributes/methods for other classes:"""

class BaseModel:
        """
        This class contains basic info such as uuid, created at, and updated at times
        """

        def __init__(self):
                self.id = uuid4()
                self.created_at = datetime.now()
                self.updated_at = self.created_at

        def __str__(self):
                

        def save(self):
                self.updated_at = datetime.now()

        def to_dict(self):
                self.__dict__["__class__"] = self.__class__.__name__
                self.__dict__["created_at"] = str(self.created_at.isoformat())
                self.__dict__["updated_at"] = str(self.updated_at.isoformat())
