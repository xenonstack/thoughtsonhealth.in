#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" run.py: thoughtsoncloud.in """

from ConfigParser import ConfigParser
from toh import create_server
import sys

__author__ = "Abhay Arora ( @BeliefLimitless )"
__copyright__ = "Copyright (c) 2015 Abhay Arora."
__email__ = "belieflimitless@icloud.com"
__date__ = "19/10/15"

if len(sys.argv) < 2:
    print '\nERROR: Required configuration file path!\n'
else:
    conf = ConfigParser()
    conf.read(sys.argv[1])
    server = create_server(conf)
    try:
        server.run()
    except KeyboardInterrupt:
        print '\nEXIT : Interrupt received.'
