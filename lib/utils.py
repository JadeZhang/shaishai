# -*- coding: utf-8 -*-

'''
Created on 2012-5-7

@author: jade
'''

import const
from functools import wraps
from flask import request, g, session, redirect, url_for, current_app
import types
import functions as f
import models as m
from models.tables import User
import time


def login_required(fn):
    @wraps(fn)
    def login_wrapped(*argt, **argd):
        if (not session) or ('user_id' not in session):
                return redirect(url_for('main_module.login', next=request.url))
        try:
            user = m.session.query(User).filter(User.id == session['user_id']).one()
        except:
            session.clear()
            return redirect(url_for('main_module.login', next=request.url))
        g.user = user
        ret = fn(*argt, **argd)
        return ret
    return login_wrapped

def load_user(fn):
    @wraps(fn)
    def load_user_wrapped(*argt, **argd):
        user = None
        if session and 'user_id' in session:
            user = m.session.query(User).filter(User.id == session['user_id']).first()
        g.user = user
        ret = fn(*argt, **argd)
        return ret
    return load_user_wrapped