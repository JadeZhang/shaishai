# -*- coding: utf-8 -*-
'''
Created on 2012-5-7

@author: jade
'''
import models as m
from models.tables import *
from random import choice
import string
import const
from flask import json
import hashlib
import time
import datetime
from flask import current_app
from flask import request, g
import uuid
import mail
import re
import urllib
from sqlalchemy import desc, asc
import os

def succeed(value):
    r = json.dumps({"return":value, "success":True})
    return r.decode('raw_unicode_escape').encode('utf-8')

def failed(code, detail):
    return json.dumps({"error":{"details":detail, "code":str(code)}, "success":False})


def create_new_user(email, password):
    u = User()
    u.email = email
    u.password = password
    u.jointime = time.time()
    u.nickname = email.split('@')[0]
    m.session.add(u)
    m.session.commit()
    return True , u