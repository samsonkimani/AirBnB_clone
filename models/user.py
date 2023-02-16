#!/usr/bin/env python3
""" model - user """

from models.base_model import BaseModel


class User(BaseModel):
    """ this class contains the different attributes of the user """
    email = ''
    password = ''
    first_name = ''
    last_name = ''
