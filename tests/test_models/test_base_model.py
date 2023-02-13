#!/usr/bin/python3
"""module for testing base class"""

import models
from models.base_model import BaseModel
import unittest
from datetime import datetime
import uuid
import json
import os


class TestBaseModel(unittest.TestCase):
    """ test cases for the base model"""

    def __inti__(self, *args, **kwargs):
        """ initializing the init """
        super().__init__(*args, **kwargs)

        self.name = "BaseModel"
        self.value = BaseModel

    def tearDown(self):
        try:
            os.remove('file.json')
        except PassTheError:
            pass

    def test_base_model_docstrings(self):
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_Isinstanceof(self):
        bm = BaseModel()
        self.assertIsInstance(bm, BaseModel)
        self.assertIsInstance(bm.id, str)
        self.assertIsInstance(bm.created_at, datetime)
        self.assertIsInstance(bm.updated_at, datetime)

    def test_Instatiation_kwags(self):
        bm_dict = {'id': '56d43177-cc5f-4d6c-a0c1-e167f8c27337',
                   'created_at': '2017-09-28T21:03:54.052298',
                   'updated_at': '2017-09-28T21:03:54.052298'}
        bm = BaseModel(**bm_dict)
        self.assertIsInstance(bm, BaseModel)
        self.assertEqual(bm.id, '56d43177-cc5f-4d6c-a0c1-e167f8c27337')
        self.assertEqual(bm.updated_at,
                         datetime.
                         strptime("2017-09-28T21:03:54.052298",
                                  '%Y-%m-%dT%H:%M:%S.%f'))
        self.assertEqual(bm.created_at,
                         datetime.
                         strptime("2017-09-28T21:03:54.052298",
                                  '%Y-%m-%dT%H:%M:%S.%f'))

    def test_id(self):
        """test if a new id is created"""
        bm = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm.id, bm2.id)

    def test_base_model_str(self):
        bm = BaseModel()
        self.assertEqual(str(bm), "[BaseModel] ({}) {}".
                         format(bm.id, bm.__dict__))

    def test_basemodel_save(self):
        bm = BaseModel()
        created_at = bm.created_at
        bm.save()
        self.assertEqual(bm.created_at, created_at)
        self.assertNotEqual(bm.updated_at, created_at)

    def test_basemodel_to_dict(self):
        bm = BaseModel()
        bm_dict = bm.to_dict()
        self.assertIsInstance(bm_dict, dict)
        self.assertEqual(bm_dict["id"], bm.id)
        self.assertEqual(bm_dict["created_at"], bm.created_at.isoformat())
        self.assertEqual(bm_dict["updated_at"], bm.updated_at.isoformat())
        self.assertEqual(bm_dict["__class__"], "BaseModel")


if __name__ == '__main__':
    unittest.main()
