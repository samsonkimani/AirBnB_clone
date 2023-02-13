#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import TestBaseModel
from models.place import Place


class test_Place(TestBaseModel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """ """

        new = self.value()
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """ """
        place = self.value()
        self.assertEqual(type(place.user_id), str)

    def test_name(self):
        """ """
        place = self.value()
        self.assertEqual(type(place.name), str)

    def test_description(self):
        """ """
        place = self.value()
        self.assertEqual(type(place.description), str)

    def test_number_rooms(self):
        """ """
        place = self.value()
        self.assertEqual(type(place.number_rooms), int)

    def test_number_bathrooms(self):
        """ """
        place = self.value()
        self.assertEqual(type(place.number_bathrooms), int)

    def test_max_guest(self):
        """ """
        place = self.value()
        self.assertEqual(type(place.max_guest), int)

    def test_price_by_night(self):
        """ """
        place = self.value()
        self.assertEqual(type(place.price_by_night), int)

    def test_latitude(self):
        """ """
        place = self.value()
        self.assertEqual(type(place.latitude), float)

    def test_longitude(self):
        """ """
        place = self.value()
        self.assertEqual(type(place.latitude), float)

    def test_amenity_ids(self):
        """ """
        place = self.value()
        self.assertEqual(type(place.amenity_ids), list)
