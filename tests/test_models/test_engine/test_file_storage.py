#!/usr/bin/python3
"""
Unittest to test FileStorage class
"""
import unittest
import pep8
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    '''testing file storage'''

    @classmethod
    def setUpClass(cls):
        cls.new_rev = Review()
        cls.new_rev.place_id = "Place"
        cls.new_rev.user_id = "Person"
        cls.new_rev.text = "Hi"

    @classmethod
    def teardown(cls):
        del cls.new_rev

    def teardown(self):
        try:
            os.remove("file.json")
        except:
            pass

    def test_style_check(self):
        """tests pep8"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_all(self):
        """tests if all works"""
        storage = FileStorage()
        new_dict = storage.all()
        self.assertIsNotNone(new_dict)
        self.assertEqual(type(new_dict), dict)
        self.assertIs(new_dict, storage._FileStorage__objects)

    def test_new(self):
        """tests if new works"""
        m_storage = FileStorage()
        new_dict = m_storage.all()
        new_user = User()
        new_user.id = "13312"
        new_user.name = "Andrew"
        m_storage.new(new_user)
        key = new_user.__class__.__name__ + "." + str(new_user.id)
        self.assertIsNotNone(new_dict[key])

    def test_reload(self):
        """tests the reload function"""
        new_storage = FileStorage()
        try:
            os.remove("file.json")
        except:
            pass
        with open("file.json", "w") as f:
            f.write("{}")
        with open("file.json", "r") as r:
            for line in r:
                self.assertEqual(line, "{}")
        self.assertIs(new_storage.reload(), None)