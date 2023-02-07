#!/usr/bin/python3
"""module for testing base class"""

from models.base_model import BaseModel
import unittest
<<<<<<< HEAD
import datetime
import uuid


class TestBaseModel(unittest.TestCase):
    """ checking for isinstance """
    """ def testDocstring():
        self.assertIsNotNone(__import__("models.base_model").__doc__)"""

    def test_Isinstance_of(self):
        """check if these are instances of the modules"""
=======

class TestBaseModel(unittest.TestCase):
    """ checking for isinstance """
 
    def Isinstanceof(self):
>>>>>>> refs/remotes/origin/main
        bm = BaseModel()
        self.assertIsInstance(bm, BaseModel)
        self.assertIsInstance(bm.id, str)
        #self.assertIsInstance(bm.created_at, datetime)
        #self.assertIsInstance(bm.updated_at, str)

    def test_Instatiation_kwags(self):
        bm_dict = {'id': '56d43177-cc5f-4d6c-a0c1-e167f8c27337','created_at': '2017-09-28T21:03:54.052298','updated_at': '2017-09-28T21:03:54.052298'}
        bm = BaseModel(**bm_dict)
        self.assertIsInstance(bm, BaseModel)
        self.assertEqual(bm.id, '56d43177-cc5f-4d6c-a0c1-e167f8c27337')
        #self.assertEqual(bm.created_at, '2017-09-28T21:03:54.052298')
        #self.assertEqual(bm.updated_at, '2017-09-28T21:03:54.052298')

    def test_id(self):
        """test if a new id is created"""
        bm = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm.id, bm2.id)


if __name__ == '__main__':
    unittest.main()
