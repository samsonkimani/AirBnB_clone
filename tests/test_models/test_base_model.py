#!/usr/bin/python3
"""module for testing base class"""

from models.base_model import BaseModel
from unittest import TestCase
from unittest.mock import patch

class TestBaseModel(unittest.TestCase):
    """ checking for isinstance """
   """ def testDocstring():
        self.assertIsNotNone(__import__("models.base_model").__doc__)"""

    def Isinstanceof(self):
        bm = BaseModel()
        self.assertIsInstance(bm, BaseModel)
        self.assertIsInstance(bm.id, str)
        self.assertIsInstance(bm.created_at, datetime)
        self.assertIsInstance(bm.updated_at, datetime)

    def Instatiation_kwags(self):
        bm_dict = {'id': '56d43177-cc5f-4d6c-a0c1-e167f8c27337','created_at': '2017-09-28T21:03:54.052298','updated_at': '2017-09-28T21:03:54.052298'}
        bm = BaseModel(**bm_dict)
        self.assertIsInstance(bm, BaseModel)
        self.assertIsInstance(bm.id, '56d43177-cc5f-4d6c-a0c1-e167f8c27337')
        self.assertIsInstance(bm.created_at, '2017-09-28T21:03:54.052298')
        self.assertIsInstance(bm.updated_at, '2017-09-28T21:03:54.052298')

