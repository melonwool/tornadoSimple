# -*- coding: utf-8 -*-
import logging
import os.path
import yaml
import json
import socket
import struct
import urllib
import hashlib
import datetime

#
def load_config(root, configuration):
    filename = os.path.join(os.path.join(root, "etc"), configuration + ".yml")
    logging.debug("load config: %s", filename)
    config = yaml.load(file(filename, "r"))
    return config

#
def safe_int(s):
    value = 0
    try:
        value = int(s)
    except:
        pass
    return value

#
def inet_ntoa(ip):
    packed_value = struct.pack('!I', ip)
    addr = socket.inet_ntoa(packed_value)
    return addr

def inet_aton(ip):
    packed_value = socket.inet_aton(ip)
    addr = struct.unpack('!I', packed_value)
    return addr[0]
