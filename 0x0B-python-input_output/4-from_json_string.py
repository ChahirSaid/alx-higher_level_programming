#!/usr/bin/python3
"""
function that returns an object (Python data structure)
represented by a JSON string
"""
import json


def from_json_string(my_str):
    """Function that returns an object by a JSON representation"""
    return json.loads(my_str)
