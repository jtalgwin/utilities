# -*- coding: utf-8 -*-
# JT Coding Header -----------------------------------------------------------
# Programmer:   Jopin Talgwin
# Started:      2022-02-07
# Updated:      2022-02-08
# Project:      utilities - lists.py
# JT Coding Header -----------------------------------------------------------

def list_library(list_name):
    """
    list_library(list_name) returns a list for 
    list_name in [
        'months', 
        'days_of_week', 
        'digits', 
        'letters', 
        'LETTERS',
        'us_states', 
        'element_names', 
        'element_sybols',
        ]

    All list elements are strings.
    requires list_library.json as library source

    example: 
    list_library('digits') returns ['0','1','2','3','4','5','6','7','8',9]
    """

    import json

    with open('list_library.json') as library_file:
        library = json.load(library_file)

    if list_name in library:
        return library[list_name]
    else:
        return []