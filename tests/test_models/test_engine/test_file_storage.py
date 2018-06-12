#!/usr/bin/python3
"""Unittest to test file storage"""
import unittest
import pep8
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class TestFileStorage(unittest.TestCase):
    """testing file storage functions"""

    @classmethod
    def setUpClass(cls):
        cls.bs = BaseModel()
        cls.bs.first_name = "johnny"
        cls.bs.age = "5"
        cls.storage = FileStorage()
        cls.storage2 = FileStorage()

    @classmethod
    def teardown(cls):
        del cls.bs
        del cls.storage
        del cls.storage2
        try:
            os.remove("file.json")
        except:
            pass

    def test_pep8(self):
        """tests pep8"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_docstring(self):
        """tests docstrings"""
        self.assertTrue(len(FileStorage.__doc__) > 0)
        for func in dir(FileStorage):
            self.assertTrue(len(func.__doc__) > 0)

    def test_all(self):
        """tests filestorage all function"""
        self.assertIsNotNone(self.storage.all())
        self.assertEqual(type(self.storage.all()), dict)
        self.assertIs(self.storage.all(), self.storage._FileStorage__objects)

    def test_new(self):
        """tests filestorage new function"""
        self.storage.new(self.bs)
        key = self.bs.__class__.__name__ + '.' + self.bs.id
        self.assertIsNotNone(self.storage.all()[key])

    def test_reload_and_save(self):
        """tests fileself.storage reload function and save"""
        try:
            with open("file.json", "r") as r:
                r.write("{}")
        except:
            pass
        self.storage.new(self.bs)
        self.storage.save()
        key = self.bs.__class__.__name__ + '.' + self.bs.id
        test = {key: self.bs.to_dict()}
        with open("file.json", "r") as r:
            self.assertEqual(json.load(r), test)
        self.storage2.reload()
        self.assertTrue(self.storage2.all() == self.storage.all())
