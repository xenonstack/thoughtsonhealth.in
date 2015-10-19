#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" api.py: thoughtsoncloud.in """

from flask.blueprints import Blueprint

__author__ = "Abhay Arora ( @BeliefLimitless )"
__copyright__ = "Copyright (c) 2015 Abhay Arora."
__email__ = "belieflimitless@icloud.com"
__date__ = "19/10/15"

API = Blueprint('API', __name__)

@API.route('/')
def index():
    return 'HELLO'