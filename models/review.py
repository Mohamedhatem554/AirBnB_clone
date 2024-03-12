#!/usr/bin/python3
"""module Review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class"""
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """constructor"""
        super().__init__(self, *args, **kwargs)
