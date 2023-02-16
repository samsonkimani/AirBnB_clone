#!/usr/bin/env python3
""" model - city test """

from tests.test_models.test_base_model import TestBaseModel
from models.city import City


class TestCity(TestBaseModel):
    """ testing the city model"""

    def __init__(self, *args, **kwargs):
        """ intitialization """

        super().__inti__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """ test if the state id is a string"""
        city = self.value()
        self.assertEqual(type(city.state_id), str)

    def test_city_name(self):
        """ test if the city name is a string"""

        city = self.value()
        self.assertEqual(type(city.name), str)
