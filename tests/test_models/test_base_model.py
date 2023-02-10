#!/usr/bin/python3
"""module for testing base class"""

from models.base_model import BaseModel
import unittest
from datetime import datetime
import uuid
import json
import os



class TestBaseModel(unittest.TestCase):
    """ checking for the initialization """
    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """ """
        pass

    def tearDown(self):
        try:
            os.remove('file.json')
        except:
            pass

    def test_default(self):
        """ """
        i = self.value()
        self.assertEqual(type(i),self.value)

    def test_kwargs(self):
        """ """
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwags_int(self):
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_save(self):
        """ Testing save """
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open('file.json', "r") as J_file:
            j = json.load(J_file)
            self.assertEqual(j[key], i.to_dict())

    def test_str(self):
        i = self.value()
        self.assertEqual(str(i), f"[{self.name}], ({i.id}), {i.__dict__}")

    def test_todict(self):
        i = self.value()
        dctn = i.to_dict()
        self.assertEqual(i.to_dict(), dctn)
    
    def test_kwags_none(self):
        args = {None: None}
        with self.assertEqual(i.to_dict(), args):
            new = self.value(**args)

    def test_kwags_one(self):
        """ """
        args = {'Name': 'test'}
        with self.assertRaises(KeyError):
            new = self.value(**args)


    def test_id(self):
        """ test if a new id is created """
        new = self.value()
        self.assertEqual(type(new.id),str)

    def test_created_at(self:):
        """ testing created time"""
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """ testing updated time"""
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertFalse(new.created_at == new.updated_at)

if __name__ == '__main__':
    unittest.main()
