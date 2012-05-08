# -*- coding: utf-8 -*-
'''
Created on 2012-5-6

@author: jade
'''
from flask import Blueprint
from flask import g, request, session
from flask import redirect, url_for, jsonify, flash, current_app, render_template, json
from flask import make_response
import models as m
from models.tables import *
import uuid
import hashlib
import time
from lib.utils import login_required, load_user
import lib.functions as f
import lib.mail as mail


# Flask 模块对象
module = Blueprint('main_module', __name__)


@module.route("/", methods=['GET'])
@login_required
def index():
    return render_template("index.html")

@module.route("/login/", methods=['GET','POST'])
def login():
    if session  and 'user_id' in session:
        return redirect('/square/')    
    email=''
    if request.method == 'POST' and "email" in request.form:
        email = request.form["email"]
        isCipher = request.form.get("isCipher", "").lower() == 'true'
        password = request.form.get("password", "")
        remember = request.form.get('remember', None) == 'on'
        try:
            user = m.session.query(User).filter_by(email = email).one()
        except:
            user = None
        if not isCipher:
            password = hashlib.md5(password).hexdigest()
        if not user:
            success,user = f.create_new_user(email,password)
            if success:
                user = m.session.query(User).filter_by(email = email).one()
                _update_session(user)
                mail.welcome_mail(email)
                return redirect('/welcome/')
                              
            else:
                g.error = 'create_fail'
        else:   
            if user.password == password:
                _update_session(user)
                if 'next' in request.args:
                    return redirect(request.args['next'])
                return redirect("/square/")
            else:
                g.error = 'invalid_password'
    return render_template("login.html",email=email)

@module.route('/logout/',methods=['GET','POST'])
def logout():
    session.pop('user_id', None)
    session.clear()
    if 'next' in request.args:
        return redirect(url_for('.login', next=request.args['next']))
    return redirect(url_for('.login'))

@module.route("/welcome/", methods=['GET'])
@load_user
def welcome():
    return render_template("welcome.html")

@module.route("/square/", methods=['GET'])
@login_required
def square():
    return render_template("square.html")

@module.route("/activity/", methods=['GET'])
@login_required
def activity():
    return render_template("activity.html")

def _update_session(user):
    session['user_id'] = user.id
    session['email'] = user.email
    session.update({'nickname': user.nickname})
