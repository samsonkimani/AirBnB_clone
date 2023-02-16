#!/usr/bin/env python3
"""model - reviews"""

from models.base_model import BaseModel


class Review(BaseModel):
    """class for the review model"""
    place_id = ''
    user_id = ''
    text = ''
