#!/usr/bin/python3
"""Tests the basemodels"""
import unittest
import pep8
import os
from datetime import datetime
from models.base_model import BaseModel
from models.city import City
from models.review import Review
from models.amenity import Amenity
from models.state import State
from models.place import Place

class TestBaseModel(unittest.TestCase):
    """unittests for basemodel"""

    @classmethod
    def setUp(cls):
        """creates class"""
        cls.testBase = BaseModel()
        cls.testCity = City()
        cls.testReview = Review()
        cls.testAmenity = Amenity()
        cls.testState = State()
        cls.testPlace = Place()

    @classmethod
    def tearDown(cls):
        """delets test class"""
        del cls.testBase
        del cls.testCity
        del cls.testReview
        del cls.testAmenity
        del cls.testState
        del cls.testPlace
        try:
            os.remove("file.json")
        except:
            pass

    def test_pep8(self):
        """tests pep8"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/base_model.py', 'models/city.py',
                               'models/review.py', 'models/state.py',
                               'models/place.py', 'models/amenity.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_docstrings(self):
        """tests docstrings"""
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

    def test_init_and_class_variables(self):
        """tests init and class variables"""
        self.assertTrue(isinstance(self.testBase, BaseModel))
        self.assertTrue(isinstance(self.testCity, City))
        self.assertTrue(isinstance(self.testState, State))
        self.assertTrue(isinstance(self.testReview, Review))
        self.assertTrue(isinstance(self.testPlace, Place))
        self.assertTrue(isinstance(self.testAmenity, Amenity))
        self.assertTrue(self.testCity.state_id == "")
        self.assertTrue(self.testCity.name == "")
        self.assertTrue(self.testState.name == "")
        self.assertTrue(self.testAmenity.name == "")
        self.assertTrue(self.testPlace.city_id == "")
        self.assertTrue(self.testPlace.user_id == "")
        self.assertTrue(self.testPlace.name == "")
        self.assertTrue(self.testPlace.description == "")
        self.assertTrue(self.testPlace.number_rooms == 0)
        self.assertTrue(self.testPlace.number_bathrooms == 0)
        self.assertTrue(self.testPlace.max_guest == 0)
        self.assertTrue(self.testPlace.price_by_night == 0)
        self.assertTrue(self.testPlace.latitude == 0)
        self.assertTrue(self.testPlace.longitude == 0)
        self.assertTrue(self.testPlace.amenity_ids == "")
        self.assertTrue(self.testReview.place_id == "")
        self.assertTrue(self.testReview.user_id == "")
        self.assertTrue(self.testReview.text == "")

    def test_str(self):
        self.assertEqual(self.testBase.__str__(),
                         "[{}] ({}) {}".format("BaseModel",
                                               self.testBase.id,
                                               self.testBase.__dict__))
    def test_todict(self):
        test_dict = self.testBase.to_dict()
        self.assertTrue(isinstance(test_dict, dict))
        self.assertTrue(isinstance(test_dict['created_at'], str))
        self.assertIsNotNone(test_dict['__class__'])

    def test_save(self):
        self.testBase.save()
        self.assertTrue(self.testBase.updated_at != self.testBase.created_at)

if __name__ == '__main__':
    unittest.main()
