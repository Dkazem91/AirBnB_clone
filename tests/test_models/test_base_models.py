#!/usr/bin/env python
import unittest
import os
import pep8
from models.base_model import BaseModel
from models.city import City
from models.review import Review
from models.amenity import Amenity
from models.state import State
from models.place import Place

class TestBaseModel(unittest.TestCase):

        @classmethod
        def setUpClass(cls):
                cls.testCity = City()
                cls.testReview = Review()
                cls.testAmenity = Amenity()
                cls.testState = State()
                cls.testPlace = Place()

        @classmethod
        def setUp(cls):
                cls.base = BaseModel()
                cls.base2 = BaseModel()
        
        @classmethod
        def tearDown(cls):
                del cls.base
                del cls.base2
        @classmethod
        def tearDownClass(cls):
                del cls.testCity
                del cls.testReview
                del cls.testAmenity
                del cls.testState
                del cls.testPlace

        def test_pep8_BaseModel(self):
                """
                Tests pep8 style
                """
                style = pep8.StyleGuide(quiet=True)
                p = style.check_files(['models/base_model.py'])
                self.assertEqual(p.total_errors, 0, "fix pep8")
        
        def test_doc_string_BaseModel(self):
                self.assertTrue(len(BaseModel.__doc__) > 0)
                for func in dir(BaseModel):
                        self.assertTrue(len(func.__doc__) > 0)
                for func in dir(City):
                        self.assertTrue(len(func.__doc__) > 0)
                for func in dir(State):
                        self.assertTrue(len(func.__doc__) > 0)
                for func in dir(Review):
                        self.assertTrue(len(func.__doc__) > 0)
                for func in dir(Place):
                        self.assertTrue(len(func.__doc__) > 0)
                for func in dir(Amenity):
                        self.assertTrue(len(func.__doc__) > 0)

if __name__ == '__main__':
        unittest.main()