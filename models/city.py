#!/usr/bin/env python3
"""model - city"""

from models.base_model import BaseModel


class City(BaseModel):
    """ class containing the city and the state id """
    state_id = ''
    name = ''
