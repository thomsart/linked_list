#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class ParsingError(Exception):

    def __init__(self):
        super().__init__("The list is empty.")

class UnfoundElementError(Exception):

    def __init__(self):
        super().__init__("This element is not in list.")

class IndexError(Exception):

    def __init__(self):
        super().__init__("Index out of list.")
