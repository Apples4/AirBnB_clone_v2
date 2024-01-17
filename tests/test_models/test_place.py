#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.place import Place
from datetime import datetime
import models
from models import place
from models.base_model import BaseModel
import unittest
Place = place.Place


class test_Place(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """ """
        place = Place()
        self.assertTrue(hasattr(place, "city_id"))
        if models.storage_t == 'db':
            self.assertEqual(place.city_id, None)
        else:
            self.assertEqual(place.city_id, "")

    def test_user_id(self):
        """ """
        place = Place()
        self.assertTrue(hasattr(place, "user_id"))
        if models.storage_t == 'db':
            self.assertEqual(place.user_id, None)
        else:
            self.assertEqual(place.user_id, "")

    def test_name(self):
        """ """
        place = Place()
        self.assertTrue(hasattr(place, "name"))
        if models.storage_t == 'db':
            self.assertEqual(place.name, None)
        else:
            self.assertEqual(place.name, "")

    def test_description(self):
        """ """
        place = Place()
        self.assertTrue(hasattr(place, "description"))
        if models.storage_t == 'db':
            self.assertEqual(place.description, None)
        else:
            self.assertEqual(place.description, "")

    def test_number_rooms(self):
        """ """
        place = Place()
        self.assertTrue(hasattr(place, "number_rooms"))
        if models.storage_t == 'db':
            self.assertEqual(place.number_rooms, None)
        else:
            self.assertEqual(type(place.number_rooms), int)
            self.assertEqual(place.number_rooms, 0)

    def test_number_bathrooms(self):
        """ """
        place = Place()
        self.assertTrue(hasattr(place, "number_bathrooms"))
        if models.storage_t == 'db':
            self.assertEqual(place.number_bathrooms, None)
        else:
            self.assertEqual(type(place.number_bathrooms), int)
            self.assertEqual(place.number_bathrooms, 0)

    def test_max_guest(self):
        """ """
        place = Place()
        self.assertTrue(hasattr(place, "max_guest"))
        if models.storage_t == 'db':
            self.assertEqual(place.max_guest, None)
        else:
            self.assertEqual(type(place.max_guest), int)
            self.assertEqual(place.max_guest, 0)

    def test_price_by_night(self):
        """ """
        place = Place()
        self.assertTrue(hasattr(place, "price_by_night"))
        if models.storage_t == 'db':
            self.assertEqual(place.price_by_night, None)
        else:
            self.assertEqual(type(place.price_by_night), int)
            self.assertEqual(place.price_by_night, 0)

    def test_latitude(self):
        """ """
        place = Place()
        self.assertTrue(hasattr(place, "latitude"))
        if models.storage_t == 'db':
            self.assertEqual(place.latitude, None)
        else:
            self.assertEqual(type(place.latitude), float)
            self.assertEqual(place.latitude, 0.0)

    def test_longitude(self):
        """ """
        place = Place()
        self.assertTrue(hasattr(place, "longitude"))
        if models.storage_t == 'db':
            self.assertEqual(place.longitude, None)
        else:
            self.assertEqual(type(place.longitude), float)
            self.assertEqual(place.longitude, 0.0)

    def test_amenity_ids(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)

    def test_str(self):
        """ """
        place = Place()
        string = "[Place] ({}) {}".format(place.id, place.__dict__)
        self.assertEqual(string, str(place))

    def test_to_dict_values(self):
        """ """
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        p = Place()
        new_d = p.to_dict()
        self.assertEqual(new_d["__class__"], "Place")
        self.assertEqual(type(new_d["created_at"]), str)

    def test_to_dict_creates_dict(self):
        """ """
        p = Place()
        new_d = p.to_dict()
        self.assertEqual(type(new_d), dict)
        self.assertFalse("_sa_instance_state" in new_d)
        for attr in p.__dict__:
            if attr is not "_sa_instance_state":
                self.assertTrue(attr in new_d)
        self.assertTrue("__class__" in new_d)
