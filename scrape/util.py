#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: util.py
"""
util.py
~~~~

Miscellaneous utility functions.
"""
__author__ = ["Andrew G. Dunn"]
__credits__ = ["Stephen Nettnin"]
__copyright__ = __author__
__license__ = "Check root folder LICENSE file"
__email__ = "andrew.g.dunn@gmail.com"

import requests
from bs4 import BeautifulSoup

def construct_base_url(make, model, year, style):
    """ Take several arguments and construct a url
    """
    url = 'http://www.kbb.com/'

    url += make + '/'
    url += model + '/'
    url += year + '-' + make + '-' + model + '/'
    url += style + '/'

    return url


def construct_parameters(args, optional_parameter):    
    """ We need some tests up in here!
    """
    parameters = {}

    for param in optional_parameter:
        parameters[param] = args.param

    return parameters


def url_fetch(url, parameters):
    """ Does this handle 3** and 4** well?
    """
    try:
        return requests.get(url, params=parameters)
    except Exception:
        return False

def parse_buy_new(url_payload):
    pass


def parse_buy_used(url_payload):
    pass


def parse_trade_in_sell(url_payload):
    prices = []

    soup = BeautifulSoup(url_payload)

    for div in soup.find_all('div', class_='value'):
        prices.append(div.text)

    print prices
