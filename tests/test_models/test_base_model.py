#!/usr/bin/python3
"""Tests the basemodels"""
import unittest
import pep8
import os
import time
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """unittests for basemodel"""

    @classmethod
    def setUp(cls):
        """creates class"""
        cls.testBase = BaseModel()

    @classmethod
    def tearDown(cls):
        """deletes test class"""
        del cls.testBase
        try:
            os.remove("file.json")
        except:
            pass

    def test_pep8(self):
        """tests pep8"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/base_model.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_docstrings(self):
        """tests docstrings"""
        self.assertTrue(len(BaseModel.__doc__) > 0)
        for func in dir(BaseModel):
            self.assertTrue(len(func.__doc__) > 0)

    def test_init_and_class_variables(self):
        """tests init and class variables"""
        self.assertTrue(isinstance(self.testBase, BaseModel))
        self.assertTrue(self.testBase.created_at == self.testBase.updated_at)

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
        time.sleep(2)
        self.testBase.save()
        self.assertTrue(self.testBase.updated_at != self.testBase.created_at)


if __name__ == '__main__':
    unittest.main()
