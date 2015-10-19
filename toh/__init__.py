#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" __init__.py: thoughtsoncloud.in """

from server import Server
from api import API
from drivers import MongoDB

__author__ = "Abhay Arora ( @BeliefLimitless )"
__copyright__ = "Copyright (c) 2015 Abhay Arora."
__email__ = "belieflimitless@icloud.com"
__date__ = "19/10/15"

__all__ = [Server, API, MongoDB]

def create_app(conf):
    pass